# CreateSportRequestSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**name_aka** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**gender_code** | **str** |  | [optional] 
**time_of_year_id** | **int** |  | [optional] 
**emerging** | **bool** |  | [optional] 
**meet_sport** | **bool** |  | [optional] 
**visible** | **bool** | Whether the sport is published to customer catalogs | [optional] 
**ncaa_id** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_sport_request_sport import CreateSportRequestSport

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSportRequestSport from a JSON string
create_sport_request_sport_instance = CreateSportRequestSport.from_json(json)
# print the JSON string representation of the object
print(CreateSportRequestSport.to_json())

# convert the object into a dict
create_sport_request_sport_dict = create_sport_request_sport_instance.to_dict()
# create an instance of CreateSportRequestSport from a dict
create_sport_request_sport_from_dict = CreateSportRequestSport.from_dict(create_sport_request_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


