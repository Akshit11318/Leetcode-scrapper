## Find Building Where Alice and Bob Can Meet

**Problem Link:** https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description

**Problem Statement:**
- Input format: Two arrays, `aliceAr` and `bobAr`, representing the distances Alice and Bob must travel to reach each building.
- Constraints: `1 <= aliceAr.length == bobAr.length <= 10^5`.
- Expected output format: The index of the building where Alice and Bob can meet, if such a building exists. If no such building exists, return `-1`.
- Key requirements and edge cases to consider: 
  - A building where Alice and Bob can meet is one where the sum of their distances to the building is equal.
  - If no such building exists, return `-1`.
- Example test cases with explanations:
  - `aliceAr = [2, 3, 4], bobAr = [1, 5, 5]`, Output: `2`. This is because the sum of Alice's distance to the building at index 2 (4) and Bob's distance to the same building (5) is 9, which is the minimum sum where they can meet.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through each building and calculate the sum of Alice's and Bob's distances to that building.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the minimum sum of distances.
  2. Iterate through each building.
  3. For each building, calculate the sum of Alice's and Bob's distances to that building.
  4. If this sum is less than the current minimum sum, update the minimum sum and store the index of the current building.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible building.

```cpp
class Solution {
public:
    int findBuilding(vector<int>& aliceAr, vector<int>& bobAr) {
        int minSum = INT_MAX;
        int result = -1;
        
        for (int i = 0; i < aliceAr.size(); i++) {
            int sum = aliceAr[i] + bobAr[i];
            if (sum < minSum) {
                minSum = sum;
                result = i;
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we iterate through each building once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum sum and the result.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each building. The space complexity is constant because we do not use any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must check every building to find the one with the minimum sum of distances.
- Detailed breakdown of the approach:
  1. Initialize variables to store the minimum sum and the result.
  2. Iterate through each building.
  3. For each building, calculate the sum of Alice's and Bob's distances.
  4. Update the minimum sum and result if a smaller sum is found.
- Proof of optimality: This solution is optimal because it has a linear time complexity, which is the best possible time complexity for this problem since we must examine every building at least once.

```cpp
class Solution {
public:
    int findBuilding(vector<int>& aliceAr, vector<int>& bobAr) {
        int minSum = INT_MAX;
        int result = -1;
        
        for (int i = 0; i < aliceAr.size(); i++) {
            int sum = aliceAr[i] + bobAr[i];
            if (sum < minSum) {
                minSum = sum;
                result = i;
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buildings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear search, minimum finding.
- Problem-solving patterns identified: Checking every possible solution to find the optimal one.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve finding the minimum or maximum of a certain quantity.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables properly, not checking for edge cases.
- Edge cases to watch for: An empty input array, an array with a single element.
- Performance pitfalls: Using a data structure with a higher time complexity than necessary, such as using a `std::set` to store the buildings.
- Testing considerations: Test the function with different input arrays, including edge cases.