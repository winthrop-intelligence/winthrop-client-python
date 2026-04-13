# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**accountable_id** | **int** |  | [optional] 
**accountable_type** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**divisions** | [**List[Division]**](Division.md) |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**can_see_compensation** | **bool** | Whether the user can view coach compensation data | [optional] 
**can_show_scouting** | **bool** | Whether the user can view scouting/team schedule links | [optional] 
**can_show_game_contract** | **bool** | Whether the user can view game contract/guarantee data | [optional] 
**can_see_coaches** | **bool** | Whether the user can access the Coaches section | [optional] 
**can_see_administrators** | **bool** | Whether the user can access the Administrators section | [optional] 
**can_show_financials** | **bool** | Whether the user can access the Financials section | [optional] 
**can_show_deals** | **bool** | Whether the user can access the Vendors section | [optional] 
**can_show_benchmark** | **bool** | Whether the user can access the Benchmark section | [optional] 
**can_show_athletic_profile** | **bool** | Whether the user can access the Departments section | [optional] 
**can_read_conference** | **bool** | Whether the user can access the Conferences section | [optional] 
**can_show_game_post** | **bool** | Whether the user can access the Games Wanted section | [optional] 
**can_see_school_groups** | **bool** | Whether the user can access Custom School Groups | [optional] 
**is_sport_specific** | **bool** |  | [optional] 
**is_d2_only** | **bool** |  | [optional] 
**is_conference_only** | **bool** |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 
**coli_index** | **float** | Cost of living index for the user&#39;s school | [optional] 
**subscription_type** | **str** |  | [optional] 
**schedule_sports** | [**List[UserScheduleSportsInner]**](UserScheduleSportsInner.md) | Sports the user can access for game scheduling | [optional] 
**school_city** | **str** |  | [optional] 
**school_state** | **str** |  | [optional] 
**otp_required** | **bool** | Whether the user must verify OTP to access the application | [optional] 

## Example

```python
from winthrop_client_python.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


