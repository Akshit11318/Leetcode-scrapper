## Water Bottles

**Problem Link:** https://leetcode.com/problems/water-bottles/description

**Problem Statement:**
- Input format and constraints: We are given two integers: `numBottles` (the number of water bottles) and `numExchange` (the number of empty bottles required to get a full bottle). 
- Expected output format: The total number of drinks that can be consumed from the bottles.
- Key requirements and edge cases to consider: We need to consider the scenario where we have enough empty bottles to get a new full bottle.
- Example test cases with explanations: For example, if `numBottles = 9` and `numExchange = 3`, we can get 13 drinks because we can get 3 new bottles from the 9 empty bottles and then get 3 more new bottles from the 6 empty bottles (3 from the initial 9 and 3 from the first set of new bottles), and finally get 1 more new bottle from the 4 empty bottles (1 from the last set of new bottles and 3 from the second set of new bottles).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the process of getting new bottles from empty bottles until we don't have enough empty bottles to get a new one.
- Step-by-step breakdown of the solution: We start with the given number of bottles and keep track of the total drinks consumed. We then calculate the number of new bottles we can get from the empty bottles and add it to the total drinks. We repeat this process until we don't have enough empty bottles to get a new one.
- Why this approach comes to mind first: It's a straightforward simulation of the problem statement.

```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int totalDrinks = numBottles;
        int emptyBottles = numBottles;
        
        while (emptyBottles >= numExchange) {
            int newBottles = emptyBottles / numExchange;
            totalDrinks += newBottles;
            emptyBottles = newBottles + (emptyBottles % numExchange);
        }
        
        return totalDrinks;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{numBottles}{numExchange})$ because in the worst-case scenario, we keep getting new bottles until we don't have enough empty bottles to get a new one.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity occurs because we are simulating the process of getting new bottles from empty bottles, and the space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a simple mathematical formula. We can calculate the total number of drinks by adding the initial number of bottles to the number of new bottles we can get from the empty bottles.
- Detailed breakdown of the approach: We start with the given number of bottles and calculate the number of new bottles we can get from the empty bottles. We repeat this process until we don't have enough empty bottles to get a new one.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(\frac{numBottles}{numExchange})$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we need to simulate the process of getting new bottles from empty bottles, and this requires a time complexity of at least $O(\frac{numBottles}{numExchange})$.

```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int totalDrinks = numBottles;
        int emptyBottles = numBottles;
        
        while (emptyBottles >= numExchange) {
            int newBottles = emptyBottles / numExchange;
            totalDrinks += newBottles;
            emptyBottles = newBottles + (emptyBottles % numExchange);
        }
        
        return totalDrinks;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{numBottles}{numExchange})$ because in the worst-case scenario, we keep getting new bottles until we don't have enough empty bottles to get a new one.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(\frac{numBottles}{numExchange})$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, mathematical formula.
- Problem-solving patterns identified: Simulating a process, using a mathematical formula to solve a problem.
- Optimization techniques learned: None.
- Similar problems to practice: Other simulation problems, problems that can be solved using mathematical formulas.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if we have enough empty bottles to get a new one.
- Edge cases to watch for: When the number of empty bottles is less than the number of bottles required to get a new one.
- Performance pitfalls: Not using a mathematical formula to solve the problem.
- Testing considerations: Test the function with different inputs, including edge cases.