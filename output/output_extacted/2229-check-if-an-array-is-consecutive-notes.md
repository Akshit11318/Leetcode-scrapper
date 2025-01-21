## Check If An Array Is Consecutive

**Problem Link:** https://leetcode.com/problems/check-if-an-array-is-consecutive/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is between 1 and $10^5$.
- Expected output format: A boolean value indicating whether the array is consecutive.
- Key requirements: The array is considered consecutive if the difference between any two adjacent elements is 1.
- Edge cases to consider: An empty array, an array with a single element, an array with duplicate elements, and an array with non-integer values.
- Example test cases:
  - Input: `nums = [2,1,3]`, Output: `true`
  - Input: `nums = [1,3]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array and then check if the difference between any two adjacent elements is 1.
- Step-by-step breakdown of the solution:
  1. Sort the array in ascending order.
  2. Iterate through the array and check if the difference between any two adjacent elements is 1.
  3. If a pair of adjacent elements with a difference other than 1 is found, return `false`.
  4. If the iteration completes without finding such a pair, return `true`.

```cpp
class Solution {
public:
    bool isConsecutive(vector<int>& nums) {
        // Check if the input array is empty
        if (nums.size() == 0) {
            return false;
        }
        
        // Sort the array in ascending order
        sort(nums.begin(), nums.end());
        
        // Iterate through the array and check if the difference between any two adjacent elements is 1
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] - nums[i - 1] != 1) {
                return false;
            }
        }
        
        // If the iteration completes without finding a pair with a difference other than 1, return true
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the length of the input array.
> - **Space Complexity:** $O(1)$ if the sorting is done in-place, or $O(n)$ if a new sorted array is created.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity depends on the sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of sorting the array, we can use a `set` to store the elements and then check if the difference between the maximum and minimum elements is equal to the length of the array minus 1.
- Detailed breakdown of the approach:
  1. Create a `set` to store the unique elements of the array.
  2. Calculate the minimum and maximum elements in the array.
  3. Check if the difference between the maximum and minimum elements is equal to the length of the array minus 1.
  4. If the difference is equal to the length minus 1 and the size of the `set` is equal to the length of the array, return `true`.
  5. Otherwise, return `false`.

```cpp
class Solution {
public:
    bool isConsecutive(vector<int>& nums) {
        // Check if the input array is empty
        if (nums.size() == 0) {
            return false;
        }
        
        // Create a set to store the unique elements of the array
        set<int> numSet;
        int minNum = INT_MAX;
        int maxNum = INT_MIN;
        
        // Iterate through the array and update the set, minimum, and maximum
        for (int num : nums) {
            numSet.insert(num);
            minNum = min(minNum, num);
            maxNum = max(maxNum, num);
        }
        
        // Check if the difference between the maximum and minimum elements is equal to the length of the array minus 1
        if (maxNum - minNum == nums.size() - 1 && numSet.size() == nums.size()) {
            return true;
        }
        
        // If the conditions are not met, return false
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, due to the iteration through the array.
> - **Space Complexity:** $O(n)$ due to the use of the `set`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array and uses a `set` to efficiently store and check for unique elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, sets, and iteration.
- Problem-solving patterns identified: checking for consecutive elements and using a `set` to store unique elements.
- Optimization techniques learned: avoiding unnecessary sorting and using a `set` for efficient lookup.
- Similar problems to practice: checking for duplicates, finding the maximum or minimum element, and solving problems involving arrays and sets.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not validating input, and not handling errors properly.
- Edge cases to watch for: empty arrays, arrays with a single element, and arrays with duplicate elements.
- Performance pitfalls: using inefficient algorithms or data structures, such as sorting when not necessary.
- Testing considerations: testing with a variety of input cases, including edge cases, to ensure the solution is robust and correct.