## Count Subarrays with More Ones Than Zeros
**Problem Link:** https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/description

**Problem Statement:**
- Input: An array of integers `nums` where each integer is either 0 or 1.
- Constraints: $1 \leq nums.length \leq 10^5$.
- Expected output: The number of subarrays that contain more ones than zeros.
- Key requirements and edge cases: Consider all possible subarrays, including those with a single element.

**Example Test Cases:**
- For `nums = [0,1,1,2,0]`, the output should be `9` because there are nine subarrays with more ones than zeros.
- For `nums = [0,0,0,1,0,0]`, the output should be `2` because there are two subarrays with more ones than zeros.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if it has more ones than zeros.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible start indices of subarrays.
  2. For each start index, iterate over all possible end indices of subarrays.
  3. For each subarray, count the number of ones and zeros.
  4. If the number of ones is greater than the number of zeros, increment the count of subarrays with more ones than zeros.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = 0, zeros = 0;
            for (int k = i; k <= j; k++) {
                if (nums[k] == 1) ones++;
                else zeros++;
            }
            if (ones > zeros) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `nums`. This is because we have three nested loops: one to select the start of the subarray, one to select the end of the subarray, and one to count the ones and zeros in the subarray.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the count and temporary variables.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it checks every possible subarray, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a prefix sum array to keep track of the difference between the number of ones and zeros up to each index.
- Detailed breakdown of the approach:
  1. Initialize a prefix sum array `prefixSum` where `prefixSum[i]` is the difference between the number of ones and zeros in the subarray from index 0 to i.
  2. Iterate over all possible start indices of subarrays.
  3. For each start index, iterate over all possible end indices of subarrays.
  4. Calculate the difference between the number of ones and zeros in the subarray from the start index to the end index using the prefix sum array.
  5. If the difference is positive, increment the count of subarrays with more ones than zeros.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += (nums[j] == 1) ? 1 : -1;
            if (sum > 0) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `nums`. This is because we have two nested loops: one to select the start of the subarray and one to select the end of the subarray.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the count and temporary variables.
> - **Optimality proof:** This approach is optimal because we must at least consider each subarray once to determine if it has more ones than zeros. The use of a running sum instead of a prefix sum array reduces the space complexity to constant.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sums, running sums, and the importance of considering all possible subarrays.
- Problem-solving patterns identified: Using a running sum to keep track of the difference between the number of ones and zeros in a subarray.
- Optimization techniques learned: Reducing the number of iterations by using a running sum instead of recalculating the sum for each subarray.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the count variable to zero, not checking for the case where the number of ones is equal to the number of zeros.
- Edge cases to watch for: Subarrays with a single element, subarrays with all zeros or all ones.
- Performance pitfalls: Using a brute force approach with cubic time complexity, not using a running sum to reduce the number of iterations.
- Testing considerations: Testing with different input sizes, testing with different distributions of ones and zeros.