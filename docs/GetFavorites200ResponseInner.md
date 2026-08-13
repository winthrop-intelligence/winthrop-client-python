# GetFavorites200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The favorite record ID | 
**favoritable_id** | **int** | The favorited record&#39;s ID | 
**favorites_category_id** | **int** | ID of the list (category) this favorite belongs to. | [optional] 
**category_name** | **str** | Category name (only when detailed&#x3D;1) | [optional] 
**name** | **str** | Favoritable record name (only when detailed&#x3D;1) | [optional] 
**school_id** | **int** | School ID for FilTeam/Deal favorites (only when detailed&#x3D;1) | [optional] 
**sport_name** | **str** | Sport name for FilTeam favorites (only when detailed&#x3D;1) | [optional] 
**avatar_url** | **str** | App-relative path to the coach&#39;s cropped avatar thumbnail for Coach favorites (only when detailed&#x3D;1). Null when the coach has no usable image, in which case the client falls back to initials. | [optional] 
**leader** | **bool** | True when the favorited coach is an administrator. Administrators are Coach records carrying the leader flag, so they share favoritable_type \&quot;Coach\&quot; with coaches and this is what tells the two apart. Present for Coach favorites when detailed&#x3D;1, and absent for every other favoritable type. | [optional] 

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


