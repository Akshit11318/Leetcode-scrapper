## Alert Using Same Key Card Three or More Times in a One Hour Period
**Problem Link:** https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/description

**Problem Statement:**
- Input format: A list of `string` representing key card usage records in the format "key:timestamp".
- Constraints: The input list is not empty, and all timestamps are in the format "HH:MM".
- Expected output format: A list of `string` representing the key cards that triggered an alert.
- Key requirements and edge cases to consider: 
    - A key card triggers an alert if it is used three or more times in a one-hour period.
    - The one-hour period is a sliding window, and the alert is triggered as soon as the third usage is detected within the window.
- Example test cases with explanations:
    - Example 1: Input: ["d1:0", "d1:2", "d1:3", "d1:4", "d2:1", "d2:2", "d2:3"] Output: ["d1"]
    - Example 2: Input: ["a:1", "a:2", "a:3", "b:1", "b:2", "b:3", "c:1", "c:2", "c:3"] Output: ["a", "b", "c"]

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each key card usage record, and for each record, check all previous records to see if the same key card has been used two more times within the last hour.
- Step-by-step breakdown of the solution:
    1. Sort the usage records by timestamp.
    2. Iterate over each usage record.
    3. For each record, iterate over all previous records to check if the same key card has been used two more times within the last hour.
    4. If a key card has been used three or more times within the last hour, add it to the alert list.
- Why this approach comes to mind first: It is a straightforward solution that checks all possible combinations of usage records.

```cpp
vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
    map<string, vector<int>> keyUsage;
    for (int i = 0; i < keyName.size(); i++) {
        string key = keyName[i];
        int time = stoi(keyTime[i].substr(0, 2)) * 60 + stoi(keyTime[i].substr(3, 2));
        keyUsage[key].push_back(time);
    }
    
    set<string> alert;
    for (auto& [key, usage] : keyUsage) {
        sort(usage.begin(), usage.end());
        for (int i = 2; i < usage.size(); i++) {
            if (usage[i] - usage[i - 2] <= 60) {
                alert.insert(key);
                break;
            }
        }
    }
    
    vector<string> result(alert.begin(), alert.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the usage records for each key card.
> - **Space Complexity:** $O(n)$ for storing the usage records for each key card.
> - **Why these complexities occur:** The brute force approach requires sorting the usage records for each key card, which has a time complexity of $O(n \log n)$. The space complexity is $O(n)$ because we need to store the usage records for each key card.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to keep track of the usage records for each key card within the last hour.
- Detailed breakdown of the approach:
    1. Sort the usage records by timestamp.
    2. Iterate over each usage record.
    3. For each record, check if the same key card has been used two more times within the last hour by using a sliding window.
    4. If a key card has been used three or more times within the last hour, add it to the alert list.
- Proof of optimality: The optimal approach has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem because we need to sort the usage records.

```cpp
vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
    map<string, vector<int>> keyUsage;
    for (int i = 0; i < keyName.size(); i++) {
        string key = keyName[i];
        int time = stoi(keyTime[i].substr(0, 2)) * 60 + stoi(keyTime[i].substr(3, 2));
        keyUsage[key].push_back(time);
    }
    
    set<string> alert;
    for (auto& [key, usage] : keyUsage) {
        sort(usage.begin(), usage.end());
        for (int i = 2; i < usage.size(); i++) {
            if (usage[i] - usage[i - 2] <= 60) {
                alert.insert(key);
                break;
            }
        }
    }
    
    vector<string> result(alert.begin(), alert.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the usage records for each key card.
> - **Space Complexity:** $O(n)$ for storing the usage records for each key card.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem because we need to sort the usage records.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, sliding window approach.
- Problem-solving patterns identified: Using a map to store usage records for each key card.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity.
- Similar problems to practice: Problems that require sorting and using a sliding window approach.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the usage records, not using a sliding window approach.
- Edge cases to watch for: Key cards that are used less than three times within the last hour.
- Performance pitfalls: Not using a efficient data structure to store the usage records.
- Testing considerations: Test the solution with different input sizes and edge cases.