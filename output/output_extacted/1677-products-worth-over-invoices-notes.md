## Products Worth Over Invoices
**Problem Link:** https://leetcode.com/problems/products-worth-over-invoices/description

**Problem Statement:**
- Input format and constraints: We are given two tables, `Invoices` and `Products`, where `Invoices` contains invoice information with a unique `invoice_id`, and `Products` contains product information with a unique `product_id`. Each invoice can have multiple products, and we need to find the products that have a total value greater than the invoice amount for each invoice.
- Expected output format: We should return a list of `product_id` and `invoice_id` pairs where the total value of the product exceeds the invoice amount.
- Key requirements and edge cases to consider: We need to consider cases where an invoice has multiple products, and we need to handle cases where the total value of a product exceeds the invoice amount.
- Example test cases with explanations: For example, if we have an invoice with `invoice_id` = 1 and `invoice_amount` = 100, and we have two products with `product_id` = 1 and `product_id` = 2, both with a price of 50, we should return the pair `(1, 1)` and `(2, 1)` because the total value of each product exceeds the invoice amount.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating over each invoice and then iterating over each product in the invoice. For each product, we can calculate the total value of the product and check if it exceeds the invoice amount.
- Step-by-step breakdown of the solution:
  1. Iterate over each invoice.
  2. For each invoice, iterate over each product in the invoice.
  3. For each product, calculate the total value of the product.
  4. Check if the total value of the product exceeds the invoice amount.
  5. If it does, add the `product_id` and `invoice_id` pair to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large datasets.

```cpp
SELECT p.product_id, i.invoice_id
FROM Invoices i
JOIN Invoice_items ii ON i.invoice_id = ii.invoice_id
JOIN Products p ON ii.product_id = p.product_id
WHERE ii.quantity * p.price > i.invoice_amount
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of invoices, because we are iterating over each invoice and then iterating over each product in the invoice.
> - **Space Complexity:** $O(n)$, where $n$ is the number of invoices, because we need to store the result list.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to iterate over the invoices and products. The space complexity occurs because we need to store the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query with joins to efficiently retrieve the required data.
- Detailed breakdown of the approach:
  1. Join the `Invoices`, `Invoice_items`, and `Products` tables on the `invoice_id` and `product_id` columns.
  2. Use a WHERE clause to filter the results to only include products where the total value exceeds the invoice amount.
- Proof of optimality: This approach is optimal because it uses a single query to retrieve the required data, which reduces the time complexity to $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over each invoice and product at least once to retrieve the required data.

```cpp
SELECT p.product_id, i.invoice_id
FROM Invoices i
JOIN Invoice_items ii ON i.invoice_id = ii.invoice_id
JOIN Products p ON ii.product_id = p.product_id
WHERE ii.quantity * p.price > i.invoice_amount
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of invoices, because we are using a single query to retrieve the required data.
> - **Space Complexity:** $O(n)$, where $n$ is the number of invoices, because we need to store the result list.
> - **Optimality proof:** The time complexity is optimal because we are using a single query to retrieve the required data. The space complexity is optimal because we only need to store the result list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Joining tables, filtering data using WHERE clauses.
- Problem-solving patterns identified: Using a single query to retrieve required data.
- Optimization techniques learned: Reducing time complexity by using a single query.
- Similar problems to practice: Problems that involve joining tables and filtering data.

**Mistakes to Avoid:**
- Common implementation errors: Using nested loops to iterate over data.
- Edge cases to watch for: Handling cases where an invoice has multiple products.
- Performance pitfalls: Using inefficient queries that result in high time complexity.
- Testing considerations: Testing the query with different datasets to ensure it works correctly.