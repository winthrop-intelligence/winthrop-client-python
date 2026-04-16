# SportOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport_option import SportOption

# TODO update the JSON string below
json = "{}"
# create an instance of SportOption from a JSON string
sport_option_instance = SportOption.from_json(json)
# print the JSON string representation of the object
print(SportOption.to_json())

# convert the object into a dict
sport_option_dict = sport_option_instance.to_dict()
# create an instance of SportOption from a dict
sport_option_from_dict = SportOption.from_dict(sport_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


