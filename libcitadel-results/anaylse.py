import numpy as np
import sys

filepath = "libcitadel-benchmarks" if len(sys.argv) == 1 else sys.argv[1]

# Open logs file
data = {}
with open(filepath, "r") as logs:
    for line in logs:
        parts = line.split(",")
        if parts[0] not in data:
            data[parts[0]] = []
        data[parts[0]].append(int(parts[1]))

for test in data:
    median = np.percentile(data[test], 50)
    iqr_l = np.percentile(data[test], 15.9)
    iqr_h = np.percentile(data[test], 84.1)

    std = np.mean([ median - iqr_l, iqr_h - median ])
    print("{} - {:.3f}\pm{:.3f}".format(test, median/1000.0, std/1000.0))
    #std = np.std(data[test]) / 1000.0
    #print("{} - {}us ({:.2f}-{:.2f}us)".format(test, median/1000.0, iqr_l/1000.0, iqr_h/1000.0))


