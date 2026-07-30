# FrsExportConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_mode** | **str** |  | 
**conference_id** | **int** |  | 
**school_group_id** | **int** |  | 
**school_ids** | **List[int]** |  | 
**sport_ids** | **List[int]** |  | 
**financial_year** | **int** |  | 
**filename** | **str** |  | 
**seeded_from_conference_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.frs_export_config import FrsExportConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FrsExportConfig from a JSON string
frs_export_config_instance = FrsExportConfig.from_json(json)
# print the JSON string representation of the object
print(FrsExportConfig.to_json())

# convert the object into a dict
frs_export_config_dict = frs_export_config_instance.to_dict()
# create an instance of FrsExportConfig from a dict
frs_export_config_from_dict = FrsExportConfig.from_dict(frs_export_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


