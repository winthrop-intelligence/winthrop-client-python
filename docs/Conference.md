# Conference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**founded** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**ord** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**external_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference import Conference

# TODO update the JSON string below
json = "{}"
# create an instance of Conference from a JSON string
conference_instance = Conference.from_json(json)
# print the JSON string representation of the object
print(Conference.to_json())

# convert the object into a dict
conference_dict = conference_instance.to_dict()
# create an instance of Conference from a dict
conference_form_dict = conference.from_dict(conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


