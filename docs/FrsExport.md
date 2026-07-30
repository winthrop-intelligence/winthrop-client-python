# FrsExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**status_detail** | **str** |  | 
**sport_names** | **List[str]** |  | 
**included_school_names** | **List[str]** |  | 
**selected_count** | **int** |  | 
**included_count** | **int** |  | 
**financial_year** | **int** |  | 
**created_at** | **datetime** |  | 
**download_url** | **str** |  | 
**config** | [**FrsExportConfig**](FrsExportConfig.md) |  | 

## Example

```python
from winthrop_client_python.models.frs_export import FrsExport

# TODO update the JSON string below
json = "{}"
# create an instance of FrsExport from a JSON string
frs_export_instance = FrsExport.from_json(json)
# print the JSON string representation of the object
print(FrsExport.to_json())

# convert the object into a dict
frs_export_dict = frs_export_instance.to_dict()
# create an instance of FrsExport from a dict
frs_export_from_dict = FrsExport.from_dict(frs_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


