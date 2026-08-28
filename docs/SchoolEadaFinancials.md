# SchoolEadaFinancials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**requested_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**institution** | [**EadaInstitutionResult**](EadaInstitutionResult.md) |  | [optional] 
**sports** | [**SchoolEadaFinancialsSports**](SchoolEadaFinancialsSports.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_eada_financials import SchoolEadaFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolEadaFinancials from a JSON string
school_eada_financials_instance = SchoolEadaFinancials.from_json(json)
# print the JSON string representation of the object
print(SchoolEadaFinancials.to_json())

# convert the object into a dict
school_eada_financials_dict = school_eada_financials_instance.to_dict()
# create an instance of SchoolEadaFinancials from a dict
school_eada_financials_from_dict = SchoolEadaFinancials.from_dict(school_eada_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


