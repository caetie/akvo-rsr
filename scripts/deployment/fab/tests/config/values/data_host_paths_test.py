#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.config.values.host import DataHostPaths


class DataHostPathsTest(unittest2.TestCase):

    def test_has_django_apps_home(self):
        """fab.tests.config.values.data_host_paths_test  Has Django apps home"""

        self.assertEqual('/var/lib/django', DataHostPaths().django_apps_home)

    def test_has_virtualenvs_home(self):
        """fab.tests.config.values.data_host_paths_test  Has virtualenvs home"""

        self.assertEqual('/var/virtualenvs', DataHostPaths().virtualenvs_home)


def suite():
    return TestSuiteLoader().load_tests_from(DataHostPathsTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())