## 4Sum
**Problem Link:** https://leetcode.com/problems/4sum/description

**Problem Statement:**
- Given an array `nums` of `n` integers, find all unique quadruplets in the array that sum to a given `target`.
- Input format: `nums = [int], target = int`
- Constraints: `0 <= n <= 18, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9`
- Expected output format: A list of lists, where each sublist contains four numbers that sum to the target.
- Key requirements: Find all unique quadruplets that sum to the target, handle duplicate quadruplets, and edge cases like empty input or no quadruplets summing to the target.
- Example test cases:
  - Input: `nums = [1,0,-1,0,-2,2], target = 0`
  - Output: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible combination of four numbers in the array to see if they sum to the target.
- This involves using four nested loops to generate all possible quadruplets.
- For each quadruplet, we check if the sum equals the target. If it does, we add it to our result list.
- However, this approach is inefficient because it generates many duplicate quadruplets and has a high time complexity.

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    for (int l = k + 1; l < nums.size(); l++) {
                        if (nums[i] + nums[j] + nums[k] + nums[l] == target) {
                            vector<int> quadruplet = {nums[i], nums[j], nums[k], nums[l]};
                            // Check for duplicates before adding to result
                            bool isDuplicate = false;
                            for (auto& existing : result) {
                                if (existing == quadruplet) {
                                    isDuplicate = true;
                                    break;
                                }
                            }
                            if (!isDuplicate) {
                                result.push_back(quadruplet);
                            }
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
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of elements in the input array, because we are using four nested loops to generate all possible quadruplets.
> - **Space Complexity:** $O(n)$ for storing the result, in the worst case when all quadruplets sum to the target.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of four numbers, leading to a high time complexity. The space complexity is due to storing all unique quadruplets in the result list.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a two-pointer technique to reduce the time complexity.
- First, sort the input array.
- Then, fix two numbers (the first two numbers of the quadruplet) using two nested loops.
- For the remaining two numbers, use a two-pointer technique (one starting from the next number after the second fixed number and one from the end of the array).
- Move the pointers based on the sum of the four numbers to find all unique quadruplets that sum to the target.
- Skip duplicate quadruplets by checking if the current number is the same as the previous one.

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++) {
            // Skip duplicates for i
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.size() - 2; j++) {
                // Skip duplicates for j
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int left = j + 1, right = nums.size() - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum < target) {
                        left++;
                    } else if (sum > target) {
                        right--;
                    } else {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        // Move pointers and skip duplicates
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++; right--;
                    }
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the input array, because we are using three nested loops (two for fixing the first two numbers and one implicit loop for the two-pointer technique).
> - **Space Complexity:** $O(n)$ for storing the result, in the worst case when all quadruplets sum to the target.
> - **Optimality proof:** This is the optimal approach because we have reduced the number of loops from four to three, and the two-pointer technique efficiently finds the remaining two numbers without generating all possible combinations.

---

### Final Notes

**Learning Points:**
- The importance of sorting the input array to apply the two-pointer technique.
- How to skip duplicate quadruplets by checking for equal adjacent elements.
- The use of the two-pointer technique to reduce the time complexity of finding pairs that sum to a target.
- Problem-solving patterns identified include fixing some variables and using a two-pointer technique for the remaining variables.

**Mistakes to Avoid:**
- Not sorting the input array before applying the two-pointer technique.
- Not skipping duplicate quadruplets, leading to incorrect results.
- Not considering edge cases like an empty input array or no quadruplets summing to the target.
- Testing considerations include checking for duplicate quadruplets and ensuring the solution handles edge cases correctly.