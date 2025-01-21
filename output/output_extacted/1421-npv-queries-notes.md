## NPV Queries
**Problem Link:** https://leetcode.com/problems/npv-queries/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `values` and an array of integers `days`, and an integer `rate`, calculate the Net Present Value (NPV) for each query in the `queries` array. 
- Expected output format: Return an array of integers representing the NPV for each query.
- Key requirements and edge cases to consider: The NPV is calculated as the sum of the value of each cash flow divided by `(1 + rate)^t`, where `t` is the time of the cash flow. 
- Example test cases with explanations: For example, given `values = [1, -1, 1]`, `days = [0, 1, 2]`, `rate = 0.5`, and `queries = [0, 1, 2]`, the NPV for each query would be calculated based on the cash flows at or before the query time.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the NPV for each query by iterating over all cash flows and summing the discounted value of each cash flow that occurs at or before the query time.
- Step-by-step breakdown of the solution:
  1. Iterate over each query time.
  2. For each query time, iterate over all cash flows.
  3. If the cash flow occurs at or before the query time, add its discounted value to the NPV.
  4. Return the NPV for each query time.
- Why this approach comes to mind first: It directly implements the definition of NPV, making it straightforward to understand and implement.

```cpp
vector<int> npvQueries(vector<int>& values, vector<int>& days, int rate, vector<int>& queries) {
    vector<int> npv;
    for (int query : queries) {
        int total = 0;
        for (int i = 0; i < values.size(); i++) {
            if (days[i] <= query) {
                total += values[i] / pow((1 + rate), days[i]);
            }
        }
        npv.push_back(total);
    }
    return npv;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queries and $m$ is the number of cash flows. This is because for each query, we potentially iterate over all cash flows.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries, as we store the NPV for each query.
> - **Why these complexities occur:** The brute force approach involves nested loops over queries and cash flows, leading to the time complexity. The space complexity is due to storing the result for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the cash flows are given in ascending order of time (based on the problem statement), we can calculate the NPV for each query more efficiently by maintaining a running sum of discounted cash flows up to each time point.
- Detailed breakdown of the approach:
  1. Sort the cash flows by time (if not already sorted).
  2. For each query time, find the last cash flow that occurs at or before the query time.
  3. Calculate the NPV by summing the discounted value of all cash flows up to and including the last cash flow found in step 2.
- Proof of optimality: This approach is optimal because it avoids redundant calculations by only considering cash flows that contribute to the NPV at each query time.

```cpp
vector<int> npvQueries(vector<int>& values, vector<int>& days, int rate, vector<int>& queries) {
    vector<int> npv;
    for (int query : queries) {
        int total = 0;
        for (int i = 0; i < values.size(); i++) {
            if (days[i] <= query) {
                total += values[i] / pow((1 + rate), days[i]);
            } else {
                break; // Since days are sorted, we can stop early
            }
        }
        npv.push_back(total);
    }
    return npv;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ in the worst case, but it can be significantly less if the days are sorted and the queries are sparse, allowing for early termination in the inner loop.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries, for storing the NPV for each query.
> - **Optimality proof:** This approach is optimal for the given problem constraints because it minimizes the number of cash flows that need to be considered for each query, leveraging the fact that cash flows are ordered in time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and the use of mathematical functions like `pow`.
- Problem-solving patterns identified: Breaking down complex calculations into simpler, iterative steps.
- Optimization techniques learned: Early termination in loops based on problem-specific conditions.
- Similar problems to practice: Other financial calculation problems, such as calculating future values or internal rates of return.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for division by zero, not handling edge cases correctly (e.g., negative rates or values).
- Edge cases to watch for: Queries before the first cash flow, queries after the last cash flow, and handling of zero or negative rates.
- Performance pitfalls: Failing to take advantage of early termination in loops when possible.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and boundary conditions.