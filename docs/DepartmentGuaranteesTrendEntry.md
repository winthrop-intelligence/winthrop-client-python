# DepartmentGuaranteesTrendEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | 
**out_total_cents** | **int** |  | 
**out_count** | **int** |  | 
**provisional** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_trend_entry import DepartmentGuaranteesTrendEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesTrendEntry from a JSON string
department_guarantees_trend_entry_instance = DepartmentGuaranteesTrendEntry.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesTrendEntry.to_json())

# convert the object into a dict
department_guarantees_trend_entry_dict = department_guarantees_trend_entry_instance.to_dict()
# create an instance of DepartmentGuaranteesTrendEntry from a dict
department_guarantees_trend_entry_from_dict = DepartmentGuaranteesTrendEntry.from_dict(department_guarantees_trend_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


