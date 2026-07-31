# FrsSchoolSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[FrsResolvedSchool]**](FrsResolvedSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.frs_school_search_response import FrsSchoolSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FrsSchoolSearchResponse from a JSON string
frs_school_search_response_instance = FrsSchoolSearchResponse.from_json(json)
# print the JSON string representation of the object
print(FrsSchoolSearchResponse.to_json())

# convert the object into a dict
frs_school_search_response_dict = frs_school_search_response_instance.to_dict()
# create an instance of FrsSchoolSearchResponse from a dict
frs_school_search_response_from_dict = FrsSchoolSearchResponse.from_dict(frs_school_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


