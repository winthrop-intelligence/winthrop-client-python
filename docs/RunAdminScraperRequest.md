# RunAdminScraperRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scraper** | **Dict[str, str]** | Argument values keyed by the scraper&#39;s declared argument names | [optional] 

## Example

```python
from winthrop_client_python.models.run_admin_scraper_request import RunAdminScraperRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunAdminScraperRequest from a JSON string
run_admin_scraper_request_instance = RunAdminScraperRequest.from_json(json)
# print the JSON string representation of the object
print(RunAdminScraperRequest.to_json())

# convert the object into a dict
run_admin_scraper_request_dict = run_admin_scraper_request_instance.to_dict()
# create an instance of RunAdminScraperRequest from a dict
run_admin_scraper_request_from_dict = RunAdminScraperRequest.from_dict(run_admin_scraper_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


