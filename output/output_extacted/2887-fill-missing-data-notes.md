## Fill Missing Data
**Problem Link:** https://leetcode.com/problems/fill-missing-data/description

**Problem Statement:**
- Input format: A table `Customers` with columns `customer_id`, `product_key`, `purchase_date`.
- Constraints: Primary key is `(customer_id, product_key)`.
- Expected output format: A table with all `customer_id` and `product_key` combinations from the input, where missing rows have `purchase_date` set to `NULL`.
- Key requirements and edge cases to consider:
  - A customer can have multiple products.
  - A product can be owned by multiple customers.
  - There are no duplicate rows in the input table.
- Example test cases with explanations:
  - Input: `Customers` table with some customer-product combinations.
  - Output: A table with all possible customer-product combinations, filling in missing rows with `NULL` purchase dates.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of `customer_id` and `product_key`, then left join this with the input table.
- Step-by-step breakdown of the solution:
  1. Get all unique `customer_id` values.
  2. Get all unique `product_key` values.
  3. Generate a Cartesian product of these two sets to get all possible combinations.
  4. Left join this Cartesian product with the original table on `customer_id` and `product_key`.
- Why this approach comes to mind first: It directly addresses the problem by generating all possible combinations and then filling in the missing data.

```cpp
SELECT c1.customer_id, c2.product_key, c3.purchase_date
FROM 
    (SELECT DISTINCT customer_id FROM Customers) c1
CROSS JOIN 
    (SELECT DISTINCT product_key FROM Customers) c2
LEFT JOIN 
    Customers c3 ON c1.customer_id = c3.customer_id AND c2.product_key = c3.product_key
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of unique `customer_id` values and $m$ is the number of unique `product_key` values. This is because we are generating a Cartesian product.
> - **Space Complexity:** $O(n \times m)$ for storing the Cartesian product and the result.
> - **Why these complexities occur:** The brute force approach requires generating all possible combinations of `customer_id` and `product_key`, which leads to a time and space complexity proportional to the product of the number of unique values of each.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach because the problem inherently requires generating all possible combinations of `customer_id` and `product_key`.
- Detailed breakdown of the approach: Identical to the brute force approach.
- Proof of optimality: Since we must generate all possible combinations of `customer_id` and `product_key` to fill in the missing data, any solution must have at least the complexity of generating this Cartesian product, making the brute force approach optimal for this problem.
- Why further optimization is impossible: The nature of the problem requires examining all possible combinations, so any algorithm must at least match the complexity of generating these combinations.

```cpp
SELECT c1.customer_id, c2.product_key, c3.purchase_date
FROM 
    (SELECT DISTINCT customer_id FROM Customers) c1
CROSS JOIN 
    (SELECT DISTINCT product_key FROM Customers) c2
LEFT JOIN 
    Customers c3 ON c1.customer_id = c3.customer_id AND c2.product_key = c3.product_key
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of unique `customer_id` values and $m$ is the number of unique `product_key` values.
> - **Space Complexity:** $O(n \times m)$ for storing the Cartesian product and the result.
> - **Optimality proof:** This approach is optimal because it directly generates all necessary combinations without any redundant operations, achieving the minimum complexity required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Cartesian product, left join.
- Problem-solving patterns identified: Generating all possible combinations to fill in missing data.
- Optimization techniques learned: Recognizing when a brute force approach is optimal due to the nature of the problem.
- Similar problems to practice: Other problems involving generating combinations or filling in missing data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly joining tables or missing unique values.
- Edge cases to watch for: Handling `NULL` values, ensuring primary key uniqueness.
- Performance pitfalls: Failing to recognize when a brute force approach is necessary and optimal.
- Testing considerations: Ensuring all possible combinations are correctly generated and missing data is properly filled in.