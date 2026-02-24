# SportCompensationSubdivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**compensations** | [**List[CompensationRow]**](CompensationRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.sport_compensation_subdivision import SportCompensationSubdivision

# TODO update the JSON string below
json = "{}"
# create an instance of SportCompensationSubdivision from a JSON string
sport_compensation_subdivision_instance = SportCompensationSubdivision.from_json(json)
# print the JSON string representation of the object
print(SportCompensationSubdivision.to_json())

# convert the object into a dict
sport_compensation_subdivision_dict = sport_compensation_subdivision_instance.to_dict()
# create an instance of SportCompensationSubdivision from a dict
sport_compensation_subdivision_from_dict = SportCompensationSubdivision.from_dict(sport_compensation_subdivision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


