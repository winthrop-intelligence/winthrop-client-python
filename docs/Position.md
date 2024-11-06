# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**start_on** | **date** |  | [optional] 
**end_on** | **date** |  | [optional] 
**partial_season** | **bool** |  | [optional] 
**compensation_id** | **int** |  | [optional] 
**coach_apr** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**departing** | **bool** |  | [optional] 
**departing_set_at** | **datetime** |  | [optional] 
**creation_reason** | **str** |  | [optional] 
**creation_reason_updated_at** | **datetime** |  | [optional] 
**coach** | [**Coach**](Coach.md) |  | [optional] 
**sport** | [**Sport**](Sport.md) |  | [optional] 
**school** | [**School**](School.md) |  | [optional] 
**article_link** | **str** |  | [optional] 
**article_title** | **str** |  | [optional] 
**article_description** | **str** |  | [optional] 
**article_site_name** | **str** |  | [optional] 
**article_publish_time** | **str** |  | [optional] 
**article_image_url** | **str** |  | [optional] 
**position_types** | [**List[PositionType]**](PositionType.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_form_dict = position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


