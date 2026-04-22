# SchoolFinancialGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_id** | **str** |  | [optional] 
**football** | **int** |  | [optional] 
**basketball_m** | **int** |  | [optional] 
**basketball_w** | **int** |  | [optional] 
**other** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_group import SchoolFinancialGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialGroup from a JSON string
school_financial_group_instance = SchoolFinancialGroup.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialGroup.to_json())

# convert the object into a dict
school_financial_group_dict = school_financial_group_instance.to_dict()
# create an instance of SchoolFinancialGroup from a dict
school_financial_group_from_dict = SchoolFinancialGroup.from_dict(school_financial_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


