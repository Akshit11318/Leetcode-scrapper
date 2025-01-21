## Sum of Subarray Minimums
**Problem Link:** https://leetcode.com/problems/sum-of-subarray-minimums/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `arr` and an integer `k`, find the sum of all subarray minimums.
- Expected output format: The sum of all subarray minimums as an integer.
- Key requirements and edge cases to consider: The array can contain duplicate elements and negative numbers.
- Example test cases with explanations:
  - `arr = [3, 1, 2, 4]`: The sum of all subarray minimums is `1 + 1 + 1 + 2 + 3 + 1 + 1 + 2 + 3 + 4 = 17`.
  - `arr = [11, 81, 94, 43, 3]`: The sum of all subarray minimums is `11 + 11 + 11 + 11 + 81 + 3 + 3 + 3 + 94 + 43 + 3 + 3 + 3 + 3 = 263`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible subarrays and find the minimum element in each subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, find the minimum element.
  3. Add the minimum element to the total sum.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it has a high time complexity due to the generation of all possible subarrays.

```cpp
int sumSubarrayMins(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int minVal = INT_MAX;
            for (int k = i; k <= j; k++) {
                minVal = min(minVal, arr[k]);
            }
            sum += minVal;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are generating all possible subarrays and finding the minimum element in each subarray.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The high time complexity occurs due to the nested loops used to generate all possible subarrays and find the minimum element in each subarray.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack-based approach to find the sum of all subarray minimums.
- Detailed breakdown of the approach:
  1. Initialize an empty stack and a variable `sum` to store the sum of all subarray minimums.
  2. Iterate through the input array, and for each element, pop all elements from the stack that are greater than or equal to the current element.
  3. For each popped element, calculate the contribution to the sum of all subarray minimums and add it to the `sum` variable.
  4. Push the current element onto the stack.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we need to at least read the input array once.

```cpp
int sumSubarrayMins(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    stack<pair<int, int>> st; // (value, count)
    for (int i = 0; i <= n; i++) {
        while (!st.empty() && (i == n || arr[i] <= st.top().first)) {
            int val = st.top().first;
            int count = st.top().second;
            st.pop();
            int left = st.empty() ? -1 : st.top().second;
            int right = i;
            int total = (count + left) * (right - count) * val;
            sum += total;
        }
        if (i < n) {
            if (st.empty()) {
                st.push({arr[i], i});
            } else if (st.top().first == arr[i]) {
                st.top().second = i;
            } else {
                st.push({arr[i], i});
            }
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are iterating through the input array once and performing constant-time operations for each element.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are using a stack to store the elements of the input array.
> - **Optimality proof:** This approach is optimal because we need to at least read the input array once, and we are doing so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack-based approach, contribution calculation.
- Problem-solving patterns identified: Using a stack to find the sum of all subarray minimums.
- Optimization techniques learned: Reducing the time complexity from $O(n^3)$ to $O(n)$.
- Similar problems to practice: Finding the sum of all subarray maximums, finding the sum of all subarray averages.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the contribution to the sum of all subarray minimums.
- Edge cases to watch for: Handling the case where the input array is empty.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the solution with different input arrays, including edge cases.