# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import fab.tasks.database.basetask


class BackupRSRDatabase(fab.tasks.database.basetask.RSRDatabaseTask):
    """Creates a backup of the RSR database"""

    name = 'backup_rsr_database'

    def _perform_database_actions_with(self, database_host):
        database_host.backup_rsr_database()


instance = BackupRSRDatabase()
