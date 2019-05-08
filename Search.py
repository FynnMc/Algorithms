from random import randint
import time

# Search Algorithms on Sorted, Uniform data

sorted_l = []
for i in range(200000000):
    sorted_l.append(i)


# Linear Search

def lin_search(sorted_list, element):
    for i in range(len(sorted_list)):
        if sorted_list[i] == element:
            return print(i)


# Binary Search - Recursive

# Creating a sub-array each time will result in bad performance for large arrays.
# It's better to pass in the bounds of the array instead.


def bin_search_r(sorted_list, l, r, element):
    if r >= l:
        mid = l + (r - l)//2
        if sorted_list[mid] == element:
            return print(mid)
        elif sorted_list[mid] > element:
            return bin_search_r(sorted_list, l, mid - 1, element)
        else:
            return bin_search_r(sorted_list, mid + 1, r, element)
    else:
        return print('Error: Element Not In List') # After they have become equal l will then exceed r hence exit

# Binary Search - Iterative


def bin_search_i(sorted_list, l, r, element):

    while l <= r:

        mid = l + (r-l)//2

        if sorted_list[mid] == element:
            return print(mid)
        elif sorted_list[mid] < element:
            l = mid + 1
        else:
            r = mid - 1

    return print("Element Not Present")

# Interpolation Search


def interp_search(sorted_list, l, r, element):
    if r > l:
        ind_select = l + int(round((r - l)*(element - sorted_list[l])/(sorted_list[r] - sorted_list[l])))
        if sorted_list[ind_select] == element:
            return print(ind_select)
        elif sorted_list[ind_select] > element:
            return bin_search_r(sorted_list, l, ind_select - 1, element)
        else:
            return bin_search_r(sorted_list, ind_select + 1, r, element)
    elif r == l:
        ind_select = l
        if sorted_list[ind_select] == element:
            return print(ind_select)
        elif sorted_list[ind_select] > element:
            return bin_search_r(sorted_list, l, ind_select - 1, element)
        else:
            return bin_search_r(sorted_list, ind_select + 1, r, element)
    else:
        return print('Error: Element Not In List')


start = time.time()
lin_search(sorted_l, 19879999)
end = time.time()
print(end-start)

start = time.time()
bin_search_r(sorted_l, 0, len(sorted_l)-1, 19879999)
end = time.time()
print(end-start)

start = time.time()
bin_search_i(sorted_l, 0, len(sorted_l)-1, 19879999)
end = time.time()
print(end-start)

start = time.time()
interp_search(sorted_l, 0, len(sorted_l)-1, 19879999)
end = time.time()
print(end-start)
