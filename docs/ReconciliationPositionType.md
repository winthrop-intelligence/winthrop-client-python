# ReconciliationPositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_position_type import ReconciliationPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationPositionType from a JSON string
reconciliation_position_type_instance = ReconciliationPositionType.from_json(json)
# print the JSON string representation of the object
print(ReconciliationPositionType.to_json())

# convert the object into a dict
reconciliation_position_type_dict = reconciliation_position_type_instance.to_dict()
# create an instance of ReconciliationPositionType from a dict
reconciliation_position_type_from_dict = ReconciliationPositionType.from_dict(reconciliation_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


