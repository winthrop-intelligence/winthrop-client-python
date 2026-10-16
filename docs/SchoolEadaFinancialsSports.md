# SchoolEadaFinancialsSports


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**items** | [**List[EadaSportResultItem]**](EadaSportResultItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_eada_financials_sports import SchoolEadaFinancialsSports

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolEadaFinancialsSports from a JSON string
school_eada_financials_sports_instance = SchoolEadaFinancialsSports.from_json(json)
# print the JSON string representation of the object
print(SchoolEadaFinancialsSports.to_json())

# convert the object into a dict
school_eada_financials_sports_dict = school_eada_financials_sports_instance.to_dict()
# create an instance of SchoolEadaFinancialsSports from a dict
school_eada_financials_sports_from_dict = SchoolEadaFinancialsSports.from_dict(school_eada_financials_sports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


