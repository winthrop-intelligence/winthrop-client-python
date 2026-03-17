# CoachCompensationTabSidebar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracts** | [**List[CoachCompensationTabSidebarContractsInner]**](CoachCompensationTabSidebarContractsInner.md) |  | [optional] 
**income_reports** | [**List[CoachCompensationTabSidebarIncomeReportsInner]**](CoachCompensationTabSidebarIncomeReportsInner.md) |  | [optional] 
**coaching_staff** | [**List[CoachCompensationTabSidebarCoachingStaffInner]**](CoachCompensationTabSidebarCoachingStaffInner.md) |  | [optional] 
**staff_title** | **str** |  | [optional] 
**asst_pool_spend_cents** | **int** |  | [optional] 
**coli** | [**ColiData**](ColiData.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_sidebar import CoachCompensationTabSidebar

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabSidebar from a JSON string
coach_compensation_tab_sidebar_instance = CoachCompensationTabSidebar.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabSidebar.to_json())

# convert the object into a dict
coach_compensation_tab_sidebar_dict = coach_compensation_tab_sidebar_instance.to_dict()
# create an instance of CoachCompensationTabSidebar from a dict
coach_compensation_tab_sidebar_from_dict = CoachCompensationTabSidebar.from_dict(coach_compensation_tab_sidebar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


