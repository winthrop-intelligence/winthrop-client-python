# AdminScraperArgumentDef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**description** | **str** | Markdown help text for the argument | [optional] 
**required** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.admin_scraper_argument_def import AdminScraperArgumentDef

# TODO update the JSON string below
json = "{}"
# create an instance of AdminScraperArgumentDef from a JSON string
admin_scraper_argument_def_instance = AdminScraperArgumentDef.from_json(json)
# print the JSON string representation of the object
print(AdminScraperArgumentDef.to_json())

# convert the object into a dict
admin_scraper_argument_def_dict = admin_scraper_argument_def_instance.to_dict()
# create an instance of AdminScraperArgumentDef from a dict
admin_scraper_argument_def_from_dict = AdminScraperArgumentDef.from_dict(admin_scraper_argument_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


