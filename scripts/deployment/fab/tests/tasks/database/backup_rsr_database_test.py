#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.host.controller import HostControllerMode
from fab.host.database import DatabaseHost
from fab.tasks.database.backup import BackupRSRDatabase


class StubbedBackupRSRDatabase(BackupRSRDatabase):

    def __init__(self, database_host):
        self.database_host = database_host

    def _create_database_host(self, host_controller_mode):
        return self.database_host


class BackupRSRDatabaseTest(mox.MoxTestBase):

    def setUp(self):
        super(BackupRSRDatabaseTest, self).setUp()
        self.mock_database_host = self.mox.CreateMock(DatabaseHost)

        self.backup_rsr_database_task = StubbedBackupRSRDatabase(self.mock_database_host)

    def test_has_expected_task_name(self):
        """fab.tests.tasks.database.backup_rsr_database_test  Has expected task name"""

        self.assertEqual("backup_rsr_database", BackupRSRDatabase.name)

    def test_can_create_task_instance(self):
        """fab.tests.tasks.database.backup_rsr_database_test  Can create task instance"""

        self.assertIsInstance(BackupRSRDatabase.create_task(), BackupRSRDatabase)

    def test_can_backup_rsr_database(self):
        """fab.tests.tasks.database.backup_rsr_database_test  Can backup the RSR database"""

        self.mock_database_host.backup_rsr_database()
        self.mox.ReplayAll()

        self.backup_rsr_database_task.run(HostControllerMode.REMOTE)


def suite():
    return TestSuiteLoader().load_tests_from(BackupRSRDatabaseTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
