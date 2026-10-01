# EnrichGamePostSearchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pairs** | **List[List[int]]** | The loaded page&#39;s [school_id, sport_id, season_year] card keys. A two-element [school_id, sport_id] pair (a client from before per-post seasons) reads the sport&#39;s scheduling target season. Malformed or non-positive keys are ignored; duplicates are de-duped. | 

## Example

```python
from winthrop_client_python.models.enrich_game_post_searches_request import EnrichGamePostSearchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichGamePostSearchesRequest from a JSON string
enrich_game_post_searches_request_instance = EnrichGamePostSearchesRequest.from_json(json)
# print the JSON string representation of the object
print(EnrichGamePostSearchesRequest.to_json())

# convert the object into a dict
enrich_game_post_searches_request_dict = enrich_game_post_searches_request_instance.to_dict()
# create an instance of EnrichGamePostSearchesRequest from a dict
enrich_game_post_searches_request_from_dict = EnrichGamePostSearchesRequest.from_dict(enrich_game_post_searches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


