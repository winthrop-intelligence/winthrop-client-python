# CompensationRow

A single head coach or AD compensation record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**total_comp** | **int** |  | [optional] 
**base_salary** | **int** |  | [optional] 
**talent_fee** | **float** |  | [optional] 
**outside_income** | **int** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**car_provided** | **bool** |  | [optional] 
**country_club** | **bool** |  | [optional] 
**buyout_terms** | **str** |  | [optional] 
**contract_end** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.compensation_row import CompensationRow

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationRow from a JSON string
compensation_row_instance = CompensationRow.from_json(json)
# print the JSON string representation of the object
print(CompensationRow.to_json())

# convert the object into a dict
compensation_row_dict = compensation_row_instance.to_dict()
# create an instance of CompensationRow from a dict
compensation_row_from_dict = CompensationRow.from_dict(compensation_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


