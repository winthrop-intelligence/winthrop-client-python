# AccountDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**accountable_type** | **str** |  | [optional] 
**associated_name** | **str** | School or conference display name | [optional] 
**email_domain** | **str** |  | [optional] 
**original_contract_date** | **date** |  | [optional] 
**billing_addresses** | [**List[AccountBillingAddress]**](AccountBillingAddress.md) |  | [optional] 
**subscriptions** | [**List[AccountSubscription]**](AccountSubscription.md) |  | [optional] 
**invoices** | [**List[AccountInvoice]**](AccountInvoice.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_detail import AccountDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetail from a JSON string
account_detail_instance = AccountDetail.from_json(json)
# print the JSON string representation of the object
print(AccountDetail.to_json())

# convert the object into a dict
account_detail_dict = account_detail_instance.to_dict()
# create an instance of AccountDetail from a dict
account_detail_from_dict = AccountDetail.from_dict(account_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


