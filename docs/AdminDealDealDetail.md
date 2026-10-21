# AdminDealDealDetail

Dynamic - real columns depend on `type` (one of the 13 DealDetail STI subclasses); always includes id, type, sport_ids

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**sport_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_deal_detail import AdminDealDealDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealDealDetail from a JSON string
admin_deal_deal_detail_instance = AdminDealDealDetail.from_json(json)
# print the JSON string representation of the object
print(AdminDealDealDetail.to_json())

# convert the object into a dict
admin_deal_deal_detail_dict = admin_deal_deal_detail_instance.to_dict()
# create an instance of AdminDealDealDetail from a dict
admin_deal_deal_detail_from_dict = AdminDealDealDetail.from_dict(admin_deal_deal_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


