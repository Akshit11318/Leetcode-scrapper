## Calculate Compressed Mean
**Problem Link:** https://leetcode.com/problems/calculate-compressed-mean/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= k <= nums.length`.
- Expected Output: The compressed mean of `nums` with a compression factor of `k`.
- Key Requirements: Calculate the mean of the top `k` elements after sorting `nums` in ascending order.
- Edge Cases: Handle cases where `k` is greater than the length of `nums`.

**Example Test Cases:**
- Example 1: Input: `nums = [1,2,3,4,5]`, `k = 4`. Output: `4`.
- Example 2: Input: `nums = [1,2,3,4,5]`, `k = 3`. Output: `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array `nums` in ascending order and then calculate the mean of the top `k` elements.
- Step-by-step breakdown:
  1. Sort the array `nums` in ascending order.
  2. Calculate the sum of the top `k` elements.
  3. Calculate the mean by dividing the sum by `k`.

```cpp
#include <vector>
#include <algorithm>

double calculateCompressedMean(std::vector<int>& nums, int k) {
    // Sort the array in ascending order
    std::sort(nums.begin(), nums.end());
    
    // Calculate the sum of the top k elements
    double sum = 0.0;
    for (int i = nums.size() - k; i < nums.size(); i++) {
        sum += nums[i];
    }
    
    // Calculate the mean
    double mean = sum / k;
    
    return mean;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the length of `nums`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sum and mean.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant as we only use a fixed amount of space to store the sum and mean.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use the `std::nth_element` function to partially sort the array, which has a better time complexity than sorting the entire array.
- Detailed breakdown:
  1. Use `std::nth_element` to partially sort the array such that the top `k` elements are in the correct order.
  2. Calculate the sum of the top `k` elements.
  3. Calculate the mean by dividing the sum by `k`.

```cpp
#include <vector>
#include <algorithm>

double calculateCompressedMean(std::vector<int>& nums, int k) {
    // Partially sort the array using std::nth_element
    std::nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
    
    // Calculate the sum of the top k elements
    double sum = 0.0;
    for (int i = nums.size() - k; i < nums.size(); i++) {
        sum += nums[i];
    }
    
    // Calculate the mean
    double mean = sum / k;
    
    return mean;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ on average, where $n$ is the length of `nums`, as `std::nth_element` has a linear time complexity on average.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sum and mean.
> - **Optimality proof:** This approach is optimal as we only need to partially sort the array to get the top `k` elements, and `std::nth_element` is the most efficient way to do this.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Partial sorting using `std::nth_element`.
- Problem-solving pattern: Using partial sorting to solve problems that require the top `k` elements.
- Optimization technique: Using `std::nth_element` instead of sorting the entire array.

**Mistakes to Avoid:**
- Common implementation error: Using `std::sort` instead of `std::nth_element` for partial sorting.
- Edge case to watch for: Handling cases where `k` is greater than the length of `nums`.
- Performance pitfall: Using a brute force approach that sorts the entire array.