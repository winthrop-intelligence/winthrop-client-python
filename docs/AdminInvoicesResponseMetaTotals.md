# AdminInvoicesResponseMetaTotals

Over ALL the rows the filters match, never just this page. Present for status=not_paid and null for every other status. An invoice's amount_cents, or the schedule's billing amount for a year with no invoice (a row whose amount cannot be suggested adds nothing).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount_cents** | **int** |  | 
**accounts_count** | **int** | Distinct accounts among the rows. | 
**never_sent_amount_cents** | **int** | The part of the total on rows with no send date and not an old invoice that predates send dates (a draft, a year with no invoice, a first send still queued). | 

## Example

```python
from winthrop_client_python.models.admin_invoices_response_meta_totals import AdminInvoicesResponseMetaTotals

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoicesResponseMetaTotals from a JSON string
admin_invoices_response_meta_totals_instance = AdminInvoicesResponseMetaTotals.from_json(json)
# print the JSON string representation of the object
print(AdminInvoicesResponseMetaTotals.to_json())

# convert the object into a dict
admin_invoices_response_meta_totals_dict = admin_invoices_response_meta_totals_instance.to_dict()
# create an instance of AdminInvoicesResponseMetaTotals from a dict
admin_invoices_response_meta_totals_from_dict = AdminInvoicesResponseMetaTotals.from_dict(admin_invoices_response_meta_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


