# CMPS 2200 Reciation 6
## Answers

**Name:**Mikey Sison, Max Curl


Place all written answers from `recitation-06.md` here for easier grading.







- **1b.**

Unshuffled

|   n |   qsort-fixed-pivot |   ssort-fixed-pivot |
|-----|---------------------|---------------------|
|  10 |               0.000 |               0.000 |
|  50 |               0.000 |               0.000 |
| 100 |               0.994 |               0.000 |
| 100 |               0.996 |               0.000 |
| 200 |               3.360 |               0.000 |
| 500 |              22.275 |               2.007 |
| 600 |              35.543 |               3.999 |
| 900 |              69.941 |               9.002 |


|   n |   qsort-random-pivot |   ssort-fixed-pivot |
|-----|---------------------|---------------------|
|  10 |               1.428 |               5.977 |
|  50 |               5.030 |               6.028 |
| 100 |               5.504 |               5.513 |
| 100 |               5.834 |               5.253 |
| 200 |               5.996 |               4.599 |
| 500 |               6.250 |               7.061 |
| 600 |               4.926 |               8.303 |

Shuffled

|   n |   qsort-fixed-pivot |   ssort-fixed-pivot |
|-----|---------------------|---------------------|
|  10 |               0.000 |               0.000 |
|  50 |               0.000 |               0.000 |
| 100 |               0.000 |               0.000 |
| 100 |               0.000 |               0.000 |
| 200 |               0.000 |               1.007 |
| 500 |               1.002 |               4.012 |
| 600 |               2.000 |               4.888 |
| 900 |               2.644 |               9.504 |

|   n |   qsort-random-pivot |   ssort-fixed-pivot |
|-----|---------------------|---------------------|
|  10 |               0.000 |               0.000 |
|  50 |               0.000 |               0.000 |
| 100 |               0.000 |               0.000 |
| 100 |               1.000 |               0.000 |
| 200 |               0.000 |               0.998 |
| 500 |               1.000 |               4.003 |
| 600 |               1.002 |               5.004 |
| 900 |               3.004 |               9.003 |

We are seeing that ssort is on average taking longer as the number of element in the list increases. <br> This is in accordance with the asymptotic runtime of ssort and qsort. <br> Qsort being O(nlogn), while ssort is O(n^2)
<br>Random pivot qsort with unshuffled is significantly faster than the pivot being a[0]. <br> Selection sort is unaffected by shuffling.

- **1c.**

Unshuffled

|      n |   qsort-fixed-pivot |   ssort-fixed-pivot |
|--------|---------------------|---------------------|
|     10 |               0.000 |               0.000 |
|     50 |               0.000 |               0.000 |
|    100 |               0.000 |               0.000 |
|    100 |               0.000 |               0.000 |
|    200 |               1.000 |               0.000 |
|    500 |               1.001 |               0.000 |
|    600 |               2.000 |               0.000 |
|   1000 |               3.001 |               0.000 |
|  10000 |              38.773 |               0.000 |
|  50000 |             224.306 |               0.000 |
| 100000 |             436.641 |               1.000 |

Shuffled

|      n |   qsort-fixed-pivot |   ssort-fixed-pivot |
|--------|---------------------|---------------------|
|     10 |               0.000 |               0.000 |
|     50 |               0.000 |               0.000 |
|    100 |               0.000 |               0.000 |
|    100 |               0.999 |               0.000 |
|    200 |               0.000 |               0.000 |
|    500 |               2.001 |               0.000 |
|    600 |               2.000 |               0.000 |
|   1000 |               3.003 |               0.000 |
|  10000 |              43.014 |               0.999 |
|  50000 |             241.151 |               7.004 |
| 100000 |             502.792 |              16.986 |

- Timsort is an adaptive sorting algorithm, which means that in the event it is given a sorted list, it will run in O(n). 
<br>This is reflected by the very fast sorting of the unshuffled list. <br> Quicksort operated at expected speeds. overall, Timsort sorted faster.
