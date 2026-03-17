# CoworkerTenure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | 
**start_year** | **int** |  | 
**end_year** | **int** |  | 
**school_id** | **int** |  | 
**coaches** | [**List[CoworkerEntry]**](CoworkerEntry.md) |  | 
**total_coaches** | **int** |  | 
**administrators** | [**List[CoworkerEntry]**](CoworkerEntry.md) |  | 
**total_administrators** | **int** |  | 

## Example

```python
from winthrop_client_python.models.coworker_tenure import CoworkerTenure

# TODO update the JSON string below
json = "{}"
# create an instance of CoworkerTenure from a JSON string
coworker_tenure_instance = CoworkerTenure.from_json(json)
# print the JSON string representation of the object
print(CoworkerTenure.to_json())

# convert the object into a dict
coworker_tenure_dict = coworker_tenure_instance.to_dict()
# create an instance of CoworkerTenure from a dict
coworker_tenure_from_dict = CoworkerTenure.from_dict(coworker_tenure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


