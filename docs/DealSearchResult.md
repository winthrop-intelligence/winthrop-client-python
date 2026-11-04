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
**end_at** | **datetime** |  | [optional] 
**start_on** | **date** | The deal&#39;s start date as a plain calendar date (YYYY-MM-DD): the UTC calendar date of the stored start_at/end_at instant, the same in every reader&#39;s time zone. Additive; the timestamp field next to it is unchanged. | [optional] 
**end_on** | **date** | The deal&#39;s end date as a plain calendar date (YYYY-MM-DD): the UTC calendar date of the stored start_at/end_at instant, the same in every reader&#39;s time zone. Additive; the timestamp field next to it is unchanged. | [optional] 
**created_at** | **datetime** |  | [optional] 
**summary** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**pending** | **bool** | True for a vendor deal filed as a PDF and not yet published (WINAD-10698). Customers never receive a pending row; staff can filter with q[pending_eq]&#x3D;true. | [optional] 
**vendors** | [**List[DealDetailVendor]**](DealDetailVendor.md) |  | [optional] 
**deal_detail** | [**DealDetail**](DealDetail.md) |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**raw_contract** | [**RawContractTerms**](RawContractTerms.md) | The linked RawContract&#39;s structured terms; null when raw_contract_id is null, or when the user cannot read that document (for example a pending contract&#39;s PDF). | [optional] 

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


