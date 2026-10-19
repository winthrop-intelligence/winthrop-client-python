# CreateFoiaRequestBuilderRequestFoiaRequestBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_label** | **str** | FOIA label ID encoded as a string. | 
**employment** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**outside_income** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**guarantees** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**ncaa_frs_reports** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**ncaa_audit_reports** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**vendor_deals** | **str** | Use \&quot;1\&quot; to include this request type and \&quot;0\&quot; to exclude it. | [optional] 
**employment_seasons** | **List[str]** |  | [optional] 
**employment_sports** | **List[str]** |  | [optional] 
**employment_contract_status** | **List[str]** |  | [optional] 
**outside_income_seasons** | **List[str]** |  | [optional] 
**outside_income_sports** | **List[str]** |  | [optional] 
**guarantees_sports** | **List[str]** |  | [optional] 
**guarantees_seasons** | **List[str]** |  | [optional] 
**ncaa_frs_seasons** | **List[str]** |  | [optional] 
**ncaa_audit_seasons** | **List[str]** |  | [optional] 
**vendor_deal_types** | **List[str]** |  | [optional] 
**school_groups** | **List[str]** | Selected school IDs encoded as strings. | 
**foia_label_item** | **List[str]** |  | [optional] 
**contract_statuses** | **List[str]** |  | [optional] 
**request_types** | **List[str]** |  | [optional] 
**sent_date_states** | **List[str]** |  | [optional] 
**schools** | **str** |  | [optional] 
**sent_date** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_foia_request_builder_request_foia_request_builder import CreateFoiaRequestBuilderRequestFoiaRequestBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFoiaRequestBuilderRequestFoiaRequestBuilder from a JSON string
create_foia_request_builder_request_foia_request_builder_instance = CreateFoiaRequestBuilderRequestFoiaRequestBuilder.from_json(json)
# print the JSON string representation of the object
print(CreateFoiaRequestBuilderRequestFoiaRequestBuilder.to_json())

# convert the object into a dict
create_foia_request_builder_request_foia_request_builder_dict = create_foia_request_builder_request_foia_request_builder_instance.to_dict()
# create an instance of CreateFoiaRequestBuilderRequestFoiaRequestBuilder from a dict
create_foia_request_builder_request_foia_request_builder_from_dict = CreateFoiaRequestBuilderRequestFoiaRequestBuilder.from_dict(create_foia_request_builder_request_foia_request_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


