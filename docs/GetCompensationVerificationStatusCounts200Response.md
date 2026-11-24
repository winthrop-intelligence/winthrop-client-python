# GetCompensationVerificationStatusCounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetCompensationVerificationStatusCounts200ResponseMeta**](GetCompensationVerificationStatusCounts200ResponseMeta.md) |  | 
**counts_by_status** | **Dict[str, int]** |  | 

## Example

```python
from winthrop_client_python.models.get_compensation_verification_status_counts200_response import GetCompensationVerificationStatusCounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompensationVerificationStatusCounts200Response from a JSON string
get_compensation_verification_status_counts200_response_instance = GetCompensationVerificationStatusCounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetCompensationVerificationStatusCounts200Response.to_json())

# convert the object into a dict
get_compensation_verification_status_counts200_response_dict = get_compensation_verification_status_counts200_response_instance.to_dict()
# create an instance of GetCompensationVerificationStatusCounts200Response from a dict
get_compensation_verification_status_counts200_response_from_dict = GetCompensationVerificationStatusCounts200Response.from_dict(get_compensation_verification_status_counts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


