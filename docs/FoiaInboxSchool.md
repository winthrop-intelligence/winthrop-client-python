# FoiaInboxSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**admin_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**alternate_names** | **List[Dict[str, object]]** |  | [optional] 
**state** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**portal_site** | **str** |  | [optional] 
**contacts** | **List[Dict[str, object]]** |  | [optional] 
**notes** | [**List[FoiaInboxNote]**](FoiaInboxNote.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_school import FoiaInboxSchool

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxSchool from a JSON string
foia_inbox_school_instance = FoiaInboxSchool.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxSchool.to_json())

# convert the object into a dict
foia_inbox_school_dict = foia_inbox_school_instance.to_dict()
# create an instance of FoiaInboxSchool from a dict
foia_inbox_school_from_dict = FoiaInboxSchool.from_dict(foia_inbox_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


