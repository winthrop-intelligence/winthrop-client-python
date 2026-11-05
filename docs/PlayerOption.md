# PlayerOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**external_code** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.player_option import PlayerOption

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerOption from a JSON string
player_option_instance = PlayerOption.from_json(json)
# print the JSON string representation of the object
print(PlayerOption.to_json())

# convert the object into a dict
player_option_dict = player_option_instance.to_dict()
# create an instance of PlayerOption from a dict
player_option_from_dict = PlayerOption.from_dict(player_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


