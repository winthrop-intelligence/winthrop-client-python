# ScraperArgDef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.scraper_arg_def import ScraperArgDef

# TODO update the JSON string below
json = "{}"
# create an instance of ScraperArgDef from a JSON string
scraper_arg_def_instance = ScraperArgDef.from_json(json)
# print the JSON string representation of the object
print ScraperArgDef.to_json()

# convert the object into a dict
scraper_arg_def_dict = scraper_arg_def_instance.to_dict()
# create an instance of ScraperArgDef from a dict
scraper_arg_def_form_dict = scraper_arg_def.from_dict(scraper_arg_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


