# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import MySQLdb


class DatabaseConnection(object):

    def __init__(self, username, password=None):
        if (password is None) or (password == ''):
            self.db_connection = MySQLdb.connect(user=username)
        else:
            self.db_connection = MySQLdb.connect(user=username, passwd=password)

    def create_cursor(self):
        return self.db_connection.cursor()

    def __del__(self):
        if (self.db_connection):
            self.db_connection.close()