## Find Products with Three Consecutive Digits
**Problem Link:** https://leetcode.com/problems/find-products-with-three-consecutive-digits/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `product` as input, which represents the product name. The task is to find all products that contain at least one sequence of three consecutive digits.
- Expected output format: Return a list of product names that meet the specified condition.
- Key requirements and edge cases to consider: The product name can contain letters, digits, and other characters. The sequence of three consecutive digits can appear anywhere in the product name.
- Example test cases with explanations:
  - If the input is `["123", "abc", "456def", "789ghi"]`, the output should be `["123", "456def", "789ghi"]` because these product names contain at least one sequence of three consecutive digits.
  - If the input is `["a1b2c3", "123a", "abc123"]`, the output should be `["a1b2c3", "123a", "abc123"]` because these product names contain at least one sequence of three consecutive digits.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible sequence of three characters in the product name to see if it contains three consecutive digits.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in the product name.
  2. For each character, check if it is a digit and if the next two characters are also digits.
  3. If a sequence of three consecutive digits is found, add the product name to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large inputs.

```cpp
vector<string> findProducts(vector<string>& products) {
    vector<string> result;
    for (const auto& product : products) {
        bool found = false;
        for (int i = 0; i < product.size() - 2; ++i) {
            if (isdigit(product[i]) && isdigit(product[i + 1]) && isdigit(product[i + 2])) {
                if (product[i + 1] - product[i] == 1 && product[i + 2] - product[i + 1] == 1) {
                    found = true;
                    break;
                }
            }
        }
        if (found) {
            result.push_back(product);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of products and $m$ is the maximum length of a product name. This is because we are iterating over each character in each product name.
> - **Space Complexity:** $O(n)$, where $n$ is the number of products. This is because we are storing the result in a vector.
> - **Why these complexities occur:** The time complexity is high because we are using nested loops to check every possible sequence of three characters in each product name. The space complexity is moderate because we are storing the result in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible sequence of three characters, we can use a single loop to iterate over each character in the product name and check if it is the start of a sequence of three consecutive digits.
- Detailed breakdown of the approach:
  1. Iterate over each character in the product name.
  2. For each character, check if it is a digit and if the next two characters are also digits.
  3. If a sequence of three consecutive digits is found, add the product name to the result list and break the loop.
- Proof of optimality: This approach is optimal because it only requires a single loop to check each product name, resulting in a significant reduction in time complexity.

```cpp
vector<string> findProducts(vector<string>& products) {
    vector<string> result;
    for (const auto& product : products) {
        bool found = false;
        for (int i = 0; i < product.size() - 2; ++i) {
            if (isdigit(product[i]) && isdigit(product[i + 1]) && isdigit(product[i + 2])) {
                if (product[i + 1] - product[i] == 1 && product[i + 2] - product[i + 1] == 1) {
                    found = true;
                    break;
                }
            }
        }
        if (found) {
            result.push_back(product);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of products and $m$ is the maximum length of a product name. This is because we are still iterating over each character in each product name.
> - **Space Complexity:** $O(n)$, where $n$ is the number of products. This is because we are storing the result in a vector.
> - **Optimality proof:** Although the time complexity remains the same as the brute force approach, the optimal approach is more efficient in practice because it breaks the loop as soon as a sequence of three consecutive digits is found, reducing the number of unnecessary iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of optimizing loops and reducing unnecessary iterations.
- Problem-solving patterns identified: The problem requires a careful analysis of the input and output formats, as well as the key requirements and edge cases.
- Optimization techniques learned: The problem teaches the importance of breaking loops as soon as possible and reducing the number of unnecessary iterations.
- Similar problems to practice: Other problems that involve optimizing loops and reducing unnecessary iterations, such as finding the first occurrence of a substring or the first occurrence of a pattern in a string.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as an empty product name or a product name with less than three characters.
- Edge cases to watch for: Product names with non-ASCII characters, product names with digits that are not consecutive, and product names with digits that are not in the correct order.
- Performance pitfalls: Failing to optimize loops and reduce unnecessary iterations, resulting in a high time complexity.
- Testing considerations: Testing the function with a variety of input cases, including edge cases and boundary cases, to ensure that it produces the correct output.