# PageView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**route** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.page_view import PageView

# TODO update the JSON string below
json = "{}"
# create an instance of PageView from a JSON string
page_view_instance = PageView.from_json(json)
# print the JSON string representation of the object
print(PageView.to_json())

# convert the object into a dict
page_view_dict = page_view_instance.to_dict()
# create an instance of PageView from a dict
page_view_from_dict = PageView.from_dict(page_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


