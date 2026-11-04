# AdminScraper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Scraper name; may contain dots | 
**title** | **str** |  | 
**description** | **str** | Markdown description of the scraper | [optional] 
**argument_defs** | [**List[AdminScraperArgumentDef]**](AdminScraperArgumentDef.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_scraper import AdminScraper

# TODO update the JSON string below
json = "{}"
# create an instance of AdminScraper from a JSON string
admin_scraper_instance = AdminScraper.from_json(json)
# print the JSON string representation of the object
print(AdminScraper.to_json())

# convert the object into a dict
admin_scraper_dict = admin_scraper_instance.to_dict()
# create an instance of AdminScraper from a dict
admin_scraper_from_dict = AdminScraper.from_dict(admin_scraper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


