#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, mox, os

from testing.helpers.execution import TestSuiteLoader, TestRunner

import fab.tests.templates.database_credentials_template
from database_credentials import DatabaseCredentials

from fab.config.rsr.database import RSRDatabaseConfig
from fab.config.rsr.host import CIDeploymentHostConfig
from fab.database.mysql.admin import DatabaseAdmin
from fab.helpers.feedback import ExecutionFeedback
from fab.host.controller import LocalHostController, RemoteHostController
from fab.host.database import DatabaseHost


class DatabaseHostTest(mox.MoxTestBase):

    def setUp(self):
        super(DatabaseHostTest, self).setUp()
        self.deployment_host_config = CIDeploymentHostConfig.for_test()
        self.database_config = RSRDatabaseConfig(DatabaseCredentials(), self.deployment_host_config)
        self.mock_database_admin = self.mox.CreateMock(DatabaseAdmin)

        self.database_host = DatabaseHost(self.database_config, self.mock_database_admin)

    def test_can_create_remote_database_host_instance(self):
        """fab.tests.host.database_host_test  Can create a remote DatabaseHost instance"""

        self.assertIsInstance(self._create_database_host_instance_with(RemoteHostController), DatabaseHost)

    def test_can_create_local_database_host_instance(self):
        """fab.tests.host.database_host_test  Can create a local DatabaseHost instance"""

        self.assertIsInstance(self._create_database_host_instance_with(LocalHostController), DatabaseHost)

    def _create_database_host_instance_with(self, host_controller_class):
        mock_host_controller = self.mox.CreateMock(host_controller_class)
        mock_host_controller.feedback = self.mox.CreateMock(ExecutionFeedback)

        self.mox.ReplayAll()

        return DatabaseHost.create_with(self.database_config, self.deployment_host_config, mock_host_controller)

    def test_can_backup_rsr_database(self):
        """fab.tests.host.database_host_test  Can backup the RSR database"""

        self.mock_database_admin.create_timestamped_backup_database(self.database_config.rsr_database)
        self.mox.ReplayAll()

        self.database_host.backup_rsr_database()

    def test_can_rebuild_rsr_database(self):
        """fab.tests.host.database_host_test  Can rebuild the RSR database"""

        self.mock_database_admin.rebuild_database(self.database_config.rsr_database,
                                                  self.database_config.rsr_user,
                                                  self.database_config.rsr_password)
        self.mox.ReplayAll()

        self.database_host.rebuild_rsr_database()

    def test_can_convert_database_for_migrations(self):
        """fab.tests.host.database_host_test  Can convert database for migrations"""

        self.mock_database_admin.convert_database_for_migrations()
        self.mox.ReplayAll()

        self.database_host.convert_database_for_migrations()

    def test_can_run_all_database_migrations(self):
        """fab.tests.host.database_host_test  Can run all database migrations"""

        self.mock_database_admin.run_all_migrations()
        self.mox.ReplayAll()

        self.database_host.run_all_migrations()


def suite():
    return TestSuiteLoader().load_tests_from(DatabaseHostTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
