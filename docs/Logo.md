# Logo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_url** | **str** | Signed, expiring url for the original logo image | [optional] 
**medium_url** | **str** | Signed, expiring url for the medium logo image | [optional] 
**small_url** | **str** | Signed, expiring url for the small logo image | [optional] 

## Example

```python
from winthrop_client_python.models.logo import Logo

# TODO update the JSON string below
json = "{}"
# create an instance of Logo from a JSON string
logo_instance = Logo.from_json(json)
# print the JSON string representation of the object
print(Logo.to_json())

# convert the object into a dict
logo_dict = logo_instance.to_dict()
# create an instance of Logo from a dict
logo_form_dict = logo.from_dict(logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


