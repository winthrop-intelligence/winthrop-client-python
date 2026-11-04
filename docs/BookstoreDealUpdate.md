# BookstoreDealUpdate

Bookstore deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guaranteed_amt_year_one** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**capital_improvement** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**signing_bonus** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**threshold_1** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_1** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_2** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_2** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_3** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_3** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_4** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_4** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_5** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_5** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_6** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_6** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.bookstore_deal_update import BookstoreDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BookstoreDealUpdate from a JSON string
bookstore_deal_update_instance = BookstoreDealUpdate.from_json(json)
# print the JSON string representation of the object
print(BookstoreDealUpdate.to_json())

# convert the object into a dict
bookstore_deal_update_dict = bookstore_deal_update_instance.to_dict()
# create an instance of BookstoreDealUpdate from a dict
bookstore_deal_update_from_dict = BookstoreDealUpdate.from_dict(bookstore_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


