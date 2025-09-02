# WireChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**coach_id** | **int** |  | 
**school_id** | **int** |  | 
**created_by_id** | **int** |  | 
**effective_date** | **datetime** |  | [optional] 
**wire_type** | **str** |  | [optional] 
**position_title** | **str** |  | [optional] 
**article_link** | **str** |  | [optional] 
**article_title** | **str** |  | [optional] 
**article_description** | **str** |  | [optional] 
**article_site_name** | **str** |  | [optional] 
**article_publish_time** | **datetime** |  | [optional] 
**article_image_url** | **str** |  | [optional] 
**position_types** | [**List[WireChangePositionTypesInner]**](WireChangePositionTypesInner.md) |  | [optional] 
**sports** | [**List[WireChangeSportsInner]**](WireChangeSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.wire_change import WireChange

# TODO update the JSON string below
json = "{}"
# create an instance of WireChange from a JSON string
wire_change_instance = WireChange.from_json(json)
# print the JSON string representation of the object
print(WireChange.to_json())

# convert the object into a dict
wire_change_dict = wire_change_instance.to_dict()
# create an instance of WireChange from a dict
wire_change_form_dict = wire_change.from_dict(wire_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


