## Maximum Erasure Value
**Problem Link:** https://leetcode.com/problems/maximum-erasure-value/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^5`.
- Expected output format: The maximum erasure value.
- Key requirements and edge cases to consider: The erasure value is the sum of the elements in the subarray.
- Example test cases with explanations: 
    - `nums = [4,2,4,5,6]`, the maximum erasure value is `17` because `[5,6,4,2]` can be erased.
    - `nums = [5,6,100,2,3]`, the maximum erasure value is `100` because `[100]` can be erased.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible subarrays of the given array and calculate the sum of each subarray.
- Step-by-step breakdown of the solution:
    1. Initialize the maximum sum as a negative infinity.
    2. Iterate over all possible subarrays.
    3. For each subarray, calculate its sum.
    4. Update the maximum sum if the current sum is greater.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking all possibilities.

```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxSum = INT_MIN;
        for (int i = 0; i < n; i++) {
            unordered_set<int> unique;
            int sum = 0;
            for (int j = i; j < n; j++) {
                if (unique.find(nums[j]) != unique.end()) {
                    break;
                }
                unique.insert(nums[j]);
                sum += nums[j];
                maxSum = max(maxSum, sum);
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because for each element in the array, we potentially iterate over the rest of the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we use a set to store unique elements in the current subarray, and in the worst case, the set will contain all elements from the array.
> - **Why these complexities occur:** The time complexity occurs because of the nested loop structure, and the space complexity occurs because we use a set to store unique elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach with two pointers and a set to keep track of unique elements in the current window.
- Detailed breakdown of the approach:
    1. Initialize two pointers, `left` and `right`, to the start of the array.
    2. Initialize a set `unique` to store unique elements in the current window.
    3. Initialize a variable `windowSum` to store the sum of elements in the current window.
    4. Move the `right` pointer to the right, adding elements to the set and updating the `windowSum`.
    5. If a duplicate element is found, move the `left` pointer to the right, removing elements from the set and updating the `windowSum`.
    6. Update the maximum sum at each step.
- Proof of optimality: This approach has a linear time complexity because each element is visited at most twice (once by the `right` pointer and once by the `left` pointer).

```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxSum = 0;
        int windowSum = 0;
        int left = 0;
        unordered_set<int> unique;
        for (int right = 0; right < n; right++) {
            while (unique.find(nums[right]) != unique.end()) {
                unique.erase(nums[left]);
                windowSum -= nums[left];
                left++;
            }
            unique.insert(nums[right]);
            windowSum += nums[right];
            maxSum = max(maxSum, windowSum);
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because each element is visited at most twice.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we use a set to store unique elements in the current window.
> - **Optimality proof:** This approach has a linear time complexity, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, use of sets for efficient lookup and insertion.
- Problem-solving patterns identified: Using two pointers and a set to solve problems involving subarrays and uniqueness.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary iterations and using efficient data structures.
- Similar problems to practice: Problems involving subarrays, uniqueness, and sliding window approaches.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the `windowSum` or `maxSum` variables.
- Edge cases to watch for: Empty input array, array with duplicate elements.
- Performance pitfalls: Using inefficient data structures or algorithms, such as iterating over the array multiple times.
- Testing considerations: Test with different input sizes, including edge cases like empty arrays or arrays with duplicate elements.