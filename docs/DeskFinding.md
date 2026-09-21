# DeskFinding

One desk-report v1 finding (doc/desk/report-markup.md §10) — a 07.1 row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**severity** | **str** |  | 
**message** | **str** |  | 
**line** | **int** |  | 
**node_hint** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_finding import DeskFinding

# TODO update the JSON string below
json = "{}"
# create an instance of DeskFinding from a JSON string
desk_finding_instance = DeskFinding.from_json(json)
# print the JSON string representation of the object
print(DeskFinding.to_json())

# convert the object into a dict
desk_finding_dict = desk_finding_instance.to_dict()
# create an instance of DeskFinding from a dict
desk_finding_from_dict = DeskFinding.from_dict(desk_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


