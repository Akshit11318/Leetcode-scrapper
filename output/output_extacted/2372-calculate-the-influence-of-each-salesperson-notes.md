## Calculate the Influence of Each Salesperson
**Problem Link:** https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/description

**Problem Statement:**
- Input format and constraints: The input is a list of sales, where each sale is represented by three integers: `sale_id`, `sales_person_id`, and `customer_id`. The output should be a list of tuples, where each tuple contains a `sales_person_id` and their corresponding influence.
- Expected output format: The influence of a salesperson is the number of unique customers they have.
- Key requirements and edge cases to consider: Handling duplicate sales, ensuring each customer is only counted once for each salesperson, and considering salespeople with no sales.
- Example test cases with explanations: 
    - Example 1: If there are multiple sales with the same `customer_id` and `sales_person_id`, the customer should only be counted once towards the salesperson's influence.
    - Example 2: A salesperson with no sales should have an influence of 0.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each sale and count the unique customers for each salesperson.
- Step-by-step breakdown of the solution:
    1. Initialize an empty map to store the unique customers for each salesperson.
    2. Iterate through each sale in the list.
    3. For each sale, check if the salesperson is already in the map. If not, add them with an empty set to store unique customers.
    4. Add the customer to the set of unique customers for the salesperson.
    5. After iterating through all sales, calculate the influence for each salesperson by getting the size of their set of unique customers.
- Why this approach comes to mind first: It directly addresses the problem by counting unique customers for each salesperson.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<vector<int>> calculate_influence(vector<vector<int>>& sales) {
    unordered_map<int, unordered_set<int>> salesperson_customers;
    
    for (auto& sale : sales) {
        int salesperson_id = sale[1];
        int customer_id = sale[2];
        
        if (salesperson_customers.find(salesperson_id) == salesperson_customers.end()) {
            salesperson_customers[salesperson_id] = unordered_set<int>();
        }
        
        salesperson_customers[salesperson_id].insert(customer_id);
    }
    
    vector<vector<int>> influence;
    
    for (auto& pair : salesperson_customers) {
        influence.push_back({pair.first, pair.second.size()});
    }
    
    return influence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of sales. This is because we are iterating through each sale once.
> - **Space Complexity:** $O(n)$, for storing the unique customers for each salesperson. In the worst case, every sale could be for a different customer and salesperson.
> - **Why these complexities occur:** The brute force approach requires iterating through each sale and potentially storing every customer and salesperson, leading to linear time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using an unordered_map to store the unique customers for each salesperson allows for efficient lookup and insertion, which is the same as the brute force approach. However, this is already the most efficient approach given the need to process each sale and store unique customers for each salesperson.
- Detailed breakdown of the approach: The optimal approach is essentially the same as the brute force approach since the problem inherently requires processing each sale and storing unique customers for each salesperson.
- Proof of optimality: The time complexity of $O(n)$ is optimal because we must at least read the input once. The space complexity of $O(n)$ is also optimal because in the worst case, we might need to store every customer and salesperson.
- Why further optimization is impossible: Further optimization is not possible because the problem requires at least a single pass through the data and storing the unique customers for each salesperson, which dictates the time and space complexities.

```cpp
// The code remains the same as the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of sales.
> - **Space Complexity:** $O(n)$, for storing the unique customers for each salesperson.
> - **Optimality proof:** The approach is optimal because it only requires a single pass through the sales data and uses a data structure that allows for efficient insertion and lookup of unique customers for each salesperson.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using unordered_maps and sets for efficient lookup and insertion, and understanding the trade-offs between time and space complexity.
- Problem-solving patterns identified: The importance of choosing the right data structures for the problem at hand.
- Optimization techniques learned: Recognizing when a problem requires at least a certain level of complexity due to the nature of the input and output.
- Similar problems to practice: Problems involving counting unique elements or efficient lookup and insertion.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of a key in a map before accessing it, or not using the correct data structure for the problem.
- Edge cases to watch for: Handling duplicate sales, ensuring each customer is only counted once for each salesperson.
- Performance pitfalls: Using data structures with high time complexities for insertion or lookup, such as vectors instead of sets for storing unique customers.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases like duplicate sales or salespeople with no sales.