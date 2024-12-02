# AverageCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**mode** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.average_compensation import AverageCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of AverageCompensation from a JSON string
average_compensation_instance = AverageCompensation.from_json(json)
# print the JSON string representation of the object
print(AverageCompensation.to_json())

# convert the object into a dict
average_compensation_dict = average_compensation_instance.to_dict()
# create an instance of AverageCompensation from a dict
average_compensation_form_dict = average_compensation.from_dict(average_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


