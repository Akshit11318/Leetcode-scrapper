## Count the Number of Inremovable Subarrays I

**Problem Link:** https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 10^5$.
- Expected output format: The number of subarrays that are inremovable.
- Key requirements and edge cases to consider: A subarray is inremovable if it is strictly increasing and has no adjacent elements with a difference of 1.

**Example Test Cases with Explanations:**

- Example 1: Input `nums = [3,2,1]`, Output `3`. Explanation: The subarrays `[3]`, `[2]`, and `[1]` are all inremovable because they are strictly increasing and have no adjacent elements with a difference of 1.
- Example 2: Input `nums = [2,1,3]`, Output `2`. Explanation: The subarrays `[2,1]` and `[3]` are inremovable.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subarrays and check each one to see if it is inremovable.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, check if it is strictly increasing.
  3. If the subarray is strictly increasing, check if it has any adjacent elements with a difference of 1.
  4. If the subarray does not have any adjacent elements with a difference of 1, increment the count of inremovable subarrays.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves checking all possible subarrays.

```cpp
int countInremovableSubarrays(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            bool isIncreasing = true;
            bool hasAdjacentDifferenceOne = false;
            for (int k = 0; k < subarray.size() - 1; k++) {
                if (subarray[k] >= subarray[k + 1]) {
                    isIncreasing = false;
                    break;
                }
                if (abs(subarray[k] - subarray[k + 1]) == 1) {
                    hasAdjacentDifferenceOne = true;
                }
            }
            if (isIncreasing && !hasAdjacentDifferenceOne) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we are generating all possible subarrays (which takes $O(n^2)$ time) and then checking each subarray to see if it is inremovable (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are storing each subarray in memory.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays and checking each one, which results in a high time complexity. The space complexity is also high because we are storing each subarray in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subarrays, we can use a single pass through the input array to count the number of inremovable subarrays.
- Detailed breakdown of the approach:
  1. Initialize a count variable to 0.
  2. Iterate through the input array.
  3. For each element, check if it can be extended to form an inremovable subarray with the previous element.
  4. If the current element can be extended to form an inremovable subarray with the previous element, increment the count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array, resulting in a time complexity of $O(n)$.

```cpp
int countInremovableSubarrays(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        bool isIncreasing = true;
        bool hasAdjacentDifferenceOne = false;
        for (int j = i; j < nums.size(); j++) {
            if (j > i && (nums[j] <= nums[j - 1] || abs(nums[j] - nums[j - 1]) == 1)) {
                break;
            }
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are iterating through the input array and for each element, we are checking if it can be extended to form an inremovable subarray with the previous element.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array and uses a minimal amount of additional space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of iterating through the input array only once to achieve optimal time complexity.
- Problem-solving patterns identified: Using a single pass through the input array to count the number of inremovable subarrays.
- Optimization techniques learned: Avoiding unnecessary computations by breaking out of the inner loop as soon as possible.
- Similar problems to practice: Other problems that involve counting the number of subarrays with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not breaking out of the inner loop as soon as possible, resulting in unnecessary computations.
- Edge cases to watch for: Empty input arrays, input arrays with a single element, and input arrays with duplicate elements.
- Performance pitfalls: Using a brute force approach that generates all possible subarrays, resulting in a high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases, to ensure that it produces the correct output.