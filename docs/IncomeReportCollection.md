# IncomeReportCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IncomeReport]**](IncomeReport.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.income_report_collection import IncomeReportCollection

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReportCollection from a JSON string
income_report_collection_instance = IncomeReportCollection.from_json(json)
# print the JSON string representation of the object
print IncomeReportCollection.to_json()

# convert the object into a dict
income_report_collection_dict = income_report_collection_instance.to_dict()
# create an instance of IncomeReportCollection from a dict
income_report_collection_form_dict = income_report_collection.from_dict(income_report_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


