# SalarySiteAssociationsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_at** | **datetime** |  | 
**filters_applied** | **Dict[str, object]** |  | [optional] 
**current_page** | **int** |  | 
**per_page** | **int** |  | 
**max_per_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.salary_site_associations_meta import SalarySiteAssociationsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SalarySiteAssociationsMeta from a JSON string
salary_site_associations_meta_instance = SalarySiteAssociationsMeta.from_json(json)
# print the JSON string representation of the object
print(SalarySiteAssociationsMeta.to_json())

# convert the object into a dict
salary_site_associations_meta_dict = salary_site_associations_meta_instance.to_dict()
# create an instance of SalarySiteAssociationsMeta from a dict
salary_site_associations_meta_from_dict = SalarySiteAssociationsMeta.from_dict(salary_site_associations_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


