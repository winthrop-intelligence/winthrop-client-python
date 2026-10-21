# CompensationVerificationChangeUser

Who made it; null when no author was recorded. A script's label has a null id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.compensation_verification_change_user import CompensationVerificationChangeUser

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationVerificationChangeUser from a JSON string
compensation_verification_change_user_instance = CompensationVerificationChangeUser.from_json(json)
# print the JSON string representation of the object
print(CompensationVerificationChangeUser.to_json())

# convert the object into a dict
compensation_verification_change_user_dict = compensation_verification_change_user_instance.to_dict()
# create an instance of CompensationVerificationChangeUser from a dict
compensation_verification_change_user_from_dict = CompensationVerificationChangeUser.from_dict(compensation_verification_change_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


