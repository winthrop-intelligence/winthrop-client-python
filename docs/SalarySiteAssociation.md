# SalarySiteAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_id** | **int** |  | 
**school_id** | **int** |  | 
**site_id** | **int** |  | 
**site_url** | **str** |  | 
**site_type** | **str** |  | 
**notes** | **str** |  | [optional] 
**association_created_at** | **datetime** |  | 
**association_updated_at** | **datetime** |  | 
**site_created_at** | **datetime** |  | 
**site_updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.salary_site_association import SalarySiteAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of SalarySiteAssociation from a JSON string
salary_site_association_instance = SalarySiteAssociation.from_json(json)
# print the JSON string representation of the object
print(SalarySiteAssociation.to_json())

# convert the object into a dict
salary_site_association_dict = salary_site_association_instance.to_dict()
# create an instance of SalarySiteAssociation from a dict
salary_site_association_from_dict = SalarySiteAssociation.from_dict(salary_site_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


