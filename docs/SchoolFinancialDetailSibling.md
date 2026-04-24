# SchoolFinancialDetailSibling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_id** | **str** |  | [optional] 
**report_label** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_detail_sibling import SchoolFinancialDetailSibling

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialDetailSibling from a JSON string
school_financial_detail_sibling_instance = SchoolFinancialDetailSibling.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialDetailSibling.to_json())

# convert the object into a dict
school_financial_detail_sibling_dict = school_financial_detail_sibling_instance.to_dict()
# create an instance of SchoolFinancialDetailSibling from a dict
school_financial_detail_sibling_from_dict = SchoolFinancialDetailSibling.from_dict(school_financial_detail_sibling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


