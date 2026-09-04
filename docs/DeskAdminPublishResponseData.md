# DeskAdminPublishResponseData

The 06.4 receipt (DeskPublishReceipt) plus the version minted — never the body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**DeskAdminPublishResponseDataReport**](DeskAdminPublishResponseDataReport.md) |  | 
**client** | **str** | The account the report went live on; null &#x3D; every school (WINAD-10415) | 
**audience_user_count** | **int** | \&quot;Visible to N people\&quot; — the active users the report reaches (Desk::Audience): the account&#39;s, or every school&#39;s. Replaces the emailed count on the 06.4 receipt while the publish email is paused (WINAD-10415 / D-29).  | 
**turnaround_label** | **str** |  | 
**requester_name** | **str** |  | 
**version** | [**DeskAdminVersion**](DeskAdminVersion.md) |  | 
**notified** | **bool** | Whether this publish queued the delivery email (async; not a delivery receipt). PAUSED at WINAD-10415 (D-29): always false, with notified_count 0 and no names, until the delivery is re-enabled in Desk::PublishReport.  | 
**notified_count** | **int** | How many people on the client&#39;s account it went to | 
**notified_names** | **List[str]** | WHO was written to, named from the list the mailer addressed. The receipt used to pair notified_count with the ask&#39;s stored requester_name — two facts nothing checked against each other, so a publish that mailed one colleague could announce that the (deactivated, unmailed) asker had been emailed.  | 
**notify_failed** | **bool** | The publish committed but the delivery could not be queued (a Redis outage, say). The 06.4 receipt renders it as an amber caution on a successful publish — this used to escape as a 500 over work that had succeeded, and the natural retry minted a second version notifying nobody. Without the caution the receipt simply omits its email row, which reads exactly like \&quot;no email was asked for\&quot;.  | 
**warnings** | [**List[DeskFinding]**](DeskFinding.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_publish_response_data import DeskAdminPublishResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminPublishResponseData from a JSON string
desk_admin_publish_response_data_instance = DeskAdminPublishResponseData.from_json(json)
# print the JSON string representation of the object
print(DeskAdminPublishResponseData.to_json())

# convert the object into a dict
desk_admin_publish_response_data_dict = desk_admin_publish_response_data_instance.to_dict()
# create an instance of DeskAdminPublishResponseData from a dict
desk_admin_publish_response_data_from_dict = DeskAdminPublishResponseData.from_dict(desk_admin_publish_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


