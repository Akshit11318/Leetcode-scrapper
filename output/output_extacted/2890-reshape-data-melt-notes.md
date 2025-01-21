## Reshape Data Melt
**Problem Link:** https://leetcode.com/problems/reshape-data-melt/description

**Problem Statement:**
- Input format and constraints: The input is a table with columns `id`, `name`, `attribute`, and `value`. The table contains `m` rows and `n` columns.
- Expected output format: The output should be a table with columns `id`, `name`, and `attribute_value` where `attribute_value` is a JSON object containing the melted attributes.
- Key requirements and edge cases to consider: Handle duplicate `id` and `name` pairs, and ensure the `attribute_value` JSON object is correctly formatted.
- Example test cases with explanations:
  - Test case 1: Input table with unique `id` and `name` pairs, and a single attribute.
  - Test case 2: Input table with duplicate `id` and `name` pairs, and multiple attributes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each row in the input table, and for each row, iterate over the `attribute` and `value` columns.
- Step-by-step breakdown of the solution:
  1. Initialize an empty map to store the melted data.
  2. Iterate over each row in the input table.
  3. For each row, get the `id`, `name`, `attribute`, and `value`.
  4. Use the `id` and `name` as a key in the map, and append the `attribute` and `value` to the corresponding JSON object.
  5. Finally, construct the output table from the map.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly implements the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>

struct Row {
    int id;
    std::string name;
    std::string attribute;
    std::string value;
};

std::vector<std::map<std::string, std::string>> bruteForce(std::vector<Row>& rows) {
    std::map<std::pair<int, std::string>, std::map<std::string, std::string>> meltedData;
    
    for (const auto& row : rows) {
        auto key = std::make_pair(row.id, row.name);
        meltedData[key][row.attribute] = row.value;
    }
    
    std::vector<std::map<std::string, std::string>> result;
    for (const auto& pair : meltedData) {
        std::map<std::string, std::string> row;
        row["id"] = std::to_string(pair.first.first);
        row["name"] = pair.first.second;
        row["attribute_value"] = "{}"; // Initialize with an empty JSON object
        for (const auto& attribute : pair.second) {
            row["attribute_value"] += "\"" + attribute.first + "\":\"" + attribute.second + "\",";
        }
        row["attribute_value"].pop_back(); // Remove the trailing comma
        row["attribute_value"] = "{" + row["attribute_value"] + "}";
        result.push_back(row);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of rows and $n$ is the number of attributes.
> - **Space Complexity:** $O(m \cdot n)$ for storing the melted data.
> - **Why these complexities occur:** The solution iterates over each row and attribute, resulting in a time complexity of $O(m \cdot n)$. The space complexity is also $O(m \cdot n)$ because in the worst case, each row and attribute is stored in the melted data map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `std::map` to store the melted data, where the key is a pair of `id` and `name`, and the value is another `std::map` containing the attributes and their values.
- Detailed breakdown of the approach:
  1. Initialize an empty map to store the melted data.
  2. Iterate over each row in the input table.
  3. For each row, get the `id`, `name`, `attribute`, and `value`.
  4. Use the `id` and `name` as a key in the map, and append the `attribute` and `value` to the corresponding JSON object.
  5. Finally, construct the output table from the map.
- Proof of optimality: This solution has the same time and space complexity as the brute force approach, but it is more efficient in practice because it uses a `std::map` to store the melted data, which reduces the number of iterations.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

std::vector<json> optimal(std::vector<Row>& rows) {
    std::map<std::pair<int, std::string>, json> meltedData;
    
    for (const auto& row : rows) {
        auto key = std::make_pair(row.id, row.name);
        meltedData[key][row.attribute] = row.value;
    }
    
    std::vector<json> result;
    for (const auto& pair : meltedData) {
        json row;
        row["id"] = pair.first.first;
        row["name"] = pair.first.second;
        row["attribute_value"] = pair.second;
        result.push_back(row);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of rows and $n$ is the number of attributes.
> - **Space Complexity:** $O(m \cdot n)$ for storing the melted data.
> - **Optimality proof:** The solution uses a `std::map` to store the melted data, which reduces the number of iterations and makes the solution more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `std::map` to store the melted data and iterating over each row in the input table.
- Problem-solving patterns identified: Using a `std::map` to reduce the number of iterations and improve efficiency.
- Optimization techniques learned: Using a `std::map` to store the melted data and iterating over each row in the input table.
- Similar problems to practice: Problems that involve iterating over a table and storing data in a `std::map`.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `std::map` to store the melted data, which can result in inefficient solutions.
- Edge cases to watch for: Handling duplicate `id` and `name` pairs, and ensuring the `attribute_value` JSON object is correctly formatted.
- Performance pitfalls: Not using a `std::map` to store the melted data, which can result in inefficient solutions.
- Testing considerations: Testing the solution with different input tables and edge cases to ensure it works correctly.