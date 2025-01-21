## Minimum Time Difference
**Problem Link:** https://leetcode.com/problems/minimum-time-difference/description

**Problem Statement:**
- Input format: A list of strings representing time in the format "HH:MM".
- Constraints: The input list contains at least 2 and at most 24 strings, each string representing a time in the format "HH:MM".
- Expected output format: The minimum time difference in minutes between any two times in the input list.
- Key requirements and edge cases to consider: 
    * Handle cases where times are in different days (e.g., 23:59 and 00:00).
    * Consider times that are the same.
- Example test cases with explanations:
    * Input: ["23:59","00:00"] - Output: 1 (1 minute difference between 23:59 and 00:00).
    * Input: ["00:00","23:59","00:00"] - Output: 0 (0 minute difference between two "00:00" times).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each time with every other time in the list to find the minimum time difference.
- Step-by-step breakdown of the solution:
    1. Convert each time from string to minutes since the start of the day.
    2. Compare each time with every other time to calculate the absolute difference in minutes.
    3. Keep track of the minimum difference found so far.
- Why this approach comes to mind first: It's straightforward and simple, but inefficient for large inputs.

```cpp
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int n = timePoints.size();
        int minDiff = INT_MAX;
        
        // Convert time to minutes
        vector<int> times;
        for (const auto& time : timePoints) {
            int h = stoi(time.substr(0, 2));
            int m = stoi(time.substr(3, 2));
            times.push_back(h * 60 + m);
        }
        
        // Compare each time with every other time
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int diff = abs(times[i] - times[j]);
                minDiff = min(minDiff, diff);
            }
        }
        
        // Consider times that are in different days
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int diff = abs(times[i] - times[j] + 24 * 60);
                minDiff = min(minDiff, diff);
            }
        }
        
        return minDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of time points. This is because we compare each time with every other time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of time points. This is because we store the converted times in a vector.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops, and space complexity due to storing the converted times.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can sort the times and compare adjacent times to find the minimum difference.
- Detailed breakdown of the approach:
    1. Convert each time to minutes since the start of the day.
    2. Sort the times in ascending order.
    3. Compare adjacent times to calculate the minimum difference.
    4. Consider the difference between the first and last times (in case they are in different days).
- Proof of optimality: This approach has a lower time complexity than the brute force approach, and it's impossible to do better than $O(n \log n)$ due to the sorting step.

```cpp
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int n = timePoints.size();
        vector<int> times;
        
        // Convert time to minutes
        for (const auto& time : timePoints) {
            int h = stoi(time.substr(0, 2));
            int m = stoi(time.substr(3, 2));
            times.push_back(h * 60 + m);
        }
        
        // Sort times
        sort(times.begin(), times.end());
        
        int minDiff = INT_MAX;
        
        // Compare adjacent times
        for (int i = 1; i < n; ++i) {
            int diff = times[i] - times[i - 1];
            minDiff = min(minDiff, diff);
        }
        
        // Consider times that are in different days
        int diff = 24 * 60 - times.back() + times[0];
        minDiff = min(minDiff, diff);
        
        return minDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of time points. This is because we sort the times.
> - **Space Complexity:** $O(n)$, where $n$ is the number of time points. This is because we store the converted times in a vector.
> - **Optimality proof:** This approach is optimal because it has a lower time complexity than the brute force approach, and it's impossible to do better than $O(n \log n)$ due to the sorting step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, comparing adjacent elements.
- Problem-solving patterns identified: Considering edge cases (times in different days).
- Optimization techniques learned: Reducing time complexity by sorting and comparing adjacent elements.
- Similar problems to practice: Other problems involving time or date comparisons.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to consider times in different days.
- Edge cases to watch for: Times that are the same, times that are in different days.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test with different inputs, including edge cases.