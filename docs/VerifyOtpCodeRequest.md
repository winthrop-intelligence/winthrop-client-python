# VerifyOtpCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_code** | **str** | The 6-digit OTP code | 

## Example

```python
from winthrop_client_python.models.verify_otp_code_request import VerifyOtpCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyOtpCodeRequest from a JSON string
verify_otp_code_request_instance = VerifyOtpCodeRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyOtpCodeRequest.to_json())

# convert the object into a dict
verify_otp_code_request_dict = verify_otp_code_request_instance.to_dict()
# create an instance of VerifyOtpCodeRequest from a dict
verify_otp_code_request_from_dict = VerifyOtpCodeRequest.from_dict(verify_otp_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


