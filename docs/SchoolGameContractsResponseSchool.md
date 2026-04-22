# SchoolGameContractsResponseSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_game_contracts_response_school import SchoolGameContractsResponseSchool

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolGameContractsResponseSchool from a JSON string
school_game_contracts_response_school_instance = SchoolGameContractsResponseSchool.from_json(json)
# print the JSON string representation of the object
print(SchoolGameContractsResponseSchool.to_json())

# convert the object into a dict
school_game_contracts_response_school_dict = school_game_contracts_response_school_instance.to_dict()
# create an instance of SchoolGameContractsResponseSchool from a dict
school_game_contracts_response_school_from_dict = SchoolGameContractsResponseSchool.from_dict(school_game_contracts_response_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


