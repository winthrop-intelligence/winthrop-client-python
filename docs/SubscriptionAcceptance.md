# SubscriptionAcceptance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**subscription_type_name** | **str** |  | [optional] 
**annual_price** | **str** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**start_at** | **date** |  | [optional] 
**end_at** | **date** |  | [optional] 
**contract_term** | **int** |  | [optional] 
**contract_term_options** | [**List[ContractTermOption]**](ContractTermOption.md) |  | [optional] 
**standard_length_contract** | **bool** |  | [optional] 
**total_price** | **str** |  | [optional] 
**contract_accepted** | **bool** |  | [optional] 
**raw_contract_attached** | **bool** |  | [optional] 
**accepted** | **bool** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.subscription_acceptance import SubscriptionAcceptance

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAcceptance from a JSON string
subscription_acceptance_instance = SubscriptionAcceptance.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAcceptance.to_json())

# convert the object into a dict
subscription_acceptance_dict = subscription_acceptance_instance.to_dict()
# create an instance of SubscriptionAcceptance from a dict
subscription_acceptance_from_dict = SubscriptionAcceptance.from_dict(subscription_acceptance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


