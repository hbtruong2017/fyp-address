from app import app
from .analytics_helper.property_category import *
from .api_helper.common import *
from pydantic import BaseModel

class Item(BaseModel):
    address: str

@app.post("/api/address")
def get_individual_address_data(item:Item):
    """
    Main API to receive an address input and do the following:
    1. Verify whether it is a valid address
    2. Find out what type of property
    3. Find which region does the address belong to
    4. Return region data
    5. Return country data (at the moment, Singapore)

    """
    address = item.address

    # Call Onemap API to get detailed address
    onemap_result = search_onemap_api(address)
    onemap_address = onemap_result["results"][0]

    # Validation
    if onemap_result["found"] == 0:
        return {"status": "error", "data": "Address is invalid. Please enter another address."}

    elif onemap_result["found"] != 1:
        return {"status": "error", "data": "Too many similar addresses found. Please enter a more specific address."}

    result = {"status": "success", "data": {}}

    # Find out property type
    property_type = check_property_type(onemap_address)

    result["data"]["house_type"] = property_type

    return result