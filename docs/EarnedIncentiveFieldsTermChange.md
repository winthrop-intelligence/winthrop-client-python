# EarnedIncentiveFieldsTermChange

non_cash extensions only

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years_added** | **int** |  | 
**new_end_date** | **date** | May be left out or null when the extension sets no new date | [optional] 

## Example

```python
from winthrop_client_python.models.earned_incentive_fields_term_change import EarnedIncentiveFieldsTermChange

# TODO update the JSON string below
json = "{}"
# create an instance of EarnedIncentiveFieldsTermChange from a JSON string
earned_incentive_fields_term_change_instance = EarnedIncentiveFieldsTermChange.from_json(json)
# print the JSON string representation of the object
print(EarnedIncentiveFieldsTermChange.to_json())

# convert the object into a dict
earned_incentive_fields_term_change_dict = earned_incentive_fields_term_change_instance.to_dict()
# create an instance of EarnedIncentiveFieldsTermChange from a dict
earned_incentive_fields_term_change_from_dict = EarnedIncentiveFieldsTermChange.from_dict(earned_incentive_fields_term_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


