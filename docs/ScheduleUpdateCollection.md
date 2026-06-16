# ScheduleUpdateCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScheduleUpdate]**](ScheduleUpdate.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_update_collection import ScheduleUpdateCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUpdateCollection from a JSON string
schedule_update_collection_instance = ScheduleUpdateCollection.from_json(json)
# print the JSON string representation of the object
print(ScheduleUpdateCollection.to_json())

# convert the object into a dict
schedule_update_collection_dict = schedule_update_collection_instance.to_dict()
# create an instance of ScheduleUpdateCollection from a dict
schedule_update_collection_from_dict = ScheduleUpdateCollection.from_dict(schedule_update_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


