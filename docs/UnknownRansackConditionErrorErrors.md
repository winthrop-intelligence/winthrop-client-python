# UnknownRansackConditionErrorErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **List[str]** | One entry per bad condition, in the form &#x60;unknown condition: &lt;name&gt;&#x60;, or &#x60;condition has no predicate: &lt;name&gt; (use &lt;name&gt;_eq, &lt;name&gt;_cont, ...)&#x60; for an attribute given without a predicate. | 

## Example

```python
from winthrop_client_python.models.unknown_ransack_condition_error_errors import UnknownRansackConditionErrorErrors

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownRansackConditionErrorErrors from a JSON string
unknown_ransack_condition_error_errors_instance = UnknownRansackConditionErrorErrors.from_json(json)
# print the JSON string representation of the object
print(UnknownRansackConditionErrorErrors.to_json())

# convert the object into a dict
unknown_ransack_condition_error_errors_dict = unknown_ransack_condition_error_errors_instance.to_dict()
# create an instance of UnknownRansackConditionErrorErrors from a dict
unknown_ransack_condition_error_errors_from_dict = UnknownRansackConditionErrorErrors.from_dict(unknown_ransack_condition_error_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


