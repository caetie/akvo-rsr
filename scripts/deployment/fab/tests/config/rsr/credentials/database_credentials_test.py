#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os, unittest2

from testing.helpers.execution import TestRunner, TestSuiteLoader

import fab.tests.templates.database_credentials_template
from database_credentials import DatabaseCredentials


class DatabaseCredentialsTest(unittest2.TestCase):

    def setUp(self):
        super(DatabaseCredentialsTest, self).setUp()

        self.database_credentials = DatabaseCredentials()

    def test_has_admin_user(self):
        """fab.tests.config.rsr.credentials.database_credentials_test  Has database admin user"""

        self._verify_expected_config_value(self.database_credentials.admin_user, "admin user")

    def test_has_admin_password(self):
        """fab.tests.config.rsr.credentials.database_credentials_test  Has database admin password"""

        self._verify_expected_config_value(self.database_credentials.admin_password, "admin password")

    def test_has_rsr_user(self):
        """fab.tests.config.rsr.credentials.database_credentials_test  Has RSR database user"""

        self._verify_expected_config_value(self.database_credentials.rsr_user, "RSR user")

    def test_has_rsr_password(self):
        """fab.tests.config.rsr.credentials.database_credentials_test  Has RSR database password"""

        self._verify_expected_config_value(self.database_credentials.rsr_password, "RSR password")

    def _verify_expected_config_value(self, config_value, config_value_description):
        self.assertTrue(len(config_value) > 0, "Expected %s config value" % config_value_description)


def suite():
    return TestSuiteLoader().load_tests_from(DatabaseCredentialsTest)

if __name__ == '__main__':
    TestRunner().run_test_suite(suite())
