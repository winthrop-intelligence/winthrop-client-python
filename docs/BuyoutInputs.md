# BuyoutInputs

One checked buyout-inputs document per coach contract (WINAD-10717, schema buyout-inputs-v1). Only `schema`, `rc` and `as_of` are required and checked here; the rest (terms_version, terms_revision, inputs, outside_facts, qa, ...) is validated against data-quality/data/schemas/buyout-inputs-v1.schema.json and stored as sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | 
**rc** | **int** | Must equal the RawContract id in the path | 
**as_of** | **date** |  | 

## Example

```python
from winthrop_client_python.models.buyout_inputs import BuyoutInputs

# TODO update the JSON string below
json = "{}"
# create an instance of BuyoutInputs from a JSON string
buyout_inputs_instance = BuyoutInputs.from_json(json)
# print the JSON string representation of the object
print(BuyoutInputs.to_json())

# convert the object into a dict
buyout_inputs_dict = buyout_inputs_instance.to_dict()
# create an instance of BuyoutInputs from a dict
buyout_inputs_from_dict = BuyoutInputs.from_dict(buyout_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


