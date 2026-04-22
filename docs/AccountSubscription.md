# AccountSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subscription_type_name** | **str** |  | [optional] 
**start_at** | **date** |  | [optional] 
**end_at** | **date** |  | [optional] 
**contract_term** | **int** | Length in months (12 or 36) | [optional] 
**amount_cents** | **int** |  | [optional] 
**total_price** | **str** | Pre-formatted total price string | [optional] 
**has_intercollegiate_access** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**raw_contract_filename** | **str** |  | [optional] 
**raw_contract_attached** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_subscription import AccountSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSubscription from a JSON string
account_subscription_instance = AccountSubscription.from_json(json)
# print the JSON string representation of the object
print(AccountSubscription.to_json())

# convert the object into a dict
account_subscription_dict = account_subscription_instance.to_dict()
# create an instance of AccountSubscription from a dict
account_subscription_from_dict = AccountSubscription.from_dict(account_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


