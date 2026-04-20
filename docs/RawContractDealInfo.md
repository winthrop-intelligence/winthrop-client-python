# RawContractDealInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**vendors** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**deal_type_name** | **str** |  | [optional] 
**start_year** | **int** |  | [optional] 
**end_year** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**signed** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**summary** | **str** |  | [optional] 
**term_years** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.raw_contract_deal_info import RawContractDealInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractDealInfo from a JSON string
raw_contract_deal_info_instance = RawContractDealInfo.from_json(json)
# print the JSON string representation of the object
print(RawContractDealInfo.to_json())

# convert the object into a dict
raw_contract_deal_info_dict = raw_contract_deal_info_instance.to_dict()
# create an instance of RawContractDealInfo from a dict
raw_contract_deal_info_from_dict = RawContractDealInfo.from_dict(raw_contract_deal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


