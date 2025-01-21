## Number of Smooth Descent Periods of a Stock

**Problem Link:** https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description

**Problem Statement:**
- Input: An integer array `prices` where `prices[i]` is the price of the stock on the `i-th` day.
- Output: The number of **smooth descent periods**.
- A smooth descent period is a subarray of `prices` where each element is less than or equal to its previous element.
- Key requirements and edge cases to consider: The input array can be empty, and the smooth descent period can be of any length, including 1.

**Example Test Cases:**
- Example 1: `prices = [3,2,1,4]`, the output is `7`. The smooth descent periods are `[3, 2, 1], [3, 2], [2, 1], [1], [4], [2], [1]`.
- Example 2: `prices = [8,6,7,7]`, the output is `4`. The smooth descent periods are `[8,6], [6], [7], [7]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible subarrays and check if they are smooth descent periods.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, check if it is a smooth descent period by comparing each element with its previous element.
  3. Count the number of smooth descent periods.

```cpp
int getDescentPeriods(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool isDescent = true;
            for (int k = i + 1; k <= j; k++) {
                if (prices[k] > prices[k - 1]) {
                    isDescent = false;
                    break;
                }
            }
            if (isDescent) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the input array. This is because we are generating all possible subarrays and checking each one.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The brute force approach is inefficient because it checks all possible subarrays, resulting in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the length of the current smooth descent period.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to 0, which will store the total number of smooth descent periods.
  2. Initialize a variable `length` to 1, which will store the length of the current smooth descent period.
  3. Iterate through the input array. If the current element is less than or equal to the previous element, increment `length` and update `count` by adding the new `length`.
  4. If the current element is greater than the previous element, reset `length` to 1 and update `count` by adding 1.

```cpp
int getDescentPeriods(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    int length = 1;
    for (int i = 1; i < n; i++) {
        if (prices[i] <= prices[i - 1]) {
            length++;
            count += length;
        } else {
            length = 1;
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are iterating through the input array once.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Optimality proof:** This is the optimal solution because we are only iterating through the input array once and keeping track of the necessary information using a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration.
- Problem-solving patterns identified: Using dynamic programming to keep track of the length of the current smooth descent period.
- Optimization techniques learned: Avoiding unnecessary iterations and using dynamic programming to improve time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not resetting the `length` variable when the current element is greater than the previous element.
- Edge cases to watch for: Handling the case where the input array is empty.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.