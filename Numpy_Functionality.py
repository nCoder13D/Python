# Create an N by N 2D array with 1 on both diagonals and zeros everywhere else. 
# Examples :
#           N = 4                N = 3
#       [[1, 0, 0, 1],        [[1, 0, 1],
#        [0, 1, 1, 0],         [0, 1, 0],
#        [0, 1, 1, 0],         [1, 0, 1]]
#        [1, 0, 0, 1]])

def xmatrix(N):
    a=np.eye(N)
    b=np.fliplr(a)+np.eye(N)
    x=N//2
    b[x,x]=1
    return b

# Write a function that given a 2D array m finds the column with the lowest sum, 
# and the row with the lowest sum and returns their indices.
# min_row_col(m) => [min_row_idx, min_col_idx]
# For example:
# m1 = np.array( [[0, 1, 2],
#                 [0, 0, 0],
#                 [0, 1, 2]])
# In [n]: min_row_col(m1)
# Out[n]: [1, 0]
# The lowest sums are in the middle row (row 1) and the leftmost column (col 0).
#
# The output value should be either a list or a tuple of length 2, row index
# first, and then column index.
# If two or more rows (or columns) have the same lowest sum, use the one with 
# the lowest index.
# 
# Hints:
#  - Check out the numpy argmin() function: same as min, but returns the index
#    of the minimum rather than the minimum itself.
#    For example, for 1D array `b` if ix = b.argmin() then b[ix] == b.min()

def min_row_col(m):
    row=m.sum(axis=1)
    col=m.sum(axis=0)
    return row.argmin(),col.argmin()

# The `car_data` array holds reading from a car dashboard. The first column is
# speed in km/h and the second column is engine rotation speed in revolutions
# per minute (RPM). After the readings were taken it was discovered that both
# gauges exaggerate their readings, the speed is reported `speed_bias` above the
# real speed and the RPMs are `rpm_bias` above the real RPMs. Write a function
# that takes the readings and the biases and returns the corrected data.
# The returned array should be of the same shape as `car_data`.
#
# FYI: The RPM gauge is called "tachometer"
def fix_gauge_bias(car_data, speed_bias, rpm_bias):
    speed=car_data[:,0]-speed_bias
    rpm=car_data[:,1]-rpm_bias
    car_data=np.column_stack((speed,rpm))
    return car_data

# Continuing with car data from previous task. In most cars the ratio between
# car speed and engine rotation speed only changes when the car shifts gears.
# For example in the test data for the previous task (after adjustment for
# biases), RPMs=(car speed)*85 for _all_ rows. This means the car was in the
# same gear while all of the readings were taken and the speed ratio was 85.
#
# Write a function that detects if the car switched gears and returns True if it
# did and False otherwise. Use the following assumptions:
#  - The car from which this data originates has simple gears with constatant
#    ratios as described above.
#  - RPMs/(car speed) ratios for different gears differ by at least 10%. For
#    example ratios of 75 and 95 are definitely from different gears, while 85.1
#    and 85.2 should be considered the same gear. The slight variations can
#    result from measurement inaccuracies and rounding errors, but you can
#    safely assume that those variations are way below 10%.
#  - The data is in the same format as before - two columns - [km/h, RPMs]
#  - Any known biases were already accounted for in the input - no need to call
#    fix_gauge_bias()
#

def was_gear_switched(car_data):
    rpm= car_data[:,1]
    sp=car_data[:,0]
    gear=rpm/sp
    low=gear-(gear*0.1)
    high=gear+(gear*0.1)
    gear_shift=np.array([])
    for i in range(len(gear)):
        if ((gear[i]>=low) & (gear[i]<=high)).all():
            gear_shift=np.append(gear_shift,gear[i])
        else:
            return True
    return False
