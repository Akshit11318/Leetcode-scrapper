## Grumpy Bookstore Owner
**Problem Link:** https://leetcode.com/problems/grumpy-bookstore-owner/description

**Problem Statement:**
- Input format: An array of integers `customers` representing the number of customers at each time unit and an array of integers `grumpy` indicating whether the owner is grumpy at each time unit, and an integer `minutes` representing the number of minutes the owner can be grumpy.
- Expected output format: The maximum number of customers that can be satisfied.
- Key requirements and edge cases to consider: The owner can be grumpy for `minutes` minutes, and during this time, the customers will not leave due to the owner's grumpiness.
- Example test cases with explanations:
  - Example 1: `customers = [1,0,1,2,1,1,7,5]`, `grumpy = [0,1,0,1,0,1,0,1]`, `minutes = 3`. The maximum number of customers that can be satisfied is `16`.
  - Example 2: `customers = [1,0,1,2,1,1,7,5]`, `grumpy = [0,1,0,1,0,1,0,1]`, `minutes = 0`. The maximum number of customers that can be satisfied is `10`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the total number of customers that can be satisfied if the owner is not grumpy at all, and then try all possible combinations of `minutes` minutes where the owner can be grumpy.
- Step-by-step breakdown of the solution:
  1. Calculate the total number of customers that can be satisfied if the owner is not grumpy at all.
  2. Try all possible combinations of `minutes` minutes where the owner can be grumpy.
  3. For each combination, calculate the number of customers that can be satisfied.
  4. Update the maximum number of customers that can be satisfied.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxSatisfied(std::vector<int>& customers, std::vector<int>& grumpy, int minutes) {
    int n = customers.size();
    int maxCustomers = 0;
    int totalCustomers = 0;
    
    // Calculate the total number of customers that can be satisfied if the owner is not grumpy at all
    for (int i = 0; i < n; i++) {
        if (grumpy[i] == 0) {
            totalCustomers += customers[i];
        }
    }
    
    // Try all possible combinations of minutes minutes where the owner can be grumpy
    for (int i = 0; i < n - minutes + 1; i++) {
        int customersSatisfied = totalCustomers;
        for (int j = i; j < i + minutes; j++) {
            customersSatisfied += customers[j];
        }
        maxCustomers = std::max(maxCustomers, customersSatisfied);
    }
    
    return maxCustomers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot minutes)$, where $n$ is the number of customers.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of `minutes` minutes where the owner can be grumpy, and for each combination, we calculate the number of customers that can be satisfied. The space complexity occurs because we only use a constant amount of space to store the maximum number of customers that can be satisfied.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to calculate the maximum number of customers that can be satisfied.
- Detailed breakdown of the approach:
  1. Initialize a window of size `minutes`.
  2. Calculate the number of customers that can be satisfied within the window.
  3. Move the window to the right and update the number of customers that can be satisfied.
  4. Update the maximum number of customers that can be satisfied.

```cpp
#include <iostream>
#include <vector>

int maxSatisfied(std::vector<int>& customers, std::vector<int>& grumpy, int minutes) {
    int n = customers.size();
    int maxCustomers = 0;
    int totalCustomers = 0;
    int windowCustomers = 0;
    
    // Calculate the total number of customers that can be satisfied if the owner is not grumpy at all
    for (int i = 0; i < n; i++) {
        if (grumpy[i] == 0) {
            totalCustomers += customers[i];
        }
    }
    
    // Initialize a window of size minutes
    for (int i = 0; i < minutes; i++) {
        windowCustomers += customers[i];
    }
    
    // Update the maximum number of customers that can be satisfied
    maxCustomers = totalCustomers + windowCustomers;
    
    // Move the window to the right and update the number of customers that can be satisfied
    for (int i = minutes; i < n; i++) {
        windowCustomers = windowCustomers - customers[i - minutes] + customers[i];
        maxCustomers = std::max(maxCustomers, totalCustomers + windowCustomers);
    }
    
    return maxCustomers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of customers.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Optimality proof:** The time complexity occurs because we only need to iterate through the customers once to calculate the maximum number of customers that can be satisfied. The space complexity occurs because we only use a constant amount of space to store the maximum number of customers that can be satisfied.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, optimization techniques.
- Problem-solving patterns identified: Using a window to calculate the maximum number of customers that can be satisfied.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity.
- Similar problems to practice: [https://leetcode.com/problems/maximum-average-subarray](https://leetcode.com/problems/maximum-average-subarray), [https://leetcode.com/problems/longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters).

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the window correctly, not updating the maximum number of customers that can be satisfied correctly.
- Edge cases to watch for: When the owner is not grumpy at all, when the owner is grumpy for the entire duration.
- Performance pitfalls: Using a brute force approach, not optimizing the time complexity.
- Testing considerations: Testing with different inputs, testing with edge cases.