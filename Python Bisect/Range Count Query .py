import bisect


details="""Given a sorted list of integers and multiple queries [L, R], use bisect_left and bisect_right to efficiently count how many numbers fall within each range."""
print(details)

lst=list([1,2,3,4,5,52,96,6])
print(bisect.bisect_left(lst,90))
print(bisect.bisect_right(lst,90))


bisect.insort_left(lst,30)
print(lst)


