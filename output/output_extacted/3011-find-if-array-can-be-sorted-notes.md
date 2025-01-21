## Find If Array Can Be Sorted
**Problem Link:** https://leetcode.com/problems/find-if-array-can-be-sorted/description

**Problem Statement:**
- Input format: An array of integers `arr` and an integer `k`.
- Constraints: The array `arr` can have any length, and `k` is a positive integer.
- Expected output format: A boolean value indicating whether the array can be sorted by reversing at most `k` subarrays.
- Key requirements and edge cases to consider: Empty arrays, arrays with a single element, arrays that are already sorted, and arrays where `k` is larger than the number of elements.
- Example test cases with explanations:
  - `[4, 2, 3, 1]`, `k = 2`: Returns `true` because the array can be sorted by reversing at most `k` subarrays (e.g., reverse `[4, 2, 3, 1]` to `[1, 2, 3, 4]`).
  - `[5, 0, -1, 4]`, `k = 2`: Returns `false` because the array cannot be sorted by reversing at most `k` subarrays.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of reversing subarrays and check if the resulting array is sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, reverse it and check if the resulting array is sorted.
  3. Keep track of the minimum number of reversals required to sort the array.
- Why this approach comes to mind first: It's a straightforward approach that involves checking all possible combinations of reversing subarrays.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool canBeSorted(std::vector<int>& arr, int k) {
    int n = arr.size();
    std::vector<int> sortedArr = arr;
    std::sort(sortedArr.begin(), sortedArr.end());
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != sortedArr[i]) {
            count++;
        }
    }
    
    return count / 2 <= k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the length of the input array.
> - **Space Complexity:** $O(n)$ for storing the sorted array.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to storing the sorted array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible combinations of reversing subarrays, we can use a single pass through the array to count the number of reversals required to sort the array.
- Detailed breakdown of the approach:
  1. Initialize a counter to keep track of the number of reversals required.
  2. Iterate through the array, and for each element, check if it's in the correct position.
  3. If an element is not in the correct position, increment the counter.
- Proof of optimality: This approach has a linear time complexity, which is optimal for this problem.
- Why further optimization is impossible: The time complexity cannot be improved further because we need to at least read the input array once.

```cpp
bool canBeSorted(std::vector<int>& arr, int k) {
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            count++;
        }
    }
    
    return count / 2 <= k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter.
> - **Optimality proof:** The time complexity is optimal because we only need to make a single pass through the array to count the number of reversals required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting the number of reversals required to sort an array.
- Problem-solving patterns identified: Using a single pass through the array to solve the problem.
- Optimization techniques learned: Avoiding unnecessary operations and using a counter to keep track of the number of reversals required.
- Similar problems to practice: Other problems that involve counting the number of operations required to transform one array into another.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the counter correctly or not incrementing the counter correctly.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays that are already sorted.
- Performance pitfalls: Using a sorting algorithm that has a high time complexity or using unnecessary operations.
- Testing considerations: Testing the function with different input arrays and values of `k` to ensure it works correctly.