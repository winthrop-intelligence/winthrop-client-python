# GeoRegion

A geographic region (geo division) with its parent region name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**geo_region_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.geo_region import GeoRegion

# TODO update the JSON string below
json = "{}"
# create an instance of GeoRegion from a JSON string
geo_region_instance = GeoRegion.from_json(json)
# print the JSON string representation of the object
print(GeoRegion.to_json())

# convert the object into a dict
geo_region_dict = geo_region_instance.to_dict()
# create an instance of GeoRegion from a dict
geo_region_from_dict = GeoRegion.from_dict(geo_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


