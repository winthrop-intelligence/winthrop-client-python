# CreateAdminPositionRequestPositionDeparture

WINAD-10656 departure details, read when position.departing is ticked. `on` is required to set departing (and to edit an already-departing position's details); reason and source_url are optional. Omitted on an already-departing position, the recorded details are kept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **date** |  | [optional] 
**reason** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_position_request_position_departure import CreateAdminPositionRequestPositionDeparture

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminPositionRequestPositionDeparture from a JSON string
create_admin_position_request_position_departure_instance = CreateAdminPositionRequestPositionDeparture.from_json(json)
# print the JSON string representation of the object
print(CreateAdminPositionRequestPositionDeparture.to_json())

# convert the object into a dict
create_admin_position_request_position_departure_dict = create_admin_position_request_position_departure_instance.to_dict()
# create an instance of CreateAdminPositionRequestPositionDeparture from a dict
create_admin_position_request_position_departure_from_dict = CreateAdminPositionRequestPositionDeparture.from_dict(create_admin_position_request_position_departure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


