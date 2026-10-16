# AdminInvoiceRow

One row, whichever of the two things it actually is: a real Invoice (Sent/Paid/All) or a subscription_year with no sent/paid invoice yet (Not sent, and the same rows again inside All). `key` is stable either way — \"invoice-<id>\" once an Invoice exists for the row (even an unsent draft), \"syear-<id>\" otherwise. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**account_id** | **int** |  | 
**account_name** | **str** |  | 
**subscription_type_name** | **str** | The row&#39;s agreement type as the subscription pages name it (name_display). Null on a legacy agreement with no type. | 
**autorenew** | **bool** | The agreement&#39;s Auto-renew flag. | 
**access_active** | **bool** | The agreement&#39;s active (access) flag, the Sales Report&#39;s Current State. Not a billing flag. | 
**renewing** | **bool** | The agreement&#39;s Might renew? box. False is what the list tags Leaving. | 
**legacy** | **bool** | An Invoice sent before send dates were recorded. | 
**year_number** | **int** |  | 
**amount_cents** | **int** | The invoice&#39;s own amount, else what the schedule suggests billing for the year. A legacy (backfilled) row stores the ANNUAL rate, so the suggestion is that rate times the months the row covers over 12 (a six-month row at $12,000 a year suggests $6,000). Null when the legacy amount cannot be told (a row longer than a year, or shorter than a month), even when has_price is true. | 
**has_price** | **bool** | The invoice or its schedule year carries a price. True with a null amount_cents means the amount needs checking against the agreement; false means the schedule has no price yet. | 
**due_date** | **date** |  | 
**sent_at** | **datetime** |  | 
**sent_label** | **str** | \&quot;Not sent\&quot; | \&quot;Queued\&quot; | \&quot;Sent &lt;date&gt;\&quot; | \&quot;Sent · date unknown\&quot; (legacy, no sent_at) | 
**invoice_id** | **int** | The invoice behind the row (a draft counts); null for a schedule year with no invoice yet. | 
**never_sent** | **bool** | Nothing has gone to the customer yet (no sent_at, and not an old invoice that predates send dates) and no first send is queued. It does not read the clock: the client tags a row Never sent when this is true and the row is due before the viewer&#39;s today. | 
**notes** | **str** | The invoice&#39;s whole notes text as written (line breaks kept, not capped). Null when blank or no invoice. | 
**notes_preview** | **str** | One line of the notes for the list, starting at the LAST M/D/YY or M/D/YYYY date stamp (month 1-12, day 1-31, not glued to a word, number or slash) and running to the end. A note with no stamp previews as its first characters. Whitespace is collapsed and the line is capped at 200 characters plus an ellipsis. Null when notes is null. | 
**status_kind** | **str** | paid | sending | pending | draft_saved | no_draft | needs_schedule | needs_split. Sending means a queued delivery attempt; pending means a sent invoice awaiting payment. needs_split applies to an explicit schedule period longer than a year. | 
**status_label** | **str** |  | 
**action** | [**AdminInvoiceRowAction**](AdminInvoiceRowAction.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_row import AdminInvoiceRow

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceRow from a JSON string
admin_invoice_row_instance = AdminInvoiceRow.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceRow.to_json())

# convert the object into a dict
admin_invoice_row_dict = admin_invoice_row_instance.to_dict()
# create an instance of AdminInvoiceRow from a dict
admin_invoice_row_from_dict = AdminInvoiceRow.from_dict(admin_invoice_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


