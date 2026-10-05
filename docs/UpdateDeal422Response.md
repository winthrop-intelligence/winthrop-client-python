# UpdateDeal422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** | Field paths such as deal.verified or deal_detail.grf mapped to errors. | [optional] 

## Example

```python
from winthrop_client_python.models.update_deal422_response import UpdateDeal422Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeal422Response from a JSON string
update_deal422_response_instance = UpdateDeal422Response.from_json(json)
# print the JSON string representation of the object
print(UpdateDeal422Response.to_json())

# convert the object into a dict
update_deal422_response_dict = update_deal422_response_instance.to_dict()
# create an instance of UpdateDeal422Response from a dict
update_deal422_response_from_dict = UpdateDeal422Response.from_dict(update_deal422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


