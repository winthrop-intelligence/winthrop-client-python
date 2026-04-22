# UploadItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**uploaded_by** | **str** |  | [optional] 
**created_at** | **str** | Pre-formatted date string in the user&#39;s timezone | [optional] 

## Example

```python
from winthrop_client_python.models.upload_item import UploadItem

# TODO update the JSON string below
json = "{}"
# create an instance of UploadItem from a JSON string
upload_item_instance = UploadItem.from_json(json)
# print the JSON string representation of the object
print(UploadItem.to_json())

# convert the object into a dict
upload_item_dict = upload_item_instance.to_dict()
# create an instance of UploadItem from a dict
upload_item_from_dict = UploadItem.from_dict(upload_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


