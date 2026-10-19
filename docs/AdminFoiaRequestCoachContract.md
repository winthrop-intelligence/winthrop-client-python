# AdminFoiaRequestCoachContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**at_will** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_coach_contract import AdminFoiaRequestCoachContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestCoachContract from a JSON string
admin_foia_request_coach_contract_instance = AdminFoiaRequestCoachContract.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestCoachContract.to_json())

# convert the object into a dict
admin_foia_request_coach_contract_dict = admin_foia_request_coach_contract_instance.to_dict()
# create an instance of AdminFoiaRequestCoachContract from a dict
admin_foia_request_coach_contract_from_dict = AdminFoiaRequestCoachContract.from_dict(admin_foia_request_coach_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


