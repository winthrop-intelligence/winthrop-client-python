# GadCohortSummarySellerFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**subdivision_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_cohort_summary_seller_filters import GadCohortSummarySellerFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GadCohortSummarySellerFilters from a JSON string
gad_cohort_summary_seller_filters_instance = GadCohortSummarySellerFilters.from_json(json)
# print the JSON string representation of the object
print(GadCohortSummarySellerFilters.to_json())

# convert the object into a dict
gad_cohort_summary_seller_filters_dict = gad_cohort_summary_seller_filters_instance.to_dict()
# create an instance of GadCohortSummarySellerFilters from a dict
gad_cohort_summary_seller_filters_from_dict = GadCohortSummarySellerFilters.from_dict(gad_cohort_summary_seller_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


