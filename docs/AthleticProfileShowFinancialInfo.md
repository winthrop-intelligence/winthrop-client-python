# AthleticProfileShowFinancialInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**total_student_enrollment** | **int** |  | [optional] 
**male_students** | **int** |  | [optional] 
**female_students** | **int** |  | [optional] 
**student_athlete_enrollment** | **int** |  | [optional] 
**male_athletes** | **int** |  | [optional] 
**female_athletes** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_financial_info import AthleticProfileShowFinancialInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowFinancialInfo from a JSON string
athletic_profile_show_financial_info_instance = AthleticProfileShowFinancialInfo.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowFinancialInfo.to_json())

# convert the object into a dict
athletic_profile_show_financial_info_dict = athletic_profile_show_financial_info_instance.to_dict()
# create an instance of AthleticProfileShowFinancialInfo from a dict
athletic_profile_show_financial_info_from_dict = AthleticProfileShowFinancialInfo.from_dict(athletic_profile_show_financial_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


