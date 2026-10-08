# DeskComposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_html** | **str** | Cover theme HTML; only supported background and text styles are used. Visible text comes from report metadata. Draft covers may be cleared. A published cover cannot be replaced with null or blank text; an unchanged missing legacy cover is preserved.  | [optional] 
**cover_file** | [**DeskHtmlFile**](DeskHtmlFile.md) |  | [optional] 
**report_file** | [**DeskHtmlFile**](DeskHtmlFile.md) |  | [optional] 
**recipient_user_ids** | **List[int]** | Null means everyone on the account; an empty array means admin only. Newly selected IDs must exist and be active, non-viewer readers of the selected account. Existing selections are retained when a user becomes inactive, gains viewer restrictions, or moves accounts; they grant no access or email until the user is eligible again. Explicit removal or hard deletion does not automatically reselect a user. Changing account requires an explicit selection (including null or an empty array), and every selected ID is validated against the new account. Invalid changes are atomic.  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_composition import DeskComposition

# TODO update the JSON string below
json = "{}"
# create an instance of DeskComposition from a JSON string
desk_composition_instance = DeskComposition.from_json(json)
# print the JSON string representation of the object
print(DeskComposition.to_json())

# convert the object into a dict
desk_composition_dict = desk_composition_instance.to_dict()
# create an instance of DeskComposition from a dict
desk_composition_from_dict = DeskComposition.from_dict(desk_composition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


