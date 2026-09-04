# EadaSportResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_code** | **str** |  | 
**sport_name** | **str** |  | [optional] 
**match_status** | **str** |  | [optional] 
**mapping_status** | **str** | Eada::SportMapping status for this source sport code (mapped/ambiguous/unmapped/unknown) | 
**metrics** | [**List[EadaNormalizedMetric]**](EadaNormalizedMetric.md) |  | [optional] 
**source_payload** | **object** |  | [optional] 

## Example

```python
from winthrop_client_python.models.eada_sport_result_item import EadaSportResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of EadaSportResultItem from a JSON string
eada_sport_result_item_instance = EadaSportResultItem.from_json(json)
# print the JSON string representation of the object
print(EadaSportResultItem.to_json())

# convert the object into a dict
eada_sport_result_item_dict = eada_sport_result_item_instance.to_dict()
# create an instance of EadaSportResultItem from a dict
eada_sport_result_item_from_dict = EadaSportResultItem.from_dict(eada_sport_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


