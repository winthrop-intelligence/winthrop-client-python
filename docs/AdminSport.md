# AdminSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_aka** | **str** |  | 
**name_display** | **str** |  | 
**gender_code** | **str** | M or W; null for a sport without one | 
**time_of_year_id** | **int** |  | 
**time_of_year** | [**AdminSportTimeOfYear**](AdminSportTimeOfYear.md) |  | 
**emerging** | **bool** |  | 
**meet_sport** | **bool** |  | 
**visible** | **bool** | Whether the sport is published to customer catalogs | 
**ncaa_id** | **str** |  | 
**positions_count** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_sport import AdminSport

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSport from a JSON string
admin_sport_instance = AdminSport.from_json(json)
# print the JSON string representation of the object
print(AdminSport.to_json())

# convert the object into a dict
admin_sport_dict = admin_sport_instance.to_dict()
# create an instance of AdminSport from a dict
admin_sport_from_dict = AdminSport.from_dict(admin_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


