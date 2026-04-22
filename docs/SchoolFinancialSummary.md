# SchoolFinancialSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**years** | **List[int]** |  | [optional] 
**school_info** | [**SchoolInfo**](SchoolInfo.md) |  | [optional] 
**student_fee_per_student** | **float** |  | [optional] 
**ncaa_report_id** | **int** |  | [optional] 
**audited_report_id** | **int** |  | [optional] 
**revenues** | [**List[SchoolFinancialGroup]**](SchoolFinancialGroup.md) |  | [optional] 
**expenses** | [**List[SchoolFinancialGroup]**](SchoolFinancialGroup.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_summary import SchoolFinancialSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialSummary from a JSON string
school_financial_summary_instance = SchoolFinancialSummary.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialSummary.to_json())

# convert the object into a dict
school_financial_summary_dict = school_financial_summary_instance.to_dict()
# create an instance of SchoolFinancialSummary from a dict
school_financial_summary_from_dict = SchoolFinancialSummary.from_dict(school_financial_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


