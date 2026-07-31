# CreateFrsExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_mode** | **str** |  | 
**conference_id** | **int** |  | [optional] 
**school_group_id** | **int** |  | [optional] 
**financial_year** | **int** |  | 
**filename** | **str** |  | 
**seeded_from_conference_id** | **int** |  | [optional] 
**school_ids** | **List[int]** |  | [optional] 
**sport_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.create_frs_export_request import CreateFrsExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFrsExportRequest from a JSON string
create_frs_export_request_instance = CreateFrsExportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFrsExportRequest.to_json())

# convert the object into a dict
create_frs_export_request_dict = create_frs_export_request_instance.to_dict()
# create an instance of CreateFrsExportRequest from a dict
create_frs_export_request_from_dict = CreateFrsExportRequest.from_dict(create_frs_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


