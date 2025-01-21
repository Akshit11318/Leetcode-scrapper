## The K-Strongest Values in an Array
**Problem Link:** https://leetcode.com/problems/the-k-strongest-values-in-an-array/description

**Problem Statement:**
- Input format: Given an array of integers `arr` and an integer `k`.
- Constraints: The array `arr` contains distinct integers and `1 <= k <= arr.length`.
- Expected output format: Return the `k` strongest values in the array.
- Key requirements and edge cases to consider:
  - The `k` strongest values are the `k` values that have the smallest absolute difference with their median.
  - If there are multiple answers, return them in any order.

**Example Test Cases:**
- `arr = [1, 2, 3, 4, 5], k = 2` -> `[5, 1]` (both have the same absolute difference with the median, which is 3)
- `arr = [1, 1, 3, 5, 5], k = 2` -> `[1, 5]` (both have the same absolute difference with the median, which is 2)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the median of the array and then for each element, calculate its absolute difference with the median.
- Step-by-step breakdown of the solution:
  1. Sort the array `arr` in ascending order.
  2. Calculate the median of the sorted array.
  3. For each element in the array, calculate its absolute difference with the median.
  4. Store the absolute differences in a separate array or data structure.
  5. Sort the array of absolute differences and select the `k` smallest ones.
- Why this approach comes to mind first: It is straightforward and involves basic operations like sorting and calculating absolute differences.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> getStrongest(vector<int>& arr, int k) {
    // Sort the array
    sort(arr.begin(), arr.end());
    
    // Calculate the median
    double median;
    if (arr.size() % 2 == 0) {
        median = (arr[arr.size() / 2 - 1] + arr[arr.size() / 2]) / 2.0;
    } else {
        median = arr[arr.size() / 2];
    }
    
    // Calculate absolute differences with the median
    vector<pair<int, int>> diffAndVal;
    for (int val : arr) {
        diffAndVal.push_back({abs(val - median), val});
    }
    
    // Sort the absolute differences and select the k smallest ones
    sort(diffAndVal.begin(), diffAndVal.end());
    vector<int> strongest;
    for (int i = 0; i < k; ++i) {
        strongest.push_back(diffAndVal[i].second);
    }
    
    return strongest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the array and the array of absolute differences.
> - **Space Complexity:** $O(n)$ for storing the array of absolute differences.
> - **Why these complexities occur:** Sorting operations dominate the time complexity, and storing additional arrays for absolute differences and strongest values contributes to the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved more efficiently by directly calculating the absolute differences and storing them along with their corresponding values in a single pass, then sorting this combined data structure.
- Detailed breakdown of the approach:
  1. Calculate the median of the array `arr`.
  2. Create a vector of pairs where each pair contains an absolute difference with the median and the corresponding value from `arr`.
  3. Sort this vector of pairs based on the absolute differences.
  4. Select the `k` smallest absolute differences (which correspond to the `k` strongest values).
- Proof of optimality: This approach optimizes the calculation of absolute differences and sorting by combining these steps into a single, efficient process.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> getStrongest(vector<int>& arr, int k) {
    // Calculate the median
    sort(arr.begin(), arr.end());
    double median = (arr.size() % 2 == 0) ? (arr[arr.size() / 2 - 1] + arr[arr.size() / 2]) / 2.0 : arr[arr.size() / 2];
    
    // Calculate absolute differences with the median and store with values
    vector<pair<int, int>> diffAndVal;
    for (int val : arr) {
        diffAndVal.push_back({abs(val - median), val});
    }
    
    // Sort the absolute differences and select the k smallest ones
    sort(diffAndVal.begin(), diffAndVal.end());
    vector<int> strongest;
    for (int i = 0; i < k; ++i) {
        strongest.push_back(diffAndVal[i].second);
    }
    
    return strongest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the array and the vector of pairs.
> - **Space Complexity:** $O(n)$ for storing the vector of pairs.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the `k` strongest values, leveraging sorting to efficiently select the smallest absolute differences.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, calculating absolute differences, and selecting the `k` smallest values.
- Problem-solving patterns identified: The importance of understanding the problem constraints and leveraging sorting for efficient selection.
- Optimization techniques learned: Combining calculations and sorting into a single, efficient process.
- Similar problems to practice: Problems involving sorting, absolute differences, and selection based on specific criteria.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the median or absolute differences.
- Edge cases to watch for: Handling arrays with an even or odd number of elements when calculating the median.
- Performance pitfalls: Failing to optimize the sorting and selection process.
- Testing considerations: Thoroughly testing with different array sizes, values, and `k` values to ensure correctness.