# AdminFinancialsQcRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**ncca_pdf** | **str** |  | [optional] 
**audited_pdf** | **str** |  | [optional] 
**nca_csv** | **str** |  | [optional] 
**school_info_csv** | **str** |  | [optional] 
**sport_stats_csv** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_financials_qc_row import AdminFinancialsQcRow

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFinancialsQcRow from a JSON string
admin_financials_qc_row_instance = AdminFinancialsQcRow.from_json(json)
# print the JSON string representation of the object
print(AdminFinancialsQcRow.to_json())

# convert the object into a dict
admin_financials_qc_row_dict = admin_financials_qc_row_instance.to_dict()
# create an instance of AdminFinancialsQcRow from a dict
admin_financials_qc_row_from_dict = AdminFinancialsQcRow.from_dict(admin_financials_qc_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


