'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def sort_intervals(intervals):
    """ sort intervals by start time, breaking ties by end time
        merge sort """

    if len(intervals) <= 1:
        return intervals
    
    mid = len(intervals) // 2
    left = sort_intervals(intervals[0:mid])
    right = sort_intervals(intervals[mid:])

    return merge(left, right)

def merge(left, right):
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Compare start times first, then end times if start is equal
        if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and left[i][1] <= right[j][1]):
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list



def interval_covering(M: int, intervals: list) -> list:
    sorted_intervals = sort_intervals(intervals)

    result = []
    result.append(sorted_intervals[0])
    farthest = sorted_intervals[0][1]

    for i in range(1,len(sorted_intervals)): # a is start, b is end
        current_start = sorted_intervals[i][0]
        current_end = sorted_intervals[i][1]
        if current_start >= farthest:
            result.append(sorted_intervals[i])
            farthest = current_end


    return result