# winthrop-client-python
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/winthrop-intelligence/winthrop-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/winthrop-intelligence/winthrop-client-python.git`)

Then import the package:
```python
import winthrop_client_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import winthrop_client_python
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_label = winthrop_client_python.FoiaLabel() # FoiaLabel | Foia label to create

    try:
        api_response = api_instance.create_foia_label(foia_label)
        print("The response of DefaultApi->create_foia_label:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_foia_label: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**create_foia_label**](docs/DefaultApi.md#create_foia_label) | **POST** /api/v1/foia_labels | 
*DefaultApi* | [**create_foia_request**](docs/DefaultApi.md#create_foia_request) | **POST** /api/v1/foia_requests | 
*DefaultApi* | [**create_job_post**](docs/DefaultApi.md#create_job_post) | **POST** /central_jobs/job_posts | Create a job post
*DefaultApi* | [**create_requested_item**](docs/DefaultApi.md#create_requested_item) | **POST** /api/v1/requested_items | 
*DefaultApi* | [**delete_foia_label**](docs/DefaultApi.md#delete_foia_label) | **DELETE** /api/v1/foia_labels/{foiaLabelId} | 
*DefaultApi* | [**delete_foia_request**](docs/DefaultApi.md#delete_foia_request) | **DELETE** /api/v1/foia_requests/{foiaRequestId} | 
*DefaultApi* | [**delete_job_post**](docs/DefaultApi.md#delete_job_post) | **DELETE** /central_jobs/job_posts/{jobPostId} | Delete a job post
*DefaultApi* | [**delete_requested_item**](docs/DefaultApi.md#delete_requested_item) | **DELETE** /api/v1/requested_items/{requestedItemId} | 
*DefaultApi* | [**get_administrator**](docs/DefaultApi.md#get_administrator) | **GET** /api/v1/administrators/{administratorId} | 
*DefaultApi* | [**get_administrators**](docs/DefaultApi.md#get_administrators) | **GET** /api/v1/administrators | 
*DefaultApi* | [**get_audited_financial_report_status**](docs/DefaultApi.md#get_audited_financial_report_status) | **GET** /api/v1/audited_financial_report_statuses/{auditedFinancialReportStatusId} | 
*DefaultApi* | [**get_audited_financial_report_statuses**](docs/DefaultApi.md#get_audited_financial_report_statuses) | **GET** /api/v1/audited_financial_report_statuses | 
*DefaultApi* | [**get_categories**](docs/DefaultApi.md#get_categories) | **GET** /central_jobs/categories | List all categories
*DefaultApi* | [**get_coach**](docs/DefaultApi.md#get_coach) | **GET** /api/v1/coaches/{coachId} | 
*DefaultApi* | [**get_coaches**](docs/DefaultApi.md#get_coaches) | **GET** /api/v1/coaches | 
*DefaultApi* | [**get_compensation**](docs/DefaultApi.md#get_compensation) | **GET** /api/v1/compensations/{compensationId} | 
*DefaultApi* | [**get_compensations**](docs/DefaultApi.md#get_compensations) | **GET** /api/v1/compensations | 
*DefaultApi* | [**get_contract**](docs/DefaultApi.md#get_contract) | **GET** /api/v1/contracts/{contractId} | 
*DefaultApi* | [**get_contracts**](docs/DefaultApi.md#get_contracts) | **GET** /api/v1/contracts | 
*DefaultApi* | [**get_deal_status**](docs/DefaultApi.md#get_deal_status) | **GET** /api/v1/deal_statuses/{dealStatusId} | 
*DefaultApi* | [**get_deal_statuses**](docs/DefaultApi.md#get_deal_statuses) | **GET** /api/v1/deal_statuses | 
*DefaultApi* | [**get_foia_label**](docs/DefaultApi.md#get_foia_label) | **GET** /api/v1/foia_labels/{foiaLabelId} | 
*DefaultApi* | [**get_foia_labels**](docs/DefaultApi.md#get_foia_labels) | **GET** /api/v1/foia_labels | 
*DefaultApi* | [**get_foia_request**](docs/DefaultApi.md#get_foia_request) | **GET** /api/v1/foia_requests/{foiaRequestId} | 
*DefaultApi* | [**get_foia_requests**](docs/DefaultApi.md#get_foia_requests) | **GET** /api/v1/foia_requests | 
*DefaultApi* | [**get_game**](docs/DefaultApi.md#get_game) | **GET** /api/v1/games/{gameId} | 
*DefaultApi* | [**get_games**](docs/DefaultApi.md#get_games) | **GET** /api/v1/games | 
*DefaultApi* | [**get_income_report**](docs/DefaultApi.md#get_income_report) | **GET** /api/v1/income_reports/{incomeReportId} | 
*DefaultApi* | [**get_income_reports**](docs/DefaultApi.md#get_income_reports) | **GET** /api/v1/income_reports | 
*DefaultApi* | [**get_job_post**](docs/DefaultApi.md#get_job_post) | **GET** /central_jobs/job_posts/{jobPostId} | Get a job post
*DefaultApi* | [**get_job_posts**](docs/DefaultApi.md#get_job_posts) | **GET** /central_jobs/job_posts | List all job posts
*DefaultApi* | [**get_ncaa_financial_report_status**](docs/DefaultApi.md#get_ncaa_financial_report_status) | **GET** /api/v1/ncaa_financial_report_statuses/{ncaaFinancialReportStatusId} | 
*DefaultApi* | [**get_ncaa_financial_report_statuses**](docs/DefaultApi.md#get_ncaa_financial_report_statuses) | **GET** /api/v1/ncaa_financial_report_statuses | 
*DefaultApi* | [**get_position**](docs/DefaultApi.md#get_position) | **GET** /api/v1/positions/{positionId} | 
*DefaultApi* | [**get_positions**](docs/DefaultApi.md#get_positions) | **GET** /api/v1/positions | 
*DefaultApi* | [**get_requested_item**](docs/DefaultApi.md#get_requested_item) | **GET** /api/v1/requested_items/{requestedItemId} | 
*DefaultApi* | [**get_requested_items**](docs/DefaultApi.md#get_requested_items) | **GET** /api/v1/requested_items | 
*DefaultApi* | [**get_school**](docs/DefaultApi.md#get_school) | **GET** /api/v1/schools/{schoolId} | 
*DefaultApi* | [**get_schools**](docs/DefaultApi.md#get_schools) | **GET** /api/v1/schools | 
*DefaultApi* | [**get_season**](docs/DefaultApi.md#get_season) | **GET** /api/v1/seasons/{seasonId} | 
*DefaultApi* | [**get_seasons**](docs/DefaultApi.md#get_seasons) | **GET** /api/v1/seasons | 
*DefaultApi* | [**get_sport**](docs/DefaultApi.md#get_sport) | **GET** /api/v1/sports/{sportId} | 
*DefaultApi* | [**get_sports**](docs/DefaultApi.md#get_sports) | **GET** /api/v1/sports | 
*DefaultApi* | [**get_user**](docs/DefaultApi.md#get_user) | **GET** /api/v1/users/{userId} | 
*DefaultApi* | [**get_users**](docs/DefaultApi.md#get_users) | **GET** /api/v1/users | 
*DefaultApi* | [**summarizer_post_qa_s3**](docs/DefaultApi.md#summarizer_post_qa_s3) | **POST** /summarizer/qa_s3 | Answer questions over a file from S3
*DefaultApi* | [**summarizer_post_summarize_s3**](docs/DefaultApi.md#summarizer_post_summarize_s3) | **POST** /summarizer/summarize_s3 | Summarize a file from S3
*DefaultApi* | [**update_coach**](docs/DefaultApi.md#update_coach) | **PATCH** /api/v1/coaches/{coachId} | 
*DefaultApi* | [**update_foia_label**](docs/DefaultApi.md#update_foia_label) | **PATCH** /api/v1/foia_labels/{foiaLabelId} | 
*DefaultApi* | [**update_foia_request**](docs/DefaultApi.md#update_foia_request) | **PATCH** /api/v1/foia_requests/{foiaRequestId} | 
*DefaultApi* | [**update_job_post**](docs/DefaultApi.md#update_job_post) | **PATCH** /central_jobs/job_posts/{jobPostId} | Update a job post
*DefaultApi* | [**update_requested_item**](docs/DefaultApi.md#update_requested_item) | **PATCH** /api/v1/requested_items/{requestedItemId} | 
*ReportingApi* | [**get_coach_contract_requests**](docs/ReportingApi.md#get_coach_contract_requests) | **GET** /api/v1/reports/coach_contract_requests | 
*ReportingApi* | [**get_coach_history**](docs/ReportingApi.md#get_coach_history) | **GET** /api/v1/reports/coach_history | 
*ReportingApi* | [**get_conferenceships**](docs/ReportingApi.md#get_conferenceships) | **GET** /api/v1/reports/conferenceships | 
*ReportingApi* | [**get_foia_details**](docs/ReportingApi.md#get_foia_details) | **GET** /api/v1/reports/foia_details | 
*ReportingApi* | [**get_games**](docs/ReportingApi.md#get_games) | **GET** /api/v1/reports/games | 
*ReportingApi* | [**get_invoices**](docs/ReportingApi.md#get_invoices) | **GET** /api/v1/reports/invoices | 
*ReportingApi* | [**get_school_contract_requests**](docs/ReportingApi.md#get_school_contract_requests) | **GET** /api/v1/reports/school_contract_requests | 
*ReportingApi* | [**get_subscriptions**](docs/ReportingApi.md#get_subscriptions) | **GET** /api/v1/reports/subscriptions | 
*ScraperApi* | [**list_scrapers**](docs/ScraperApi.md#list_scrapers) | **GET** /ondemand-scrapers/ | List all available scrapers
*ScraperApi* | [**run_scraper**](docs/ScraperApi.md#run_scraper) | **POST** /ondemand-scrapers/run/{command} | Run a scraper


## Documentation For Models

 - [Administrator](docs/Administrator.md)
 - [AdministratorCollection](docs/AdministratorCollection.md)
 - [AuditedFinancialReportStatus](docs/AuditedFinancialReportStatus.md)
 - [AuditedFinancialReportStatusCollection](docs/AuditedFinancialReportStatusCollection.md)
 - [Avatar](docs/Avatar.md)
 - [Category](docs/Category.md)
 - [CategoryCollection](docs/CategoryCollection.md)
 - [Coach](docs/Coach.md)
 - [CoachCollection](docs/CoachCollection.md)
 - [Compensation](docs/Compensation.md)
 - [CompensationCollection](docs/CompensationCollection.md)
 - [Contract](docs/Contract.md)
 - [ContractCollection](docs/ContractCollection.md)
 - [DealStatus](docs/DealStatus.md)
 - [DealStatusCollection](docs/DealStatusCollection.md)
 - [FoiaLabel](docs/FoiaLabel.md)
 - [FoiaLabelCollection](docs/FoiaLabelCollection.md)
 - [FoiaRequest](docs/FoiaRequest.md)
 - [FoiaRequestCollection](docs/FoiaRequestCollection.md)
 - [Game](docs/Game.md)
 - [GameCollection](docs/GameCollection.md)
 - [IncomeReport](docs/IncomeReport.md)
 - [IncomeReportCollection](docs/IncomeReportCollection.md)
 - [JobPost](docs/JobPost.md)
 - [JobPostCollection](docs/JobPostCollection.md)
 - [Logo](docs/Logo.md)
 - [Meta](docs/Meta.md)
 - [NcaaFinancialReportStatus](docs/NcaaFinancialReportStatus.md)
 - [NcaaFinancialReportStatusCollection](docs/NcaaFinancialReportStatusCollection.md)
 - [Position](docs/Position.md)
 - [PositionCollection](docs/PositionCollection.md)
 - [PositionType](docs/PositionType.md)
 - [PositionTypeGroup](docs/PositionTypeGroup.md)
 - [RequestedItem](docs/RequestedItem.md)
 - [RequestedItemCollection](docs/RequestedItemCollection.md)
 - [School](docs/School.md)
 - [SchoolCollection](docs/SchoolCollection.md)
 - [Scraper](docs/Scraper.md)
 - [Season](docs/Season.md)
 - [SeasonCollection](docs/SeasonCollection.md)
 - [Sport](docs/Sport.md)
 - [SportCollection](docs/SportCollection.md)
 - [SummarizerPostQaS3Request](docs/SummarizerPostQaS3Request.md)
 - [SummarizerPostSummarizeS3Request](docs/SummarizerPostSummarizeS3Request.md)
 - [UnprocessableEntity](docs/UnprocessableEntity.md)
 - [User](docs/User.md)
 - [UserCollection](docs/UserCollection.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
### ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




