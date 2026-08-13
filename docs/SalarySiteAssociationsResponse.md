# SalarySiteAssociationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**SalarySiteAssociationsMeta**](SalarySiteAssociationsMeta.md) |  | 
**data** | [**List[SalarySiteAssociation]**](SalarySiteAssociation.md) |  | 

## Example

```python
from winthrop_client_python.models.salary_site_associations_response import SalarySiteAssociationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalarySiteAssociationsResponse from a JSON string
salary_site_associations_response_instance = SalarySiteAssociationsResponse.from_json(json)
# print the JSON string representation of the object
print(SalarySiteAssociationsResponse.to_json())

# convert the object into a dict
salary_site_associations_response_dict = salary_site_associations_response_instance.to_dict()
# create an instance of SalarySiteAssociationsResponse from a dict
salary_site_associations_response_from_dict = SalarySiteAssociationsResponse.from_dict(salary_site_associations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


