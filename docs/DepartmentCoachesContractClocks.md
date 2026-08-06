# DepartmentCoachesContractClocks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**horizon_months** | **int** |  | 
**renewal_window_months** | **int** |  | 
**rows** | [**List[DepartmentCoachesClockRow]**](DepartmentCoachesClockRow.md) |  | 
**all_seats** | [**List[DepartmentCoachesClockRow]**](DepartmentCoachesClockRow.md) |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_contract_clocks import DepartmentCoachesContractClocks

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesContractClocks from a JSON string
department_coaches_contract_clocks_instance = DepartmentCoachesContractClocks.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesContractClocks.to_json())

# convert the object into a dict
department_coaches_contract_clocks_dict = department_coaches_contract_clocks_instance.to_dict()
# create an instance of DepartmentCoachesContractClocks from a dict
department_coaches_contract_clocks_from_dict = DepartmentCoachesContractClocks.from_dict(department_coaches_contract_clocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


