# Conferenceship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.conferenceship import Conferenceship

# TODO update the JSON string below
json = "{}"
# create an instance of Conferenceship from a JSON string
conferenceship_instance = Conferenceship.from_json(json)
# print the JSON string representation of the object
print Conferenceship.to_json()

# convert the object into a dict
conferenceship_dict = conferenceship_instance.to_dict()
# create an instance of Conferenceship from a dict
conferenceship_form_dict = conferenceship.from_dict(conferenceship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


