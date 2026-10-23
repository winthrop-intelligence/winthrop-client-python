# DealErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** | Attribute (school_id, deal_type, vendor_id, file, drive_id, change_note, base; for a publish a field path such as deal.end_on or deal_detail.partner) mapped to its messages. | 

## Example

```python
from winthrop_client_python.models.deal_errors_response import DealErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DealErrorsResponse from a JSON string
deal_errors_response_instance = DealErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(DealErrorsResponse.to_json())

# convert the object into a dict
deal_errors_response_dict = deal_errors_response_instance.to_dict()
# create an instance of DealErrorsResponse from a dict
deal_errors_response_from_dict = DealErrorsResponse.from_dict(deal_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


