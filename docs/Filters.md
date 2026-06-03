# Filters

Request body for the legacy coach search endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_ids** | **List[int]** | Coach IDs to prioritize at the top of the result set. | [optional] 
**page** | **int** |  | [optional] [default to 1]
**per_page** | **int** |  | [optional] [default to 100]
**q** | **Dict[str, object]** | Ransack query parameters for filtering coaches. | [optional] 

## Example

```python
from winthrop_client_python.models.filters import Filters

# TODO update the JSON string below
json = "{}"
# create an instance of Filters from a JSON string
filters_instance = Filters.from_json(json)
# print the JSON string representation of the object
print(Filters.to_json())

# convert the object into a dict
filters_dict = filters_instance.to_dict()
# create an instance of Filters from a dict
filters_from_dict = Filters.from_dict(filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


