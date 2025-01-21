## Calculate Delayed Arrival Time

**Problem Link:** https://leetcode.com/problems/calculate-delayed-arrival-time/description

**Problem Statement:**
- Input: `arrivalTime`, `delayTime`
- Constraints: `arrivalTime` and `delayTime` are integers
- Expected Output: The delayed arrival time
- Key requirements: Calculate the delayed arrival time by adding the delay to the arrival time and handle cases where the result exceeds 24 hours
- Example test cases:
  - `arrivalTime = 15`, `delayTime = 5`, expected output: `20`
  - `arrivalTime = 23`, `delayTime = 7`, expected output: `6`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simply add the `arrivalTime` and `delayTime` and handle the case where the result exceeds 24 hours by taking the modulus with 24.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayTime) {
        // Add arrival time and delay time
        int delayedTime = arrivalTime + delayTime;
        
        // If the result exceeds 24 hours, take the modulus with 24
        if (delayedTime >= 24) {
            delayedTime %= 24;
        }
        
        return delayedTime;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the variables.
> - **Why these complexities occur:** The operations are simple arithmetic and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we can use the modulus operator to handle the case where the result exceeds 24 hours in a single operation.
- This approach is optimal because it eliminates the need for an if statement and directly calculates the delayed arrival time.

```cpp
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayTime) {
        // Add arrival time and delay time, and take the modulus with 24
        return (arrivalTime + delayTime) % 24;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the variables.
> - **Optimality proof:** This is the best possible complexity because we must perform at least one operation to calculate the delayed arrival time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: modulus operator, simple arithmetic operations
- Problem-solving patterns identified: handling cases where the result exceeds a certain threshold
- Optimization techniques learned: eliminating unnecessary if statements
- Similar problems to practice: other problems involving simple arithmetic operations and modulus operator

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle the case where the result exceeds 24 hours
- Edge cases to watch for: arrival time and delay time exceeding 24 hours
- Performance pitfalls: using unnecessary if statements or loops
- Testing considerations: testing with different input values, including edge cases.