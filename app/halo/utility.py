from __future__ import print_function
from datetime import datetime
import plotly.express as px
import pandas as pd
import sys


class Utility(object):
    """This is a collection of widely-used functions"""

    @classmethod
    def date_to_iso8601(cls, date_obj):
        """Returns an ISO8601-formatted string for datetime arg"""
        retval = date_obj.isoformat()
        return retval

    @classmethod
    def log_stdout(cls, message, component="CLOUD_CSM_REPORTS"):
        """Log messages to stdout.

        Args:
            message(str): Message to be logged to stdout.
            component(str): Component name. Defaults to "CLOUD_CSM_REPORTS".
        """
        out = "%s: %s" % (component, message)
        print(out, file=sys.stdout)
        return

    @classmethod
    def log_stderr(cls, message, component="CLOUD_CSM_REPORTS"):
        """Log messages to stderr.

        Args:
            message(str): Message to be logged to stdout.
            component(str): Component name. Defaults to "CLOUD_CSM_REPORTS".
        """
        out = "%s: %s" % (component, message)
        print(out, file=sys.stderr)
        return

    def plot_pie_graph(self, output_directory, overall_pass, overall_critical_fail, overall_noncritical_fail):
        current_time = Utility.date_to_iso8601(datetime.now())
        figure_name = 'Figure_Report_' + current_time + '.png'
        figure_name = figure_name.replace(':', '-')
        d_labels = ['Overall Pass', 'Overall Critical Fail',
                    'Overall Non-Critical Fail']
        values = [overall_pass, overall_critical_fail, overall_noncritical_fail]
        data = {'Item': d_labels,
                'Percentage': values}
        df = pd.DataFrame(data)
        fig = px.pie(df, values='Percentage', names='Item', color='Item', color_discrete_map={'Overall Pass':'green',
                                 'Overall Critical Fail':'red',
                                 'Overall Non-Critical Fail':'yellow'})
        fig.write_image("%s/%s" %(output_directory, figure_name))

    def plot_bar_graph(self, overall_pass, overall_critical_fail, overall_noncritical_fail):
        current_time = Utility.date_to_iso8601(datetime.now())
        figure_name = 'Figure_Report_' + current_time + '.png'
        figure_name = figure_name.replace(':', '-')
        d_labels = ['Overall Pass', 'Overall Critical Fail',
                    'Overall Non-Critical Fail']
        values = [overall_pass, overall_critical_fail, overall_noncritical_fail]
        data = {'Item': d_labels,
                'Percentage': values}
        df = pd.DataFrame(data)
        fig = px.bar(df, x="Item", y="Percentage",
                     color="Item", title="Cloud CSM Report")
        fig.write_image("../resources/%s" %(figure_name))