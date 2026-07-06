# GuaranteeEconomics

Per-school guarantee economics over the last three completed seasons (WINAD-10005). host/travel are null both for \"no qualifying money games\" and for \"caller lacks guarantee aggregate access\" — deliberately indistinguishable. When params are missing/invalid the `error` block is returned instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**sport** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**season_window** | **str** |  | [optional] 
**seasons** | **List[int]** |  | [optional] 
**host** | [**GuaranteeEconomicsSide**](GuaranteeEconomicsSide.md) |  | [optional] 
**travel** | [**GuaranteeEconomicsSide**](GuaranteeEconomicsSide.md) |  | [optional] 
**error** | [**GuaranteeEconomicsError**](GuaranteeEconomicsError.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_economics import GuaranteeEconomics

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeEconomics from a JSON string
guarantee_economics_instance = GuaranteeEconomics.from_json(json)
# print the JSON string representation of the object
print(GuaranteeEconomics.to_json())

# convert the object into a dict
guarantee_economics_dict = guarantee_economics_instance.to_dict()
# create an instance of GuaranteeEconomics from a dict
guarantee_economics_from_dict = GuaranteeEconomics.from_dict(guarantee_economics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


