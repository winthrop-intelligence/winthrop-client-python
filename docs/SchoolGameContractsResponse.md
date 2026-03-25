# SchoolGameContractsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolGameContractsResponseSchool**](SchoolGameContractsResponseSchool.md) |  | [optional] 
**sports** | [**List[SchoolSportSection]**](SchoolSportSection.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_game_contracts_response import SchoolGameContractsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolGameContractsResponse from a JSON string
school_game_contracts_response_instance = SchoolGameContractsResponse.from_json(json)
# print the JSON string representation of the object
print(SchoolGameContractsResponse.to_json())

# convert the object into a dict
school_game_contracts_response_dict = school_game_contracts_response_instance.to_dict()
# create an instance of SchoolGameContractsResponse from a dict
school_game_contracts_response_from_dict = SchoolGameContractsResponse.from_dict(school_game_contracts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


