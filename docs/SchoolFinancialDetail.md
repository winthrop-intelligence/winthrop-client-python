# SchoolFinancialDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**group** | [**SchoolFinancialDetailGroup**](SchoolFinancialDetailGroup.md) |  | [optional] 
**total** | **int** |  | [optional] 
**sports** | [**List[SchoolFinancialDetailSport]**](SchoolFinancialDetailSport.md) |  | [optional] 
**siblings** | [**List[SchoolFinancialDetailSibling]**](SchoolFinancialDetailSibling.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_detail import SchoolFinancialDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialDetail from a JSON string
school_financial_detail_instance = SchoolFinancialDetail.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialDetail.to_json())

# convert the object into a dict
school_financial_detail_dict = school_financial_detail_instance.to_dict()
# create an instance of SchoolFinancialDetail from a dict
school_financial_detail_from_dict = SchoolFinancialDetail.from_dict(school_financial_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


