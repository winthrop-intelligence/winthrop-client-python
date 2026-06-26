# GamePostAvailabilityCollectionGroupsInnerPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_post_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**var_date** | **date** | The school&#39;s most recent posted date in this bucket; null for a fully flexible post. | [optional] 
**last_rpi** | **int** |  | [optional] 
**last_net_rank** | **int** |  | [optional] 
**avg_rpi** | **int** |  | [optional] 
**avg_net_rank** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_availability_collection_groups_inner_posts_inner import GamePostAvailabilityCollectionGroupsInnerPostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostAvailabilityCollectionGroupsInnerPostsInner from a JSON string
game_post_availability_collection_groups_inner_posts_inner_instance = GamePostAvailabilityCollectionGroupsInnerPostsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostAvailabilityCollectionGroupsInnerPostsInner.to_json())

# convert the object into a dict
game_post_availability_collection_groups_inner_posts_inner_dict = game_post_availability_collection_groups_inner_posts_inner_instance.to_dict()
# create an instance of GamePostAvailabilityCollectionGroupsInnerPostsInner from a dict
game_post_availability_collection_groups_inner_posts_inner_from_dict = GamePostAvailabilityCollectionGroupsInnerPostsInner.from_dict(game_post_availability_collection_groups_inner_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


