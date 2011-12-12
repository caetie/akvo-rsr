#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os, unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

CONFIG_VALUES_TEMPLATE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../../config/values.py.template'))
imp.load_source('config_values', CONFIG_VALUES_TEMPLATE_PATH)

from config_values import DeploymentHostConfigValues

from fab.environment.python.packageinstallationpaths import SystemPackageInstallationPaths


class SystemPackageInstallationPathsTest(unittest2.TestCase):

    def setUp(self):
        super(SystemPackageInstallationPathsTest, self).setUp()
        self.deployment_host_config_values = DeploymentHostConfigValues()

        self.installation_paths = SystemPackageInstallationPaths(self.deployment_host_config_values)

    def test_can_create_instance(self):
        """fab.tests.environment.python.system_package_installation_paths_test  Can create SystemPackageInstallationPaths instance"""

        self.assertIsInstance(SystemPackageInstallationPaths.create_instance(), SystemPackageInstallationPaths)

    def test_has_explicit_pip_version(self):
        """fab.tests.environment.python.system_package_installation_paths_test  Has explicit pip version"""

        self.assertEqual("1.0.2", SystemPackageInstallationPaths.PIP_VERSION)

    def test_has_package_download_dir(self):
        """fab.tests.environment.python.system_package_installation_paths_test  Has package download directory"""

        expected_package_download_dir = os.path.join(self.deployment_host_config_values.deployment_processing_home, 'python_packages')

        self.assertEqual(expected_package_download_dir, self.installation_paths.package_download_dir)

    def test_has_distribute_setup_url(self):
        """fab.tests.environment.python.system_package_installation_paths_test  Has distribute package setup URL"""

        self.assertEqual("http://python-distribute.org/distribute_setup.py", self.installation_paths.distribute_setup_url)

    def test_has_versioned_pip_setup_url(self):
        """fab.tests.environment.python.system_package_installation_paths_test  Has versioned pip setup URL"""

        expected_pip_setup_url = os.path.join("https://raw.github.com/pypa/pip", SystemPackageInstallationPaths.PIP_VERSION, "contrib/get-pip.py")

        self.assertEqual(expected_pip_setup_url, self.installation_paths.pip_setup_url)


def suite():
    return TestSuiteLoader().load_tests_from(SystemPackageInstallationPathsTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())