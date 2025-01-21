## Count Unhappy Friends
**Problem Link:** https://leetcode.com/problems/count-unhappy-friends/description

**Problem Statement:**
- Input: `n` (number of friends), `preferences` (preferences of each friend), `pairs` (existing pairs of friends)
- Output: The number of unhappy friends
- Key requirements and edge cases to consider: 
  - A friend is unhappy if they are paired with someone they do not like more than their current partner.
  - There are `n` friends, and each friend has a preference list of the other friends.
  - The `preferences` list contains `n` lists, each representing the preference of a friend.
  - The `pairs` list contains `n/2` pairs of friends.
- Example test cases with explanations:
  - If a friend `i` is paired with friend `j`, but friend `i` likes friend `k` more than friend `j`, then friend `i` is unhappy.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through each friend and check if they are unhappy by comparing their preference list with their current partner.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the partner of each friend.
  2. Iterate through each friend and check if they are unhappy by comparing their preference list with their current partner.
  3. Count the number of unhappy friends.
- Why this approach comes to mind first: It is a straightforward approach that involves checking each friend's preference list and comparing it with their current partner.

```cpp
int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
    // Create a dictionary to store the partner of each friend
    unordered_map<int, int> partner;
    for (auto& pair : pairs) {
        partner[pair[0]] = pair[1];
        partner[pair[1]] = pair[0];
    }
    
    // Initialize count of unhappy friends
    int unhappy_count = 0;
    
    // Iterate through each friend
    for (int i = 0; i < n; i++) {
        // Check if friend i is unhappy
        bool is_unhappy = false;
        for (int j = 0; j < preferences[i].size(); j++) {
            if (preferences[i][j] == partner[i]) break;
            if (find(preferences[partner[i]].begin(), preferences[partner[i]].end(), i) > find(preferences[partner[i]].begin(), preferences[partner[i]].end(), preferences[i][j])) {
                is_unhappy = true;
                break;
            }
        }
        if (is_unhappy) unhappy_count++;
    }
    
    return unhappy_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of friends and $m$ is the average length of the preference lists.
> - **Space Complexity:** $O(n)$, for storing the partner of each friend.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through each friend and checking their preference list. The space complexity occurs because we are storing the partner of each friend.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the preference list of each friend and iterate through each friend to check if they are unhappy.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the preference list of each friend.
  2. Create a dictionary to store the partner of each friend.
  3. Iterate through each friend and check if they are unhappy by comparing their preference list with their current partner.
  4. Count the number of unhappy friends.
- Proof of optimality: This approach is optimal because it involves a single pass through the preference lists and partners of each friend.

```cpp
int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
    // Create a dictionary to store the preference list of each friend
    unordered_map<int, vector<int>> preference;
    for (int i = 0; i < n; i++) {
        preference[i] = preferences[i];
    }
    
    // Create a dictionary to store the partner of each friend
    unordered_map<int, int> partner;
    for (auto& pair : pairs) {
        partner[pair[0]] = pair[1];
        partner[pair[1]] = pair[0];
    }
    
    // Initialize count of unhappy friends
    int unhappy_count = 0;
    
    // Iterate through each friend
    for (int i = 0; i < n; i++) {
        // Check if friend i is unhappy
        bool is_unhappy = false;
        for (int j = 0; j < preference[i].size(); j++) {
            if (preference[i][j] == partner[i]) break;
            if (find(preference[partner[i]].begin(), preference[partner[i]].end(), i) > find(preference[partner[i]].begin(), preference[partner[i]].end(), preference[i][j])) {
                is_unhappy = true;
                break;
            }
        }
        if (is_unhappy) unhappy_count++;
    }
    
    return unhappy_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of friends and $m$ is the average length of the preference lists.
> - **Space Complexity:** $O(n)$, for storing the partner and preference list of each friend.
> - **Optimality proof:** This approach is optimal because it involves a single pass through the preference lists and partners of each friend.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary, preference lists, partner matching.
- Problem-solving patterns identified: Checking each friend's preference list and comparing it with their current partner.
- Optimization techniques learned: Using a dictionary to store the partner and preference list of each friend.
- Similar problems to practice: Other problems involving preference lists and partner matching.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a friend is already paired before checking if they are unhappy.
- Edge cases to watch for: When a friend has no preference list or no partner.
- Performance pitfalls: Using a brute force approach that involves iterating through each friend's preference list multiple times.
- Testing considerations: Testing the function with different input sizes and preference lists.