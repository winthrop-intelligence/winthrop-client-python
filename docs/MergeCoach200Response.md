# MergeCoach200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**primary_coach_id** | **int** |  | [optional] 
**duplicate_coach_id** | **int** |  | [optional] 
**failure_reason** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.merge_coach200_response import MergeCoach200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MergeCoach200Response from a JSON string
merge_coach200_response_instance = MergeCoach200Response.from_json(json)
# print the JSON string representation of the object
print(MergeCoach200Response.to_json())

# convert the object into a dict
merge_coach200_response_dict = merge_coach200_response_instance.to_dict()
# create an instance of MergeCoach200Response from a dict
merge_coach200_response_from_dict = MergeCoach200Response.from_dict(merge_coach200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


