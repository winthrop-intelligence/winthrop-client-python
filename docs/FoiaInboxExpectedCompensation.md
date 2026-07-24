# FoiaInboxExpectedCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**school_id** | **int** |  | 
**coach_id** | **int** |  | 
**contract_status** | **str** |  | 
**comment** | **str** |  | 
**updated_at** | **datetime** |  | 
**positions_sha256** | **str** |  | 
**positions** | [**List[FoiaInboxExpectedPosition]**](FoiaInboxExpectedPosition.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_expected_compensation import FoiaInboxExpectedCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxExpectedCompensation from a JSON string
foia_inbox_expected_compensation_instance = FoiaInboxExpectedCompensation.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxExpectedCompensation.to_json())

# convert the object into a dict
foia_inbox_expected_compensation_dict = foia_inbox_expected_compensation_instance.to_dict()
# create an instance of FoiaInboxExpectedCompensation from a dict
foia_inbox_expected_compensation_from_dict = FoiaInboxExpectedCompensation.from_dict(foia_inbox_expected_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


