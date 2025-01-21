## Generate the Invoice
**Problem Link:** https://leetcode.com/problems/generate-the-invoice/description

**Problem Statement:**
- Input format and constraints: The problem takes in a `name` and a list of `items` with their respective `prices`.
- Expected output format: The function should return a formatted invoice as a string.
- Key requirements and edge cases to consider: The invoice should include the `name`, a list of `items` and their `prices`, and a `total` cost.
- Example test cases with explanations:
    - Test case 1: `name = "John", items = ["Item1", "Item2"], prices = [10, 20]`. Expected output: `Invoice for John\nItem1: 10\nItem2: 20\nTotal: 30`.
    - Test case 2: `name = "Jane", items = [], prices = []`. Expected output: `Invoice for Jane\nTotal: 0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the `items` and `prices` lists, formatting each item and its price, and then calculating the total cost.
- Step-by-step breakdown of the solution:
    1. Initialize an empty string `invoice` to store the formatted invoice.
    2. Add the `name` to the `invoice` string.
    3. Iterate over the `items` and `prices` lists, adding each item and its price to the `invoice` string.
    4. Calculate the total cost by summing up all the prices.
    5. Add the total cost to the `invoice` string.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural first thought.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::string generateInvoice(const std::string& name, const std::vector<std::string>& items, const std::vector<int>& prices) {
    std::string invoice = "Invoice for " + name + "\n";
    int total = 0;
    for (int i = 0; i < items.size(); i++) {
        invoice += items[i] + ": " + std::to_string(prices[i]) + "\n";
        total += prices[i];
    }
    invoice += "Total: " + std::to_string(total);
    return invoice;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of items. This is because we iterate over the `items` and `prices` lists once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of items. This is because we store the formatted invoice in a string, which can grow up to $n$ items.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the lists, and the space complexity occurs because we store the formatted invoice in a string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `std::stringstream` to efficiently build the formatted invoice.
- Detailed breakdown of the approach:
    1. Initialize a `std::stringstream` object `invoice` to store the formatted invoice.
    2. Add the `name` to the `invoice` stream.
    3. Iterate over the `items` and `prices` lists, adding each item and its price to the `invoice` stream.
    4. Calculate the total cost by summing up all the prices.
    5. Add the total cost to the `invoice` stream.
- Proof of optimality: This approach is optimal because it uses a `std::stringstream` to efficiently build the formatted invoice, reducing the number of string concatenations and improving performance.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

std::string generateInvoice(const std::string& name, const std::vector<std::string>& items, const std::vector<int>& prices) {
    std::stringstream invoice;
    invoice << "Invoice for " << name << "\n";
    int total = 0;
    for (int i = 0; i < items.size(); i++) {
        invoice << items[i] << ": " << prices[i] << "\n";
        total += prices[i];
    }
    invoice << "Total: " << total;
    return invoice.str();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of items. This is because we iterate over the `items` and `prices` lists once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of items. This is because we store the formatted invoice in a `std::stringstream`, which can grow up to $n$ items.
> - **Optimality proof:** This approach is optimal because it uses a `std::stringstream` to efficiently build the formatted invoice, reducing the number of string concatenations and improving performance.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string formatting, and total calculation.
- Problem-solving patterns identified: Using a `std::stringstream` to efficiently build a formatted string.
- Optimization techniques learned: Reducing the number of string concatenations using a `std::stringstream`.
- Similar problems to practice: Generating a formatted report or a table.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty input lists, not handling invalid input.
- Edge cases to watch for: Empty input lists, invalid input.
- Performance pitfalls: Using string concatenation instead of a `std::stringstream`.
- Testing considerations: Test with different input sizes, test with empty input lists, test with invalid input.