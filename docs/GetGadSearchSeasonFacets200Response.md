# GetGadSearchSeasonFacets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_facets** | **List[int]** | Season years, newest first. An empty array means no season matches the current filters. | [optional] 

## Example

```python
from winthrop_client_python.models.get_gad_search_season_facets200_response import GetGadSearchSeasonFacets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGadSearchSeasonFacets200Response from a JSON string
get_gad_search_season_facets200_response_instance = GetGadSearchSeasonFacets200Response.from_json(json)
# print the JSON string representation of the object
print(GetGadSearchSeasonFacets200Response.to_json())

# convert the object into a dict
get_gad_search_season_facets200_response_dict = get_gad_search_season_facets200_response_instance.to_dict()
# create an instance of GetGadSearchSeasonFacets200Response from a dict
get_gad_search_season_facets200_response_from_dict = GetGadSearchSeasonFacets200Response.from_dict(get_gad_search_season_facets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


