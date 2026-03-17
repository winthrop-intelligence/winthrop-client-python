# QuartileRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**percent_rank** | **str** |  | 
**q25** | **int** |  | 
**q50** | **int** |  | 
**q75** | **int** |  | 
**q100** | **int** |  | 

## Example

```python
from winthrop_client_python.models.quartile_row import QuartileRow

# TODO update the JSON string below
json = "{}"
# create an instance of QuartileRow from a JSON string
quartile_row_instance = QuartileRow.from_json(json)
# print the JSON string representation of the object
print(QuartileRow.to_json())

# convert the object into a dict
quartile_row_dict = quartile_row_instance.to_dict()
# create an instance of QuartileRow from a dict
quartile_row_from_dict = QuartileRow.from_dict(quartile_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


