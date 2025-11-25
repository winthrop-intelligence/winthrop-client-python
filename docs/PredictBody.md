# PredictBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.predict_body import PredictBody

# TODO update the JSON string below
json = "{}"
# create an instance of PredictBody from a JSON string
predict_body_instance = PredictBody.from_json(json)
# print the JSON string representation of the object
print(PredictBody.to_json())

# convert the object into a dict
predict_body_dict = predict_body_instance.to_dict()
# create an instance of PredictBody from a dict
predict_body_from_dict = PredictBody.from_dict(predict_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


