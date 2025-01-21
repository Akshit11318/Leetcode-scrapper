## Unpopular Books

**Problem Link:** https://leetcode.com/problems/unpopular-books/description

**Problem Statement:**
- Input format and constraints: Given a table `Books` with columns `id`, `name`, and `borrowed`, where `id` is the unique identifier for each book, `name` is the title of the book, and `borrowed` is the number of times the book has been borrowed. The problem requires finding the names of books that have been borrowed less than twice.
- Expected output format: A list of book names that meet the specified condition, sorted in ascending order.
- Key requirements and edge cases to consider: Handling cases where a book has not been borrowed at all (i.e., `borrowed` equals 0), and ensuring the output is sorted.
- Example test cases with explanations:
  - A book with `borrowed` count of 1 or 0 should be included in the result.
  - A book with `borrowed` count of 2 or more should not be included.
  - The result should be sorted alphabetically by book `name`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each row in the `Books` table, check the `borrowed` count, and if it's less than 2, add the book's `name` to the result list.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the names of unpopular books.
  2. Iterate through each row in the `Books` table.
  3. For each row, check if the `borrowed` count is less than 2.
  4. If the condition is met, add the book's `name` to the result list.
  5. After iterating through all rows, sort the result list alphabetically.
- Why this approach comes to mind first: It directly implements the problem's requirements without considering optimization, making it straightforward but potentially inefficient for large datasets.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Book {
    int id;
    std::string name;
    int borrowed;
};

std::vector<std::string> unpopularBooks(std::vector<Book>& books) {
    std::vector<std::string> unpopular;
    for (const auto& book : books) {
        if (book.borrowed < 2) {
            unpopular.push_back(book.name);
        }
    }
    std::sort(unpopular.begin(), unpopular.end());
    return unpopular;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of books. This is because we potentially iterate through all books once (which is $O(n)$), and then sort the result, which can be $O(n \log n)$ in the worst case.
> - **Space Complexity:** $O(n)$, as in the worst-case scenario (all books are unpopular), we need to store all book names in the result list.
> - **Why these complexities occur:** The iteration through the books list is linear, but the sorting operation at the end can introduce a logarithmic factor, leading to $O(n \log n)$ time complexity. The space complexity is linear because we might need to store all book names if all are unpopular.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single SQL query that filters books based on the `borrowed` count and sorts the result by `name`. This approach is more efficient as it leverages the database's ability to filter and sort data directly, reducing the need for additional processing steps.
- Detailed breakdown of the approach:
  1. Use a SQL query to select the `name` of books from the `Books` table where the `borrowed` count is less than 2.
  2. Sort the result by `name` in ascending order.
- Proof of optimality: This approach is optimal because it minimizes the amount of data that needs to be processed and transferred, by filtering and sorting the data directly in the database.
- Why further optimization is impossible: Given the constraints of the problem (i.e., needing to filter and sort based on specific conditions), this approach is the most direct and efficient way to achieve the desired result.

```sql
SELECT name
FROM Books
WHERE borrowed < 2
ORDER BY name;
```

> Complexity Analysis:
> - **Time Complexity:** The time complexity of this SQL query depends on the database's implementation and indexing. However, assuming proper indexing on the `borrowed` column, the query can achieve a time complexity of $O(n \log n)$ due to the sorting, where $n$ is the number of rows that match the condition. The filtering itself can be $O(n)$, but with indexing, it can be more efficient.
> - **Space Complexity:** $O(n)$, as the database needs to store the result set in memory, which could potentially include all rows from the table if they all meet the condition.
> - **Optimality proof:** This query is optimal because it directly addresses the problem's requirements without unnecessary steps, leveraging the database's capabilities for filtering and sorting, which are typically more efficient than processing the data in an application.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Filtering, sorting, and the importance of leveraging the capabilities of the underlying system (in this case, the database) for efficiency.
- Problem-solving patterns identified: Directly addressing the problem's requirements and minimizing unnecessary processing steps.
- Optimization techniques learned: Using indexing for faster filtering and sorting.
- Similar problems to practice: Other database query optimization problems that involve filtering and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Not properly validating the input or handling edge cases (e.g., an empty table).
- Edge cases to watch for: Handling cases where the table is empty or where all books have been borrowed at least twice.
- Performance pitfalls: Not using indexing on columns used in the WHERE clause, which can significantly slow down the query.
- Testing considerations: Ensure to test with various datasets, including edge cases, to verify the correctness and efficiency of the solution.