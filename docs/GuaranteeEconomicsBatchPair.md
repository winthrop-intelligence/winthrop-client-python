# GuaranteeEconomicsBatchPair

One requested pair's guarantee economics. host/travel are null both for \"no qualifying money games\" and for \"caller lacks guarantee aggregate access\" — deliberately indistinguishable, exactly like the singular endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**host** | [**GuaranteeEconomicsSide**](GuaranteeEconomicsSide.md) |  | [optional] 
**travel** | [**GuaranteeEconomicsSide**](GuaranteeEconomicsSide.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_economics_batch_pair import GuaranteeEconomicsBatchPair

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeEconomicsBatchPair from a JSON string
guarantee_economics_batch_pair_instance = GuaranteeEconomicsBatchPair.from_json(json)
# print the JSON string representation of the object
print(GuaranteeEconomicsBatchPair.to_json())

# convert the object into a dict
guarantee_economics_batch_pair_dict = guarantee_economics_batch_pair_instance.to_dict()
# create an instance of GuaranteeEconomicsBatchPair from a dict
guarantee_economics_batch_pair_from_dict = GuaranteeEconomicsBatchPair.from_dict(guarantee_economics_batch_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


