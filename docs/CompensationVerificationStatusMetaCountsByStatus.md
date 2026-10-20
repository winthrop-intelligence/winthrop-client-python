# CompensationVerificationStatusMetaCountsByStatus

Rows per status for the whole scope, before status[] and q.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **int** |  | 
**changed_since_verified** | **int** |  | 
**mismatch** | **int** |  | 
**could_not_verify** | **int** |  | 
**revoked** | **int** |  | 
**not_verified** | **int** |  | 
**unlinked** | **int** |  | 

## Example

```python
from winthrop_client_python.models.compensation_verification_status_meta_counts_by_status import CompensationVerificationStatusMetaCountsByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationVerificationStatusMetaCountsByStatus from a JSON string
compensation_verification_status_meta_counts_by_status_instance = CompensationVerificationStatusMetaCountsByStatus.from_json(json)
# print the JSON string representation of the object
print(CompensationVerificationStatusMetaCountsByStatus.to_json())

# convert the object into a dict
compensation_verification_status_meta_counts_by_status_dict = compensation_verification_status_meta_counts_by_status_instance.to_dict()
# create an instance of CompensationVerificationStatusMetaCountsByStatus from a dict
compensation_verification_status_meta_counts_by_status_from_dict = CompensationVerificationStatusMetaCountsByStatus.from_dict(compensation_verification_status_meta_counts_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


