# AdminInvoiceFormScheduleInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_number** | **int** |  | 
**amount_cents** | **int** | The same suggested amount as the prefill&#39;s amount_cents for that year. | 
**label** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_schedule_inner import AdminInvoiceFormScheduleInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormScheduleInner from a JSON string
admin_invoice_form_schedule_inner_instance = AdminInvoiceFormScheduleInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormScheduleInner.to_json())

# convert the object into a dict
admin_invoice_form_schedule_inner_dict = admin_invoice_form_schedule_inner_instance.to_dict()
# create an instance of AdminInvoiceFormScheduleInner from a dict
admin_invoice_form_schedule_inner_from_dict = AdminInvoiceFormScheduleInner.from_dict(admin_invoice_form_schedule_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


