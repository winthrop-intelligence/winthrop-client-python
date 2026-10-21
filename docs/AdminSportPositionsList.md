# AdminSportPositionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminSportPosition]**](AdminSportPosition.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 
**sport** | [**AdminSportReportSummary**](AdminSportReportSummary.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_sport_positions_list import AdminSportPositionsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSportPositionsList from a JSON string
admin_sport_positions_list_instance = AdminSportPositionsList.from_json(json)
# print the JSON string representation of the object
print(AdminSportPositionsList.to_json())

# convert the object into a dict
admin_sport_positions_list_dict = admin_sport_positions_list_instance.to_dict()
# create an instance of AdminSportPositionsList from a dict
admin_sport_positions_list_from_dict = AdminSportPositionsList.from_dict(admin_sport_positions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


