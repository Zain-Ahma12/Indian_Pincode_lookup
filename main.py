from fastapi import FastAPI
import uvicorn
from exceptions import (
    PinCodeNotFoundError, pincode_not_found_handler,
    InvalidPinCodeError, invalid_pincode_handler
)
from data import pincode_data
from models import LocationResponse, PincodeRequest, BulkPinCodesRequest, BulkPinCodesResponse

app = FastAPI(
    title="Pincode lookup API",
    description="This api autofills the city and state from an Indian Pincode during the checkout",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openAPI",
    version="1.0.0"
)

# register your custom exception handlers
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)

@app.get(
    "/",
    tags=["root"],
    description=(
        "Root endpoint"
        "return the basic information about the api"
    )
)
def root():
    """
    Returns the basic info about this api
    """
    return {"message" : "Pincode lookup api"}

@app.get(
    "/pincode/{code}",
    response_model=LocationResponse,
    description=(
        "Pincode endpoint"
        "Fetch location information for a single Indian PIN code."
    ),
    tags=["pincode"]
)
def pincode_lookup(code: str) -> LocationResponse:
    if len(code) != 6 or not code.isdigit(): 
        raise InvalidPinCodeError(code, "Must be exactly 6 digit (Indian pincode format)")

    if code not in pincode_data:
        raise PinCodeNotFoundError(code)
    
    return pincode_data[code]

@app.post(
    f"/pincode/bulk",
    response_model=BulkPinCodesResponse,
    description=(
        "Bulk Pincode endpoint"
        "Fetch location information for multiple Indian PIN codes " 
        "in a single request."
    ),
    tags=["pincode"]
)
def bulk_pincodes_lookup(request: BulkPinCodesRequest) -> BulkPinCodesResponse:
    results: list[dict[str, str | float]] = []
    missing: list[str] = []

    for code in request.pincodes:
        if code in pincode_data:
            results.append(pincode_data[code])
        else:
            missing.append(code)
    
    return BulkPinCodesResponse(
        results = results,
        missing = missing,
        found = len(results),
        not_found = len(missing)
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)