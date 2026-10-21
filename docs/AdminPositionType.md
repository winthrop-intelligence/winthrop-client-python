# AdminPositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 
**ord** | **int** |  | 
**group_stub** | **bool** |  | 
**force_display_title** | **bool** |  | 
**intercollegiate_only** | **bool** |  | 
**visible** | **bool** | Whether the position type is published to customer catalogs | 
**position_type_group_id** | **int** |  | 
**position_type_category_id** | **int** |  | 
**positions_count** | **int** | Number of coach positions currently assigned this position type | 
**position_type_group** | [**AdminPositionTypeGroupSummary**](AdminPositionTypeGroupSummary.md) |  | 
**position_type_category** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_type import AdminPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionType from a JSON string
admin_position_type_instance = AdminPositionType.from_json(json)
# print the JSON string representation of the object
print(AdminPositionType.to_json())

# convert the object into a dict
admin_position_type_dict = admin_position_type_instance.to_dict()
# create an instance of AdminPositionType from a dict
admin_position_type_from_dict = AdminPositionType.from_dict(admin_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


