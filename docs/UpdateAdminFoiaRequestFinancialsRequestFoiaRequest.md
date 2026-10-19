# UpdateAdminFoiaRequestFinancialsRequestFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ncaa_financial_report_status_ids** | **List[int]** |  | [optional] 
**audited_financial_report_status_ids** | **List[int]** |  | [optional] 
**ncaa_financial_report_status_years** | **List[int]** |  | [optional] 
**audited_financial_report_status_years** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_request_financials_request_foia_request import UpdateAdminFoiaRequestFinancialsRequestFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaRequestFinancialsRequestFoiaRequest from a JSON string
update_admin_foia_request_financials_request_foia_request_instance = UpdateAdminFoiaRequestFinancialsRequestFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaRequestFinancialsRequestFoiaRequest.to_json())

# convert the object into a dict
update_admin_foia_request_financials_request_foia_request_dict = update_admin_foia_request_financials_request_foia_request_instance.to_dict()
# create an instance of UpdateAdminFoiaRequestFinancialsRequestFoiaRequest from a dict
update_admin_foia_request_financials_request_foia_request_from_dict = UpdateAdminFoiaRequestFinancialsRequestFoiaRequest.from_dict(update_admin_foia_request_financials_request_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


