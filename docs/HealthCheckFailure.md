# HealthCheckFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.health_check_failure import HealthCheckFailure

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckFailure from a JSON string
health_check_failure_instance = HealthCheckFailure.from_json(json)
# print the JSON string representation of the object
print(HealthCheckFailure.to_json())

# convert the object into a dict
health_check_failure_dict = health_check_failure_instance.to_dict()
# create an instance of HealthCheckFailure from a dict
health_check_failure_form_dict = health_check_failure.from_dict(health_check_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


