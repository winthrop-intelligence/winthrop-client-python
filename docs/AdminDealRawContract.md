# AdminDealRawContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**term_sheet_only** | **bool** |  | [optional] 
**filename** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deal_raw_contract import AdminDealRawContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealRawContract from a JSON string
admin_deal_raw_contract_instance = AdminDealRawContract.from_json(json)
# print the JSON string representation of the object
print(AdminDealRawContract.to_json())

# convert the object into a dict
admin_deal_raw_contract_dict = admin_deal_raw_contract_instance.to_dict()
# create an instance of AdminDealRawContract from a dict
admin_deal_raw_contract_from_dict = AdminDealRawContract.from_dict(admin_deal_raw_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


