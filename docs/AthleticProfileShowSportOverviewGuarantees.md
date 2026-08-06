# AthleticProfileShowSportOverviewGuarantees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreements_count** | **int** |  | [optional] 
**priced_count** | **int** | Agreements whose amount is filed (not comp_tbd) | [optional] 
**out_cents** | **int** |  | [optional] 
**in_cents** | **int** |  | [optional] 
**all_on_file** | **bool** |  | [optional] 
**upcoming** | [**List[AthleticProfileShowSportOverviewGuaranteesUpcomingInner]**](AthleticProfileShowSportOverviewGuaranteesUpcomingInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview_guarantees import AthleticProfileShowSportOverviewGuarantees

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverviewGuarantees from a JSON string
athletic_profile_show_sport_overview_guarantees_instance = AthleticProfileShowSportOverviewGuarantees.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverviewGuarantees.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_guarantees_dict = athletic_profile_show_sport_overview_guarantees_instance.to_dict()
# create an instance of AthleticProfileShowSportOverviewGuarantees from a dict
athletic_profile_show_sport_overview_guarantees_from_dict = AthleticProfileShowSportOverviewGuarantees.from_dict(athletic_profile_show_sport_overview_guarantees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


