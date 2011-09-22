# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import fabric.tasks

import fab.config.environment.linux.systempackages
import fab.host.linux


class VerifySystemPackages(fabric.tasks.Task):
    """Verifies that the expected Linux system packages exist"""

    name = "verify_system_packages"

    def __init__(self, linux_host):
        self.linux_host = linux_host

    @staticmethod
    def create_task_instance():
        return VerifySystemPackages(fab.host.linux.LinuxHost.create_instance())

    def run(self):
        for package_specifications in fab.config.environment.linux.systempackages.SystemPackageSpecifications.ALL_PACKAGES:
            self.linux_host.exit_if_system_package_dependencies_not_met(package_specifications)


instance = VerifySystemPackages.create_task_instance()