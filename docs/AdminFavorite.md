# AdminFavorite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**favoritable_type** | **str** |  | [optional] 
**favoritable_id** | **int** |  | [optional] 
**favorites_category_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**account_name** | **str** |  | [optional] 
**account_subscription_type** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_state** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**favoritable_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_favorite import AdminFavorite

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFavorite from a JSON string
admin_favorite_instance = AdminFavorite.from_json(json)
# print the JSON string representation of the object
print(AdminFavorite.to_json())

# convert the object into a dict
admin_favorite_dict = admin_favorite_instance.to_dict()
# create an instance of AdminFavorite from a dict
admin_favorite_from_dict = AdminFavorite.from_dict(admin_favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


