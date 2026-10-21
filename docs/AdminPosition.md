# AdminPosition

A per-coach, per-season position assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season_id** | **int** |  | 
**coach_id** | **int** |  | 
**title** | **str** |  | 
**departing** | **bool** |  | 
**departing_set_at** | **datetime** |  | 
**departure_on** | **date** | WINAD-10656 departure date (YYYY-MM-DD); empty for a position departed without one | 
**departure_reason** | **str** |  | 
**departure_source_url** | **str** |  | 
**creation_reason** | **str** |  | 
**creation_reason_updated_at** | **datetime** |  | 
**article_link** | **str** |  | 
**article_title** | **str** |  | 
**article_description** | **str** |  | 
**article_site_name** | **str** |  | 
**article_publish_time** | **datetime** |  | 
**article_image_url** | **str** |  | 
**compensation_id** | **int** |  | 
**position_type_ids** | **List[int]** |  | 
**position_types_name_display** | **str** |  | 
**season** | [**AdminPositionSeasonSummary**](AdminPositionSeasonSummary.md) |  | 
**coach** | [**AdminPositionCoachSummary**](AdminPositionCoachSummary.md) |  | 
**compensation** | [**AdminPositionCompensationSummary**](AdminPositionCompensationSummary.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_position import AdminPosition

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPosition from a JSON string
admin_position_instance = AdminPosition.from_json(json)
# print the JSON string representation of the object
print(AdminPosition.to_json())

# convert the object into a dict
admin_position_dict = admin_position_instance.to_dict()
# create an instance of AdminPosition from a dict
admin_position_from_dict = AdminPosition.from_dict(admin_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


