## Display Table of Food Orders in a Restaurant

**Problem Link:** https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/description

**Problem Statement:**
- Input format and constraints: The input will be a list of orders, where each order is a list containing the customer name, table number, and food item.
- Expected output format: The output should be a list of lists, where each sublist contains the table number, the total number of orders for that table, and the list of food items ordered for that table.
- Key requirements and edge cases to consider: The table numbers should be sorted in ascending order, and the food items for each table should be sorted in alphabetical order.
- Example test cases with explanations: For example, if the input is `[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]`, the output should be `[["3", "3", ["Ceviche", "Fried Chicken"]], ["5", "2", ["Ceviche", "Water"]], ["10", "1", ["Beef Burrito"]]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate over each order and store the table number and food item in a dictionary. Then, we can iterate over the dictionary and calculate the total number of orders for each table.
- Step-by-step breakdown of the solution: 
    1. Create a dictionary to store the table number and food items.
    2. Iterate over each order and add the food item to the corresponding table number in the dictionary.
    3. Iterate over the dictionary and calculate the total number of orders for each table.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

vector<vector<string>> displayTable(vector<vector<string>>& orders) {
    map<string, map<string, int>> tableOrders;
    for (auto& order : orders) {
        if (tableOrders.find(order[1]) == tableOrders.end()) {
            tableOrders[order[1]] = {};
        }
        if (tableOrders[order[1]].find(order[2]) == tableOrders[order[1]].end()) {
            tableOrders[order[1]][order[2]] = 0;
        }
        tableOrders[order[1]][order[2]]++;
    }

    vector<vector<string>> result;
    for (auto& table : tableOrders) {
        vector<string> row = {table.first};
        int totalOrders = 0;
        set<string> foodItems;
        for (auto& food : table.second) {
            totalOrders += food.second;
            foodItems.insert(food.first);
        }
        row.push_back(to_string(totalOrders));
        for (auto& food : foodItems) {
            row.push_back(food);
        }
        result.push_back(row);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log(m))$ where $n$ is the number of orders and $m$ is the maximum number of food items for a table, due to the use of `std::set` for storing unique food items.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of orders and $m$ is the maximum number of food items for a table, due to the use of `std::map` for storing table orders.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each order and then iterating over the food items for each table. The space complexity occurs because we are storing the table orders and food items in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the table number and food items, and then use a set to store the unique food items for each table.
- Detailed breakdown of the approach: 
    1. Create a dictionary to store the table number and food items.
    2. Iterate over each order and add the food item to the corresponding table number in the dictionary.
    3. Iterate over the dictionary and calculate the total number of orders for each table.
    4. Use a set to store the unique food items for each table and sort them in alphabetical order.
- Proof of optimality: This approach is optimal because we are only iterating over each order once and using a dictionary and set to store the table orders and food items, which has a time complexity of $O(n \cdot m \cdot \log(m))$.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

vector<vector<string>> displayTable(vector<vector<string>>& orders) {
    map<int, map<string, int>> tableOrders;
    for (auto& order : orders) {
        int table = stoi(order[1]);
        if (tableOrders.find(table) == tableOrders.end()) {
            tableOrders[table] = {};
        }
        if (tableOrders[table].find(order[2]) == tableOrders[table].end()) {
            tableOrders[table][order[2]] = 0;
        }
        tableOrders[table][order[2]]++;
    }

    vector<vector<string>> result;
    for (auto& table : tableOrders) {
        vector<string> row = {to_string(table.first)};
        int totalOrders = 0;
        vector<string> foodItems;
        for (auto& food : table.second) {
            totalOrders += food.second;
            foodItems.push_back(food.first);
        }
        sort(foodItems.begin(), foodItems.end());
        row.push_back(to_string(totalOrders));
        for (auto& food : foodItems) {
            row.push_back(food);
        }
        result.push_back(row);
    }

    sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
        return stoi(a[0]) < stoi(b[0]);
    });

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log(m))$ where $n$ is the number of orders and $m$ is the maximum number of food items for a table, due to the use of `std::set` for storing unique food items and sorting the food items in alphabetical order.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of orders and $m$ is the maximum number of food items for a table, due to the use of `std::map` for storing table orders and `std::vector` for storing food items.
> - **Optimality proof:** This approach is optimal because we are only iterating over each order once and using a dictionary and set to store the table orders and food items, which has a time complexity of $O(n \cdot m \cdot \log(m))$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using dictionaries and sets to store and manipulate data, sorting data in alphabetical order.
- Problem-solving patterns identified: Iterating over each order and using a dictionary to store the table orders and food items.
- Optimization techniques learned: Using a set to store unique food items and sorting them in alphabetical order.
- Similar problems to practice: Problems that involve manipulating and sorting data, such as sorting a list of strings or finding the most frequent element in a list.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables or using the wrong data structure.
- Edge cases to watch for: Handling cases where there are no orders or where there are multiple tables with the same number.
- Performance pitfalls: Using a data structure that has a high time complexity, such as a list instead of a dictionary.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.