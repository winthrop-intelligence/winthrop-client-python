# AdminCoachContractsPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[str]** |  | [optional] 
**rows** | **List[Dict[str, Optional[str]]]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_contracts_preview import AdminCoachContractsPreview

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachContractsPreview from a JSON string
admin_coach_contracts_preview_instance = AdminCoachContractsPreview.from_json(json)
# print the JSON string representation of the object
print(AdminCoachContractsPreview.to_json())

# convert the object into a dict
admin_coach_contracts_preview_dict = admin_coach_contracts_preview_instance.to_dict()
# create an instance of AdminCoachContractsPreview from a dict
admin_coach_contracts_preview_from_dict = AdminCoachContractsPreview.from_dict(admin_coach_contracts_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


