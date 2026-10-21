# CopyPositionsForYearRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | The season year to fill from the year before | 

## Example

```python
from winthrop_client_python.models.copy_positions_for_year_request import CopyPositionsForYearRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyPositionsForYearRequest from a JSON string
copy_positions_for_year_request_instance = CopyPositionsForYearRequest.from_json(json)
# print the JSON string representation of the object
print(CopyPositionsForYearRequest.to_json())

# convert the object into a dict
copy_positions_for_year_request_dict = copy_positions_for_year_request_instance.to_dict()
# create an instance of CopyPositionsForYearRequest from a dict
copy_positions_for_year_request_from_dict = CopyPositionsForYearRequest.from_dict(copy_positions_for_year_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


