# DossierReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leadership** | **str** |  | 
**university_state** | **str** |  | 

## Example

```python
from winthrop_client_python.models.dossier_report_response import DossierReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DossierReportResponse from a JSON string
dossier_report_response_instance = DossierReportResponse.from_json(json)
# print the JSON string representation of the object
print(DossierReportResponse.to_json())

# convert the object into a dict
dossier_report_response_dict = dossier_report_response_instance.to_dict()
# create an instance of DossierReportResponse from a dict
dossier_report_response_from_dict = DossierReportResponse.from_dict(dossier_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


