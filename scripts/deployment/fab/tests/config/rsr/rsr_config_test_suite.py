#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.tests.config.rsr.codebase_config_test import RSRCodebaseConfigTest
from fab.tests.config.rsr.deployment_config_test import RSRDeploymentConfigTest
from fab.tests.config.rsr.virtualenv_installer_config_test import RSRVirtualEnvInstallerConfigTest


def rsr_config_suite():
    return TestSuiteLoader().create_suite_from_classes([RSRCodebaseConfigTest, RSRDeploymentConfigTest, RSRVirtualEnvInstallerConfigTest])

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(rsr_config_suite())