# CtbCompensationAppliedException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | 
**compensation_id** | **int** |  | 
**role** | **str** |  | 
**actions** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_applied_exception import CtbCompensationAppliedException

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationAppliedException from a JSON string
ctb_compensation_applied_exception_instance = CtbCompensationAppliedException.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationAppliedException.to_json())

# convert the object into a dict
ctb_compensation_applied_exception_dict = ctb_compensation_applied_exception_instance.to_dict()
# create an instance of CtbCompensationAppliedException from a dict
ctb_compensation_applied_exception_from_dict = CtbCompensationAppliedException.from_dict(ctb_compensation_applied_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


