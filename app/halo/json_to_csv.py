import csv
from datetime import datetime
from halo.utility import Utility


class JSONToCSV(object):

    def prepare_csv_file(self, output_directory):
        # Preparing CSV file for writing
        current_time = Utility.date_to_iso8601(datetime.now())
        file_name = 'Cloud_CSM_Report_' + current_time + '.csv'
        file_name = file_name.replace(':', '-')
        if output_directory == "":
            absolute_path = file_name
        else:
            absolute_path = output_directory + "/" + file_name
        return absolute_path, file_name, current_time

    def prepare_report_statistics(self, json_object):
        json_data = json_object[0]
        csp_findings_data = json_data['csp_findings']
        total_pass_count = 0
        total_count = 0
        total_critical_fail_count = 0
        total_non_critical_fail_count = 0
        total_fail_count = 0
        for csp_finding in csp_findings_data:
            total_pass_count += csp_finding['pass']
            total_count += csp_finding['total']
            criticality = csp_finding['criticality']
            if criticality == 'critical':
                total_critical_fail_count += csp_finding['fail']
            else:
                total_non_critical_fail_count += csp_finding['fail']
            total_fail_count += csp_finding['fail']

        return total_pass_count, total_count, total_critical_fail_count, total_non_critical_fail_count, total_fail_count

    def convert_json_to_csv(self, counter, absolute_path, file_name, current_time, json_object, overall_pass, overall_critical_fail, overall_non_critical_fail):
        json_data = json_object[0]
        csp_findings_data = json_data['csp_findings']
        total_rows = json_data['count']
        with open(absolute_path, 'a') as data_file:
            csv_writer = csv.writer(data_file, lineterminator='\n')
            # counter variable used for writing headers to the CSV file
            for csp_finding in csp_findings_data:
                if counter == 0:
                    csv_writer.writerow(
                        ["# ------------------------------- #"])
                    csv_writer.writerow(["# Report Name: %s" % (file_name)])
                    csv_writer.writerow(
                        ["# Report Generated at: %s" % (current_time)])
                    csv_writer.writerow(
                        ["# Overall Pass: %s" % (overall_pass)+" %"])
                    csv_writer.writerow(
                        ["# Overall Critical Fail: %s" % (overall_critical_fail)+" %"])
                    csv_writer.writerow(
                        ["# Overall Non-Critical Fail: %s" % (overall_non_critical_fail)+" %"])
                    csv_writer.writerow(["# Total Rows: %s" % (total_rows)])
                    csv_writer.writerow(
                        ["# ------------------------------- #"])
                    # Writing headers of CSV file
                    #header = csp_finding.keys()
                    modified_header = ['CSP Service Type', 'CSP Resource Type', 'Policy Name', 'CP Rule ID', 'Rule Name',
                                       'Criticality', 'Pass Count', 'Pass Percentage', 'Fail Count', 'Fail Percentage',
                                       'Indeterminate Count', 'Indeterminate Percentage', 'Total Count']
                    # csv_writer.writerow(header)
                    csv_writer.writerow(modified_header)
                    counter += 1
                pass_percentage = str(
                    round(((csp_finding['pass']/csp_finding['total'])*100), 2))+" %"
                fail_percentage = str(
                    round(((csp_finding['fail']/csp_finding['total'])*100), 2))+" %"
                indeterminate_percentage = str(
                    round(((csp_finding['error']/csp_finding['total'])*100), 2))+" %"
                # Writing data of CSV file
                modified_values = [csp_finding['csp_service_type'], csp_finding['csp_resource_type'], csp_finding['policy_name'],
                                   csp_finding['cp_rule_id'], csp_finding['rule_name'], csp_finding[
                                       'criticality'], csp_finding['pass'], pass_percentage,
                                   csp_finding['fail'], fail_percentage, csp_finding['error'], indeterminate_percentage, csp_finding['total']]
                # csv_writer.writerow(csp_finding.values())
                csv_writer.writerow(modified_values)
            data_file.close()
