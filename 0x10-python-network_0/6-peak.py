#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    """Returns the  peak in a list of unsorted integers
    """
    if list_int == []:
        return None
    if len(list_int) == 1:
        return list_int[0]
    if len(list_int) == 2:
        return max(list_int)

    middle_position = len(list_int) // 2
    middle_p = list_int[middle_position]
    right_p = list_int[middle_position + 1]
    left_t = list_int[middle_position - 1]

    if middle_p > right_point and middle_point > left_point:
        return middle_p
    if middle_p < right_p:
        return find_peak(list_int[middle_position + 1:])
    else:
        return find_peak(list_int[:middle_position])
