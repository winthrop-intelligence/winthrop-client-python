# CreateSportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**CreateSportRequestSport**](CreateSportRequestSport.md) |  | 

## Example

```python
from winthrop_client_python.models.create_sport_request import CreateSportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSportRequest from a JSON string
create_sport_request_instance = CreateSportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSportRequest.to_json())

# convert the object into a dict
create_sport_request_dict = create_sport_request_instance.to_dict()
# create an instance of CreateSportRequest from a dict
create_sport_request_from_dict = CreateSportRequest.from_dict(create_sport_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


