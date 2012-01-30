# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import os, subprocess

DEPLOYMENT_STEPS_HOME = os.path.realpath(os.path.join(os.path.dirname(__file__), '../steps'))


class ScenarioRunner(object):

    def run_step(self, step_name, host_config_specification):
        exit_code = self._run_script(os.path.join(DEPLOYMENT_STEPS_HOME, step_name + '.py'), host_config_specification)

        self._stop_scenario_execution_if_deployment_step_failed(exit_code)

    def _run_script(self, script_path, host_config_specification):
        return subprocess.call([script_path, host_config_specification])

    def _stop_scenario_execution_if_deployment_step_failed(self, exit_code):
        # we should already see a failure message when a deployment fails
        if exit_code != 0:
            raise SystemExit