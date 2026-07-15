# GamePostEnrichmentScheduleIntentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**game_types** | **List[str]** | Deal-type designations for this availability day, as raw GameType *name* strings (e.g. \&quot;HomeAndHome\&quot;). Never includes \&quot;Pending\&quot;. | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_enrichment_schedule_intents_inner import GamePostEnrichmentScheduleIntentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostEnrichmentScheduleIntentsInner from a JSON string
game_post_enrichment_schedule_intents_inner_instance = GamePostEnrichmentScheduleIntentsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostEnrichmentScheduleIntentsInner.to_json())

# convert the object into a dict
game_post_enrichment_schedule_intents_inner_dict = game_post_enrichment_schedule_intents_inner_instance.to_dict()
# create an instance of GamePostEnrichmentScheduleIntentsInner from a dict
game_post_enrichment_schedule_intents_inner_from_dict = GamePostEnrichmentScheduleIntentsInner.from_dict(game_post_enrichment_schedule_intents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


