# NewerSeasonContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | Recorded position season, expressed as its ending year | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**school_short_name** | **str** |  | 
**conference_name** | **str** |  | 
**position_title** | **str** |  | 
**compensation_cents** | **int** | Positive total compensation for this position season only; null when missing or unauthorized | 

## Example

```python
from winthrop_client_python.models.newer_season_context import NewerSeasonContext

# TODO update the JSON string below
json = "{}"
# create an instance of NewerSeasonContext from a JSON string
newer_season_context_instance = NewerSeasonContext.from_json(json)
# print the JSON string representation of the object
print(NewerSeasonContext.to_json())

# convert the object into a dict
newer_season_context_dict = newer_season_context_instance.to_dict()
# create an instance of NewerSeasonContext from a dict
newer_season_context_from_dict = NewerSeasonContext.from_dict(newer_season_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


