# EadaInstitutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **bool** |  | 
**year** | **int** |  | 
**match_status** | **str** |  | [optional] 
**match_reason** | **str** |  | [optional] 
**unitid** | **int** |  | [optional] 
**metrics** | [**List[EadaNormalizedMetric]**](EadaNormalizedMetric.md) |  | [optional] 
**source_payload** | **object** | Only present when include&#x3D;source_payload was requested by an authorized viewer | [optional] 

## Example

```python
from winthrop_client_python.models.eada_institution_result import EadaInstitutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of EadaInstitutionResult from a JSON string
eada_institution_result_instance = EadaInstitutionResult.from_json(json)
# print the JSON string representation of the object
print(EadaInstitutionResult.to_json())

# convert the object into a dict
eada_institution_result_dict = eada_institution_result_instance.to_dict()
# create an instance of EadaInstitutionResult from a dict
eada_institution_result_from_dict = EadaInstitutionResult.from_dict(eada_institution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


