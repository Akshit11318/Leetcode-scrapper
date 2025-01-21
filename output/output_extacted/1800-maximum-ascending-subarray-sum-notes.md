## Maximum Ascending Subarray Sum
**Problem Link:** https://leetcode.com/problems/maximum-ascending-subarray-sum/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`.
- Expected Output: The maximum ascending subarray sum.
- Key Requirements:
  - An ascending subarray is defined as a subarray where every element is strictly greater than its previous element.
  - We need to find the maximum sum of such a subarray.
- Edge Cases:
  - The input array can contain duplicate elements.
  - The array can be empty, but given the constraints, this is not the case here.
- Example Test Cases:
  - For `nums = [10,1,2,3,4]`, the maximum ascending subarray sum is `10 + 1 + 2 + 3 + 4 = 20`.
  - For `nums = [3,6,1,0]`, the maximum ascending subarray sum is `3 + 6 = 9`.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: One straightforward approach is to check every possible subarray of the input array to see if it's ascending and then keep track of the maximum sum found.
- Step-by-Step Breakdown:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, check if it's ascending.
  3. If it's ascending, calculate its sum.
  4. Update the maximum sum if the current sum is greater.

```cpp
int maxAscendingSum(vector<int>& nums) {
    int maxSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            int sum = 0;
            bool isAscending = true;
            for (int k = i; k <= j; k++) {
                if (k > i && nums[k] <= nums[k - 1]) {
                    isAscending = false;
                    break;
                }
                sum += nums[k];
            }
            if (isAscending) {
                maxSum = max(maxSum, sum);
            }
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of elements in the input array. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the maximum sum and other variables.
> - **Why these complexities occur:** The brute force approach checks every possible subarray, leading to a cubic time complexity due to the nested loops. However, it uses constant space as it doesn't require any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of checking every possible subarray, we can iterate through the array and whenever we find an element that is greater than the previous one, we can extend the current ascending subarray. If the element is not greater, we start a new ascending subarray from that element.
- Detailed Breakdown:
  1. Initialize variables to keep track of the current sum and the maximum sum found so far.
  2. Iterate through the input array.
  3. For each element, check if it's greater than the previous element. If it is, add it to the current sum. If not, update the maximum sum if necessary and reset the current sum to the current element.
  4. After the loop, update the maximum sum one last time if necessary.

```cpp
int maxAscendingSum(vector<int>& nums) {
    if (nums.empty()) return 0;
    int maxSum = nums[0];
    int currentSum = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] > nums[i - 1]) {
            currentSum += nums[i];
        } else {
            maxSum = max(maxSum, currentSum);
            currentSum = nums[i];
        }
    }
    return max(maxSum, currentSum);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the input array. This is because we only iterate through the array once.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the maximum sum, current sum, and other variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array, and it keeps track of the maximum ascending sum seen so far. It avoids unnecessary comparisons and calculations by only considering elements that could potentially extend the current ascending subarray or start a new one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative approach, keeping track of maximum and current sums.
- Problem-solving patterns identified: Avoiding brute force by exploiting the structure of the problem (in this case, the definition of an ascending subarray).
- Optimization techniques learned: Reducing the number of comparisons and calculations by only considering relevant elements.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum sum correctly, not handling the edge case where the input array is empty (though the problem statement guarantees it won't be).
- Edge cases to watch for: The array containing a single element, the array being empty (though this is not applicable given the constraints).
- Performance pitfalls: Using a brute force approach for larger inputs, not considering the structure of the problem to optimize the solution.