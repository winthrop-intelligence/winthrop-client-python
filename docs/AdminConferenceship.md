# AdminConferenceship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**sport** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 
**conference** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conferenceship import AdminConferenceship

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceship from a JSON string
admin_conferenceship_instance = AdminConferenceship.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceship.to_json())

# convert the object into a dict
admin_conferenceship_dict = admin_conferenceship_instance.to_dict()
# create an instance of AdminConferenceship from a dict
admin_conferenceship_from_dict = AdminConferenceship.from_dict(admin_conferenceship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


