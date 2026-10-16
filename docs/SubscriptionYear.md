# SubscriptionYear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**year_number** | **int** |  | [optional] 
**service_start** | **date** |  | [optional] 
**service_end** | **date** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**due_date** | **date** |  | [optional] 
**backfilled** | **bool** | Came from the schedule backfill. Such a row may cover the whole agreement and is invoiced without being split. Its amount_cents is the legacy ANNUAL rate, not the price of its period. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.subscription_year import SubscriptionYear

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionYear from a JSON string
subscription_year_instance = SubscriptionYear.from_json(json)
# print the JSON string representation of the object
print(SubscriptionYear.to_json())

# convert the object into a dict
subscription_year_dict = subscription_year_instance.to_dict()
# create an instance of SubscriptionYear from a dict
subscription_year_from_dict = SubscriptionYear.from_dict(subscription_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


