#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import os, subprocess, unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.config.rsr.credentials.user import UserCredentials


class UserCredentialsTest(unittest2.TestCase):

    def test_has_current_user_name(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  Has current user name"""

        self.assertEqual(subprocess.check_output('whoami').strip(), UserCredentials.CURRENT_USER)

    def test_default_password_is_empty(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  Default password is empty"""

        self.assertEqual('', UserCredentials.NO_PASSWORD)

    def test_has_default_ssh_id_path(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  Has default SSH ID file path"""

        self.assertEqual('~/.ssh/id_rsa', UserCredentials.DEFAULT_SSH_ID_PATH)

    def test_can_create_default_user_credentials(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  Can create default user credentials"""

        expected_default_credentials = UserCredentials(UserCredentials.CURRENT_USER,
                                                       UserCredentials.NO_PASSWORD,
                                                       UserCredentials.DEFAULT_SSH_ID_PATH)

        self.assertEqual(expected_default_credentials, UserCredentials.default())

    def test_ssh_id_path_has_expanded_user_directory_instead_of_tilde(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  SSH ID path has expanded user directory instead of tilde"""

        self.assertEqual(os.path.expanduser(UserCredentials.DEFAULT_SSH_ID_PATH), UserCredentials.default().ssh_id_file_path)

    def test_will_exit_if_ssh_key_not_found(self):
        """fab.tests.config.rsr.credentials.user_credentials_test  Will exit if the SSH key cannot be found"""

        with self.assertRaises(SystemExit) as raised:
            expected_default_credentials = UserCredentials(UserCredentials.CURRENT_USER,
                                                           UserCredentials.NO_PASSWORD,
                                                           '.non_existent/ssh_id')

        self.assertEqual('\n## SSH key not found: .non_existent/ssh_id\n', raised.exception.message)


def suite():
    return TestSuiteLoader().load_tests_from(UserCredentialsTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())