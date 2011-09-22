#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.helpers.hosts import RemoteHost


class RemoteHostTest(unittest2.TestCase):

    def test_can_create_a_deploymenthost_instance(self):
        """fab.tests.helpers.hosts.remote_host_test  Can create a RemoteHost instance"""

        self.assertIsInstance(RemoteHost.create_instance(), RemoteHost)


def suite():
    return TestSuiteLoader().load_tests_from(RemoteHostTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())