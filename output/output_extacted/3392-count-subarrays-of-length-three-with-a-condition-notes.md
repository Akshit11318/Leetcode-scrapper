## Count Subarrays of Length Three with a Condition
**Problem Link:** https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description

**Problem Statement:**
- Input format and constraints: The problem takes an array `nums` as input, where `1 <= nums.length <= 1000` and `0 <= nums[i] <= 1000`. The goal is to count the number of subarrays of length three that satisfy the given condition.
- Expected output format: The output should be the number of subarrays of length three where the sum of the elements in the subarray is less than the sum of the elements in any other subarray of length three.
- Key requirements and edge cases to consider: The array may contain duplicate elements, and the subarrays must have a length of exactly three.
- Example test cases with explanations: For example, given the array `[1, 2, 3, 4, 5]`, the subarrays of length three are `[1, 2, 3]`, `[2, 3, 4]`, and `[3, 4, 5]`. The sums of these subarrays are `6`, `9`, and `12`, respectively. Therefore, the output should be `1`, because only the subarray `[1, 2, 3]` has a sum less than any other subarray of length three.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to generate all possible subarrays of length three and compare their sums.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of length three.
  2. Calculate the sum of each subarray.
  3. Compare the sums of all subarrays and count the number of subarrays with a sum less than any other subarray.
- Why this approach comes to mind first: This approach is intuitive because it directly addresses the problem statement by considering all possible subarrays and comparing their sums.

```cpp
int countSubarrays(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        int sum = nums[i] + nums[i + 1] + nums[i + 2];
        bool isMin = true;
        for (int j = 0; j < n - 2; j++) {
            if (i == j) continue;
            int otherSum = nums[j] + nums[j + 1] + nums[j + 2];
            if (sum >= otherSum) {
                isMin = false;
                break;
            }
        }
        if (isMin) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we have two nested loops: one to generate all subarrays and another to compare the sums.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count and other variables.
> - **Why these complexities occur:** The time complexity is quadratic because we compare each subarray with every other subarray, resulting in $n^2$ comparisons. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each subarray with every other subarray, we can find the minimum sum of all subarrays first and then count the number of subarrays with this minimum sum.
- Detailed breakdown of the approach:
  1. Calculate the sum of each subarray of length three.
  2. Find the minimum sum among all subarrays.
  3. Count the number of subarrays with the minimum sum.
- Proof of optimality: This approach is optimal because it reduces the number of comparisons from $n^2$ to $n$, which significantly improves the time complexity.
- Why further optimization is impossible: This approach is already optimal because we must consider each subarray at least once to find the minimum sum and count the subarrays with this sum.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int minSum = INT_MAX;
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        int sum = nums[i] + nums[i + 1] + nums[i + 2];
        if (sum < minSum) {
            minSum = sum;
            count = 1;
        } else if (sum == minSum) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the array to calculate the sums and find the minimum.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum sum and count.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array, which is the minimum number of operations needed to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of finding the minimum or maximum value in an array and using it to simplify comparisons.
- Problem-solving patterns identified: The problem illustrates the pattern of finding a minimum or maximum value and then counting the number of elements that match this value.
- Optimization techniques learned: The problem shows how to optimize a solution by reducing the number of comparisons from quadratic to linear.
- Similar problems to practice: Other problems that involve finding minimum or maximum values and counting elements that match these values.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to use a brute force approach without considering more efficient solutions.
- Edge cases to watch for: The problem requires considering edge cases such as arrays with duplicate elements or arrays with a small number of elements.
- Performance pitfalls: The problem illustrates the importance of avoiding quadratic time complexity by finding more efficient solutions.
- Testing considerations: The problem requires testing with different input arrays to ensure that the solution works correctly in all cases.