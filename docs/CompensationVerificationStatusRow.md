# CompensationVerificationStatusRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensation_id** | **int** |  | 
**coach_id** | **int** |  | 
**position_id** | **int** | The row&#39;s head coach position, else its lowest position id; null when it has none. | 
**position_type** | **str** | PositionType name of that position (HEAD_COACH when it has that type). | 
**school_id** | **int** |  | 
**raw_contract_id** | **int** | Null for an unlinked row. | 
**contract_id** | **int** | Null for an unlinked row. | 
**contract_status** | **str** | ContractStatus name of the compensation row (for example COMPLETE). | 
**at_will** | **bool** | The linked contract&#39;s flag; null for an unlinked row. | 
**status** | [**CompensationVerificationStatusValue**](CompensationVerificationStatusValue.md) |  | 
**verification_event_id** | **int** | The latest event covering the season; null when there is none. | 
**method** | **str** |  | 
**verified_at** | **datetime** |  | 
**agent_run_id** | **str** |  | 
**changed_since** | [**List[CompensationVerificationChange]**](CompensationVerificationChange.md) | Always an array; empty unless the status is changed_since_verified. | 

## Example

```python
from winthrop_client_python.models.compensation_verification_status_row import CompensationVerificationStatusRow

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationVerificationStatusRow from a JSON string
compensation_verification_status_row_instance = CompensationVerificationStatusRow.from_json(json)
# print the JSON string representation of the object
print(CompensationVerificationStatusRow.to_json())

# convert the object into a dict
compensation_verification_status_row_dict = compensation_verification_status_row_instance.to_dict()
# create an instance of CompensationVerificationStatusRow from a dict
compensation_verification_status_row_from_dict = CompensationVerificationStatusRow.from_dict(compensation_verification_status_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


