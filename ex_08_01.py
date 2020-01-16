#Write two functions: both take a list, one modifies it removing first and last item and it returns None,
#the second takes a list and returns a new list with all but the first and last items

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e']

print('original list1:', list1)
print('original list2:', list2)


def chop(t):
    del t[0]
    del t[-1]
    return None

chop(list1)
print('modified with chop func:', list1)

def middle(t):
    new_t = t[1:-1]
    return new_t

print('unmodified but creates new list:', middle(list2))

print('list2 unmodified:', list2)
