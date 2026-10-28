# CreateSeasonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**sport_id** | **int** |  | 
**year** | **int** | Season-ending year (2025-26 is 2026) | 
**change_note** | **str** | Why the Season was missing; stored on the create&#39;s audit version | [optional] 

## Example

```python
from winthrop_client_python.models.create_season_request import CreateSeasonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSeasonRequest from a JSON string
create_season_request_instance = CreateSeasonRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSeasonRequest.to_json())

# convert the object into a dict
create_season_request_dict = create_season_request_instance.to_dict()
# create an instance of CreateSeasonRequest from a dict
create_season_request_from_dict = CreateSeasonRequest.from_dict(create_season_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


