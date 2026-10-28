# AthleticsSoftwareDealUpdate

Athletics Software deals (WINAD-10741). Every field is optional and null or blank means not stated (never 0). Prices only compare within the same vendor and bundle, so send products and sports with the fees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | **str** | Vendor products, modules or packages bought, e.g. \&quot;Hub, ARMS, INFLCR\&quot;. Blank clears. | [optional] 
**sports** | [**List[ApparelDealUpdateSportsInner]**](ApparelDealUpdateSportsInner.md) | Teams covered. Sport IDs or case-insensitive display names; an empty array clears all sports. Leave empty and set all_sports for department-wide deals. | [optional] 
**all_sports** | **bool** | True only when the contract says department-wide or all teams. Null restores not stated. | [optional] 
**annual_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**final_year_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**implementation_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletics_software_deal_update import AthleticsSoftwareDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticsSoftwareDealUpdate from a JSON string
athletics_software_deal_update_instance = AthleticsSoftwareDealUpdate.from_json(json)
# print the JSON string representation of the object
print(AthleticsSoftwareDealUpdate.to_json())

# convert the object into a dict
athletics_software_deal_update_dict = athletics_software_deal_update_instance.to_dict()
# create an instance of AthleticsSoftwareDealUpdate from a dict
athletics_software_deal_update_from_dict = AthleticsSoftwareDealUpdate.from_dict(athletics_software_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


