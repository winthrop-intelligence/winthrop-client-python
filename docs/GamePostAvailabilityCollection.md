# GamePostAvailabilityCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_name** | **str** |  | [optional] 
**total_active** | **int** | The sport&#39;s full active-post total (headline count) | [optional] 
**groups** | [**List[GamePostAvailabilityCollectionGroupsInner]**](GamePostAvailabilityCollectionGroupsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_availability_collection import GamePostAvailabilityCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostAvailabilityCollection from a JSON string
game_post_availability_collection_instance = GamePostAvailabilityCollection.from_json(json)
# print the JSON string representation of the object
print(GamePostAvailabilityCollection.to_json())

# convert the object into a dict
game_post_availability_collection_dict = game_post_availability_collection_instance.to_dict()
# create an instance of GamePostAvailabilityCollection from a dict
game_post_availability_collection_from_dict = GamePostAvailabilityCollection.from_dict(game_post_availability_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


