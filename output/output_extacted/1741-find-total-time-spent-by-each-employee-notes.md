## Find Total Time Spent by Each Employee

**Problem Link:** https://leetcode.com/problems/find-total-time-spent-by-each-employee/description

**Problem Statement:**
- Input format and constraints: The problem takes a table `activity` with columns `id`, `employee_id`, and `minutes` as input. The `id` is unique, and `employee_id` and `minutes` are integers.
- Expected output format: The output should be a table with columns `employee_id` and `total_time` where `total_time` is the sum of `minutes` for each `employee_id`.
- Key requirements and edge cases to consider: The problem requires calculating the total time spent by each employee based on the `minutes` column in the `activity` table. Edge cases include handling employees with no activity or those with multiple activities.
- Example test cases with explanations:
  - Test case 1: An employee with a single activity.
  - Test case 2: An employee with multiple activities.
  - Test case 3: An employee with no activities.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each row in the `activity` table and summing up the `minutes` for each `employee_id`.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the total time for each employee.
  2. Iterate over each row in the `activity` table.
  3. For each row, check if the `employee_id` is already in the dictionary. If it is, add the `minutes` to the existing total. If not, create a new entry in the dictionary with the `minutes` as the total.
  4. After iterating over all rows, create a result table with the `employee_id` and `total_time` columns.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural first choice.

```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

struct Activity {
    int id;
    int employee_id;
    int minutes;
};

void findTotalTimeSpentByEachEmployee(Activity activities[], int size) {
    unordered_map<int, int> totalTimeMap;

    for (int i = 0; i < size; i++) {
        int employee_id = activities[i].employee_id;
        int minutes = activities[i].minutes;

        if (totalTimeMap.find(employee_id) != totalTimeMap.end()) {
            totalTimeMap[employee_id] += minutes;
        } else {
            totalTimeMap[employee_id] = minutes;
        }
    }

    for (auto& pair : totalTimeMap) {
        cout << "Employee ID: " << pair.first << ", Total Time: " << pair.second << endl;
    }
}

int main() {
    Activity activities[] = {
        {1, 1, 30},
        {2, 1, 60},
        {3, 2, 30},
        {4, 1, 120}
    };

    int size = sizeof(activities) / sizeof(activities[0]);

    findTotalTimeSpentByEachEmployee(activities, size);

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `activity` table, because we are iterating over each row once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique `employee_id` values, because we are storing the total time for each employee in a dictionary.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over each row in the `activity` table once. The space complexity is dependent on the number of unique `employee_id` values because we are storing the total time for each employee in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a SQL query to calculate the total time for each employee. This is because the problem is essentially asking for a group-by operation, which is a fundamental operation in SQL.
- Detailed breakdown of the approach:
  1. Write a SQL query that selects the `employee_id` and the sum of `minutes` as `total_time` from the `activity` table.
  2. Group the results by `employee_id` to get the total time for each employee.
- Proof of optimality: This approach is optimal because it directly uses the capabilities of the database to perform the calculation, which is more efficient than trying to load the data into memory and perform the calculation manually.
- Why further optimization is impossible: This approach is already optimal because it uses the most efficient method available for performing the calculation.

```sql
SELECT 
    employee_id, 
    SUM(minutes) AS total_time
FROM 
    activity
GROUP BY 
    employee_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `activity` table, because the database needs to sort the data before grouping it.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `activity` table, because the database needs to store the intermediate results.
> - **Optimality proof:** This approach is optimal because it directly uses the capabilities of the database to perform the calculation, which is more efficient than trying to load the data into memory and perform the calculation manually.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Group-by operations, SQL queries.
- Problem-solving patterns identified: Using the most efficient method available for performing a calculation.
- Optimization techniques learned: Using database capabilities to perform calculations.
- Similar problems to practice: Other problems that involve group-by operations or using database capabilities.

**Mistakes to Avoid:**
- Common implementation errors: Not grouping the results correctly, not using the most efficient method available.
- Edge cases to watch for: Handling employees with no activities or those with multiple activities.
- Performance pitfalls: Trying to load the data into memory and perform the calculation manually, which can be slower than using database capabilities.
- Testing considerations: Testing the query with different inputs to ensure it produces the correct results.