# QuartilesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**sport** | **str** |  | [optional] 
**year_str** | **str** |  | 
**coach_comp_cents** | **int** |  | 
**rows** | [**List[QuartileRow]**](QuartileRow.md) |  | 

## Example

```python
from winthrop_client_python.models.quartiles_data import QuartilesData

# TODO update the JSON string below
json = "{}"
# create an instance of QuartilesData from a JSON string
quartiles_data_instance = QuartilesData.from_json(json)
# print the JSON string representation of the object
print(QuartilesData.to_json())

# convert the object into a dict
quartiles_data_dict = quartiles_data_instance.to_dict()
# create an instance of QuartilesData from a dict
quartiles_data_from_dict = QuartilesData.from_dict(quartiles_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


