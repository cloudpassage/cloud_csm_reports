import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from halo import config_helper
from halo import halo_api_caller
from halo import utility

def test_pie_graph_plot():
    utility.Utility.plot_pie_graph()

def test_bar_graph_plot():
    utility.Utility.plot_bar_graph()

def test_get_group_policies(group_id):
    config = config_helper.ConfigHelper()
    halo_api_caller_obj = halo_api_caller.HaloAPICaller(config)
    halo_api_caller_obj.authenticate_client()
    group_policy_list = halo_api_caller_obj.get_group_policies(group_id)
    print(group_policy_list[0])

def test_get_csp_findings_count():
    config = config_helper.ConfigHelper()
    halo_api_caller_obj = halo_api_caller.HaloAPICaller(config)
    halo_api_caller_obj.authenticate_client()
    no_of_csp_findings = halo_api_caller_obj.get_csp_findings_count()
    print("No of CSP Findings= %s" %(no_of_csp_findings[0]))


if __name__ == "__main__":
    test_pie_graph_plot()
    
    # test_bar_graph_plot()
    
    # group_id = "35b94c18f5a811e98e3a27c3c76fe100"
    # test_get_group_policies(group_id)

    # test_get_csp_findings_count()