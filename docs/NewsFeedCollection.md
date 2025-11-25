# NewsFeedCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NewsFeed]**](NewsFeed.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.news_feed_collection import NewsFeedCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NewsFeedCollection from a JSON string
news_feed_collection_instance = NewsFeedCollection.from_json(json)
# print the JSON string representation of the object
print(NewsFeedCollection.to_json())

# convert the object into a dict
news_feed_collection_dict = news_feed_collection_instance.to_dict()
# create an instance of NewsFeedCollection from a dict
news_feed_collection_from_dict = NewsFeedCollection.from_dict(news_feed_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


