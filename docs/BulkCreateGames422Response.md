# BulkCreateGames422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Zero-based index of the row that failed validation. | [optional] 
**errors** | [**Dict[str, BulkCreateGames422ResponseErrorsValue]**](BulkCreateGames422ResponseErrorsValue.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_create_games422_response import BulkCreateGames422Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGames422Response from a JSON string
bulk_create_games422_response_instance = BulkCreateGames422Response.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGames422Response.to_json())

# convert the object into a dict
bulk_create_games422_response_dict = bulk_create_games422_response_instance.to_dict()
# create an instance of BulkCreateGames422Response from a dict
bulk_create_games422_response_from_dict = BulkCreateGames422Response.from_dict(bulk_create_games422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


