# AdminFinancialsQcList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminFinancialsQcListMeta**](AdminFinancialsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminFinancialsQcRow]**](AdminFinancialsQcRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_financials_qc_list import AdminFinancialsQcList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFinancialsQcList from a JSON string
admin_financials_qc_list_instance = AdminFinancialsQcList.from_json(json)
# print the JSON string representation of the object
print(AdminFinancialsQcList.to_json())

# convert the object into a dict
admin_financials_qc_list_dict = admin_financials_qc_list_instance.to_dict()
# create an instance of AdminFinancialsQcList from a dict
admin_financials_qc_list_from_dict = AdminFinancialsQcList.from_dict(admin_financials_qc_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


