# SchoolLogo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_url** | **str** | Signed, expiring url for the original logo image | [optional] 
**medium_url** | **str** | Signed, expiring url for the medium logo image | [optional] 
**small_url** | **str** | Signed, expiring url for the small logo image | [optional] 

## Example

```python
from winthrop_client_python.models.school_logo import SchoolLogo

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolLogo from a JSON string
school_logo_instance = SchoolLogo.from_json(json)
# print the JSON string representation of the object
print SchoolLogo.to_json()

# convert the object into a dict
school_logo_dict = school_logo_instance.to_dict()
# create an instance of SchoolLogo from a dict
school_logo_form_dict = school_logo.from_dict(school_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


