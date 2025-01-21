## Sales by Day of the Week

**Problem Link:** https://leetcode.com/problems/sales-by-day-of-the-week/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of `items` and `items` is a table with columns `item_id`, `item_category`, `sell_date`, and `quantity`. 
- Expected output format: The output should be the total sales for each day of the week, with the day of the week in the format 'Monday', 'Tuesday', etc.
- Key requirements and edge cases to consider: The problem requires us to calculate the total sales for each day of the week, and we need to handle the case where there are no sales on a particular day.
- Example test cases with explanations: For example, if we have the following `items` table:

| item_id | item_category | sell_date | quantity |
| --- | --- | --- | --- |
| 1 | A | 2022-01-01 | 10 |
| 2 | B | 2022-01-02 | 20 |
| 3 | A | 2022-01-03 | 30 |

The output should be the total sales for each day of the week.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to iterate over each row in the `items` table, calculate the day of the week for the `sell_date`, and then add the `quantity` to the total sales for that day.
- Step-by-step breakdown of the solution:
  1. Initialize a dictionary to store the total sales for each day of the week.
  2. Iterate over each row in the `items` table.
  3. For each row, calculate the day of the week for the `sell_date`.
  4. Add the `quantity` to the total sales for that day.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to calculate the total sales for each day of the week.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <ctime>

struct Item {
    int item_id;
    std::string item_category;
    std::string sell_date;
    int quantity;
};

std::vector<std::string> days_of_week = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

std::string get_day_of_week(const std::string& date) {
    tm time = {};
    strptime(date.c_str(), "%Y-%m-%d", &time);
    return days_of_week[time.tm_wday];
}

void brute_force(const std::vector<Item>& items) {
    std::map<std::string, int> sales;
    for (const auto& item : items) {
        std::string day_of_week = get_day_of_week(item.sell_date);
        if (sales.find(day_of_week) != sales.end()) {
            sales[day_of_week] += item.quantity;
        } else {
            sales[day_of_week] = item.quantity;
        }
    }
    for (const auto& pair : sales) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `items` table. This is because we need to iterate over each row in the table.
> - **Space Complexity:** $O(1)$ because we only need to store the total sales for each day of the week, and there are only 7 days in a week.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over each row in the table, and the space complexity occurs because we only need to store a fixed amount of data.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can use a `GROUP BY` statement in SQL to group the rows by the day of the week and calculate the total sales for each day.
- Detailed breakdown of the approach:
  1. Use a `GROUP BY` statement to group the rows by the day of the week.
  2. Use the `SUM` function to calculate the total sales for each day.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data, and it uses the most efficient data structures and algorithms available.
- Why further optimization is impossible: Further optimization is impossible because this approach already uses the most efficient data structures and algorithms available.

```sql
SELECT 
    CASE 
        WHEN DAYOFWEEK(sell_date) = 1 THEN 'Sunday'
        WHEN DAYOFWEEK(sell_date) = 2 THEN 'Monday'
        WHEN DAYOFWEEK(sell_date) = 3 THEN 'Tuesday'
        WHEN DAYOFWEEK(sell_date) = 4 THEN 'Wednesday'
        WHEN DAYOFWEEK(sell_date) = 5 THEN 'Thursday'
        WHEN DAYOFWEEK(sell_date) = 6 THEN 'Friday'
        WHEN DAYOFWEEK(sell_date) = 7 THEN 'Saturday'
    END AS day_of_week,
    SUM(quantity) AS total_sales
FROM 
    items
GROUP BY 
    DAYOFWEEK(sell_date)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `items` table. This is because we need to iterate over each row in the table.
> - **Space Complexity:** $O(1)$ because we only need to store the total sales for each day of the week, and there are only 7 days in a week.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the data, and it uses the most efficient data structures and algorithms available.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated is the use of a `GROUP BY` statement in SQL to group rows by a common attribute and calculate aggregate values.
- Problem-solving patterns identified: The problem-solving pattern identified is the use of a single pass over the data to calculate aggregate values.
- Optimization techniques learned: The optimization technique learned is the use of efficient data structures and algorithms to minimize the time and space complexity of the solution.
- Similar problems to practice: Similar problems to practice include other SQL problems that require the use of aggregate functions and `GROUP BY` statements.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a subquery to calculate the aggregate values, which can be less efficient than using a `GROUP BY` statement.
- Edge cases to watch for: An edge case to watch for is when there are no sales on a particular day, in which case the `SUM` function will return `NULL`.
- Performance pitfalls: A performance pitfall is to use a `SELECT \*` statement, which can retrieve unnecessary columns and reduce performance.
- Testing considerations: A testing consideration is to test the solution with a large dataset to ensure that it performs well and does not run out of memory.