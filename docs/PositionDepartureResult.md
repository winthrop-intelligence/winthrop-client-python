# PositionDepartureResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**departing** | **bool** |  | [optional] 
**departing_set_at** | **datetime** |  | [optional] 
**departure_on** | **date** |  | [optional] 
**departure_reason** | **str** |  | [optional] 
**departure_source_url** | **str** |  | [optional] 
**approval_quote** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_departure_result import PositionDepartureResult

# TODO update the JSON string below
json = "{}"
# create an instance of PositionDepartureResult from a JSON string
position_departure_result_instance = PositionDepartureResult.from_json(json)
# print the JSON string representation of the object
print(PositionDepartureResult.to_json())

# convert the object into a dict
position_departure_result_dict = position_departure_result_instance.to_dict()
# create an instance of PositionDepartureResult from a dict
position_departure_result_from_dict = PositionDepartureResult.from_dict(position_departure_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


