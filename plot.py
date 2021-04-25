import plotly.graph_objects as go
import os

from plotly.subplots import make_subplots

from constants import Columns, Labels
from util import banner


def generate_plots(data):
    """
    Generate plots for each lift

    :param data: dict, source data for the plots

    Example:
    {
        "Back Squat": {
            "LSRPE": [9, 8, 8],
            "sets": [[185.0, 190.0, 195.0], [190.0, 190.0, 195.0], [195.0, 195.0, 200.0]],
            "averages": [190.0, 192.5, 197.5]
        },
        "Bench Press": {
            "LSRPE": [7, 9, 9]
            "sets": [[145.0, 145.0, 155.0], [155.0, 160.0, 160.0], [160.0, 165.0, 165.0]],
            "averages": [147.5, 157.5, 162.5]
        }
    }

    :returns: list of go.Figure, the generated plots
    """

    print(f'Generating plots...')
    plots = []
    for exercise_name, collected_data in data.items():
        msg = banner(f'{exercise_name} - Avg Set + LSRPE', char='-')
        print(msg)


        averages = collected_data[Labels.AVERAGES]
        lsrpe = collected_data[Labels.LSRPE]
        plot = generate_averages_lsrpe_plot(exercise_name, averages, lsrpe)
        export_to_png(exercise_name, plot)
        plots.append(plot)

        print('Done')
    print(f'Plots successfully generated')


def generate_averages_lsrpe_plot(exercise_name, averages, lsrpe):
    print('Generating plot...')

    # Create figure with secondary y-axis
    plot = make_subplots(specs=[[{"secondary_y": True}]])

    # Add averages data
    plot.add_trace(go.Scatter(x=list(range(1, len(averages)+1)), y=averages, name='Weight',
                             line=dict(color='royalblue', width=4)))

    # Add lsrpe data
    plot.add_trace(go.Scatter(x=list(range(1, len(lsrpe)+1)), y=lsrpe, name='LSRPE',
                             line=dict(color='firebrick', width=4)), secondary_y=True)

    # Update titles
    plot.update_layout(title=f'<b>{exercise_name} - Average Weight and LSRPE</b>',
                      xaxis_title='<b>Workout Number</b>',
                      yaxis_title='<b>Average Weight (lbs)</b>')
    plot.update_layout(xaxis=dict(
            tickmode='linear',
            tick0=1,
            dtick=1
        )
    )
    plot.update_yaxes(tickmode='linear', dtick=5)
    plot.update_yaxes(title_text='<b>Last Set RPE</b>',
                     tickmode='linear',
                     tick0=5,
                     dtick=1,
                     gridcolor='#f59890',
                     secondary_y=True)

    return plot


def export_to_png(exercise_name, plot):
    filename = f'output/plots/{exercise_name.replace(" ", "_")}_avg_set_and_lsrpe.png'
    print(f'Exporting png to {filename}...')
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f'Removed previous version of {filename}')
        except Exception as e:
            print(f'Error: Unable to remove previous version of {filename}: {e}')
            return
    plot.write_image(filename, engine='kaleido')
