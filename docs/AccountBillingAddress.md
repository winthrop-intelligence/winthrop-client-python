# AccountBillingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_billing_address import AccountBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBillingAddress from a JSON string
account_billing_address_instance = AccountBillingAddress.from_json(json)
# print the JSON string representation of the object
print(AccountBillingAddress.to_json())

# convert the object into a dict
account_billing_address_dict = account_billing_address_instance.to_dict()
# create an instance of AccountBillingAddress from a dict
account_billing_address_from_dict = AccountBillingAddress.from_dict(account_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


