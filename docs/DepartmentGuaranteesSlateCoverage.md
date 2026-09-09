# DepartmentGuaranteesSlateCoverage

Coverage of the season's non-conference slate (WINAD-10394): the scheduling module's non-conference games for the season plus every ledger agreement whose game the schedule does not carry. A scheduled game is documented when an agreement the ledger lists backs it — by the schedule's link, or by describing the same dated game (sport, the two schools in either order, date) — and a game known only from its agreement is documented by definition, so documented_count never falls below the distinct games the ledger lists. A link to an agreement the ledger does not carry (cancelled, another season's, a tournament deal) documents nothing. private_vs_private_count is the undocumented games against a private opponent — the ones no public filing could ever recover. Null when nothing is scheduled and nothing is on file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_count** | **int** |  | 
**documented_count** | **int** |  | 
**private_vs_private_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_slate_coverage import DepartmentGuaranteesSlateCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesSlateCoverage from a JSON string
department_guarantees_slate_coverage_instance = DepartmentGuaranteesSlateCoverage.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesSlateCoverage.to_json())

# convert the object into a dict
department_guarantees_slate_coverage_dict = department_guarantees_slate_coverage_instance.to_dict()
# create an instance of DepartmentGuaranteesSlateCoverage from a dict
department_guarantees_slate_coverage_from_dict = DepartmentGuaranteesSlateCoverage.from_dict(department_guarantees_slate_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


