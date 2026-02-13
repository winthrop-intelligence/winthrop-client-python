# DealSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deal_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**deal_type_name** | **str** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**vendor_names** | **List[str]** |  | [optional] 
**start_year** | **int** |  | [optional] 
**end_year** | **int** |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**summary** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_search_result import DealSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DealSearchResult from a JSON string
deal_search_result_instance = DealSearchResult.from_json(json)
# print the JSON string representation of the object
print(DealSearchResult.to_json())

# convert the object into a dict
deal_search_result_dict = deal_search_result_instance.to_dict()
# create an instance of DealSearchResult from a dict
deal_search_result_from_dict = DealSearchResult.from_dict(deal_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


