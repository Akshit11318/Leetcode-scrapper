## Find K Closest Elements
**Problem Link:** https://leetcode.com/problems/find-k-closest-elements/description

**Problem Statement:**
- Input format: An array of integers `arr`, an integer `k`, and a target integer `x`.
- Constraints: The input array is sorted in ascending order.
- Expected output format: A list of `k` closest elements to the target `x` in the array.
- Key requirements and edge cases to consider:
  - Handling cases where there are multiple closest elements.
  - Considering the scenario where the target `x` is exactly equal to an element in the array.
- Example test cases with explanations:
  - For `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.
  - For `arr = [1, 5, 10, 15, 20]`, `k = 3`, and `x = 8`, the output should be `[5, 10, 15]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the absolute difference between each element in the array and the target `x`, then sort these differences along with their corresponding elements.
- Step-by-step breakdown of the solution:
  1. Calculate the absolute difference between each element in the array and the target `x`.
  2. Store these differences along with their corresponding elements in a new array or data structure.
  3. Sort this new array based on the differences.
  4. Select the `k` elements with the smallest differences.
- Why this approach comes to mind first: It directly addresses the requirement of finding the closest elements by calculating and comparing distances.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
    std::vector<std::pair<int, int>> diffArr;
    for (int i = 0; i < arr.size(); ++i) {
        diffArr.push_back({abs(arr[i] - x), arr[i]});
    }
    std::sort(diffArr.begin(), diffArr.end(), [](const auto& a, const auto& b) {
        return a.first < b.first;
    });
    std::vector<int> result;
    for (int i = 0; i < k; ++i) {
        result.push_back(diffArr[i].second);
    }
    std::sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of the array of differences, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$ for storing the array of differences.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the differences requires additional space proportional to the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize the fact that the input array is sorted to apply a binary search approach for finding the closest elements.
- Detailed breakdown of the approach:
  1. Perform a binary search to find the closest element to the target `x`.
  2. Expand from this closest element to find the `k` closest elements, considering both the left and right sides.
- Proof of optimality: This approach minimizes the number of comparisons needed to find the closest elements by leveraging the sorted nature of the input array.

```cpp
#include <vector>

std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    std::vector<int> result(arr.begin() + left, arr.begin() + left + k);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log(n - k))$ due to the binary search, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(k)$ for storing the result.
> - **Optimality proof:** The binary search approach minimizes the time complexity by reducing the search space exponentially, making it optimal for finding the starting point of the closest `k` elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and its application in finding closest elements in a sorted array.
- Problem-solving patterns identified: Leveraging the properties of the input data (sorted array) to optimize the solution.
- Optimization techniques learned: Applying binary search to reduce the time complexity.

**Mistakes to Avoid:**
- Not considering the sorted nature of the input array.
- Incorrectly implementing the binary search.
- Failing to handle edge cases, such as when the target `x` is exactly equal to an element in the array.