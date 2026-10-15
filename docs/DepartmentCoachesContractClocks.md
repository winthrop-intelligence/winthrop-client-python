# DepartmentCoachesContractClocks

Every row is a contract on the clock. Seats and assistants with no contract on file are left out of both lists, and so are contracts that have already ended: the clock is measured from today whatever season is selected, so a historical season keeps only the deals still running now. Either list can be empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**horizon_months** | **int** |  | 
**renewal_window_months** | **int** |  | 
**rows** | [**List[DepartmentCoachesClockRow]**](DepartmentCoachesClockRow.md) | Head-coach seats and grouped assistant deals, most urgent first. | 
**all_seats** | [**List[DepartmentCoachesClockRow]**](DepartmentCoachesClockRow.md) | One row per head-coach seat whose contract is on the clock. A seat with no contract on file, or whose contract has already ended, has no row, so this can be shorter than &#x60;seat_count&#x60;; the contract-on-file fact lives on the seat (&#x60;pay.has_filed_contract&#x60;). | 

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


