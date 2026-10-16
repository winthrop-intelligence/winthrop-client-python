# AdminContactLatestPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**sport_name_display** | **str** |  | [optional] 
**position_name_display** | **str** |  | [optional] 
**departing** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_contact_latest_positions_inner import AdminContactLatestPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContactLatestPositionsInner from a JSON string
admin_contact_latest_positions_inner_instance = AdminContactLatestPositionsInner.from_json(json)
# print the JSON string representation of the object
print(AdminContactLatestPositionsInner.to_json())

# convert the object into a dict
admin_contact_latest_positions_inner_dict = admin_contact_latest_positions_inner_instance.to_dict()
# create an instance of AdminContactLatestPositionsInner from a dict
admin_contact_latest_positions_inner_from_dict = AdminContactLatestPositionsInner.from_dict(admin_contact_latest_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


