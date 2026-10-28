# AdminScraperRunningJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**active** | **int** |  | [optional] 
**succeeded** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_scraper_running_job import AdminScraperRunningJob

# TODO update the JSON string below
json = "{}"
# create an instance of AdminScraperRunningJob from a JSON string
admin_scraper_running_job_instance = AdminScraperRunningJob.from_json(json)
# print the JSON string representation of the object
print(AdminScraperRunningJob.to_json())

# convert the object into a dict
admin_scraper_running_job_dict = admin_scraper_running_job_instance.to_dict()
# create an instance of AdminScraperRunningJob from a dict
admin_scraper_running_job_from_dict = AdminScraperRunningJob.from_dict(admin_scraper_running_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


