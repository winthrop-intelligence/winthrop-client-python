# PositionDepartureRequest

Full replacement, not a partial update. Omitted optional details become null. When departing is false, departure_on must be omitted or null; reason, source URL, and approval quote can be supplied as context for clearing the departure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departing** | **bool** |  | 
**departure_on** | **date** | YYYY-MM-DD date required when departing is true; must be null or omitted when false. | [optional] 
**departure_reason** | **str** | Trimmed reason, required and nonblank when departing is true. Blank becomes null. | [optional] 
**departure_source_url** | **str** | Public http(s) URL required when departing is true. Trimmed; blank URLs are invalid. | [optional] 
**approval_quote** | **str** | Optional trimmed approval quote; omitted, null, or blank becomes null. | [optional] 
**change_note** | **str** | Why this change is being made, for the internal audit history (WINAD-10632). It is stored on the audit version this write creates and is never returned. Blank is the same as omitted; a non-string value is refused with 422 (errors.change_note). It is separate from approval_quote, which is departure data stored on the position. | [optional] 

## Example

```python
from winthrop_client_python.models.position_departure_request import PositionDepartureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PositionDepartureRequest from a JSON string
position_departure_request_instance = PositionDepartureRequest.from_json(json)
# print the JSON string representation of the object
print(PositionDepartureRequest.to_json())

# convert the object into a dict
position_departure_request_dict = position_departure_request_instance.to_dict()
# create an instance of PositionDepartureRequest from a dict
position_departure_request_from_dict = PositionDepartureRequest.from_dict(position_departure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


