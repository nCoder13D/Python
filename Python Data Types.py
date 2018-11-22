# You are only allowed to use the Python standard libraries for this task: 
# No NumPy, no Pandas !!!
#
# Given a table of data represented as a list of lists, compute the averages
# of a specified column `col`, within groups specified by column `by`
# `col` and `by` are column indices.
# The input table is a list lists, each inner list is a row of the table.
# The output should be a dictionary.
#
# Example:
# Calculating the average of col 0, grouped by col 3
#[[15 29  6  2], [16  9  8  0],  [ 7 27 16  0]]
# OUT - {0: 11.5, 2: 15.0}
#     - OK
#
# Make sure to try edge cases, such as an empty table.
# No need to check input validity.
def avgby(tbl, col, by):
    hold={}
    avg={}
    if tbl is None:
        return {}
    else:
        for row in tbl:
            if row[by] in hold:
                hold[row[by]].append(row[col])
            else:
                hold[row[by]]=[row[col]]
        for keys, values in sorted(hold.items()):
            avg[keys]=(sum(values))/len(values)
        return avg
    
# You are only allowed to use the Python standard libraries for this task: 
# No NumPy, no Pandas !!!
#
# Write a merge function to implement a _inner_ join of two data tables each 
# represented as a list of rows where each row is a list.
#
# Inputs:
#  - `left` and `right` - data tables
#  - `left_on` and `right_on` - the column indices containing the key to merge 
#     on in each of the tables.
# 
# Example 1:
# Merging on column 0 of each table (person name)
left = [['Bob', 'Accounting'],
         ['Jake', 'Engineering'],
         ['Lisa', 'HR']]
right = [['Lisa', 2004],
         ['Bob', 2008], 
         ['Jake', 2012], 
         ['Sue', 2014]]
# merged =   [['Bob', 'Accounting', 'Bob', 2008],
#             ['Jake', 'Engineering', 'Jake', 2012],
#             ['Lisa', 'HR', 'Lisa', 2004]]
#  
# Example 2:
# Merging on columns 1 and 0, note that 'B' appears twice in the right table.
# left = [[1, 'A'], [2, 'B'], [3, 'C']]
# right = [['A', 2004], ['B', 2008], ['C', 2012], ['B', 2014]]
# merged =   [[1, 'A', 'A', 2004],
#             [2, 'B', 'B', 2008],
#             [2, 'B', 'B', 2014],
#             [3, 'C', 'C', 2012]]
#
# "Inner join" means that only rows with data from both tables are returned.
# Each row in the merged table should be the concatenation of corresponding
# rows from the left and right tables. 
# In terms of Python lists:
#     row_in_merged_tbl = row_from_left + row_from_right
# where the following is true
#     row_from_left[left_on] == row_from_right[right_on]
# This merge is essentially equivalent to pd.merge(tbl1, tbl2, left_on=?, right_on=?)

def merge(left, right, left_on, right_on):
    merged=[]
    ls=[]
    if left and right is None:
        return merged
    for lrow in left:
        for rrow in right:
            if rrow[right_on] in lrow:
                ls=lrow+rrow
                merged.append(ls)
    return merged
