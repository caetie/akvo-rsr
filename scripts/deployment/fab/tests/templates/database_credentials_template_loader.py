#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os

CREDENTIALS_TEMPLATE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../config/rsr/credentials.py.template'))
imp.load_source('credentials', CREDENTIALS_TEMPLATE_PATH)