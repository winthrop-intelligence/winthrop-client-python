# ListNotes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**notable_id** | **str** | The notable record&#39;s ID (string to avoid JS precision loss) | 
**notable_type** | **str** | The model type (e.g. \&quot;Coach\&quot;) | 
**content** | **str** | The note text | 
**name** | **str** | The notable record&#39;s name | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**school_id** | **int** | School ID for FilTeam notes | [optional] 
**sport_name** | **str** | Sport name for FilTeam notes | [optional] 

## Example

```python
from winthrop_client_python.models.list_notes200_response_inner import ListNotes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotes200ResponseInner from a JSON string
list_notes200_response_inner_instance = ListNotes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListNotes200ResponseInner.to_json())

# convert the object into a dict
list_notes200_response_inner_dict = list_notes200_response_inner_instance.to_dict()
# create an instance of ListNotes200ResponseInner from a dict
list_notes200_response_inner_from_dict = ListNotes200ResponseInner.from_dict(list_notes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


