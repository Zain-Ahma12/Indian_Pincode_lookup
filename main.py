from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Pincode lookup API",
    description="This api autofills the city and state from an Indian Pincode during the checkout",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openAPI",
    version="1.0.0"
)

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


if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)