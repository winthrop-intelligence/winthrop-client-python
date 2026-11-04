# UpdateRawContractSchoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** | ID of an existing school | 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. At most 500 characters after trimming; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.update_raw_contract_school_request import UpdateRawContractSchoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRawContractSchoolRequest from a JSON string
update_raw_contract_school_request_instance = UpdateRawContractSchoolRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRawContractSchoolRequest.to_json())

# convert the object into a dict
update_raw_contract_school_request_dict = update_raw_contract_school_request_instance.to_dict()
# create an instance of UpdateRawContractSchoolRequest from a dict
update_raw_contract_school_request_from_dict = UpdateRawContractSchoolRequest.from_dict(update_raw_contract_school_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


