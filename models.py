from sre_parse import SUCCESS
from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    """
    Request model for looking up a single Indian PIN code. 
    
    Attributes: 
        pincode: A six-digit Indian postal PIN code. 
        
    """

    pincode : str

    # pincode must be exactly 6 digits long.
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value: str) -> str:
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digits (Indian pincode format)")
        return value
    
class LocationResponse(BaseModel):
    """
    Response model containing location information for a PIN code. 
    
    Attributes: 
        pincode: The six-digit Indian PIN code. 
        city: The city associated with the PIN code. 
        state: The state in which the location is situated. 
        district: The district associated with the PIN code. 
    """

    pincode : str
    city : str
    state : str
    district : str

class BulkPinCodesRequest(BaseModel):
    """
    Request model for looking up multiple Indian PIN codes. A maximum of 10 PIN codes can be submitted in a single request. 
    
    Attributes: 
        pincodes: A list containing one to ten six-digit Indian PIN codes. 
    
    """

    pincodes : list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, values: list[str]) -> list[str]:
        if len(values) == 0:
            raise ValueError("At least one pincode is required")
        if len(values) > 10:
            raise ValueError("Maximum 10 pincodes are allowed per requests")
        for pcode in values:
            if len(pcode) != 6 or not pcode.isdigit():
                raise ValueError("Each Pincode must be exactly 6 digits (Indian pincode format)")
        return values

class BulkPinCodesResponse(BaseModel):
    """
    Response model containing the results of a bulk PIN-code lookup. 
    
    Attributes: 
        status: Indicates the overall status of the bulk lookup. 
        found: Number of PIN codes for which location data was found. 
        not_found: Number of PIN codes for which no location was found. 
        results: Location information for successfully resolved PIN codes. 
        missing: PIN codes for which no location information was found. 
    """

    status : str = "sucess"
    found : int
    not_found : int
    results : list[LocationResponse]
    missing : list[str]
