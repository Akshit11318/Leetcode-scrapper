## Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold

**Problem Link:** https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description

**Problem Statement:**
- Input format and constraints: The problem takes an array `arr`, an integer `k`, and a threshold value `threshold` as inputs. The array `arr` contains integers, and `k` and `threshold` are positive integers.
- Expected output format: The function should return the number of sub-arrays of size `k` in `arr` where the average of the elements is greater than or equal to `threshold`.
- Key requirements and edge cases to consider: The function should handle arrays of varying lengths, including edge cases where `k` is equal to or larger than the length of `arr`. It should also correctly calculate the average of sub-arrays and compare it to the threshold.
- Example test cases with explanations:
  - Example 1: `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4`. The sub-arrays of size 3 with an average greater than or equal to 4 are `[2,2,5], [2,5,5], [5,5,5], [5,5,8], [2,5,5], [5,5,8]`. So, the output should be 3.
  - Example 2: `arr = [11,1,12,13,2,3,4,5], k = 3, threshold = 6`. The sub-arrays of size 3 with an average greater than or equal to 6 are `[11,1,12], [1,12,13], [12,13,2], [13,2,3], [2,3,4], [3,4,5]`. However, not all of these meet the threshold condition. After calculation, we find that the number of such sub-arrays is less.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify all possible sub-arrays of size `k` within the given array `arr`. Then, for each sub-array, calculate the average of its elements and check if this average is greater than or equal to the threshold.
- Step-by-step breakdown of the solution:
  1. Generate all sub-arrays of size `k` from `arr`.
  2. For each sub-array, calculate the sum of its elements.
  3. Calculate the average of the sub-array by dividing the sum by `k`.
  4. Compare the average to the threshold. If it's greater than or equal to the threshold, increment a counter.
  5. After checking all sub-arrays, return the counter as the result.

```cpp
int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int count = 0;
    for (int i = 0; i <= arr.size() - k; i++) {
        int sum = 0;
        for (int j = i; j < i + k; j++) {
            sum += arr[j];
        }
        double average = (double)sum / k;
        if (average >= threshold) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the array `arr`. This is because for each starting position of the sub-array (which can be $n-k+1$ positions), we potentially iterate through `k` elements to calculate the sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and other variables.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, while the constant space usage is due to not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sum for each sub-array from scratch, we can use a sliding window approach. This involves maintaining a running sum of the current sub-array and updating it as we slide the window through the array.
- Detailed breakdown of the approach:
  1. Initialize a variable to keep track of the sum of the current sub-array.
  2. For the first sub-array, calculate the sum directly.
  3. For subsequent sub-arrays, subtract the element going out of the window and add the element entering the window to update the sum.
  4. Calculate the average and compare it to the threshold for each sub-array.
  5. Count the number of sub-arrays where the average is greater than or equal to the threshold.

```cpp
int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int count = 0;
    int windowSum = 0;
    for (int i = 0; i < arr.size(); i++) {
        windowSum += arr[i];
        if (i >= k) {
            windowSum -= arr[i - k];
        }
        if (i >= k - 1) {
            double average = (double)windowSum / k;
            if (average >= threshold) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array `arr`. This is because we make a single pass through the array, updating the window sum as we go.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count, window sum, and other variables.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best we can do for this problem since we must at least examine each element once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, optimization of nested loops.
- Problem-solving patterns identified: Using running sums to avoid redundant calculations.
- Optimization techniques learned: Reducing the time complexity by avoiding unnecessary recalculations.
- Similar problems to practice: Other problems involving sub-arrays or sliding windows, such as maximum sub-array problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the window sum or forgetting to subtract the outgoing element.
- Edge cases to watch for: When `k` is larger than the array size, or when the threshold is very large/small.
- Performance pitfalls: Using nested loops when a single pass can suffice.
- Testing considerations: Ensure to test with various array sizes, `k` values, and threshold values to cover all edge cases.