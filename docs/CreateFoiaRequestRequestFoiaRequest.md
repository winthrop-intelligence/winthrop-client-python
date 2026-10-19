# CreateFoiaRequestRequestFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**foia_label_id** | **int** |  | 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_sent** | **date** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**follow_up_date** | **date** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**deal_status_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_foia_request_request_foia_request import CreateFoiaRequestRequestFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFoiaRequestRequestFoiaRequest from a JSON string
create_foia_request_request_foia_request_instance = CreateFoiaRequestRequestFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFoiaRequestRequestFoiaRequest.to_json())

# convert the object into a dict
create_foia_request_request_foia_request_dict = create_foia_request_request_foia_request_instance.to_dict()
# create an instance of CreateFoiaRequestRequestFoiaRequest from a dict
create_foia_request_request_foia_request_from_dict = CreateFoiaRequestRequestFoiaRequest.from_dict(create_foia_request_request_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


