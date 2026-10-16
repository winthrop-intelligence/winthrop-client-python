# PrefillAdminInvoice422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | 
**subscription_id** | **int** | Subscription whose annual schedule must be split and saved. | 

## Example

```python
from winthrop_client_python.models.prefill_admin_invoice422_response import PrefillAdminInvoice422Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillAdminInvoice422Response from a JSON string
prefill_admin_invoice422_response_instance = PrefillAdminInvoice422Response.from_json(json)
# print the JSON string representation of the object
print(PrefillAdminInvoice422Response.to_json())

# convert the object into a dict
prefill_admin_invoice422_response_dict = prefill_admin_invoice422_response_instance.to_dict()
# create an instance of PrefillAdminInvoice422Response from a dict
prefill_admin_invoice422_response_from_dict = PrefillAdminInvoice422Response.from_dict(prefill_admin_invoice422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


