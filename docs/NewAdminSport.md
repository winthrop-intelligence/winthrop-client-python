# NewAdminSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_of_years** | [**List[TimeOfYearOption]**](TimeOfYearOption.md) | The selectable times of year for the form&#39;s select | 

## Example

```python
from winthrop_client_python.models.new_admin_sport import NewAdminSport

# TODO update the JSON string below
json = "{}"
# create an instance of NewAdminSport from a JSON string
new_admin_sport_instance = NewAdminSport.from_json(json)
# print the JSON string representation of the object
print(NewAdminSport.to_json())

# convert the object into a dict
new_admin_sport_dict = new_admin_sport_instance.to_dict()
# create an instance of NewAdminSport from a dict
new_admin_sport_from_dict = NewAdminSport.from_dict(new_admin_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


