#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os, sys

VERIFIERS_HOME = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../verifiers'))
imp.load_source("syspath_verification", os.path.join(VERIFIERS_HOME, 'ensure_syspath_contains_deployment_scripts_home.py'))

from execution.scenarios.runner import ScenarioRunner

import execution.verification


def prepare_database_for_migrations(scenario_runner, deployment_host_config_specification):
    scenario_runner.run_step('fetch_rsr_data')
    scenario_runner.run_step('rebuild_rsr_database', deployment_host_config_specification) # performs a backup as well


if __name__ == '__main__':
    execution.verification.display_usage_and_exit_if_host_config_spec_is_missing(os.path.basename(__file__))
    prepare_database_for_migrations(ScenarioRunner(), sys.argv[1])