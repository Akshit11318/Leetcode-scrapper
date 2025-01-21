## Friend Requests I: Overall Acceptance Rate
**Problem Link:** https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/description

**Problem Statement:**
- Input: A table `acceptance` with columns `id`, `like_id`, `dislike_id`, and `decision_date`.
- Constraints: `id` is the primary key, and `decision_date` is in the format 'YYYY-MM-DD'.
- Expected Output: The overall acceptance rate, which is the total number of accepted friend requests divided by the total number of requests.
- Key Requirements: Calculate the acceptance rate for the entire table.
- Example Test Cases:
  - If there are 10 requests and 5 are accepted, the acceptance rate is 0.5.
  - If there are no requests, the acceptance rate is 0.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each row in the table and count the total number of requests and the number of accepted requests.
- Then, we can calculate the acceptance rate by dividing the number of accepted requests by the total number of requests.

```cpp
double calculateAcceptanceRate(vector<vector<int>>& acceptance) {
    int totalRequests = 0;
    int acceptedRequests = 0;
    
    for (const auto& request : acceptance) {
        totalRequests++;
        if (request[2] == 1) { // assuming decision_date is not used in this problem
            acceptedRequests++;
        }
    }
    
    if (totalRequests == 0) {
        return 0.0;
    }
    
    return static_cast<double>(acceptedRequests) / totalRequests;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because we iterate over each row once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts.
> - **Why these complexities occur:** The time complexity is linear because we need to examine each row to count the requests. The space complexity is constant because we only need a few variables to store the counts.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we can use a single SQL query to calculate the acceptance rate.
- We can use the `COUNT` function to count the total number of requests and the number of accepted requests.
- Then, we can use the `AVG` function to calculate the acceptance rate.

```cpp
SELECT 
    IFNULL(ROUND(SUM(CASE WHEN decision = 'accept' THEN 1 ELSE 0 END) / COUNT(*), 2), 0.00) 
    AS accept_rate
FROM 
    acceptance;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because the database needs to scan each row to calculate the counts.
> - **Space Complexity:** $O(1)$, as the database uses a constant amount of space to store the intermediate results.
> - **Optimality proof:** This is the optimal approach because we can calculate the acceptance rate in a single pass over the data. Further optimization is impossible because we need to examine each row at least once to calculate the counts.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: counting, iteration, and calculation of ratios.
- Problem-solving patterns identified: using a single pass over the data to calculate the acceptance rate.
- Optimization techniques learned: using SQL queries to simplify the calculation.
- Similar problems to practice: calculating other types of rates or ratios from a dataset.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where there are no requests, not using a robust method to calculate the ratio.
- Edge cases to watch for: an empty table, a table with only one row.
- Performance pitfalls: using a non-optimized algorithm that scans the table multiple times.
- Testing considerations: testing the function with different inputs, including edge cases.