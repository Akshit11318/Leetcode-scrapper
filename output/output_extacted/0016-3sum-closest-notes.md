## 3Sum Closest
**Problem Link:** https://leetcode.com/problems/3sum-closest/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums` and an integer `target`. The constraints are that the length of `nums` is at least 3, and all elements in `nums` are integers.
- Expected output format: The output should be the sum of three numbers in `nums` that is closest to `target`.
- Key requirements and edge cases to consider: The key requirement is to find the sum of three numbers that is closest to `target`. The edge cases include when the length of `nums` is exactly 3, and when there are multiple sums that are equally close to `target`.
- Example test cases with explanations:
  - Example 1: Input: `nums = [-1,2,1,-4]`, `target = 1`. Output: `2`. Explanation: The sum of `-1 + 2 + 1 = 2`, which is closest to `target`.
  - Example 2: Input: `nums = [0,0,0]`, `target = 1`. Output: `0`. Explanation: The sum of `0 + 0 + 0 = 0`, which is closest to `target`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to try all possible combinations of three numbers in the array and calculate their sum.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of three numbers in the array.
  2. Calculate the sum of each combination.
  3. Compare the sum with the target and keep track of the sum that is closest to the target.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closestSum = nums[0] + nums[1] + nums[2];
        int minDiff = abs(closestSum - target);
        
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    int sum = nums[i] + nums[j] + nums[k];
                    int diff = abs(sum - target);
                    if (diff < minDiff) {
                        minDiff = diff;
                        closestSum = sum;
                    }
                }
            }
        }
        
        return closestSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we are generating all possible combinations of three numbers in the array, which takes $O(n^3)$ time.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, so it is constant.
> - **Why these complexities occur:** The time complexity occurs because we are using three nested loops to generate all possible combinations of three numbers. The space complexity is constant because we are only using a constant amount of space to store the closest sum and the minimum difference.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a two-pointer technique to find the closest sum.
- Detailed breakdown of the approach:
  1. Sort the input array.
  2. Fix one number and use two pointers to find the closest sum.
  3. Move the pointers based on the comparison of the sum with the target.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we need to consider all pairs of numbers in the array to find the closest sum, which takes at least $O(n^2)$ time.

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int closestSum = nums[0] + nums[1] + nums[2];
        int minDiff = abs(closestSum - target);
        
        for (int i = 0; i < nums.size() - 2; i++) {
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                int diff = abs(sum - target);
                if (diff < minDiff) {
                    minDiff = diff;
                    closestSum = sum;
                }
                if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return closestSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using two nested loops to find the closest sum.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, so it is constant.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The two-pointer technique and sorting.
- Problem-solving patterns identified: The pattern of using a two-pointer technique to find the closest sum.
- Optimization techniques learned: Reducing the time complexity from $O(n^3)$ to $O(n^2)$.
- Similar problems to practice: Other problems that involve finding the closest sum or using the two-pointer technique.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the input array or not moving the pointers correctly.
- Edge cases to watch for: When the length of the input array is less than 3 or when there are multiple sums that are equally close to the target.
- Performance pitfalls: Using a brute force approach or not optimizing the solution.
- Testing considerations: Testing the solution with different input arrays and targets to ensure it works correctly.