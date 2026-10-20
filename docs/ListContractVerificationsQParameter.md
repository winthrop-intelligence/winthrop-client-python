# ListContractVerificationsQParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id_in** | **List[int]** |  | [optional] 
**contract_school_id_eq** | **int** |  | [optional] 
**contract_school_id_in** | **List[int]** |  | [optional] 
**seasons_contains** | **int** | Events whose seasons array includes this season-ending year. | [optional] 
**batch_id_eq** | **str** | Events posted with this batch_id (other Ransack predicates, e.g. batch_id_start, also work). | [optional] 
**code_version_eq** | **str** | Events posted with this commit SHA, lower case (other Ransack predicates also work). | [optional] 

## Example

```python
from winthrop_client_python.models.list_contract_verifications_q_parameter import ListContractVerificationsQParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ListContractVerificationsQParameter from a JSON string
list_contract_verifications_q_parameter_instance = ListContractVerificationsQParameter.from_json(json)
# print the JSON string representation of the object
print(ListContractVerificationsQParameter.to_json())

# convert the object into a dict
list_contract_verifications_q_parameter_dict = list_contract_verifications_q_parameter_instance.to_dict()
# create an instance of ListContractVerificationsQParameter from a dict
list_contract_verifications_q_parameter_from_dict = ListContractVerificationsQParameter.from_dict(list_contract_verifications_q_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


