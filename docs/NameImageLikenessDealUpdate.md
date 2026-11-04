# NameImageLikenessDealUpdate

NIL deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_annual_avg** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**total_guar** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.name_image_likeness_deal_update import NameImageLikenessDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NameImageLikenessDealUpdate from a JSON string
name_image_likeness_deal_update_instance = NameImageLikenessDealUpdate.from_json(json)
# print the JSON string representation of the object
print(NameImageLikenessDealUpdate.to_json())

# convert the object into a dict
name_image_likeness_deal_update_dict = name_image_likeness_deal_update_instance.to_dict()
# create an instance of NameImageLikenessDealUpdate from a dict
name_image_likeness_deal_update_from_dict = NameImageLikenessDealUpdate.from_dict(name_image_likeness_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


