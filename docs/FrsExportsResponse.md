# FrsExportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exports** | [**List[FrsExport]**](FrsExport.md) |  | 

## Example

```python
from winthrop_client_python.models.frs_exports_response import FrsExportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FrsExportsResponse from a JSON string
frs_exports_response_instance = FrsExportsResponse.from_json(json)
# print the JSON string representation of the object
print(FrsExportsResponse.to_json())

# convert the object into a dict
frs_exports_response_dict = frs_exports_response_instance.to_dict()
# create an instance of FrsExportsResponse from a dict
frs_exports_response_from_dict = FrsExportsResponse.from_dict(frs_exports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


