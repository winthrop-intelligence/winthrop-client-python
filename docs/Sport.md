# Sport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_aka** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**gender_code** | **str** |  | [optional] 
**emerging** | **bool** |  | [optional] 
**meet_sport** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport import Sport

# TODO update the JSON string below
json = "{}"
# create an instance of Sport from a JSON string
sport_instance = Sport.from_json(json)
# print the JSON string representation of the object
print Sport.to_json()

# convert the object into a dict
sport_dict = sport_instance.to_dict()
# create an instance of Sport from a dict
sport_form_dict = sport.from_dict(sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


