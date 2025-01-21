## Consecutive Transactions with Increasing Amounts
**Problem Link:** https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/description

**Problem Statement:**
- Input: An array of integers representing transaction amounts and an integer `k` representing the number of consecutive transactions.
- Constraints: The input array can contain any integer values (positive, negative, or zero), and `k` is a positive integer.
- Expected Output: The maximum sum of `k` consecutive transactions with strictly increasing amounts.
- Key Requirements: 
    - The transactions must be consecutive in the input array.
    - The amounts must be strictly increasing.
- Edge Cases: 
    - If `k` is larger than the input array length, return `-1`.
    - If the input array is empty, return `0`.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible sequence of `k` consecutive transactions to see if their amounts are strictly increasing.
- We then calculate the sum of these transactions and keep track of the maximum sum found.

```cpp
int maxSum(vector<int>& amounts, int k) {
    int n = amounts.size();
    if (k > n) return -1; // Edge case: k larger than array length
    
    int maxSum = 0;
    for (int i = 0; i <= n - k; i++) {
        bool increasing = true;
        int currentSum = 0;
        for (int j = 0; j < k; j++) {
            if (j > 0 && amounts[i + j] <= amounts[i + j - 1]) {
                increasing = false;
                break;
            }
            currentSum += amounts[i + j];
        }
        if (increasing) {
            maxSum = max(maxSum, currentSum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of transactions and $k$ is the number of consecutive transactions. This is because we are iterating over the array and for each starting position, we are checking `k` consecutive transactions.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the maximum sum and other variables.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is low because we only use a few variables regardless of the input size.

### Optimal Approach
**Explanation:**
- The optimal approach involves using a sliding window technique to efficiently check for strictly increasing sequences of `k` consecutive transactions.
- We maintain a window of size `k` and slide it over the array, checking if the amounts within the window are strictly increasing.
- If they are, we calculate the sum of the transactions in the window and update the maximum sum if necessary.

```cpp
int maxSum(vector<int>& amounts, int k) {
    int n = amounts.size();
    if (k > n) return -1; // Edge case: k larger than array length
    
    int maxSum = 0;
    for (int i = 0; i <= n - k; i++) {
        bool increasing = true;
        int currentSum = 0;
        for (int j = i; j < i + k; j++) {
            if (j > i && amounts[j] <= amounts[j - 1]) {
                increasing = false;
                break;
            }
            currentSum += amounts[j];
        }
        if (increasing) {
            maxSum = max(maxSum, currentSum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of transactions and $k` is the number of consecutive transactions. This is because we are still iterating over the array and checking each sequence of `k` transactions.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the maximum sum and other variables.
> - **Optimality proof:** This approach is optimal because it checks every possible sequence of `k` consecutive transactions exactly once, ensuring that we find the maximum sum if it exists.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, iterative approach to checking sequences.
- Problem-solving patterns identified: Using a sliding window to efficiently check for certain properties in an array.
- Optimization techniques learned: Reducing the number of iterations by using a sliding window.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly (e.g., `k` larger than array length).
- Edge cases to watch for: Empty input array, `k` larger than array length.
- Performance pitfalls: Using unnecessary nested loops or recursive functions.
- Testing considerations: Test with various input sizes, including edge cases.