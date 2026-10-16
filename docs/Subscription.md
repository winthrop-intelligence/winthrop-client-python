# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** |  | [optional] 
**subscription_type_name** | **str** |  | [optional] 
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
**contract_term** | **int** | Length in months. Null on some legacy agreements. | [optional] 
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
**standard_agreement** | **bool** |  | [optional] 
**active_users_count** | **int** |  | [optional] 
**has_intercollegiate_access** | **bool** |  | [optional] 
**contract_value_cents** | **int** | Read-only value of the whole agreement in cents. While the schedule is untouched legacy data (every row backfilled, all at the same annual amount_cents, and contract_term present), use amount_cents * contract_term / 12, rounded down, preserving the agreed legacy term even when dates were extended independently. Otherwise sum the period values: backfilled rows use amount_cents * whole calendar months / 12, and explicit rows use their amount_cents. Correcting one row&#39;s price therefore moves a legacy schedule to the row sum (three $10,000 years with year two saved at $14,700 is $34,700), and saving the row back at the shared rate restores the term-based value. With no rows, use term math, or amount_cents when contract_term is null. | [optional] 
**free** | **bool** | Read-only. True for a FREE subscription, whose schedule years may be priced at $0. | [optional] 
**subscription_years** | [**List[SubscriptionYear]**](SubscriptionYear.md) |  | [optional] 
**year_invoices** | [**List[SubscriptionYearInvoicesInner]**](SubscriptionYearInvoicesInner.md) | Show and update responses only. The invoice standing for each invoiced year: a paid invoice wins over a pending delivery, then a sent invoice, then the newest draft. Years with no invoice are absent. Pending delivery reserves the year against removal. | [optional] 
**has_file** | **bool** | Whether the raw_contract has an attached, non-empty PDF. | [optional] 
**raw_contract_filename** | **str** | Present only when has_file is true. | [optional] 
**pdf_preview_url** | **str** | Present only when has_file is true. | [optional] 

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
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


