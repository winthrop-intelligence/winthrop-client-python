# SchoolFinancialDetailSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_name** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_financial_detail_sport import SchoolFinancialDetailSport

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolFinancialDetailSport from a JSON string
school_financial_detail_sport_instance = SchoolFinancialDetailSport.from_json(json)
# print the JSON string representation of the object
print(SchoolFinancialDetailSport.to_json())

# convert the object into a dict
school_financial_detail_sport_dict = school_financial_detail_sport_instance.to_dict()
# create an instance of SchoolFinancialDetailSport from a dict
school_financial_detail_sport_from_dict = SchoolFinancialDetailSport.from_dict(school_financial_detail_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


