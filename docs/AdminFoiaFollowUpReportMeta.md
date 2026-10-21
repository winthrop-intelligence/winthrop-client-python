# AdminFoiaFollowUpReportMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**follow_up_today_count** | **int** |  | [optional] 
**follow_up_yesterday_count** | **int** |  | [optional] 
**total_on_page_count** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_direction** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_follow_up_report_meta import AdminFoiaFollowUpReportMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaFollowUpReportMeta from a JSON string
admin_foia_follow_up_report_meta_instance = AdminFoiaFollowUpReportMeta.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaFollowUpReportMeta.to_json())

# convert the object into a dict
admin_foia_follow_up_report_meta_dict = admin_foia_follow_up_report_meta_instance.to_dict()
# create an instance of AdminFoiaFollowUpReportMeta from a dict
admin_foia_follow_up_report_meta_from_dict = AdminFoiaFollowUpReportMeta.from_dict(admin_foia_follow_up_report_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


