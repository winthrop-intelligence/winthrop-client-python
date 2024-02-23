# Coach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**leader** | **bool** |  | [optional] 
**bio** | **str** |  | [optional] 
**bio_text** | **str** |  | [optional] 
**dob** | **date** |  | [optional] 
**alma_mater_id** | **int** | ID of School, You can view Alma Mater using School API | [optional] 
**alma_mater_year** | **str** |  | [optional] 
**hometown_city** | **str** |  | [optional] 
**hometown_state** | **str** |  | [optional] 
**twitter_handle** | **str** |  | [optional] 
**avatar** | [**Avatar**](Avatar.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach import Coach

# TODO update the JSON string below
json = "{}"
# create an instance of Coach from a JSON string
coach_instance = Coach.from_json(json)
# print the JSON string representation of the object
print Coach.to_json()

# convert the object into a dict
coach_dict = coach_instance.to_dict()
# create an instance of Coach from a dict
coach_form_dict = coach.from_dict(coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


