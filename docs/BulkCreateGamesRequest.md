# BulkCreateGamesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[BulkCreateGamesRequestGamesInner]**](BulkCreateGamesRequestGamesInner.md) |  | 

## Example

```python
from winthrop_client_python.models.bulk_create_games_request import BulkCreateGamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGamesRequest from a JSON string
bulk_create_games_request_instance = BulkCreateGamesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGamesRequest.to_json())

# convert the object into a dict
bulk_create_games_request_dict = bulk_create_games_request_instance.to_dict()
# create an instance of BulkCreateGamesRequest from a dict
bulk_create_games_request_from_dict = BulkCreateGamesRequest.from_dict(bulk_create_games_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


