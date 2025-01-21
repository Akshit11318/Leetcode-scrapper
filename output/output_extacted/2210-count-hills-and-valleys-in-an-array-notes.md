## Count Hills and Valleys in an Array

**Problem Link:** https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The array will contain at least 3 elements and at most $10^5$ elements.
- Expected output format: The number of hills and valleys in the array.
- Key requirements and edge cases to consider: A hill is defined as a sequence of three or more elements where the middle element is greater than its neighbors. A valley is defined as a sequence of three or more elements where the middle element is less than its neighbors.
- Example test cases with explanations:
  - For `nums = [2,4,1,1,6,5]`, the output should be `3` because there is one hill (`4`) and two valleys (`1`, `5`).
  - For `nums = [6,6,6]`, the output should be `0` because there are no hills or valleys.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray of length 3 or more in the input array to determine if it contains a hill or valley.
- Step-by-step breakdown of the solution:
  1. Iterate over the array with a sliding window of size 3.
  2. For each window, check if the middle element is greater than its neighbors (hill) or less than its neighbors (valley).
  3. If a hill or valley is found, increment the count.
- Why this approach comes to mind first: It is straightforward to understand and implement, as it directly checks all possible subarrays for the conditions of a hill or valley.

```cpp
int countHillsAndValleys(vector<int>& nums) {
    int count = 0;
    for (int i = 1; i < nums.size() - 1; i++) {
        bool isHill = nums[i] > nums[i - 1] && nums[i] > nums[i + 1];
        bool isValley = nums[i] < nums[i - 1] && nums[i] < nums[i + 1];
        if (isHill || isValley) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are scanning the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The time complexity is linear because we are checking each element in the array once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The definition of a hill or valley requires checking only the immediate neighbors of an element, not all possible subarrays of length 3 or more. Thus, a single pass through the array is sufficient.
- Detailed breakdown of the approach:
  1. Initialize a count variable to 0.
  2. Iterate through the array from the second element to the second last element.
  3. For each element, check if it is a hill (greater than both neighbors) or a valley (less than both neighbors).
  4. If it is a hill or a valley, increment the count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, and it checks the minimum necessary conditions for a hill or valley, resulting in a time complexity of $O(n)$.

```cpp
int countHillsAndValleys(vector<int>& nums) {
    int count = 0;
    for (int i = 1; i < nums.size() - 1; i++) {
        if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) || 
            (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the count.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to identify hills and valleys, only requiring a comparison with immediate neighbors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the problem definition and identifying the minimum necessary conditions to check for a solution.
- Problem-solving patterns identified: The use of a single pass through the data to solve the problem efficiently.
- Optimization techniques learned: Minimizing the number of comparisons and operations needed to achieve the solution.
- Similar problems to practice: Other problems involving pattern recognition or sequence analysis.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly checking for hill or valley conditions, or not considering edge cases.
- Edge cases to watch for: The first and last elements of the array, which do not have two neighbors to compare with.
- Performance pitfalls: Using unnecessary loops or data structures that increase the time or space complexity.
- Testing considerations: Thoroughly testing the function with various input arrays, including edge cases and arrays with different lengths.