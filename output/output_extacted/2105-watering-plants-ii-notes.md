## Watering Plants II
**Problem Link:** [https://leetcode.com/problems/watering-plants-ii/description](https://leetcode.com/problems/watering-plants-ii/description)

**Problem Statement:**
- Input format and constraints: Given a list of plants, a watering can, and the capacity of the can, we need to determine the minimum number of refills required to water all plants.
- Expected output format: The function should return the minimum number of refills needed.
- Key requirements and edge cases to consider: We need to ensure that the can is refilled when its capacity is exceeded, and we should also handle cases where the can's capacity is greater than the total amount of water required by all plants.
- Example test cases with explanations:
  - Example 1: plants = [2,2,3,3], capacity = 5. Output: 1. Explanation: Water the first two plants with 2 units of water, then refill the can with 5 units of water and water the last two plants with 3 units of water.
  - Example 2: plants = [2,2,3,3], capacity = 3. Output: 3. Explanation: Water the first plant with 2 units of water, then refill the can with 3 units of water and water the second plant with 2 units of water, then refill the can with 3 units of water and water the third plant with 3 units of water, then refill the can with 3 units of water and water the last plant with 3 units of water.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the process of watering each plant one by one and refill the can whenever its capacity is exceeded.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to keep track of the number of refills.
  2. Iterate through each plant and calculate the amount of water required to water it.
  3. If the can's capacity is not sufficient to water the current plant, refill the can and increment the number of refills.
  4. Update the can's capacity after watering each plant.
- Why this approach comes to mind first: This approach is straightforward and directly simulates the process of watering plants.

```cpp
class Solution {
public:
    int minimumRefillPlant(vector<int>& plant, int capacity) {
        int can = capacity;
        int refills = 0;
        for (int i = 0; i < plant.size(); i++) {
            if (can < plant[i]) {
                can = capacity;
                refills++;
            }
            can -= plant[i];
        }
        return refills;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of plants. This is because we are iterating through each plant once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the number of refills and the can's capacity.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through each plant, and the space complexity is constant because we are using a fixed amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we need to iterate through each plant at least once to determine the minimum number of refills required.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach.
- Proof of optimality: The time complexity of $O(n)$ is optimal because we need to examine each plant at least once to determine the minimum number of refills required.
- Why further optimization is impossible: We cannot do better than $O(n)$ time complexity because we need to iterate through each plant at least once.

```cpp
class Solution {
public:
    int minimumRefillPlant(vector<int>& plant, int capacity) {
        int can = capacity;
        int refills = 0;
        for (int i = 0; i < plant.size(); i++) {
            if (can < plant[i]) {
                can = capacity;
                refills++;
            }
            can -= plant[i];
        }
        return refills;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of plants.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the number of refills and the can's capacity.
> - **Optimality proof:** The time complexity of $O(n)$ is optimal because we need to examine each plant at least once to determine the minimum number of refills required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and basic arithmetic operations.
- Problem-solving patterns identified: Simulating a process and iterating through a sequence of elements.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve simulating a process or iterating through a sequence of elements.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to refill the can when its capacity is exceeded, or not updating the can's capacity after watering each plant.
- Edge cases to watch for: Cases where the can's capacity is greater than the total amount of water required by all plants, or cases where the can's capacity is not sufficient to water any plant.
- Performance pitfalls: Using unnecessary data structures or algorithms that have higher time complexities.
- Testing considerations: Test the function with different input values, including edge cases, to ensure that it works correctly.