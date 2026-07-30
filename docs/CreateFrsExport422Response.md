# CreateFrsExport422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_frs_export422_response import CreateFrsExport422Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFrsExport422Response from a JSON string
create_frs_export422_response_instance = CreateFrsExport422Response.from_json(json)
# print the JSON string representation of the object
print(CreateFrsExport422Response.to_json())

# convert the object into a dict
create_frs_export422_response_dict = create_frs_export422_response_instance.to_dict()
# create an instance of CreateFrsExport422Response from a dict
create_frs_export422_response_from_dict = CreateFrsExport422Response.from_dict(create_frs_export422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


