# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**accountable_id** | **int** |  | [optional] 
**creator_id** | **int** |  | [optional] 
**start_at** | **date** |  | [optional] 
**end_at** | **date** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**subscription_type_id** | **int** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**activity_cache_id** | **int** |  | [optional] 
**old_email_domain** | **str** |  | [optional] 
**account_id** | **int** |  | [optional] 
**contract_term** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**contract_accepted** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**contract_accepted_ip_address** | **str** |  | [optional] 
**renewal** | **bool** |  | [optional] 
**renewing** | **bool** |  | [optional] 
**invoicing** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**send_renewal** | **bool** |  | [optional] 
**has_foia_clause** | **bool** |  | [optional] 
**standard_agreement** | **bool** |  | [optional] 
**active_users_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


