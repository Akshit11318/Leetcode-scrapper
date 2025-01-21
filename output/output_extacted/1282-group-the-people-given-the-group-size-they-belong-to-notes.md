## Group the People Given the Group Size They Belong To
**Problem Link:** https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description

**Problem Statement:**
- Input format and constraints: The input is a list of integers where each integer represents the group size that the person belongs to. The constraint is that each person can only be in one group.
- Expected output format: The output should be a list of lists where each sublist contains the indices of people in the same group.
- Key requirements and edge cases to consider: The number of people in each group should match the group size, and each person can only be in one group.
- Example test cases with explanations:
  - Input: `[3,3,3,3,3,1,3]`
  - Output: `[[5],[0,1,2],[4,6]]`
  - Explanation: There are three groups of size 3, and one group of size 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the input list and grouping people based on their group size.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the groups where the key is the group size and the value is a list of lists containing the indices of people in each group.
  2. Iterate over the input list and for each person, check if a group of the corresponding size exists in the dictionary.
  3. If a group exists, add the person's index to the last group of the corresponding size. If not, create a new group.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large inputs.

```cpp
vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
    vector<vector<int>> result;
    unordered_map<int, vector<vector<int>>> groups;
    
    for (int i = 0; i < groupSizes.size(); i++) {
        int size = groupSizes[i];
        if (groups.find(size) == groups.end()) {
            groups[size] = {};
        }
        
        if (groups[size].empty() || groups[size].back().size() == size) {
            groups[size].push_back({i});
        } else {
            groups[size].back().push_back(i);
        }
        
        if (groups[size].back().size() == size) {
            result.push_back(groups[size].back());
            groups[size].pop_back();
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of people. This is because we iterate over the input list once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of people. This is because we store the groups in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the input list once, and the space complexity occurs because we store the groups in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a dictionary to store the groups and iterating over the input list only once.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the groups where the key is the group size and the value is a list of lists containing the indices of people in each group.
  2. Iterate over the input list and for each person, check if a group of the corresponding size exists in the dictionary.
  3. If a group exists, add the person's index to the last group of the corresponding size. If not, create a new group.
- Proof of optimality: This approach is optimal because we iterate over the input list only once and use a dictionary to store the groups, which allows us to look up and insert groups in constant time.

```cpp
vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
    vector<vector<int>> result;
    unordered_map<int, vector<vector<int>>> groups;
    
    for (int i = 0; i < groupSizes.size(); i++) {
        int size = groupSizes[i];
        groups[size].push_back({i});
        
        if (groups[size].back().size() == size) {
            result.push_back(groups[size].back());
            groups[size].pop_back();
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of people. This is because we iterate over the input list once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of people. This is because we store the groups in a dictionary.
> - **Optimality proof:** This approach is optimal because we iterate over the input list only once and use a dictionary to store the groups, which allows us to look up and insert groups in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary, iteration, and grouping.
- Problem-solving patterns identified: Using a dictionary to store groups and iterating over the input list only once.
- Optimization techniques learned: Using a dictionary to look up and insert groups in constant time.
- Similar problems to practice: Grouping problems, dictionary problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a group exists before adding a person to it, not removing a group from the dictionary when it is full.
- Edge cases to watch for: Empty input list, group size of 1.
- Performance pitfalls: Iterating over the input list multiple times, using a data structure that does not allow constant time lookup and insertion.
- Testing considerations: Test with different input sizes, test with different group sizes, test with edge cases.