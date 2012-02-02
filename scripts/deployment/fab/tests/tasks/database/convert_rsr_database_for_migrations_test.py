#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox

from testing.helpers.execution import TestRunner, TestSuiteLoader

from fab.config.spec import HostConfigSpecification
from fab.config.values.host import HostAlias
from fab.host.controller import HostControllerMode
from fab.host.database import DatabaseHost
from fab.os.filesystem import LocalFileSystem
from fab.tasks.database.convert import ConvertRSRDatabaseForMigrations
from fab.verifiers.config import ConfigFileVerifier


class StubbedConvertRSRDatabaseForMigrations(ConvertRSRDatabaseForMigrations):

    def __init__(self, config_verifier, configured_database_host):
        super(StubbedConvertRSRDatabaseForMigrations, self).__init__(config_verifier)
        self.configured_database_host = configured_database_host

    def _configure_database_host_with(self, host_controller_mode, host_config):
        return self.configured_database_host


class ConvertRSRDatabaseForMigrationsTest(mox.MoxTestBase):

    def setUp(self):
        super(ConvertRSRDatabaseForMigrationsTest, self).setUp()
        self.mock_config_verifier = self.mox.CreateMock(ConfigFileVerifier)
        self.mock_database_host = self.mox.CreateMock(DatabaseHost)

        self.convert_rsr_database_task = StubbedConvertRSRDatabaseForMigrations(self.mock_config_verifier, self.mock_database_host)

    def test_has_expected_task_name(self):
        """fab.tests.tasks.database.convert_rsr_database_for_migrations_test  Has expected task name"""

        self.assertEqual('convert_rsr_database_for_migrations', ConvertRSRDatabaseForMigrations.name)

    def test_can_convert_rsr_database_for_migrations(self):
        """fab.tests.tasks.database.convert_rsr_database_for_migrations_test  Can convert the RSR database for migrations"""

        self.mock_database_host.convert_database_for_migrations()
        self.mox.ReplayAll()

        self.convert_rsr_database_task.run(HostControllerMode.REMOTE, HostConfigSpecification().create_preconfigured_with(HostAlias.TEST))


def suite():
    return TestSuiteLoader().load_tests_from(ConvertRSRDatabaseForMigrationsTest)

if __name__ == '__main__':
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
