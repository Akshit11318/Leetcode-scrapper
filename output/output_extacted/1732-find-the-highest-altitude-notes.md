## Find the Highest Altitude
**Problem Link:** https://leetcode.com/problems/find-the-highest-altitude/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `gain` where `gain[i]` represents the net change in altitude at index `i`, find the highest altitude.
- Expected output format: Return the maximum altitude.
- Key requirements and edge cases to consider: The initial altitude is 0. The altitude at each step is the sum of the previous altitude and the current gain.
- Example test cases with explanations:
  - Input: `gain = [2,1,2,1]`
    - Output: `3`
    - Explanation: The altitude changes by 2, then 1, then 2, then 1 again. The sequence of altitudes is [0, 2, 3, 5, 6].
  - Input: `gain = [5,0,2,1]`
    - Output: `5`
    - Explanation: The altitude changes by 5, then 0, then 2, then 1 again. The sequence of altitudes is [0, 5, 5, 7, 8].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to simulate the process of calculating the altitude at each step.
- Step-by-step breakdown of the solution:
  1. Initialize an array to store the altitude at each step.
  2. Iterate through the `gain` array, calculating the altitude at each step as the sum of the previous altitude and the current gain.
  3. Keep track of the maximum altitude encountered.
- Why this approach comes to mind first: It directly simulates the problem description and is straightforward to implement.

```cpp
vector<int> calculateAltitude(vector<int>& gain) {
    int n = gain.size();
    vector<int> altitudes(n + 1);
    altitudes[0] = 0; // Initial altitude is 0
    int maxAltitude = 0;
    for (int i = 0; i < n; i++) {
        altitudes[i + 1] = altitudes[i] + gain[i];
        maxAltitude = max(maxAltitude, altitudes[i + 1]);
    }
    return altitudes;
}

int largestAltitude(vector<int>& gain) {
    vector<int> altitudes = calculateAltitude(gain);
    int maxAltitude = 0;
    for (int altitude : altitudes) {
        maxAltitude = max(maxAltitude, altitude);
    }
    return maxAltitude;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the `gain` array. This is because we iterate through the `gain` array once to calculate the altitudes and then potentially again to find the maximum altitude.
> - **Space Complexity:** $O(n)$ for storing the altitudes array.
> - **Why these complexities occur:** The iteration through the `gain` array to calculate altitudes and the potential second iteration to find the maximum altitude cause the time complexity. The space complexity is due to storing the altitudes array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We don't need to store all altitudes; we only need to keep track of the current altitude and the maximum altitude seen so far.
- Detailed breakdown of the approach:
  1. Initialize variables for the current altitude and the maximum altitude.
  2. Iterate through the `gain` array, updating the current altitude by adding the current gain.
  3. Update the maximum altitude if the current altitude is greater.
- Proof of optimality: This solution has the best possible time complexity because it only requires a single pass through the `gain` array.

```cpp
int largestAltitude(vector<int>& gain) {
    int currentAltitude = 0;
    int maxAltitude = 0;
    for (int g : gain) {
        currentAltitude += g;
        maxAltitude = max(maxAltitude, currentAltitude);
    }
    return maxAltitude;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the `gain` array. This is because we only need to iterate through the `gain` array once.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the current and maximum altitudes.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity ($O(n)$) and uses minimal space ($O(1)$), making it efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, keeping track of maximum values, and optimizing space usage.
- Problem-solving patterns identified: Simulating processes and optimizing by reducing unnecessary computations and space usage.
- Optimization techniques learned: Reducing space complexity by only keeping necessary information and minimizing the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not updating maximum values properly.
- Edge cases to watch for: Handling empty input arrays, ensuring the initial altitude is correctly set to 0.
- Performance pitfalls: Using unnecessary data structures or iterations that increase time or space complexity.
- Testing considerations: Ensure the solution works for various input sizes, including edge cases like empty arrays or arrays with a single element.