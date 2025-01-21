## Find Peak Calling Hours for Each City

**Problem Link:** https://leetcode.com/problems/find-peak-calling-hours-for-each-city/description

**Problem Statement:**
- Input format: A list of calls, where each call is represented as a tuple `(city, time, duration)`.
- Constraints: The input list is not empty, and each city has at least one call.
- Expected output format: A dictionary where the keys are city names and the values are the peak calling hours for each city.
- Key requirements and edge cases to consider:
  - Each city can have multiple peak calling hours if there are multiple hours with the same maximum number of calls.
  - The input list can contain calls from different cities.
  - The duration of a call is not considered when calculating the peak calling hours.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each call and update the count of calls for each hour of each city.
- Then, for each city, find the hour(s) with the maximum count of calls.
- This approach comes to mind first because it directly addresses the problem statement and does not require any complex data structures or algorithms.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

vector<int> findPeakHours(vector<vector<string>>& calls, string city) {
    unordered_map<int, int> hourCount;
    for (auto& call : calls) {
        if (call[0] == city) {
            int hour = stoi(call[1].substr(0, 2));
            hourCount[hour]++;
        }
    }
    int maxCount = 0;
    for (auto& pair : hourCount) {
        maxCount = max(maxCount, pair.second);
    }
    vector<int> peakHours;
    for (auto& pair : hourCount) {
        if (pair.second == maxCount) {
            peakHours.push_back(pair.first);
        }
    }
    return peakHours;
}

unordered_map<string, vector<int>> findPeakCallingHours(vector<vector<string>>& calls) {
    unordered_map<string, vector<int>> result;
    unordered_set<string> cities;
    for (auto& call : calls) {
        cities.insert(call[0]);
    }
    for (auto& city : cities) {
        result[city] = findPeakHours(calls, city);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of calls and $m$ is the number of cities. This is because we iterate over each call for each city.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of calls and $m$ is the number of cities. This is because we store the count of calls for each hour of each city.
> - **Why these complexities occur:** These complexities occur because we use a brute force approach that involves iterating over each call and updating the count of calls for each hour of each city.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a hashmap to store the count of calls for each hour of each city.
- We can then find the maximum count of calls for each city and store the corresponding hours.
- This approach is optimal because it only requires a single pass over the input list and uses a constant amount of space to store the count of calls for each hour of each city.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

unordered_map<string, unordered_map<int, int>> findPeakCallingHours(vector<vector<string>>& calls) {
    unordered_map<string, unordered_map<int, int>> cityHourCount;
    for (auto& call : calls) {
        string city = call[0];
        int hour = stoi(call[1].substr(0, 2));
        cityHourCount[city][hour]++;
    }
    unordered_map<string, vector<int>> result;
    for (auto& cityPair : cityHourCount) {
        string city = cityPair.first;
        unordered_map<int, int> hourCount = cityPair.second;
        int maxCount = 0;
        for (auto& pair : hourCount) {
            maxCount = max(maxCount, pair.second);
        }
        vector<int> peakHours;
        for (auto& pair : hourCount) {
            if (pair.second == maxCount) {
                peakHours.push_back(pair.first);
            }
        }
        result[city] = peakHours;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of calls. This is because we only need to iterate over each call once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of calls. This is because we store the count of calls for each hour of each city.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input list and uses a constant amount of space to store the count of calls for each hour of each city.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap, single pass over input list.
- Problem-solving patterns identified: using a hashmap to store count of calls for each hour of each city.
- Optimization techniques learned: reducing time complexity by using a single pass over input list.
- Similar problems to practice: problems involving finding maximum or minimum values in a list.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables, not checking for edge cases.
- Edge cases to watch for: empty input list, calls with invalid city or hour.
- Performance pitfalls: using brute force approach, not using hashmap to store count of calls.
- Testing considerations: testing with different input lists, testing with edge cases.