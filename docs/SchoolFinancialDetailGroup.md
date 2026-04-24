# SchoolFinancialDetailGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_id** | **str** |  | [optional] 
**cashflow_type** | **str** |  | [optional] 
**report_label** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_detail_group import SchoolFinancialDetailGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialDetailGroup from a JSON string
school_financial_detail_group_instance = SchoolFinancialDetailGroup.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialDetailGroup.to_json())

# convert the object into a dict
school_financial_detail_group_dict = school_financial_detail_group_instance.to_dict()
# create an instance of SchoolFinancialDetailGroup from a dict
school_financial_detail_group_from_dict = SchoolFinancialDetailGroup.from_dict(school_financial_detail_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


