# VideoDealUpdate

Video Mgmt deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sports** | [**List[ApparelDealUpdateSportsInner]**](ApparelDealUpdateSportsInner.md) | Sport IDs or case-insensitive display names; an empty array clears all sports. | [optional] 
**annual_host_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.video_deal_update import VideoDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VideoDealUpdate from a JSON string
video_deal_update_instance = VideoDealUpdate.from_json(json)
# print the JSON string representation of the object
print(VideoDealUpdate.to_json())

# convert the object into a dict
video_deal_update_dict = video_deal_update_instance.to_dict()
# create an instance of VideoDealUpdate from a dict
video_deal_update_from_dict = VideoDealUpdate.from_dict(video_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


