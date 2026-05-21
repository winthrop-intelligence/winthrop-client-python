# CoachCompensationTabQuartiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**position_name** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**year_str** | **str** |  | [optional] 
**coach_total_comp_cents** | **int** |  | 
**rows** | [**List[CoachCompensationTabQuartilesRowsInner]**](CoachCompensationTabQuartilesRowsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_quartiles import CoachCompensationTabQuartiles

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabQuartiles from a JSON string
coach_compensation_tab_quartiles_instance = CoachCompensationTabQuartiles.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabQuartiles.to_json())

# convert the object into a dict
coach_compensation_tab_quartiles_dict = coach_compensation_tab_quartiles_instance.to_dict()
# create an instance of CoachCompensationTabQuartiles from a dict
coach_compensation_tab_quartiles_from_dict = CoachCompensationTabQuartiles.from_dict(coach_compensation_tab_quartiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


