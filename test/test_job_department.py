# coding: utf-8

"""
    Winthrop Intelligence Internal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from winthrop_client_python.models.job_department import JobDepartment


class TestJobDepartment(unittest.TestCase):
    """JobDepartment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobDepartment:
        """Test JobDepartment
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JobDepartment`
        """
        model = JobDepartment()
        if include_optional:
            return JobDepartment(
                name = 'Athletics'
            )
        else:
            return JobDepartment(
        )
        """

    def testJobDepartment(self):
        """Test JobDepartment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
