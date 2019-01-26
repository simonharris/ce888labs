from bootstrap import bootstrap
import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')

    mean_all = df.mean().mean()

    old_fleet = df.values.T[0]
    new_fleet = df.values.T[1]
    new_fleet = new_fleet[~np.isnan(new_fleet)] # remove NaN values

    # arbitrary number
    iterations = 1000

    mean_old, lower_old, upper_old = bootstrap(old_fleet, old_fleet.shape[0], iterations)
    mean_new, lower_new, upper_new = bootstrap(new_fleet, new_fleet.shape[0], iterations)

    print('Overall mean:', mean_all)
    print('Old Lower:', lower_old)
    print('Old Upper:', upper_old)
    print('New Lower:', lower_new)
    print('New Upper:', upper_new)
