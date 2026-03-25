# ColiData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_salary_cents** | **int** |  | 
**city** | **str** |  | 

## Example

```python
from winthrop_client_python.models.coli_data import ColiData

# TODO update the JSON string below
json = "{}"
# create an instance of ColiData from a JSON string
coli_data_instance = ColiData.from_json(json)
# print the JSON string representation of the object
print(ColiData.to_json())

# convert the object into a dict
coli_data_dict = coli_data_instance.to_dict()
# create an instance of ColiData from a dict
coli_data_from_dict = ColiData.from_dict(coli_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


