# CoachSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Coach ID | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**position_types** | **List[str]** |  | [optional] 
**compensation_cents** | **int** | Total compensation in cents (included based on authorization) | [optional] 
**base_salary_cents** | **int** | Base salary in cents (included based on authorization) | [optional] 
**adjusted_comp_cents** | **int** | Cost-of-living adjusted compensation in cents (included based on authorization) | [optional] 
**contract_expires_on** | **date** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_search_result import CoachSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSearchResult from a JSON string
coach_search_result_instance = CoachSearchResult.from_json(json)
# print the JSON string representation of the object
print(CoachSearchResult.to_json())

# convert the object into a dict
coach_search_result_dict = coach_search_result_instance.to_dict()
# create an instance of CoachSearchResult from a dict
coach_search_result_from_dict = CoachSearchResult.from_dict(coach_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


