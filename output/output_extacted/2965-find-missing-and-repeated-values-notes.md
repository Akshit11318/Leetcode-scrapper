## Find Missing and Repeated Values
**Problem Link:** https://leetcode.com/problems/find-missing-and-repeated-values/description

**Problem Statement:**
- Given an array of integers `nums` of length `n`, where each integer is in the range $[1, n]$, find the missing and repeated values.
- Input format: The input array `nums`.
- Constraints: The array contains `n` integers, where each integer is in the range $[1, n]$.
- Expected output format: Return two integers, the missing and the repeated values.
- Key requirements and edge cases to consider: The array contains a single missing and a single repeated value.
- Example test cases with explanations: For example, given `nums = [1, 1]`, the output should be `[2, 1]`, indicating that `2` is the missing value and `1` is the repeated value.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem can be solved by iterating over all possible values in the range $[1, n]$ and checking if each value exists in the array.
- Step-by-step breakdown of the solution:
  1. Initialize two variables, `missing` and `repeated`, to store the missing and repeated values.
  2. Create a frequency array `freq` of size `n` to store the frequency of each value in the input array.
  3. Iterate over the input array and update the frequency of each value in the frequency array.
  4. Iterate over the frequency array to find the missing and repeated values.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
#include <iostream>
#include <vector>

std::vector<int> findErrorNums(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> freq(n + 1, 0);
    for (int num : nums) {
        freq[num]++;
    }
    int missing = 0, repeated = 0;
    for (int i = 1; i <= n; i++) {
        if (freq[i] == 0) {
            missing = i;
        }
        if (freq[i] > 1) {
            repeated = i;
        }
    }
    return {repeated, missing};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate over the input array twice.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we create a frequency array of size $n + 1$.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the input array twice, and the space complexity occurs because we create a frequency array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the input array itself to store the frequency of each value, instead of creating a separate frequency array.
- Detailed breakdown of the approach:
  1. Initialize two variables, `missing` and `repeated`, to store the missing and repeated values.
  2. Iterate over the input array and use the absolute value of each element as an index to mark the corresponding index as negative.
  3. Iterate over the input array again to find the missing and repeated values.
- Proof of optimality: This approach is optimal because it uses the input array itself to store the frequency of each value, reducing the space complexity to $O(1)$.

```cpp
#include <iostream>
#include <vector>

std::vector<int> findErrorNums(std::vector<int>& nums) {
    int n = nums.size();
    int missing = 0, repeated = 0;
    for (int i = 0; i < n; i++) {
        int index = abs(nums[i]) - 1;
        if (nums[index] < 0) {
            repeated = abs(nums[i]);
        } else {
            nums[index] = -nums[index];
        }
    }
    for (int i = 0; i < n; i++) {
        if (nums[i] > 0) {
            missing = i + 1;
        }
    }
    return {repeated, missing};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate over the input array twice.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we use the input array itself to store the frequency of each value.
> - **Optimality proof:** This approach is optimal because it uses the input array itself to store the frequency of each value, reducing the space complexity to $O(1)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using the input array itself to store the frequency of each value.
- Problem-solving patterns identified: Using the absolute value of each element as an index to mark the corresponding index as negative.
- Optimization techniques learned: Reducing the space complexity by using the input array itself.
- Similar problems to practice: Other problems that involve finding missing and repeated values in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input array is empty.
- Edge cases to watch for: Not handling the case where the input array contains duplicate values.
- Performance pitfalls: Not using the input array itself to store the frequency of each value, resulting in a higher space complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.