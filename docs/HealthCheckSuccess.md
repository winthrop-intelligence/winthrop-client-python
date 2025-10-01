# HealthCheckSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**model** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.health_check_success import HealthCheckSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckSuccess from a JSON string
health_check_success_instance = HealthCheckSuccess.from_json(json)
# print the JSON string representation of the object
print(HealthCheckSuccess.to_json())

# convert the object into a dict
health_check_success_dict = health_check_success_instance.to_dict()
# create an instance of HealthCheckSuccess from a dict
health_check_success_form_dict = health_check_success.from_dict(health_check_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


