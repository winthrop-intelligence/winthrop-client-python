# DepartmentOverviewFlowSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earns** | [**DepartmentFinancialsRankLine**](DepartmentFinancialsRankLine.md) |  | 
**spends** | [**DepartmentFinancialsRankLine**](DepartmentFinancialsRankLine.md) |  | 
**keeps** | [**DepartmentFinancialsRankLine**](DepartmentFinancialsRankLine.md) |  | 
**debt_share** | **float** | Debt service as a percentage of total expenses | 

## Example

```python
from winthrop_client_python.models.department_overview_flow_summary import DepartmentOverviewFlowSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewFlowSummary from a JSON string
department_overview_flow_summary_instance = DepartmentOverviewFlowSummary.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewFlowSummary.to_json())

# convert the object into a dict
department_overview_flow_summary_dict = department_overview_flow_summary_instance.to_dict()
# create an instance of DepartmentOverviewFlowSummary from a dict
department_overview_flow_summary_from_dict = DepartmentOverviewFlowSummary.from_dict(department_overview_flow_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


