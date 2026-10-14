# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_note** | **str** | Write-only (POST and PATCH). Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 
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
**terminated** | **bool** | Stored terminated flag of the position. Read-only in this API. null means unknown. | [optional] [readonly] 
**departing_set_at** | **datetime** |  | [optional] 
**departure_on** | **date** | Date the person left the position (YYYY-MM-DD), as recorded through PATCH /positions/{positionId}/departure or the admin departing form. null when none is recorded, as on every departure that was only ticked before this field existed. Unlike departing_set_at, which is when the box was ticked, this is when the person actually left. Returned to every caller who can read positions. Read-only here. | [optional] [readonly] 
**departure_reason** | **str** | Recorded reason for the departure. null when none is recorded. Staff only. The key is absent (not null) in responses to callers who may not update positions, such as customers. Read-only here. | [optional] [readonly] 
**departure_source_url** | **str** | Public source URL for the departure. null when none is recorded. Staff only. The key is absent (not null) in responses to callers who may not update positions, such as customers. Read-only here. | [optional] [readonly] 
**suppress_departing_set_at** | **bool** | Write-only control flag for trusted automation. When true and departing is set to true, WinAD does not stamp departing_set_at, so historical/catch-up departures are not published as current wire events. Ignored on responses. | [optional] 
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
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


