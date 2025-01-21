## Count Pairs that Form a Complete Day I

**Problem Link:** https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description

**Problem Statement:**
- Input: An array of integers representing the hour and minute of each day.
- Constraints: The input array `timePoints` will have a length in the range [1, 1000].
- Expected Output: The number of pairs of time points that form a complete day.
- Key Requirements and Edge Cases:
  - Two times `time1` and `time2` form a complete day if the minute difference between them is less than or equal to `60`.
  - The hour difference must be such that when added with the minute difference, it forms a complete day, i.e., `1440` minutes.

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each time point with every other time point to check if they form a complete day.
- Step-by-step breakdown:
  1. Convert each time point to minutes since the start of the day.
  2. Iterate through all pairs of time points.
  3. For each pair, calculate the absolute difference in minutes.
  4. Check if the difference is less than or equal to `1440` and the minute difference is less than or equal to `60`.
  5. Count all such pairs.

```cpp
int countCompleteDays(vector<string>& timePoints) {
    int count = 0;
    for (int i = 0; i < timePoints.size(); i++) {
        for (int j = i + 1; j < timePoints.size(); j++) {
            int time1 = stoi(timePoints[i].substr(0, 2)) * 60 + stoi(timePoints[i].substr(3));
            int time2 = stoi(timePoints[j].substr(0, 2)) * 60 + stoi(timePoints[j].substr(3));
            int diff = abs(time1 - time2);
            if (diff <= 1440 && (time1 % 60) + (time2 % 60) <= 60) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of time points. This is because we are iterating through all pairs of time points.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we are using a constant amount of space.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, but the space complexity is low because we are not using any additional data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to consider the minute part of the time when calculating the difference.
- Detailed breakdown:
  1. Convert each time point to minutes since the start of the day.
  2. Use a hashmap to store the frequency of each time point.
  3. Iterate through all time points and for each time point, calculate the required time to form a complete day.
  4. Check if the required time exists in the hashmap and increment the count accordingly.

```cpp
int countCompleteDays(vector<string>& timePoints) {
    int count = 0;
    unordered_map<int, int> freq;
    for (const auto& time : timePoints) {
        int timeInMins = stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3));
        freq[timeInMins]++;
    }
    for (const auto& time : freq) {
        for (const auto& otherTime : freq) {
            int diff = abs(time.first - otherTime.first);
            if (diff <= 1440 && (time.first % 60) + (otherTime.first % 60) <= 60) {
                if (time.first == otherTime.first) {
                    count += time.second * (time.second - 1) / 2;
                } else {
                    count += time.second * otherTime.second;
                }
            }
        }
    }
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of unique time points. This is because we are iterating through all pairs of unique time points.
> - **Space Complexity:** $O(n)$, where $n$ is the number of time points. This is because we are using a hashmap to store the frequency of each time point.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2)$ because we are still iterating through all pairs of time points. However, we have reduced the number of iterations by only considering unique time points and using a hashmap to store their frequencies.

### Final Notes

**Learning Points:**
- The importance of considering the minute part of the time when calculating the difference.
- The use of a hashmap to store the frequency of each time point and reduce the number of iterations.
- The need to handle the case where the same time point is paired with itself.

**Mistakes to Avoid:**
- Not considering the minute part of the time when calculating the difference.
- Not using a hashmap to store the frequency of each time point and reduce the number of iterations.
- Not handling the case where the same time point is paired with itself.