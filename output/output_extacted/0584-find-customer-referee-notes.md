## Find Customer Referee
**Problem Link:** https://leetcode.com/problems/find-customer-referee/description

**Problem Statement:**
- Input format and constraints: You are given a table `customer` with columns `id`, `name`, and `referee_id`.
- Expected output format: Return a list of `name` of customers where `referee_id` equals 2.
- Key requirements and edge cases to consider: 
  - Handling customers with no referee_id (NULL).
  - Handling customers with referee_id not equal to 2.
- Example test cases with explanations: 
  - If there are no customers with referee_id = 2, return an empty list.
  - If all customers have referee_id = 2, return a list of all customer names.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each customer in the table and check if their referee_id equals 2.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store customer names.
  2. Iterate over each customer in the table.
  3. Check if the customer's referee_id equals 2.
  4. If it does, add their name to the list.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Customer {
    int id;
    string name;
    int referee_id;
};

vector<string> findCustomerReferee(vector<Customer>& customers) {
    vector<string> result;
    for (Customer customer : customers) {
        if (customer.referee_id == 2) {
            result.push_back(customer.name);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of customers, because we are iterating over each customer once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store the names of all customers.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each customer. The space complexity is also linear because we are storing the names of customers in a list.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a simple SQL query that directly filters the customers based on the referee_id.
- Detailed breakdown of the approach:
  1. Write a SQL query to select the names of customers where referee_id equals 2.
- Proof of optimality: This approach is optimal because it directly addresses the problem statement and does not require any unnecessary operations.
- Why further optimization is impossible: This approach is already optimal because it uses a single, efficient database query.

```sql
SELECT name 
FROM customer 
WHERE referee_id = 2;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because the database needs to scan the table to find the matching rows.
> - **Space Complexity:** $O(1)$, because the database does not need to use any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it uses a single, efficient database query that directly addresses the problem statement.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Database queries, filtering data.
- Problem-solving patterns identified: Directly addressing the problem statement, using efficient data structures and algorithms.
- Optimization techniques learned: Using efficient database queries to reduce the number of operations.
- Similar problems to practice: Other database query problems, such as filtering data or performing aggregations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for NULL values, not handling edge cases.
- Edge cases to watch for: Customers with no referee_id, customers with referee_id not equal to 2.
- Performance pitfalls: Using inefficient database queries, not indexing the table.
- Testing considerations: Testing the query with different inputs, testing the query with edge cases.