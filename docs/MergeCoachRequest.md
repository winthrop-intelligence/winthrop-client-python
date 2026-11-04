# MergeCoachRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_coach_id** | **int** | ID of the duplicate coach to merge in | 
**change_note** | **str** | Optional reason, stored on every version the merge writes | [optional] 

## Example

```python
from winthrop_client_python.models.merge_coach_request import MergeCoachRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeCoachRequest from a JSON string
merge_coach_request_instance = MergeCoachRequest.from_json(json)
# print the JSON string representation of the object
print(MergeCoachRequest.to_json())

# convert the object into a dict
merge_coach_request_dict = merge_coach_request_instance.to_dict()
# create an instance of MergeCoachRequest from a dict
merge_coach_request_from_dict = MergeCoachRequest.from_dict(merge_coach_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


