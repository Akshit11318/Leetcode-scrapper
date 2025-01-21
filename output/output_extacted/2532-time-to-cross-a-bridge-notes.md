## Time to Cross a Bridge
**Problem Link:** https://leetcode.com/problems/time-to-cross-a-bridge/description

**Problem Statement:**
- Input format: An array of integers representing the weights of people.
- Constraints: The number of people is in the range [1, 10^5].
- Expected output format: The minimum time required for all people to cross the bridge.
- Key requirements and edge cases to consider: The bridge can only hold a maximum of two people at a time, and the time it takes to cross the bridge is equal to the maximum weight of the two people on the bridge.

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the minimum time required for all people to cross the bridge, we need to consider all possible combinations of people crossing the bridge at the same time.
- Step-by-step breakdown of the solution: We can use a recursive approach to try all possible combinations of people crossing the bridge.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible scenarios.

```cpp
class Solution {
public:
    int findCrossingTime(int weight[], int n) {
        int res = INT_MAX;
        vector<int> people(weight, weight + n);
        sort(people.begin(), people.end());
        int time = 0;
        while (!people.empty()) {
            // Try all possible combinations of people crossing the bridge
            for (int i = 0; i < people.size(); i++) {
                for (int j = i + 1; j < people.size(); j++) {
                    int currentTime = max(people[i], people[j]);
                    people.erase(people.begin() + i);
                    people.erase(people.begin() + j - 1);
                    time += currentTime;
                    if (people.empty()) {
                        res = min(res, time);
                    } else {
                        // Backtrack and try other combinations
                        people.insert(people.begin() + i, max(people[i], people[j]));
                        people.insert(people.begin() + j, min(people[i], people[j]));
                    }
                }
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of people. This is because we are trying all possible combinations of people crossing the bridge.
> - **Space Complexity:** $O(n)$, where $n$ is the number of people. This is because we need to store the weights of all people in the `people` vector.
> - **Why these complexities occur:** The recursive approach and the use of backtracking lead to exponential time complexity. The space complexity is linear because we only need to store the weights of all people.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the minimum time required for all people to cross the bridge. The idea is to always send the heaviest person first, because this will minimize the time required for the next person to cross the bridge.
- Detailed breakdown of the approach: We can sort the people by their weights in descending order. Then, we can iterate through the sorted list and calculate the time required for each person to cross the bridge.
- Proof of optimality: This approach is optimal because it always sends the heaviest person first, which minimizes the time required for the next person to cross the bridge.

```cpp
class Solution {
public:
    int findCrossingTime(int weight[], int n) {
        int time = 0;
        vector<int> people(weight, weight + n);
        sort(people.rbegin(), people.rend());
        for (int i = 0; i < n; i += 2) {
            if (i + 1 < n) {
                time += max(people[i], people[i + 1]);
            } else {
                time += people[i];
            }
        }
        return time;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is because we are sorting the people by their weights.
> - **Space Complexity:** $O(n)$, where $n$ is the number of people. This is because we need to store the weights of all people in the `people` vector.
> - **Optimality proof:** This approach is optimal because it always sends the heaviest person first, which minimizes the time required for the next person to cross the bridge.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Always send the heaviest person first to minimize the time required for the next person to cross the bridge.
- Optimization techniques learned: Use a greedy approach to find the minimum time required for all people to cross the bridge.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the people by their weights in descending order.
- Edge cases to watch for: When there is only one person, the time required is equal to the weight of that person.
- Performance pitfalls: Using a recursive approach with backtracking, which can lead to exponential time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases such as an empty array or an array with only one element.