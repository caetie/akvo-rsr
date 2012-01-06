#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox, os

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.config.rsr.virtualenv import RSRVirtualEnvInstallerConfig
from fab.host.controller import HostControllerMode
from fab.host.virtualenv import VirtualEnvDeploymentHost

from fab.tasks.environment.python.virtualenv.rsr import RebuildRSREnv


class StubbedRebuildRSREnv(RebuildRSREnv):

    def _configure_host_using(self, host_controller_mode):
        pass # so that we can mock the host configuration


class RebuildRSREnvTest(mox.MoxTestBase):

    def setUp(self):
        super(RebuildRSREnvTest, self).setUp()
        self.deployment_user = "rupaul"

        self.virtualenv_installer_config = RSRVirtualEnvInstallerConfig.create_instance(self.deployment_user)
        self.mock_virtualenv_deployment_host = self.mox.CreateMock(VirtualEnvDeploymentHost)

        self.rebuild_virtualenv_task = StubbedRebuildRSREnv(self.virtualenv_installer_config)
        self.rebuild_virtualenv_task.virtualenv_deployment_host = self.mock_virtualenv_deployment_host

    def test_has_expected_task_name(self):
        """fab.tests.tasks.environment.python.virtualenv.rebuild_rsr_env_test  Has expected task name"""

        self.assertEqual("rebuild_rsr_env", RebuildRSREnv.name)

    def test_can_create_task_instance(self):
        """fab.tests.tasks.environment.python.virtualenv.rebuild_rsr_env_test  Can create task instance"""

        self.assertIsInstance(RebuildRSREnv.create_task_instance(self.deployment_user), RebuildRSREnv)

    def test_can_configure_host_using_local_hostcontrollermode(self):
        """fab.tests.tasks.environment.python.virtualenv.rebuild_rsr_env_test  Can configure host using local HostControllerMode"""

        self._verify_host_configuration_with(HostControllerMode.LOCAL)

    def test_can_configure_host_using_remote_hostcontrollermode(self):
        """fab.tests.tasks.environment.python.virtualenv.rebuild_rsr_env_test  Can configure host using remote HostControllerMode"""

        self._verify_host_configuration_with(HostControllerMode.REMOTE)

    def _verify_host_configuration_with(self, host_controller_mode):
        rebuild_rsr_env_task = RebuildRSREnv.create_task_instance(self.deployment_user)
        rebuild_rsr_env_task._configure_host_using(host_controller_mode)

        self.assertIsInstance(rebuild_rsr_env_task.virtualenv_deployment_host, VirtualEnvDeploymentHost)

    def test_can_rebuild_rsr_virtualenv(self):
        """fab.tests.tasks.environment.python.virtualenv.rebuild_rsr_env_test  Can rebuild an RSR virtualenv"""

        self.mock_virtualenv_deployment_host.ensure_user_has_required_deployment_permissions()
        self.mock_virtualenv_deployment_host.ensure_virtualenv_exists()
        self.mock_virtualenv_deployment_host.install_virtualenv_packages(self.virtualenv_installer_config.rsr_requirements_path)
        self.mock_virtualenv_deployment_host.install_virtualenv_packages(self.virtualenv_installer_config.testing_requirements_path)
        self.mox.ReplayAll()

        self.rebuild_virtualenv_task.run(HostControllerMode.REMOTE)


def suite():
    return TestSuiteLoader().load_tests_from(RebuildRSREnvTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
