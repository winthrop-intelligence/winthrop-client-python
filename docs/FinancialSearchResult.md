# FinancialSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**total_student_enrollment** | **int** |  | [optional] 
**student_athlete_enrollment** | **int** |  | [optional] 
**sport_count** | **int** |  | [optional] 
**rev_total_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ticket_sales_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_rights_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_student_fees_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_university_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_guarantees_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_total_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_coaching_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_recruiting_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_travel_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_facilities_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_guarantees_amt** | **float** | Amount in whole US dollars | [optional] 
**has_audited_report** | **bool** |  | [optional] 
**rev_contributions_no_ik_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_conf_distributions_non_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_conf_bowl_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ncaa_distributions_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ncaa_distributions_grants_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ncaa_host_settlements_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_ncaa_postseason_reimb_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_branding_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_endowment_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_parking_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_admin_support_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_compensation_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_govt_support_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_in_kind_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_sports_camps_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_transfers_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_other_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_indirect_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_contributions_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_conf_distributions_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_bowl_amt** | **float** | Amount in whole US dollars | [optional] 
**rev_indirect_facilities_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_tuition_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_marketing_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_games_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_support_staff_salaries_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_indirect_support_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_equipment_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_sports_camps** | **float** | Amount in whole US dollars | [optional] 
**exp_debt_service_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_medical_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_dues_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_support_staff_other_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_severance_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_spirit_groups_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_head_coaches_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_facilities_maintenance_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_asst_coaches_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_head_coaches_third_party_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_asst_coaches_third_party_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_total_coaches_third_party_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_admin_support_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_meals_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_bowl_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_bowl_comp_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_postseason_fb_host_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_postseason_other_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_postseason_other_coaching_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_postseason_other_host_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_alston_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_other_amt** | **float** | Amount in whole US dollars | [optional] 
**exp_nil_revenue_share_amt** | **float** | Amount in whole US dollars | [optional] 

## Example

```python
from winthrop_client_python.models.financial_search_result import FinancialSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSearchResult from a JSON string
financial_search_result_instance = FinancialSearchResult.from_json(json)
# print the JSON string representation of the object
print(FinancialSearchResult.to_json())

# convert the object into a dict
financial_search_result_dict = financial_search_result_instance.to_dict()
# create an instance of FinancialSearchResult from a dict
financial_search_result_from_dict = FinancialSearchResult.from_dict(financial_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


