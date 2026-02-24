# AdminCompensationSubdivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**compensations** | [**List[CompensationRow]**](CompensationRow.md) |  | [optional] 
**schools_no_comp** | [**List[SchoolNoComp]**](SchoolNoComp.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_subdivision import AdminCompensationSubdivision

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationSubdivision from a JSON string
admin_compensation_subdivision_instance = AdminCompensationSubdivision.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationSubdivision.to_json())

# convert the object into a dict
admin_compensation_subdivision_dict = admin_compensation_subdivision_instance.to_dict()
# create an instance of AdminCompensationSubdivision from a dict
admin_compensation_subdivision_from_dict = AdminCompensationSubdivision.from_dict(admin_compensation_subdivision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


