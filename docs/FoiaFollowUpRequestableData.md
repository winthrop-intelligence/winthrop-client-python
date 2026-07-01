# FoiaFollowUpRequestableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_requestable_data import FoiaFollowUpRequestableData

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpRequestableData from a JSON string
foia_follow_up_requestable_data_instance = FoiaFollowUpRequestableData.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpRequestableData.to_json())

# convert the object into a dict
foia_follow_up_requestable_data_dict = foia_follow_up_requestable_data_instance.to_dict()
# create an instance of FoiaFollowUpRequestableData from a dict
foia_follow_up_requestable_data_from_dict = FoiaFollowUpRequestableData.from_dict(foia_follow_up_requestable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


