# AdminScraperJobsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | [**List[AdminScraperRunningJob]**](AdminScraperRunningJob.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_scraper_jobs_list import AdminScraperJobsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminScraperJobsList from a JSON string
admin_scraper_jobs_list_instance = AdminScraperJobsList.from_json(json)
# print the JSON string representation of the object
print(AdminScraperJobsList.to_json())

# convert the object into a dict
admin_scraper_jobs_list_dict = admin_scraper_jobs_list_instance.to_dict()
# create an instance of AdminScraperJobsList from a dict
admin_scraper_jobs_list_from_dict = AdminScraperJobsList.from_dict(admin_scraper_jobs_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


