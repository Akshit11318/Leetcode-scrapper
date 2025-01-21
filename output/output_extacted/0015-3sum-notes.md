## 3Sum
**Problem Link:** https://leetcode.com/problems/3sum/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: The length of `nums` will be in the range `[0, 3000]`, and the elements of `nums` will be in the range `[-10^5, 10^5]`.
- Expected output: All unique triplets in `nums` that sum to zero.
- Key requirements and edge cases:
  - The solution must handle duplicate triplets and return unique triplets only.
  - The input array can be empty or contain a single element, in which case the solution should return an empty list.
- Example test cases:
  - Input: `nums = [-1,0,1,2,-1,-4]`
    - Output: `[[-1,-1,2],[-1,0,1]]`
  - Input: `nums = [0,1,1]`
    - Output: `[]`
  - Input: `nums = [0,0,0]`
    - Output: `[[0,0,0]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible combination of three elements in the array to see if their sum is zero.
- This approach comes to mind first because it is straightforward and guarantees finding all triplets that sum to zero, but it is inefficient for large arrays.
- Step-by-step breakdown:
  1. Generate all possible triplets from the input array.
  2. For each triplet, calculate the sum of its elements.
  3. If the sum is zero, add the triplet to the result list.
  4. Remove duplicates from the result list.

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> triplet = {nums[i], nums[j], nums[k]};
                        sort(triplet.begin(), triplet.end()); // For duplicate removal
                        bool found = false;
                        for (const auto& res : result) {
                            if (res == triplet) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            result.push_back(triplet);
                        }
                    }
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`, because we have three nested loops iterating over the array.
> - **Space Complexity:** $O(n)$ for storing the result, where $n$ is the number of unique triplets found.
> - **Why these complexities occur:** The brute force approach checks every possible combination of three elements, leading to cubic time complexity. The space complexity is linear because, in the worst case, we might store every triplet.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is sorting the array first and then using a two-pointer technique to find pairs that sum to the negation of the current element.
- This approach is optimal because it reduces the time complexity significantly by avoiding the need to check every possible triplet.
- Step-by-step breakdown:
  1. Sort the input array `nums`.
  2. Iterate over the sorted array. For each element at index `i`, use two pointers, `left` and `right`, starting from `i + 1` and the end of the array, respectively.
  3. Calculate the target sum as the negation of the current element `nums[i]`.
  4. Move the pointers based on the sum of the elements at `left` and `right` compared to the target sum.
  5. If the sum is zero, add the triplet to the result list and move both pointers.
  6. Skip duplicates for `nums[i]`, `nums[left]`, and `nums[right]` to ensure unique triplets.

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicates
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left + 1]) left++; // Skip duplicates
                    while (left < right && nums[right] == nums[right - 1]) right--; // Skip duplicates
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`, because we have a nested loop structure but the inner loop runs in linear time due to the two-pointer technique.
> - **Space Complexity:** $O(n)$ for storing the result, where $n$ is the number of unique triplets found.
> - **Optimality proof:** This solution is optimal because it minimizes the number of comparisons needed to find all unique triplets that sum to zero, leveraging the sorted array and two-pointer technique to achieve quadratic time complexity.

---

### Final Notes

**Learning Points:**
- The importance of sorting and using two-pointer techniques for efficient solutions.
- How to handle duplicates in arrays to ensure uniqueness of results.
- The trade-off between brute force and optimal approaches in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the edge case where the input array is empty or contains fewer than three elements.
- Failing to skip duplicates, which can lead to incorrect results.
- Not optimizing the solution, resulting in inefficient time complexity.