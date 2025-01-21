## Jump Game VIII
**Problem Link:** https://leetcode.com/problems/jump-game-viii/description

**Problem Statement:**
- Input: Two integers `a` and `b`, and an array of integers `arr`.
- Constraints: `2 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^6`, and `1 <= a, b <= 10^6`.
- Expected Output: Return the maximum value of `a * x + b * y` such that `x` and `y` are two numbers in the array and `x` is not equal to `y`.
- Key Requirements: The goal is to maximize the expression `a * x + b * y` by choosing the most suitable pair of distinct numbers from the array.
- Example Test Cases:
  - For `a = 1`, `b = 3`, and `arr = [1, 5]`, the maximum value is `3 * 5 + 1 * 1 = 16`.
  - For `a = 2`, `b = 2`, and `arr = [1, 2, 3]`, the maximum value is `2 * 3 + 2 * 1 = 8`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible pair of numbers in the array to see which pair maximizes the given expression.
- This approach involves iterating through the array and for each element, iterating through the rest of the array to consider all pairs.
- This comes to mind first because it directly addresses the problem statement without requiring any additional insight or optimization.

```cpp
int maxSum(int a, int b, vector<int>& arr) {
    int maxVal = INT_MIN;
    for (int i = 0; i < arr.size(); ++i) {
        for (int j = i + 1; j < arr.size(); ++j) {
            int sum = a * arr[i] + b * arr[j];
            maxVal = max(maxVal, sum);
            sum = a * arr[j] + b * arr[i];
            maxVal = max(maxVal, sum);
        }
    }
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of elements in the array, because we're using two nested loops to consider all pairs of numbers.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we're only using a constant amount of space to store the maximum value found so far.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to consider the maximum and minimum values in the array to maximize the expression `a * x + b * y`.
- If `a` and `b` are both positive, then we should choose the two largest numbers in the array to maximize the sum.
- If `a` and `b` have different signs, we should choose the largest number for the positive coefficient and the smallest number for the negative coefficient.
- This approach is optimal because it directly targets the conditions that maximize the given expression without unnecessary comparisons.

```cpp
int maxSum(int a, int b, vector<int>& arr) {
    int maxVal = *max_element(arr.begin(), arr.end());
    int minVal = *min_element(arr.begin(), arr.end());
    if (a > 0 && b > 0) {
        sort(arr.rbegin(), arr.rend());
        return a * arr[0] + b * arr[1];
    } else if (a < 0 && b < 0) {
        sort(arr.begin(), arr.end());
        return a * arr[0] + b * arr[1];
    } else {
        return max(a * maxVal + b * minVal, a * minVal + b * maxVal);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array, because we're using `max_element` and `min_element` to find the maximum and minimum values, and potentially sorting the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we're only using a constant amount of space to store the maximum and minimum values.
> - **Optimality proof:** This approach is optimal because it directly identifies the conditions that maximize the expression and only considers the necessary elements (maximum and minimum values) to compute the result, avoiding unnecessary comparisons.

---

### Final Notes

**Learning Points:**
- The importance of identifying key insights that can simplify the problem.
- How to analyze the problem statement to determine the optimal approach.
- The value of considering edge cases and different scenarios to ensure the solution is robust.

**Mistakes to Avoid:**
- Not considering the signs of `a` and `b` and their impact on the solution.
- Failing to recognize that only the maximum and minimum values are needed to maximize the expression.
- Not optimizing the solution to reduce unnecessary comparisons and improve performance.