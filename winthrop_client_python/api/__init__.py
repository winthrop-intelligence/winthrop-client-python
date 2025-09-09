# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from winthrop_client_python.api.default_api import DefaultApi
    from winthrop_client_python.api.dossier_api import DossierApi
    from winthrop_client_python.api.intercollegiate_api import IntercollegiateApi
    from winthrop_client_python.api.reporting_api import ReportingApi
    from winthrop_client_python.api.scraper_api import ScraperApi

else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from winthrop_client_python.api.default_api import DefaultApi
from winthrop_client_python.api.dossier_api import DossierApi
from winthrop_client_python.api.intercollegiate_api import IntercollegiateApi
from winthrop_client_python.api.reporting_api import ReportingApi
from winthrop_client_python.api.scraper_api import ScraperApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
