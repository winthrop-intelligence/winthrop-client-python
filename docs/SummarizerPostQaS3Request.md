# SummarizerPostQaS3Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**key** | **str** |  | 
**prompt** | **str** |  | [optional] 
**question** | **str** |  | 

## Example

```python
from winthrop_client_python.models.summarizer_post_qa_s3_request import SummarizerPostQaS3Request

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizerPostQaS3Request from a JSON string
summarizer_post_qa_s3_request_instance = SummarizerPostQaS3Request.from_json(json)
# print the JSON string representation of the object
print(SummarizerPostQaS3Request.to_json())

# convert the object into a dict
summarizer_post_qa_s3_request_dict = summarizer_post_qa_s3_request_instance.to_dict()
# create an instance of SummarizerPostQaS3Request from a dict
summarizer_post_qa_s3_request_form_dict = summarizer_post_qa_s3_request.from_dict(summarizer_post_qa_s3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


