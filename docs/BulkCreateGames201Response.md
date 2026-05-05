# BulkCreateGames201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[Game]**](Game.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_create_games201_response import BulkCreateGames201Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGames201Response from a JSON string
bulk_create_games201_response_instance = BulkCreateGames201Response.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGames201Response.to_json())

# convert the object into a dict
bulk_create_games201_response_dict = bulk_create_games201_response_instance.to_dict()
# create an instance of BulkCreateGames201Response from a dict
bulk_create_games201_response_from_dict = BulkCreateGames201Response.from_dict(bulk_create_games201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


