

def merge(array: list[int], p: int, q: int, r: int) -> None:
    # Create copies of the left and right subarrays
    left = array[p:q + 1]
    right = array[q + 1:r + 1]

    i = 0  # Initial index of the left subarray
    j = 0  # Initial index of the right subarray
    k = p  # Initial index of the merged subarray

    # Merge the left and right arrays back into the original array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray (if any)
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray (if any)
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def mergesort_recursive(array: list[int], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2  # Find the middle point to divide the array into two halves
        # Recursively sort the first half
        mergesort_recursive(array, p, q)
        # Recursively sort the second half
        mergesort_recursive(array, q + 1, r)
        # Merge the two sorted halves
        merge(array, p, q, r)


def mergesort(array: list[int]) -> None:
    # Call the recursive function with the full range of the array
    mergesort_recursive(array, 0, len(array) - 1)

  

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





