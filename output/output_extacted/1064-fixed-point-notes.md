## Fixed Point
**Problem Link:** https://leetcode.com/problems/fixed-point/description

**Problem Statement:**
- Input: An array of integers `arr` where each integer is in the range `[0, arr.length - 1]`.
- Constraints: `1 <= arr.length <= 5000`, `0 <= arr[i] <= 5000`.
- Expected Output: The index `i` of the array such that `arr[i] == i`. If no such index exists, return `-1`.
- Key Requirements: The function should return the smallest index `i` that satisfies the condition `arr[i] == i`.
- Edge Cases: If no fixed point exists, return `-1`. If there are multiple fixed points, return the smallest index.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each element of the array and check if it matches its index.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    int fixedPoint(vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == i) {
                return i;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through each element once.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each element in the array. The space complexity is constant because we are only using a fixed amount of space to store the loop variables.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can use a modified binary search algorithm to find the fixed point.
- The idea is to maintain two pointers, `low` and `high`, and iteratively narrow down the search range until we find the fixed point or determine that it does not exist.
- This approach is optimal because it reduces the number of comparisons required to find the fixed point.

```cpp
class Solution {
public:
    int fixedPoint(vector<int>& arr) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == mid) {
                if (mid == 0 || arr[mid - 1] != mid - 1) {
                    return mid;
                }
                high = mid - 1;
            } else if (arr[mid] < mid) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array, because we are using a binary search-like approach.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it reduces the number of comparisons required to find the fixed point. The binary search-like approach allows us to eliminate half of the search space at each step, resulting in a logarithmic time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, iterative narrowing of search range.
- Problem-solving patterns identified: using a modified binary search algorithm to find a specific element in an array.
- Optimization techniques learned: reducing the number of comparisons required to find the fixed point.
- Similar problems to practice: finding the first occurrence of a target element in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, not updating the search range correctly.
- Edge cases to watch for: empty array, array with no fixed point, array with multiple fixed points.
- Performance pitfalls: using a brute force approach, not optimizing the search range.
- Testing considerations: testing with different input sizes, testing with different edge cases.