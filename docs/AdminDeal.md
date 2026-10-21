# AdminDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**school** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**deal_type** | [**AdminCoachCurrentSport**](AdminCoachCurrentSport.md) |  | [optional] 
**vendors** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**raw_contract** | [**AdminDealRawContract**](AdminDealRawContract.md) |  | [optional] 
**deal_detail** | [**AdminDealDealDetail**](AdminDealDealDetail.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal import AdminDeal

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDeal from a JSON string
admin_deal_instance = AdminDeal.from_json(json)
# print the JSON string representation of the object
print(AdminDeal.to_json())

# convert the object into a dict
admin_deal_dict = admin_deal_instance.to_dict()
# create an instance of AdminDeal from a dict
admin_deal_from_dict = AdminDeal.from_dict(admin_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


