# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


class UbuntuPackageInfo(object):

    def __init__(self, name, version, state):
        self.name = name
        self.version = version
        self.state = state

        self._set_name_and_installed_version()

    def __eq__(self, package_info):
        return (self.name == package_info.name and
                self.version == package_info.version and
                self.state == package_info.state)

    def __ne__(self, package_info):
        return not self.__eq__(package_info)

    def _set_name_and_installed_version(self):
        installed_version = self.version if self.is_installed() else self.state
        self.name_and_installed_version = "%s (%s)" % (self.name, installed_version)

    def is_installed(self):
        return self.state == "installed"

    @staticmethod
    def from_text(package_info_text):
        return UbuntuPackageInfoParser().parse(package_info_text)


class UbuntuPackageInfoParser(object):

    def parse(self, package_info_text):
        package_info_dictionary = self._create_package_info_dictionary(package_info_text)

        return UbuntuPackageInfo(package_info_dictionary['Package'],
                                 package_info_dictionary['Version'],
                                 package_info_dictionary['State'])

    def _create_package_info_dictionary(self, package_info_text):
        package_info_lines = package_info_text.split("\r\n")[:5] # we only need the first 5 info lines
        package_info_dictionary = {}

        for info_line in package_info_lines:
            info_parts = info_line.split(":", 1) # some lines may have colons in the text so we split once only
            package_info_dictionary[info_parts[0]] = info_parts[1].strip()

        return package_info_dictionary
