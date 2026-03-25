# ConferenceDirectorsCupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **List[int]** |  | [optional] 
**schools** | [**List[DirectorsCupSchool]**](DirectorsCupSchool.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.conference_directors_cup_response import ConferenceDirectorsCupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceDirectorsCupResponse from a JSON string
conference_directors_cup_response_instance = ConferenceDirectorsCupResponse.from_json(json)
# print the JSON string representation of the object
print(ConferenceDirectorsCupResponse.to_json())

# convert the object into a dict
conference_directors_cup_response_dict = conference_directors_cup_response_instance.to_dict()
# create an instance of ConferenceDirectorsCupResponse from a dict
conference_directors_cup_response_from_dict = ConferenceDirectorsCupResponse.from_dict(conference_directors_cup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


