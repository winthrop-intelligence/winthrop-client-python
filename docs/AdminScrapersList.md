# AdminScrapersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminScraper]**](AdminScraper.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_scrapers_list import AdminScrapersList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminScrapersList from a JSON string
admin_scrapers_list_instance = AdminScrapersList.from_json(json)
# print the JSON string representation of the object
print(AdminScrapersList.to_json())

# convert the object into a dict
admin_scrapers_list_dict = admin_scrapers_list_instance.to_dict()
# create an instance of AdminScrapersList from a dict
admin_scrapers_list_from_dict = AdminScrapersList.from_dict(admin_scrapers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


