## Car Fleet II

**Problem Link:** [https://leetcode.com/problems/car-fleet-ii/description](https://leetcode.com/problems/car-fleet-ii/description)

**Problem Statement:**
- Input format and constraints: Given an integer `n` and a 2D array `congestion` of size `n x 2`, where `congestion[i] = [position, time]`, representing a car's position and the time it takes to reach the destination. The goal is to find the maximum number of car fleets that can reach the destination.
- Expected output format: The number of car fleets.
- Key requirements and edge cases to consider: Cars with the same position and time are considered the same fleet. If a car catches up to another car, they form a single fleet.
- Example test cases with explanations:
  - Example 1: `n = 4`, `congestion = [[-2,-2],[1,0],[3,0],[3,4]]`, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the cars based on their positions and then iterate over the sorted cars to count the number of fleets.
- Step-by-step breakdown of the solution:
  1. Sort the cars based on their positions.
  2. Initialize a variable to store the maximum time it takes for a car to reach the destination.
  3. Iterate over the sorted cars and update the maximum time if a car takes more time to reach the destination.
  4. If a car takes less time to reach the destination than the current maximum time, it forms a new fleet.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem by iterating over all cars and counting the number of fleets.

```cpp
int carFleetII(int n, vector<vector<int>>& congestion) {
    // Sort the cars based on their positions
    sort(congestion.begin(), congestion.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    int maxTime = 0;
    int fleets = 0;

    for (int i = 0; i < n; i++) {
        int time = -congestion[i][0] - congestion[i][1];
        if (time > maxTime) {
            maxTime = time;
            fleets++;
        }
    }

    return fleets;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of cars. This is because we sort the cars based on their positions, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the maximum time and the number of fleets.
> - **Why these complexities occur:** The time complexity occurs because of the sorting operation, and the space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to store the cars that form a fleet. When we encounter a car that takes less time to reach the destination than the car at the top of the stack, we pop the stack until we find a car that takes more time to reach the destination.
- Detailed breakdown of the approach:
  1. Sort the cars based on their positions in descending order.
  2. Initialize a stack to store the cars that form a fleet.
  3. Iterate over the sorted cars and push each car onto the stack.
  4. If a car takes less time to reach the destination than the car at the top of the stack, pop the stack until we find a car that takes more time to reach the destination.
- Proof of optimality: This approach is optimal because we only iterate over the cars once and use a stack to store the cars that form a fleet, resulting in a time complexity of $O(n \log n)$.

```cpp
int carFleetII(int n, vector<vector<int>>& congestion) {
    // Sort the cars based on their positions in descending order
    sort(congestion.begin(), congestion.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] > b[0];
    });

    int fleets = 0;

    for (int i = 0; i < n; i++) {
        bool isNewFleet = true;
        for (int j = i + 1; j < n; j++) {
            int time1 = -congestion[i][0] - congestion[i][1];
            int time2 = -congestion[j][0] - congestion[j][1];
            if (time2 <= time1) {
                isNewFleet = false;
                break;
            }
        }
        if (isNewFleet) {
            fleets++;
        }
    }

    return fleets;
}
```

However, the code above still has a high time complexity due to the nested loop structure. Here's an optimized version using a stack:

```cpp
int carFleetII(int n, vector<vector<int>>& congestion) {
    // Sort the cars based on their positions in descending order
    sort(congestion.begin(), congestion.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] > b[0];
    });

    int fleets = 0;
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        int time = -congestion[i][0] - congestion[i][1];
        while (!stk.empty() && stk.top() <= time) {
            stk.pop();
        }
        stk.push(time);
        fleets = stk.size();
    }

    return fleets;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of cars. This is because we sort the cars based on their positions, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, excluding the space required for the input array. This is because we use a stack to store the cars that form a fleet.
> - **Optimality proof:** This approach is optimal because we only iterate over the cars once and use a stack to store the cars that form a fleet, resulting in a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, stack data structure, and iterative approach.
- Problem-solving patterns identified: Using a stack to store the cars that form a fleet and iterating over the sorted cars to count the number of fleets.
- Optimization techniques learned: Using a stack to reduce the time complexity and iterating over the sorted cars to count the number of fleets.
- Similar problems to practice: Other problems involving sorting and iterative approaches, such as finding the maximum number of pairs that can be formed from a given set of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the cars based on their positions, not using a stack to store the cars that form a fleet, and not iterating over the sorted cars to count the number of fleets.
- Edge cases to watch for: Cars with the same position and time are considered the same fleet. If a car catches up to another car, they form a single fleet.
- Performance pitfalls: Using a nested loop structure, which can result in a high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it produces the correct output.