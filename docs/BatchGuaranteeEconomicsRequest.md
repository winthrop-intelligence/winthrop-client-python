# BatchGuaranteeEconomicsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pairs** | **List[List[int]]** | The page&#39;s [school_id, sport_id] pairs. Non-basketball, malformed, or non-positive pairs are ignored; duplicates are de-duped. | 

## Example

```python
from winthrop_client_python.models.batch_guarantee_economics_request import BatchGuaranteeEconomicsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGuaranteeEconomicsRequest from a JSON string
batch_guarantee_economics_request_instance = BatchGuaranteeEconomicsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchGuaranteeEconomicsRequest.to_json())

# convert the object into a dict
batch_guarantee_economics_request_dict = batch_guarantee_economics_request_instance.to_dict()
# create an instance of BatchGuaranteeEconomicsRequest from a dict
batch_guarantee_economics_request_from_dict = BatchGuaranteeEconomicsRequest.from_dict(batch_guarantee_economics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


