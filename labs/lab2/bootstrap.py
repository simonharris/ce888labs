import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def bootstrap(sample, sample_size, iterations, confidence_interval=95):

	# Create an array of samples of shape (iterations, sample_size)
	new_samples = np.random.choice(sample, size=(iterations, sample_size))

	# Calculate and save the mean of the array (we return it at the end)
	data_mean = new_samples.mean()

	# In each iteration
	# - calculate the mean of the iteration data
	# - store it in an array
	means = np.array([iteration.mean() for iteration in new_samples])

	# Calculate the lower and upper bounds for a given CI
	gap = (100 - confidence_interval) / 2
	lower = np.percentile(means, gap)
	upper = np.percentile(means, 100 - gap)

	return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')

	data = df.values.T[1]
	boots = []

	#boot = bootstrap(data, data.shape[0], 10)

	for i in range(100, 100000, 1000):
		boot = bootstrap(data, data.shape[0], i)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')


	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))
