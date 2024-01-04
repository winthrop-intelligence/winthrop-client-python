# Scraper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.scraper import Scraper

# TODO update the JSON string below
json = "{}"
# create an instance of Scraper from a JSON string
scraper_instance = Scraper.from_json(json)
# print the JSON string representation of the object
print Scraper.to_json()

# convert the object into a dict
scraper_dict = scraper_instance.to_dict()
# create an instance of Scraper from a dict
scraper_form_dict = scraper.from_dict(scraper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


