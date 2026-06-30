# UpdateFavorite200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**favoritable_id** | **int** |  | 
**favorites_category_id** | **int** | The list (category) the favorite belongs to | [optional] 

## Example

```python
from winthrop_client_python.models.update_favorite200_response import UpdateFavorite200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFavorite200Response from a JSON string
update_favorite200_response_instance = UpdateFavorite200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateFavorite200Response.to_json())

# convert the object into a dict
update_favorite200_response_dict = update_favorite200_response_instance.to_dict()
# create an instance of UpdateFavorite200Response from a dict
update_favorite200_response_from_dict = UpdateFavorite200Response.from_dict(update_favorite200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


