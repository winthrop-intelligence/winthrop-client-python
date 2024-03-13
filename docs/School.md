# School


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**city** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**colors** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**primary_conference_id** | **int** |  | [optional] 
**cost_of_living_index_city_code** | **str** |  | [optional] 
**current_directors_cup_ranking** | **int** |  | [optional] 
**current_usnwr_ranking** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**school_classification_id** | **int** |  | [optional] 
**logo_updated_at** | **datetime** |  | [optional] 
**youtube_search_name** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**logo** | [**Logo**](Logo.md) |  | [optional] 
**athletic_director** | [**Coach**](Coach.md) |  | [optional] 
**athletics_url** | **str** |  | [optional] 
**wikipedia_url** | **str** |  | [optional] 
**athletics_wikipedia_url** | **str** |  | [optional] 
**external_logo** | [**Logo**](Logo.md) |  | [optional] 
**school_status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.school import School

# TODO update the JSON string below
json = "{}"
# create an instance of School from a JSON string
school_instance = School.from_json(json)
# print the JSON string representation of the object
print School.to_json()

# convert the object into a dict
school_dict = school_instance.to_dict()
# create an instance of School from a dict
school_form_dict = school.from_dict(school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


