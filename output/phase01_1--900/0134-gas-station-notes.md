## Gas Station Problem
**Problem Link:** https://leetcode.com/problems/gas-station/description

**Problem Statement:**
- Input: `int gas[]`, `int cost[]` representing the amount of gas at each station and the cost of gas to travel to the next station, respectively.
- Output: The starting gas station's index if it's possible to travel around the circuit once; otherwise, `-1`.
- Key requirements: Find a starting point that allows the car to complete the circuit.
- Edge cases: Empty `gas` or `cost` arrays, no solution exists.
- Example test cases:
  - `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`: Starting at index 3, we can travel the circuit.
  - `gas = [2,3,4]`, `cost = [3,4,3]`: No solution exists.

---

### Brute Force Approach
**Explanation:**
- Try each gas station as a starting point.
- For each starting point, simulate the journey around the circuit, keeping track of the current gas level.
- If we can complete the circuit without running out of gas, return the starting index.

```cpp
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    for (int start = 0; start < gasSize; start++) {
        int gasLevel = 0;
        for (int i = start; i < start + gasSize; i++) {
            gasLevel += gas[i % gasSize] - cost[i % gasSize];
            if (gasLevel < 0) break;
        }
        if (gasLevel >= 0) return start;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of gas stations, because for each starting point, we potentially travel the entire circuit.
> - **Space Complexity:** $O(1)$, excluding the input arrays, as we only use a constant amount of space.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the constant space usage is due to only needing a few variables to keep track of the gas level and current position.

---

### Optimal Approach (Required)
**Explanation:**
- Calculate the total gas and total cost.
- If total gas is less than total cost, it's impossible to complete the circuit.
- Otherwise, find a starting point where the gas level never goes below zero by maintaining a running sum of `gas[i] - cost[i]`.
- The starting point will be the first index after the minimum running sum, because that's where the tank will be empty (or as close to empty as possible) and we can start refilling.

```cpp
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    int totalGas = 0, totalCost = 0;
    int tank = 0, start = 0;
    for (int i = 0; i < gasSize; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
        tank += gas[i] - cost[i];
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return totalGas < totalCost ? -1 : start;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of gas stations, as we make a single pass through the arrays.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the running sums and the starting point.
> - **Optimality proof:** This is optimal because we only need to consider each gas station once to determine if we can complete the circuit and to find the starting point. The linear time complexity is the best we can achieve for this problem since we must at least read the input.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts: Maintaining a running sum, understanding the conditions under which a solution exists.
- Problem-solving patterns identified: Checking for the existence of a solution before finding it, using a single pass to find the optimal starting point.
- Optimization techniques learned: Avoiding unnecessary work by checking the total gas and cost before attempting to find a starting point.
- Similar problems to practice: Other problems involving finding a starting point or condition that allows for a successful outcome.

**Mistakes to Avoid:**
- Not checking if a solution exists before attempting to find it.
- Not considering edge cases, such as empty input arrays.
- Not optimizing the solution by checking the total gas and cost first.
- Not maintaining a running sum efficiently to find the starting point.