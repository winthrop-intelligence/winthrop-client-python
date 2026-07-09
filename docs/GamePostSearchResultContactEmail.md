# GamePostSearchResultContactEmail

Email address. value is null when not on file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**present** | **bool** | Whether an email is on file. | 

## Example

```python
from winthrop_client_python.models.game_post_search_result_contact_email import GamePostSearchResultContactEmail

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultContactEmail from a JSON string
game_post_search_result_contact_email_instance = GamePostSearchResultContactEmail.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultContactEmail.to_json())

# convert the object into a dict
game_post_search_result_contact_email_dict = game_post_search_result_contact_email_instance.to_dict()
# create an instance of GamePostSearchResultContactEmail from a dict
game_post_search_result_contact_email_from_dict = GamePostSearchResultContactEmail.from_dict(game_post_search_result_contact_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


