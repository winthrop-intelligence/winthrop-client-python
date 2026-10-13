# EarnedIncentiveCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EarnedIncentive]**](EarnedIncentive.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.earned_incentive_collection import EarnedIncentiveCollection

# TODO update the JSON string below
json = "{}"
# create an instance of EarnedIncentiveCollection from a JSON string
earned_incentive_collection_instance = EarnedIncentiveCollection.from_json(json)
# print the JSON string representation of the object
print(EarnedIncentiveCollection.to_json())

# convert the object into a dict
earned_incentive_collection_dict = earned_incentive_collection_instance.to_dict()
# create an instance of EarnedIncentiveCollection from a dict
earned_incentive_collection_from_dict = EarnedIncentiveCollection.from_dict(earned_incentive_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


