# FrsResolvedPopulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[FrsResolvedSchool]**](FrsResolvedSchool.md) |  | 
**selected_count** | **int** |  | 
**in_frs_scope_count** | **int** |  | 
**included_count** | **int** |  | 
**private_count** | **int** |  | 
**license_excluded_count** | **int** |  | 
**license_excluded_names** | **List[str]** |  | 
**missing_filing_count** | **int** |  | 
**membership_basis** | **str** |  | 
**data_refreshed_at** | **date** |  | 

## Example

```python
from winthrop_client_python.models.frs_resolved_population import FrsResolvedPopulation

# TODO update the JSON string below
json = "{}"
# create an instance of FrsResolvedPopulation from a JSON string
frs_resolved_population_instance = FrsResolvedPopulation.from_json(json)
# print the JSON string representation of the object
print(FrsResolvedPopulation.to_json())

# convert the object into a dict
frs_resolved_population_dict = frs_resolved_population_instance.to_dict()
# create an instance of FrsResolvedPopulation from a dict
frs_resolved_population_from_dict = FrsResolvedPopulation.from_dict(frs_resolved_population_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


