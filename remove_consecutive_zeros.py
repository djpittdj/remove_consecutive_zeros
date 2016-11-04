# the time series looks like the following in a pandas dataframe.
# it has a large amount of zeros, but the interested region is where there are consecutive zeros for, say, over 100 hour.
#                  datetime                 val
# 0     2015-01-01 00:00:00                0.00
# 1     2015-01-01 01:00:00              102.93
# 2     2015-01-01 02:00:00                0.00
# 3     2015-01-01 03:00:00                0.00
# 4     2015-01-01 04:00:00                0.00
# 5     2015-01-01 05:00:00               72.45
# 6     2015-01-01 06:00:00               81.77
# 7     2015-01-01 07:00:00                0.00
# 8     2015-01-01 08:00:00               84.05
# 9     2015-01-01 09:00:00                0.00
# 10    2015-01-01 10:00:00              128.65
# 11    2015-01-01 11:00:00               31.67
# 12    2015-01-01 12:00:00                0.00
# 13    2015-01-01 13:00:00               95.13
# 14    2015-01-01 14:00:00               44.18
# 15    2015-01-01 15:00:00                0.00
# 16    2015-01-01 16:00:00                0.00
# 17    2015-01-01 17:00:00                0.00
# 18    2015-01-01 18:00:00                0.00
# 19    2015-01-01 19:00:00              209.62
# set the cutoff number of hours as 100
cutoff = 100
# convert the relevant columns of the dataframe to a numpy array
a = df[['datetime', 'val']].values
n = len(a)

i = 0
# store the start and end of the consecutive zeros for later use
list_start_dttm = []
list_end_dttm = []
while i<n:
    row = a[i]
    if row[1] == 0.0:
        counter = 0
        start_dttm = row[0]
        for j in range((i+1), n):
            row2 = a[j]
            if row2[1] == 0:
                counter += 1
            else:
                end_dttm = row2[0]
                break
        if counter > cutoff:
            print counter, start_dttm, end_dttm
            list_start_dttm.append(start_dttm)
            list_end_dttm.append(end_dttm)
            i = j
    i += 1
