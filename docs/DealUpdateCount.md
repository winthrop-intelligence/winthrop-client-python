# DealUpdateCount

Nonnegative whole number up to 10000000 (a JSON integer or a string of digits), or null to clear.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from winthrop_client_python.models.deal_update_count import DealUpdateCount

# TODO update the JSON string below
json = "{}"
# create an instance of DealUpdateCount from a JSON string
deal_update_count_instance = DealUpdateCount.from_json(json)
# print the JSON string representation of the object
print(DealUpdateCount.to_json())

# convert the object into a dict
deal_update_count_dict = deal_update_count_instance.to_dict()
# create an instance of DealUpdateCount from a dict
deal_update_count_from_dict = DealUpdateCount.from_dict(deal_update_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


