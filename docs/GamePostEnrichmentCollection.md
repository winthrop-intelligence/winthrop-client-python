# GamePostEnrichmentCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GamePostEnrichment]**](GamePostEnrichment.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_enrichment_collection import GamePostEnrichmentCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostEnrichmentCollection from a JSON string
game_post_enrichment_collection_instance = GamePostEnrichmentCollection.from_json(json)
# print the JSON string representation of the object
print(GamePostEnrichmentCollection.to_json())

# convert the object into a dict
game_post_enrichment_collection_dict = game_post_enrichment_collection_instance.to_dict()
# create an instance of GamePostEnrichmentCollection from a dict
game_post_enrichment_collection_from_dict = GamePostEnrichmentCollection.from_dict(game_post_enrichment_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


