# CompensationVerificationStatusMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** | Null on the last page. | 
**previous_page** | **int** | Null on the first page. | 
**season** | **int** |  | 
**counts_by_status** | [**CompensationVerificationStatusMetaCountsByStatus**](CompensationVerificationStatusMetaCountsByStatus.md) |  | 

## Example

```python
from winthrop_client_python.models.compensation_verification_status_meta import CompensationVerificationStatusMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationVerificationStatusMeta from a JSON string
compensation_verification_status_meta_instance = CompensationVerificationStatusMeta.from_json(json)
# print the JSON string representation of the object
print(CompensationVerificationStatusMeta.to_json())

# convert the object into a dict
compensation_verification_status_meta_dict = compensation_verification_status_meta_instance.to_dict()
# create an instance of CompensationVerificationStatusMeta from a dict
compensation_verification_status_meta_from_dict = CompensationVerificationStatusMeta.from_dict(compensation_verification_status_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


