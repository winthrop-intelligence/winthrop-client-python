# AthleticProfileShowGuaranteesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**year** | **str** |  | [optional] 
**compensation_cents** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_guarantees_inner import AthleticProfileShowGuaranteesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowGuaranteesInner from a JSON string
athletic_profile_show_guarantees_inner_instance = AthleticProfileShowGuaranteesInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowGuaranteesInner.to_json())

# convert the object into a dict
athletic_profile_show_guarantees_inner_dict = athletic_profile_show_guarantees_inner_instance.to_dict()
# create an instance of AthleticProfileShowGuaranteesInner from a dict
athletic_profile_show_guarantees_inner_from_dict = AthleticProfileShowGuaranteesInner.from_dict(athletic_profile_show_guarantees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


