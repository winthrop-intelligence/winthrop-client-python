# NewsFeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**source_type** | **str** |  | [optional] 
**links** | [**LinkCollection**](LinkCollection.md) |  | [optional] 
**tags_list** | [**LinkCollection1**](LinkCollection1.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.news_feed import NewsFeed

# TODO update the JSON string below
json = "{}"
# create an instance of NewsFeed from a JSON string
news_feed_instance = NewsFeed.from_json(json)
# print the JSON string representation of the object
print(NewsFeed.to_json())

# convert the object into a dict
news_feed_dict = news_feed_instance.to_dict()
# create an instance of NewsFeed from a dict
news_feed_from_dict = NewsFeed.from_dict(news_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


