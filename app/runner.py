import sys
import math

from halo import config_helper
from halo import halo_api_caller
from halo import utility
from halo import json_to_csv


def main():
    util = utility.Utility()
    util.log_stdout("Cloud CSM Reports Script Started ...")
    config = config_helper.ConfigHelper()
    json_to_csv_obj = json_to_csv.JSONToCSV()
    output_directory = config.output_directory

    util.log_stdout("1- Creating HALO API CALLER Object.")
    halo_api_caller_obj = halo_api_caller.HaloAPICaller(config)

    """
    First we make sure that all configs are sound...
    """
    util.log_stdout(
        "2- Checking the provided configuration parameters")
    check_configs(config, halo_api_caller_obj, util)

    """
    Preparing Cloud CSM Report Statistics (overall_pass, overall_critical_fail, overall_non_critical_fail, total_rows)
    """
    util.log_stdout(
        "3- Preparing Cloud CSM Report Statistics (overall_pass, overall_critical_fail, overall_non_critical_fail, total_rows)")
    csp_findings_count = halo_api_caller_obj.get_csp_findings_count()
    csp_findings_count_data = csp_findings_count[0]
    try:
        total_rows = csp_findings_count_data['count']
    except:
        total_rows = 0
    pages = math.ceil(total_rows/100)

    absolute_path, file_name, current_time = json_to_csv_obj.prepare_csv_file(
        output_directory)

    overall_total_pass_count = 0
    overall_total_count = 0
    overall_total_critical_fail_count = 0
    overall_total_non_critical_fail_count = 0
    overall_total_fail_count = 0

    for page in range(pages):
        current_page = page+1
        csp_findings_lst = halo_api_caller_obj.get_csp_findings(current_page)
        total_pass_count, total_count, total_critical_fail_count, total_non_critical_fail_count, total_fail_count = json_to_csv_obj.prepare_report_statistics(
            csp_findings_lst)

        overall_total_pass_count += total_pass_count
        overall_total_count += total_count
        overall_total_critical_fail_count += total_critical_fail_count
        overall_total_non_critical_fail_count += total_non_critical_fail_count
        overall_total_fail_count += total_fail_count

    overall_pass = round(
        ((overall_total_pass_count/overall_total_count)*100), 2)
    overall_critical_fail = round(
        ((overall_total_critical_fail_count/overall_total_count)*100), 2)
    overall_non_critical_fail = round(
        ((overall_total_non_critical_fail_count/overall_total_count)*100), 2)

    """
    Exporting Cloud CSM Reports data of into CSV file format
    """
    util.log_stdout(
        "4- Retrieving & Exporting Reports Data [page - %s] into CSV file format" % (current_page))
    for page in range(pages):
        counter = page
        current_page = page+1
        csp_findings_lst = halo_api_caller_obj.get_csp_findings(current_page)

        """
        Retrieving & Exporting Reports Data Pages into CSV file format
        """
        util.log_stdout(
            "...Retrieving & Exporting reports data [page - %s] into CSV file format" % (current_page))
        json_to_csv_obj.convert_json_to_csv(counter, absolute_path, file_name, current_time,
                                            csp_findings_lst, overall_pass, overall_critical_fail, overall_non_critical_fail)

    """
    Generating Pie Chart for overall statistics
    """
    util.log_stdout(
        "5- Generating Pie Chart for overall statistics")
    util.plot_pie_graph(output_directory, overall_pass, overall_critical_fail, overall_non_critical_fail)

    """
    Operation Completed
    """
    util.log_stdout(
        "6- Operation Completed, Check Generated CSV File!")


def check_configs(config, halo_api_caller, util):
    halo_api_caller_obj = halo_api_caller
    if halo_api_caller_obj.credentials_work() is False:
        util.log_stdout("Halo credentials are bad!  Exiting!")
        sys.exit(1)

    if config.sane() is False:
        util.log_stdout("Configuration is bad!  Exiting!")
        sys.exit(1)


if __name__ == "__main__":
    main()
