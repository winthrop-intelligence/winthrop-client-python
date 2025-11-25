# RawContractCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RawContract]**](RawContract.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.raw_contract_collection import RawContractCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RawContractCollection from a JSON string
raw_contract_collection_instance = RawContractCollection.from_json(json)
# print the JSON string representation of the object
print(RawContractCollection.to_json())

# convert the object into a dict
raw_contract_collection_dict = raw_contract_collection_instance.to_dict()
# create an instance of RawContractCollection from a dict
raw_contract_collection_from_dict = RawContractCollection.from_dict(raw_contract_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


