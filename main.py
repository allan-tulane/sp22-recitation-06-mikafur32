import random, time
import tabulate

def qsort(a, pivot_fn):

    if len(a) == 0:
        return a
    p = pivot_fn(a)
    l = list(filter(lambda x: x < p, a))  # O(|a|) work, O(log|a|) span
    r = list(filter(lambda x: x > p, a))  # O(|a|) work, O(log|a|) span

    s1, s3 = qsort(l, pivot_fn), qsort(r, pivot_fn)
    return s1 + [p] + s3
def ssort(L):
    if (len(L) == 1):
        return (L)
    else:
        m = L.index(min(L))
        L[0], L[m] = L[m], L[0]
        return [L[0]] + ssort(L[1:])

def time_search_fn(sort_fn, mylist, fn):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist, fn)
    return (time.time() - start ) * 1000
    ###
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start ) * 1000

def compare_sort(sizes=[10, 50, 100, 100, 200, 500, 600, 1000, 10000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison

    qsort_fixed_pivot = qsort
    qsort_random_pivot = qsort
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search_fn(qsort_random_pivot, mylist, lambda a: random.choice(a)),
            time_search(tim_sort, mylist)
            #time_search(qsort_random_pivot, mylist, lambda a: random.choice(a))
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'ssort-fixed-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
