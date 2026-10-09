# DeskActivityMetaPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**requested_from** | **datetime** |  | 
**var_from** | **datetime** |  | 
**to** | **datetime** |  | 
**timezone** | **str** |  | 
**interval** | **str** |  | 
**across_versions** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.desk_activity_meta_period import DeskActivityMetaPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityMetaPeriod from a JSON string
desk_activity_meta_period_instance = DeskActivityMetaPeriod.from_json(json)
# print the JSON string representation of the object
print(DeskActivityMetaPeriod.to_json())

# convert the object into a dict
desk_activity_meta_period_dict = desk_activity_meta_period_instance.to_dict()
# create an instance of DeskActivityMetaPeriod from a dict
desk_activity_meta_period_from_dict = DeskActivityMetaPeriod.from_dict(desk_activity_meta_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


