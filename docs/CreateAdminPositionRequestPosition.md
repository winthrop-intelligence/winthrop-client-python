# CreateAdminPositionRequestPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**position_type_ids** | **List[int]** |  | [optional] 
**creation_reason** | **str** |  | [optional] 
**departing** | **bool** | Ticking it (on a position that is not departing yet) requires position_departure.on | [optional] 
**article_link** | **str** |  | [optional] 
**article_title** | **str** |  | [optional] 
**article_description** | **str** |  | [optional] 
**article_site_name** | **str** |  | [optional] 
**article_publish_time** | **str** |  | [optional] 
**article_image_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_position_request_position import CreateAdminPositionRequestPosition

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminPositionRequestPosition from a JSON string
create_admin_position_request_position_instance = CreateAdminPositionRequestPosition.from_json(json)
# print the JSON string representation of the object
print(CreateAdminPositionRequestPosition.to_json())

# convert the object into a dict
create_admin_position_request_position_dict = create_admin_position_request_position_instance.to_dict()
# create an instance of CreateAdminPositionRequestPosition from a dict
create_admin_position_request_position_from_dict = CreateAdminPositionRequestPosition.from_dict(create_admin_position_request_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


