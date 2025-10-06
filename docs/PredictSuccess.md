# PredictSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_athletic** | **bool** |  | [optional] 
**model** | **str** |  | [optional] 
**probability** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.predict_success import PredictSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of PredictSuccess from a JSON string
predict_success_instance = PredictSuccess.from_json(json)
# print the JSON string representation of the object
print(PredictSuccess.to_json())

# convert the object into a dict
predict_success_dict = predict_success_instance.to_dict()
# create an instance of PredictSuccess from a dict
predict_success_form_dict = predict_success.from_dict(predict_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


