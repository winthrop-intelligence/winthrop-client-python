# AdminFoiaRequestFinancialsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**data** | [**List[AdminFoiaRequestFinancialYear]**](AdminFoiaRequestFinancialYear.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_financials_list import AdminFoiaRequestFinancialsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestFinancialsList from a JSON string
admin_foia_request_financials_list_instance = AdminFoiaRequestFinancialsList.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestFinancialsList.to_json())

# convert the object into a dict
admin_foia_request_financials_list_dict = admin_foia_request_financials_list_instance.to_dict()
# create an instance of AdminFoiaRequestFinancialsList from a dict
admin_foia_request_financials_list_from_dict = AdminFoiaRequestFinancialsList.from_dict(admin_foia_request_financials_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


