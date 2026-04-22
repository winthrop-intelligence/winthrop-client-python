# SendOtpCode422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.send_otp_code422_response import SendOtpCode422Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendOtpCode422Response from a JSON string
send_otp_code422_response_instance = SendOtpCode422Response.from_json(json)
# print the JSON string representation of the object
print(SendOtpCode422Response.to_json())

# convert the object into a dict
send_otp_code422_response_dict = send_otp_code422_response_instance.to_dict()
# create an instance of SendOtpCode422Response from a dict
send_otp_code422_response_from_dict = SendOtpCode422Response.from_dict(send_otp_code422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


