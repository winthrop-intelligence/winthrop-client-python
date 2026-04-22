# UploadDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**uploaded_by** | **str** |  | [optional] 
**created_at** | **str** | Pre-formatted date string in the user&#39;s timezone | [optional] 
**has_file** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.upload_detail import UploadDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UploadDetail from a JSON string
upload_detail_instance = UploadDetail.from_json(json)
# print the JSON string representation of the object
print(UploadDetail.to_json())

# convert the object into a dict
upload_detail_dict = upload_detail_instance.to_dict()
# create an instance of UploadDetail from a dict
upload_detail_from_dict = UploadDetail.from_dict(upload_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


