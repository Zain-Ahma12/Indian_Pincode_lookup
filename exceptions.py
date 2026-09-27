from fastapi.responses import JSONResponse
from fastapi import Request, status


class PinCodeNotFoundError(Exception):
    """
    Exception raised when no location is found for a given PIN code.

    This exception is intended to be caught by a FastAPI exception handler and converted into an appropriate HTTP response. 
    
    Attributes: 
        pincode: The PIN code for which no location was found.
    """
    def __init__(self, pincode: str) -> None:
        self.pincode = pincode


class InvalidPinCodeError(Exception):
    """
    Exception raised when a PIN code has an invalid format. 
    
    This exception stores both the invalid PIN code and a reason explaining why the PIN code is considered invalid. 
    
    Attributes: 
        pincode: The PIN code that failed validation. 
        reason: A description of why the PIN code is invalid. 
    """
    def __init__(self, pincode: str, reason: str = "Invalid format") -> None:
        self.pincode = pincode
        self.reason = reason

# Custom handlers

async def pincode_not_found_handler(request: Request, exc: PinCodeNotFoundError) -> JSONResponse:
    """
    Handle :class:`PinCodeNotFoundError` exceptions.

    Returns an HTTP 404 response containing an error code, a descriptive message, and the PIN code that could not be found. 
    
    Args: 
        request: The incoming FastAPI request. exc: The ``PinCodeNotFoundError`` exception that was raised. 
    
    Returns: 
        A ``JSONResponse`` with HTTP 404 status and details about the missing PIN code. 
    """
    return JSONResponse(
        status_code = 404,
        content = {
            "error": "pincode_not_found",
            "message": f"No location for pincode: {exc.pincode}",
            "pincode": exc.pincode
        }
    )

async def invalid_pincode_handler(request: Request, exc: InvalidPinCodeError) -> JSONResponse:
    """
    Handle :class:`InvalidPinCodeError` exceptions. 
    
    Returns an HTTP 400 response containing an error code, a descriptive message, and the invalid PIN code. 
    
    Args: 
        request: The incoming FastAPI request. 
        exc: The ``InvalidPinCodeError`` exception that was raised. 
    
    Returns: 
        A ``JSONResponse`` with HTTP 400 status and details explaining why the PIN code is invalid. 
    """

    return JSONResponse(
        status_code = 400,
        content = {
            "error": "invalid_pincode",
            "message": f"pincode '{exc.pincode}' is invalid because {exc.reason}",
            "pincode": exc.pincode
        }
    )