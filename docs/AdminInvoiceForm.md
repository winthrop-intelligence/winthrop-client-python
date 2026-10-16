# AdminInvoiceForm

The invoice form/detail — same shape whether it's an unsaved prefill, a draft, or sent/paid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Null for an unsaved GET .../prefill response. | 
**subscription_id** | **int** |  | 
**subscription_year_id** | **int** |  | 
**account_id** | **int** |  | 
**account_name** | **str** |  | 
**subscription_type_name** | **str** |  | 
**year_number** | **int** |  | 
**years_total** | **int** |  | 
**service_start** | **date** |  | 
**service_end** | **date** |  | 
**invoice_date** | **date** |  | 
**description** | **str** |  | 
**amount_cents** | **int** | On a prefill, the amount the schedule year suggests for its own period: a backfilled legacy year stores the ANNUAL rate, so a short year is prorated by whole months (annual rate x months / 12, the rule behind Subscription contract_value_cents). Null when a legacy year is longer than 12 months or shorter than one month and the amount is ambiguous; hints.amount_cents then asks the operator to check the agreement. | 
**due_date** | **date** |  | 
**due_date_notes** | **str** |  | 
**due_date_notes_automatic** | **bool** | Whether the current notes match the server default for this due date. | 
**due_date_notes_template** | **str** | Localized default notes containing the literal %{due_date} placeholder. | 
**purchase_order_number** | **str** |  | 
**notes** | **str** |  | 
**reminders** | **bool** |  | 
**persisted** | **bool** |  | 
**sent_at** | **datetime** |  | 
**delivery_pending** | **bool** | A delivery attempt is queued or running; the schedule year remains reserved. | 
**status** | **str** |  | 
**payment_received** | **datetime** |  | 
**legacy** | **bool** | A persisted non-draft invoice with no known send date and no pending delivery. Editing is allowed; sending again requires explicit resend. | 
**hints** | [**AdminInvoiceFormHints**](AdminInvoiceFormHints.md) |  | 
**recipients** | [**List[AdminInvoiceFormRecipientsInner]**](AdminInvoiceFormRecipientsInner.md) | The invoice&#39;s own billing addresses: the only people it and its reminders are emailed to. On a prefill these are the account&#39;s contacts, not yet saved (id is null). | 
**account_contacts** | [**List[AdminInvoiceFormAccountContactsInner]**](AdminInvoiceFormAccountContactsInner.md) | The account&#39;s usual contacts (billing addresses plus account admins who haven&#39;t opted out of invoice emails), offered when adding a recipient. | 
**skipped_contacts** | **List[str]** | Emails of account contacts left out of recipients and account_contacts because an invoice can&#39;t be emailed to them (e.g. an admin address a billing address rejects). Worth a warning. | 
**default_message** | **str** | A suggested Review-and-send message; &#x60;message&#x60; on POST .../send overrides it for that send only. | 
**schedule** | [**List[AdminInvoiceFormScheduleInner]**](AdminInvoiceFormScheduleInner.md) | The subscription&#39;s other years, for the sidebar (empty for a legacy invoice with no subscription_year). | 
**service_periods** | [**List[AdminInvoiceFormServicePeriodsInner]**](AdminInvoiceFormServicePeriodsInner.md) | Every year of the subscription, in order, offered as the Service period select. | 
**settled_invoice** | [**AdminInvoiceFormSettledInvoice**](AdminInvoiceFormSettledInvoice.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_form import AdminInvoiceForm

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceForm from a JSON string
admin_invoice_form_instance = AdminInvoiceForm.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceForm.to_json())

# convert the object into a dict
admin_invoice_form_dict = admin_invoice_form_instance.to_dict()
# create an instance of AdminInvoiceForm from a dict
admin_invoice_form_from_dict = AdminInvoiceForm.from_dict(admin_invoice_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


