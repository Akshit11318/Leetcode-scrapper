## Rearrange Array Elements by Sign
**Problem Link:** https://leetcode.com/problems/rearrange-array-elements-by-sign/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is `2n`, where `n` is a positive integer.
- Expected Output: Rearrange the elements of `nums` such that all non-negative numbers are on the left of all negative numbers.
- Key Requirements: The non-negative numbers and negative numbers should be in the same order as they were in the original array.
- Edge Cases: The input array can contain zero, and the number of non-negative and negative numbers can vary.

### Brute Force Approach
**Explanation:**
- The initial thought process involves separating the non-negative and negative numbers into two separate arrays while preserving their original order.
- Then, concatenate these two arrays to get the final rearranged array.
- This approach comes to mind first because it directly addresses the requirement of keeping the non-negative and negative numbers in their original order.

```cpp
vector<int> rearrangeArray(vector<int>& nums) {
    vector<int> nonNegative, negative;
    for (int num : nums) {
        if (num >= 0) {
            nonNegative.push_back(num);
        } else {
            negative.push_back(num);
        }
    }
    nonNegative.insert(nonNegative.end(), negative.begin(), negative.end());
    return nonNegative;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of elements in the array, because we are scanning the array once to separate the numbers.
> - **Space Complexity:** $O(n)$, as we are using two additional arrays to store the non-negative and negative numbers, which in total can hold up to $n$ elements.
> - **Why these complexities occur:** The time complexity is linear because we process each element once, and the space complexity is linear because in the worst-case scenario (all elements are either non-negative or negative), we need to store all elements in the additional arrays.

### Optimal Approach (Required)
**Explanation:**
- The key insight to the optimal solution is to use two pointers, one starting from the beginning of the array and one from the end, to rearrange the elements in-place without using additional arrays.
- We iterate through the array, and whenever we encounter a non-negative number, we swap it with the number at the next available non-negative position.
- This approach ensures that all non-negative numbers are moved to the left of all negative numbers while maintaining their original order.

```cpp
vector<int> rearrangeArray(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0 && nums[i] < 0) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] >= 0) {
                    swap(nums[i], nums[j]);
                    break;
                }
            }
        }
        if (i % 2 == 1 && nums[i] > 0) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] < 0) {
                    swap(nums[i], nums[j]);
                    break;
                }
            }
        }
    }
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ in the worst case, where $n$ is the number of elements in the array, because for each element, we might potentially scan the rest of the array to find a suitable swap.
> - **Space Complexity:** $O(1)$, as we are rearranging the elements in-place without using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal in terms of space complexity, as we are not using any additional space that scales with the input size. However, the time complexity can be improved with a more efficient algorithm that takes advantage of the specific structure of the problem.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include the use of two pointers and in-place swapping to rearrange elements.
- Problem-solving patterns identified involve separating the problem into smaller sub-problems (separating non-negative and negative numbers) and solving them individually.
- Optimization techniques learned include reducing space complexity by using in-place algorithms.

**Mistakes to Avoid:**
- Common implementation errors include incorrect indexing and not checking for edge cases (like an empty array or an array with a single element).
- Edge cases to watch for include arrays with all non-negative or all negative numbers, and arrays with zeros.
- Performance pitfalls include using algorithms with high time complexity for large inputs, and not considering the trade-offs between time and space complexity.