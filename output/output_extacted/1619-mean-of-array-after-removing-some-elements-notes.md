## Mean of Array After Removing Some Elements
**Problem Link:** https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `arr` and an integer `k`. The array `arr` has a length of `n`, where `n` is a positive integer, and `k` is a non-negative integer. The task is to remove the smallest `k` elements and the largest `k` elements from the array `arr`, and then calculate the mean of the remaining elements.
- Expected output format: The output should be a double representing the mean of the array after removing some elements.
- Key requirements and edge cases to consider: The input array `arr` can be empty, and `k` can be greater than or equal to the length of `arr`. If `k` is greater than or equal to the length of `arr`, the output should be `0.00000`.
- Example test cases with explanations: 
  - For `arr = [1, 2, 4, 5, 6, 7, 8, 9]` and `k = 1`, the output should be `5.50000` because after removing the smallest element `1` and the largest element `9`, the remaining elements are `[2, 4, 5, 6, 7, 8]`, and their mean is `(2 + 4 + 5 + 6 + 7 + 8) / 6 = 32 / 6 = 5.33333`, which rounds to `5.50000`.
  - For `arr = [1, 1, 1, 1]` and `k = 0`, the output should be `1.00000` because no elements are removed, and the mean of the array `[1, 1, 1, 1]` is `1.00000`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to sort the array `arr` in ascending order, remove the smallest `k` elements and the largest `k` elements, and then calculate the mean of the remaining elements.
- Step-by-step breakdown of the solution: 
  1. Sort the array `arr` in ascending order.
  2. Remove the smallest `k` elements and the largest `k` elements from the sorted array.
  3. Calculate the sum of the remaining elements.
  4. Calculate the mean of the remaining elements by dividing the sum by the number of remaining elements.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves sorting the array, removing the smallest and largest elements, and calculating the mean of the remaining elements.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

double trimMean(std::vector<int>& arr, int k) {
    // Sort the array in ascending order
    std::sort(arr.begin(), arr.end());
    
    // Remove the smallest k elements and the largest k elements
    arr.erase(arr.begin(), arr.begin() + k);
    arr.erase(arr.end() - k, arr.end());
    
    // If the array is empty after removing elements, return 0.00000
    if (arr.empty()) {
        return 0.00000;
    }
    
    // Calculate the sum of the remaining elements
    double sum = std::accumulate(arr.begin(), arr.end(), 0);
    
    // Calculate the mean of the remaining elements
    double mean = sum / arr.size();
    
    return mean;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the length of the array `arr`.
> - **Space Complexity:** $O(1)$ because the sorting operation is done in-place, and the space used does not grow with the size of the input array.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a time complexity of $O(n \log n)$. The space complexity is $O(1)$ because the sorting operation is done in-place, and the space used does not grow with the size of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can use the `std::nth_element` function to find the `k`-th smallest element and the `k`-th largest element in the array without sorting the entire array. This reduces the time complexity from $O(n \log n)$ to $O(n)$.
- Detailed breakdown of the approach: 
  1. Use `std::nth_element` to find the `k`-th smallest element and the `k`-th largest element in the array.
  2. Calculate the sum of the elements between the `k`-th smallest element and the `k`-th largest element.
  3. Calculate the mean of the elements between the `k`-th smallest element and the `k`-th largest element by dividing the sum by the number of elements.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem because we need to examine each element in the array at least once.

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

double trimMean(std::vector<int>& arr, int k) {
    // If the array is empty or k is greater than or equal to the length of the array, return 0.00000
    if (arr.empty() || k >= arr.size()) {
        return 0.00000;
    }
    
    // Use std::nth_element to find the k-th smallest element and the k-th largest element
    std::nth_element(arr.begin(), arr.begin() + k, arr.end());
    std::nth_element(arr.rbegin(), arr.rbegin() + k, arr.rend());
    
    // Calculate the sum of the elements between the k-th smallest element and the k-th largest element
    double sum = std::accumulate(arr.begin() + k, arr.end() - k, 0);
    
    // Calculate the mean of the elements between the k-th smallest element and the k-th largest element
    double mean = sum / (arr.size() - 2 * k);
    
    return mean;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we use `std::nth_element` to find the `k`-th smallest element and the `k`-th largest element, and then calculate the sum of the elements between them.
> - **Space Complexity:** $O(1)$ because the space used does not grow with the size of the input array.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem because we need to examine each element in the array at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of `std::nth_element` to find the `k`-th smallest element and the `k`-th largest element in an array, and the use of `std::accumulate` to calculate the sum of a range of elements.
- Problem-solving patterns identified: The problem requires identifying the `k`-th smallest element and the `k`-th largest element in the array, and then calculating the mean of the elements between them.
- Optimization techniques learned: The problem demonstrates the use of `std::nth_element` to reduce the time complexity from $O(n \log n)$ to $O(n)$.
- Similar problems to practice: Other problems that involve finding the `k`-th smallest element or the `k`-th largest element in an array, such as finding the median of an array.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to sort the entire array instead of using `std::nth_element` to find the `k`-th smallest element and the `k`-th largest element.
- Edge cases to watch for: The problem requires handling edge cases where the array is empty or `k` is greater than or equal to the length of the array.
- Performance pitfalls: One performance pitfall is to use a sorting algorithm with a time complexity of $O(n \log n)$ instead of using `std::nth_element` with a time complexity of $O(n)$.
- Testing considerations: The problem requires testing the implementation with different input arrays and values of `k` to ensure that it works correctly in all cases.