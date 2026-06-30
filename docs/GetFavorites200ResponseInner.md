# GetFavorites200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The favorite record ID | 
**favoritable_id** | **int** | The favorited record&#39;s ID | 
**favorites_category_id** | **int** | Category ID (only when detailed&#x3D;1) | [optional] 
**category_name** | **str** | Category name (only when detailed&#x3D;1) | [optional] 
**name** | **str** | Favoritable record name (only when detailed&#x3D;1) | [optional] 
**school_id** | **int** | School ID for FilTeam/Deal favorites (only when detailed&#x3D;1) | [optional] 
**sport_name** | **str** | Sport name for FilTeam favorites (only when detailed&#x3D;1) | [optional] 

## Example

```python
from winthrop_client_python.models.get_favorites200_response_inner import GetFavorites200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFavorites200ResponseInner from a JSON string
get_favorites200_response_inner_instance = GetFavorites200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetFavorites200ResponseInner.to_json())

# convert the object into a dict
get_favorites200_response_inner_dict = get_favorites200_response_inner_instance.to_dict()
# create an instance of GetFavorites200ResponseInner from a dict
get_favorites200_response_inner_from_dict = GetFavorites200ResponseInner.from_dict(get_favorites200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


