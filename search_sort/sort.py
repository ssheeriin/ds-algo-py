def quick_sort(array):
    '''
    Step 1: find a pivot position
    
    Step 2 : partition array such that , elements left of pivot is < pivot position value
     and elements right of pivot is > pivot position value
     
    Step 3 : repeat the same for each partition
    
    :param array: 
    :return: 
    '''
    _sort(array, 0, len(array) - 1)


def _swap(array, one, two):
    array[one], array[two] = array[two], array[one]


def _partition(array, left, right, pivot_index):
    pivot_val = array[pivot_index]

    while left <= right:
        while array[left] < pivot_val:
            left += 1

        while array[right] > pivot_val:
            right -= 1

        if left <= right:
            _swap(array, left, right)
            left += 1
            right -= 1

    return left


def _sort(array, left, right):
    if left >= right:
        return

    pivot_index = (left + right) // 2

    index = _partition(array, left, right, pivot_index)
    _sort(array, left, index - 1)
    _sort(array, index, right)


def _merge_halves(array, leftStart, rightEnd):
    # to get the two halves, we need to get the boundaries
    # leftStart is the start index of first half
    # get middle again, this will be the end index of first half.
    # we call it  leftEnd
    # now we know both start and end indexes of first (left) half
    leftEnd = (leftStart + rightEnd) // 2

    # for the second half, rightEnd is known
    # now leftEnd's next index will be the start of second (right) half (rightStart)
    rightStart = leftEnd + 1

    # now we need pointers in left and right half
    # for left half, it start with leftStart
    leftPtr = leftStart

    # for right half, it start from rightStart
    rightPtr = rightStart

    # we will need a temporary array to merge the result
    temp = []

    # also we need a pointer in temp array , which start with 0, which
    # is essentially left start
    tempPtr = leftStart

    # now walk through both the halves
    # compare the pointers, add the lowest to the temp array
    while leftPtr <= leftEnd and rightPtr <= rightEnd:
        # copy smaller element of either half
        if array[leftPtr] <= array[rightPtr]:
            temp.insert(tempPtr, array[leftPtr])
            leftPtr += 1
        else:
            temp.insert(tempPtr, array[rightPtr])
            rightPtr += 1

        tempPtr += 1

    # now the above loop exists when one of the halves are done
    # we need to copy the remaining elements in the other half
    # only one of the following while loops will execute
    while (leftPtr <= leftEnd):
        temp.insert(tempPtr, array[leftPtr])
        leftPtr += 1
        tempPtr += 1

    while (rightPtr <= rightEnd):
        temp.insert(tempPtr, array[rightPtr])
        rightPtr += 1
        tempPtr += 1

    # now temp has sorted left and right halves
    # copy the same back to original array (starting from left start)
    for i in range(len(temp)):
        array[leftStart] = temp[i]
        leftStart += 1


def _merge_sort(array, leftStart, rightEnd):
    # base condition
    if leftStart >= rightEnd:
        return

    # find a middle point
    middle = (leftStart + rightEnd) // 2

    # sort left half
    _merge_sort(array, leftStart, middle)

    # sort right half
    _merge_sort(array, middle + 1, rightEnd)

    # now merge both the halves
    _merge_halves(array, leftStart, rightEnd)


def merge_sort(array):
    '''
     Algo:
     1) Find middle element
     2) sort first half
     2) sort second half
     3) Merge both halves
    :param array:
    :return:
    '''
    _merge_sort(array, 0, len(array) - 1)
