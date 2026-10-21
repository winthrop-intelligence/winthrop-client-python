# AdminFinancialStat

A single school/sport/season financial stat row (admin namespace)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**sport** | [**IdName**](IdName.md) |  | [optional] 
**equivalencies** | **float** |  | [optional] 
**athletic_aid_equivalency** | **float** |  | [optional] 
**exhausted_eligibility_or_medical_equivalency** | **float** |  | [optional] 
**students_receiving_athletic_aid** | **int** |  | [optional] 
**head_coach_positions** | **int** |  | [optional] 
**head_coach_fte** | **float** |  | [optional] 
**assistant_coach_positions** | **int** |  | [optional] 
**assistant_coach_fte** | **float** |  | [optional] 
**first_team_participants** | **int** |  | [optional] 
**second_team_participants** | **int** |  | [optional] 
**third_team_participants** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_financial_stat import AdminFinancialStat

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFinancialStat from a JSON string
admin_financial_stat_instance = AdminFinancialStat.from_json(json)
# print the JSON string representation of the object
print(AdminFinancialStat.to_json())

# convert the object into a dict
admin_financial_stat_dict = admin_financial_stat_instance.to_dict()
# create an instance of AdminFinancialStat from a dict
admin_financial_stat_from_dict = AdminFinancialStat.from_dict(admin_financial_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


