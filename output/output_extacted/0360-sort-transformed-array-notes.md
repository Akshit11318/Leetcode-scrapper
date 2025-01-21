## Sort Transformed Array

**Problem Link:** https://leetcode.com/problems/sort-transformed-array/description

**Problem Statement:**
- Given a sorted array of integers `nums` and three integers `a`, `b` and `c`, apply a transformation of the form `x -> ax^2 + bx + c` to each element in the array.
- The task is to sort the transformed array in ascending order.
- Input constraints: `1 <= nums.length <= 10^5`, `-10^9 <= nums[i], a, b, c <= 10^9`.
- Expected output format: A sorted array of transformed integers.

**Key Requirements and Edge Cases:**
- The transformation function `f(x) = ax^2 + bx + c` can be either increasing or decreasing depending on the values of `a`, `b`, and `c`.
- If `a` is positive, `f(x)` is increasing for `x >= -b/(2a)`, and if `a` is negative, `f(x)` is decreasing for `x >= -b/(2a)`.
- Special care must be taken when `a` equals zero, as the function reduces to a linear transformation `f(x) = bx + c`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves applying the transformation function to each element in the array and then sorting the resulting array.
- This approach is straightforward but may not be efficient for large inputs due to the sorting step.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> sortTransformedArray(std::vector<int>& nums, int a, int b, int c) {
    std::vector<int> transformed;
    for (int num : nums) {
        transformed.push_back(a * num * num + b * num + c);
    }
    std::sort(transformed.begin(), transformed.end());
    return transformed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, as we need to store the transformed array.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the need to store the transformed array dictates the space complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to determine the behavior of the transformation function based on the value of `a`.
- If `a` is positive, the function is increasing for `x >= -b/(2a)`, so we can apply the transformation and then sort the array in ascending order if `nums[0] >= -b/(2a)` or in descending order otherwise.
- If `a` is negative, the function is decreasing for `x >= -b/(2a)`, so we can apply the transformation and then sort the array in descending order if `nums[0] >= -b/(2a)` or in ascending order otherwise.
- If `a` is zero, we can simply apply the linear transformation and sort the array based on the sign of `b`.

```cpp
#include <vector>

std::vector<int> sortTransformedArray(std::vector<int>& nums, int a, int b, int c) {
    std::vector<int> transformed;
    for (int num : nums) {
        transformed.push_back(a * num * num + b * num + c);
    }
    if (a >= 0) {
        std::sort(transformed.begin(), transformed.end());
    } else {
        std::sort(transformed.rbegin(), transformed.rend());
    }
    return transformed;
}
```

However, a more efficient approach is to use two pointers, one at the start and one at the end of the array, to construct the sorted array directly without sorting.

```cpp
std::vector<int> sortTransformedArray(std::vector<int>& nums, int a, int b, int c) {
    int n = nums.size();
    std::vector<int> res(n);
    int left = 0, right = n - 1;
    for (int i = n - 1; i >= 0; --i) {
        if (a * nums[right] * nums[right] + b * nums[right] + c >= a * nums[left] * nums[left] + b * nums[left] + c) {
            res[i] = a * nums[right] * nums[right] + b * nums[right] + c;
            --right;
        } else {
            res[i] = a * nums[left] * nums[left] + b * nums[left] + c;
            ++left;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(n)$, as we need to store the transformed array.
> - **Optimality proof:** This approach is optimal because it avoids the sorting step, directly constructing the sorted array in linear time.

### Final Notes

**Learning Points:**
- Understanding the behavior of quadratic functions and their impact on sorting.
- Using two pointers to construct a sorted array efficiently.
- Avoiding unnecessary sorting operations by leveraging the properties of the transformation function.

**Mistakes to Avoid:**
- Failing to consider the behavior of the transformation function based on the value of `a`.
- Incorrectly applying the transformation function or sorting the array.
- Not optimizing the solution to achieve linear time complexity.