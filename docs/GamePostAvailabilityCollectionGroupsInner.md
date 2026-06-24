# GamePostAvailabilityCollectionGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**count** | **int** | Total posts in the bucket (subtitle count) | [optional] 
**posts** | [**List[GamePostAvailabilityCollectionGroupsInnerPostsInner]**](GamePostAvailabilityCollectionGroupsInnerPostsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_availability_collection_groups_inner import GamePostAvailabilityCollectionGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostAvailabilityCollectionGroupsInner from a JSON string
game_post_availability_collection_groups_inner_instance = GamePostAvailabilityCollectionGroupsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostAvailabilityCollectionGroupsInner.to_json())

# convert the object into a dict
game_post_availability_collection_groups_inner_dict = game_post_availability_collection_groups_inner_instance.to_dict()
# create an instance of GamePostAvailabilityCollectionGroupsInner from a dict
game_post_availability_collection_groups_inner_from_dict = GamePostAvailabilityCollectionGroupsInner.from_dict(game_post_availability_collection_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


