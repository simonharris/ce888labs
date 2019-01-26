import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np


if __name__ == "__main__":

	# Use Pandas to read in data -----------------------------------------------

	df = pd.read_csv('./vehicles.csv')

	# Use Seaborn to plot a scatter chart --------------------------------------

	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=True)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("veh_scatterplot.png", bbox_inches='tight')
	sns_plot.savefig("veh_scatterplot.pdf", bbox_inches='tight')

	# Use Seaborn to plot a histogram of the Fleet 2 column --------------------

	# Convert Fleet 2 column to a single row
	data = df.values.T[1]

	# Clear the current Matplotlib figure
	# This seems odd - how did Matplot globally know about our Seaborn chart?
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	# Get current axes, label them
	axes = plt.gca() # Instance of AxesSubplot
	axes.set_xlabel('Vehicle MPG (?)') # I don't know what the numbers actually refer to
	axes.set_ylabel('Vehicle Count')

	sns_plot2.savefig("veh_histogram.png", bbox_inches='tight')
	sns_plot2.savefig("veh_histogram.pdf", bbox_inches='tight')
