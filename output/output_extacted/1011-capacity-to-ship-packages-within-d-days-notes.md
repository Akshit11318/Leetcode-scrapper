## Capacity to Ship Packages Within D Days

**Problem Link:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description

**Problem Statement:**
- Input format: An array of integers `weights` representing the weights of packages and an integer `d` representing the number of days.
- Constraints: `1 <= d <= weights.length <= 50000`, `1 <= weights[i] <= 500`.
- Expected output format: The minimum capacity of a ship to ship all packages within `d` days.
- Key requirements and edge cases to consider: 
  - The ship can carry a maximum capacity of packages each day.
  - We need to find the minimum capacity to ship all packages within `d` days.
- Example test cases with explanations:
  - For `weights = [1,2,3,4,5,6,7,8,9,10]` and `d = 5`, the output should be `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible capacities from the maximum weight to the sum of all weights.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum capacity to the maximum weight in the `weights` array.
  2. Initialize the maximum capacity to the sum of all weights in the `weights` array.
  3. Iterate over all possible capacities from the minimum to the maximum.
  4. For each capacity, calculate the number of days required to ship all packages.
  5. If the number of days is less than or equal to `d`, update the minimum capacity.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible capacities.

```cpp
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int d) {
        int maxWeight = *max_element(weights.begin(), weights.end());
        int sumWeight = accumulate(weights.begin(), weights.end(), 0);
        
        for (int capacity = maxWeight; capacity <= sumWeight; capacity++) {
            int days = 1;
            int currentWeight = 0;
            for (int weight : weights) {
                if (currentWeight + weight > capacity) {
                    days++;
                    currentWeight = weight;
                } else {
                    currentWeight += weight;
                }
            }
            if (days <= d) {
                return capacity;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times w)$, where $n$ is the number of packages and $w$ is the sum of all weights.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible capacities and for each capacity, we iterate over all packages. The space complexity occurs because we only use a constant amount of space to store the minimum and maximum capacities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use binary search to find the minimum capacity.
- Detailed breakdown of the approach:
  1. Initialize the minimum capacity to the maximum weight in the `weights` array.
  2. Initialize the maximum capacity to the sum of all weights in the `weights` array.
  3. Perform binary search over the range of possible capacities.
  4. For each capacity, calculate the number of days required to ship all packages.
  5. If the number of days is less than or equal to `d`, update the maximum capacity.
  6. If the number of days is greater than `d`, update the minimum capacity.
- Why further optimization is impossible: We have reduced the search space to a range of possible capacities and we are using binary search to find the minimum capacity.

```cpp
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int d) {
        int maxWeight = *max_element(weights.begin(), weights.end());
        int sumWeight = accumulate(weights.begin(), weights.end(), 0);
        
        auto canShip = [&](int capacity) {
            int days = 1;
            int currentWeight = 0;
            for (int weight : weights) {
                if (currentWeight + weight > capacity) {
                    days++;
                    currentWeight = weight;
                } else {
                    currentWeight += weight;
                }
            }
            return days <= d;
        };
        
        int left = maxWeight;
        int right = sumWeight;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canShip(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log w)$, where $n$ is the number of packages and $w$ is the sum of all weights.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** We have reduced the search space to a range of possible capacities and we are using binary search to find the minimum capacity, which is the most efficient way to find the minimum capacity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and the concept of reducing the search space.
- Problem-solving patterns identified: The use of binary search to find the minimum or maximum of a range of values.
- Optimization techniques learned: Reducing the search space and using binary search to find the minimum or maximum of a range of values.
- Similar problems to practice: Other problems that involve finding the minimum or maximum of a range of values, such as the `kth largest element` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the minimum and maximum capacities correctly.
- Edge cases to watch for: The case where the number of days is equal to the number of packages.
- Performance pitfalls: Using a brute force approach to find the minimum capacity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure that it works correctly.