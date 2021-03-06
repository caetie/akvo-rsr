# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from fab.os.system import SystemType


class StatCommand(object):

    def __init__(self, system_type):
        self.system_type = system_type

    def for_path(self, path):
        query_format = { SystemType.LINUX: "-c %F", SystemType.MAC_OSX: "-f %HT" }[self.system_type]

        return "stat %s %s" % (query_format, path)
