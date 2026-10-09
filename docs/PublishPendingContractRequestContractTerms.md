# PublishPendingContractRequestContractTerms

Optional. Replaces the structured terms on the contract's RawContract in the same transaction (WINAD-10633). Omitted, null or an empty string leaves them unchanged. Errors are keyed contract_terms, contract_terms.schema, contract_terms.source.run_id, and so on. Accepted from service (client-credentials) tokens like the rest of publish; the audit version then records no person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The terms&#39; shape and version, for example ticketing-terms-v1, pouring-terms-v1 or coach-terms-v1 | 
**source** | [**ContractTermsSource**](ContractTermsSource.md) |  | 

## Example

```python
from winthrop_client_python.models.publish_pending_contract_request_contract_terms import PublishPendingContractRequestContractTerms

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingContractRequestContractTerms from a JSON string
publish_pending_contract_request_contract_terms_instance = PublishPendingContractRequestContractTerms.from_json(json)
# print the JSON string representation of the object
print(PublishPendingContractRequestContractTerms.to_json())

# convert the object into a dict
publish_pending_contract_request_contract_terms_dict = publish_pending_contract_request_contract_terms_instance.to_dict()
# create an instance of PublishPendingContractRequestContractTerms from a dict
publish_pending_contract_request_contract_terms_from_dict = PublishPendingContractRequestContractTerms.from_dict(publish_pending_contract_request_contract_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


