# DeskHtmlFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Original .html filename | 
**byte_size** | **int** |  | 
**uploaded_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from winthrop_client_python.models.desk_html_file import DeskHtmlFile

# TODO update the JSON string below
json = "{}"
# create an instance of DeskHtmlFile from a JSON string
desk_html_file_instance = DeskHtmlFile.from_json(json)
# print the JSON string representation of the object
print(DeskHtmlFile.to_json())

# convert the object into a dict
desk_html_file_dict = desk_html_file_instance.to_dict()
# create an instance of DeskHtmlFile from a dict
desk_html_file_from_dict = DeskHtmlFile.from_dict(desk_html_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


