## Total Sales Amount by Year

**Problem Link:** https://leetcode.com/problems/total-sales-amount-by-year/description

**Problem Statement:**
- Given a table `Sales` containing columns `sale_id`, `product_id`, `sale_date`, and `sale_amount`, find the total sales amount for each year.
- The `sale_date` column is of type `date`, and we need to extract the year from it.
- The expected output should have two columns: `year` and `total_amount`.
- Key requirements include handling null or missing values and ensuring accurate date parsing.

**Example Test Cases:**
- A table with sales data for multiple years, including sales with the same product_id on different dates.
- A table with no sales data for a particular year.
- A table with sales data for only one year.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each row in the `Sales` table, parsing the `sale_date` to extract the year, and summing up the `sale_amount` for each year.
- This approach comes to mind first because it directly addresses the problem statement without considering optimization.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

struct Sale {
    int sale_id;
    int product_id;
    std::string sale_date;
    int sale_amount;
};

std::vector<std::pair<int, int>> totalSalesAmountByYear(const std::vector<Sale>& sales) {
    std::map<int, int> yearSales;
    for (const auto& sale : sales) {
        std::istringstream iss(sale.sale_date);
        std::string token;
        std::getline(iss, token, '-');
        int year = std::stoi(token);
        
        if (yearSales.find(year) != yearSales.end()) {
            yearSales[year] += sale.sale_amount;
        } else {
            yearSales[year] = sale.sale_amount;
        }
    }
    
    std::vector<std::pair<int, int>> result;
    for (const auto& pair : yearSales) {
        result.push_back(pair);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Sales` table, because we iterate over each row once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might have a separate entry for each sale in the `yearSales` map.
> - **Why these complexities occur:** The iteration over each sale and the potential for each sale to contribute to a unique year in the map lead to these complexities.

### Optimal Approach (Required)

**Explanation:**
- The key insight for the optimal solution involves using SQL to directly query the database, leveraging its built-in functions for date manipulation and aggregation.
- This approach is optimal because databases are designed to efficiently handle such queries, and using SQL allows for the database to optimize the query plan.

```sql
SELECT 
    YEAR(sale_date) AS year,
    SUM(sale_amount) AS total_amount
FROM 
    Sales
GROUP BY 
    YEAR(sale_date)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `Sales` table, because the database will likely use an index or sorting to group the sales by year.
> - **Space Complexity:** $O(n)$, as the database needs to store the intermediate results of the grouping and summing.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input data once, and the grouping operation inherently requires some form of sorting or indexing, leading to the $O(n \log n)$ time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include data aggregation and date manipulation.
- Problem-solving patterns identified include the use of maps for grouping data and the importance of leveraging database capabilities for efficient data processing.
- Optimization techniques learned include avoiding unnecessary iterations and utilizing built-in database functions.

**Mistakes to Avoid:**
- Common implementation errors include incorrect date parsing and failure to handle null or missing values.
- Edge cases to watch for include sales data spanning multiple years and ensuring accurate aggregation of sales amounts.
- Performance pitfalls include not using indexes or optimized database queries, leading to slow performance on large datasets.
- Testing considerations include verifying the correctness of date extraction and sales amount aggregation across different years and products.