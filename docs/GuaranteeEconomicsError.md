# GuaranteeEconomicsError

Structured error returned in place of data when params are missing or invalid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**suggested_fix** | **str** |  | [optional] 
**received_args** | **Dict[str, object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_economics_error import GuaranteeEconomicsError

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeEconomicsError from a JSON string
guarantee_economics_error_instance = GuaranteeEconomicsError.from_json(json)
# print the JSON string representation of the object
print(GuaranteeEconomicsError.to_json())

# convert the object into a dict
guarantee_economics_error_dict = guarantee_economics_error_instance.to_dict()
# create an instance of GuaranteeEconomicsError from a dict
guarantee_economics_error_from_dict = GuaranteeEconomicsError.from_dict(guarantee_economics_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


