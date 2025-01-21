## Strong Friendship
**Problem Link:** https://leetcode.com/problems/strong-friendship/description

**Problem Statement:**
- Input format and constraints: The problem provides a list of friendships where each friendship is represented as an array of two integers. The goal is to find the number of `n` people who have `k` friends where `n` and `k` are given as input.
- Expected output format: The function should return the number of people who have `k` friends.
- Key requirements and edge cases to consider: The function should handle cases where there are multiple friendships between the same people, and it should also handle cases where the input list is empty.
- Example test cases with explanations: For example, given `n = 2`, `k = 1`, and `friends = [[0,1]]`, the function should return `2` because both people have one friend.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to create an adjacency list to represent the friendships between people. Then, we can iterate over each person and count the number of friends they have.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list to represent the friendships between people.
  2. Iterate over each person and count the number of friends they have.
  3. Increment a counter for each person who has `k` friends.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It involves creating a data structure to represent the friendships and then iterating over each person to count their friends.

```cpp
int countPeopleWithKFriends(int n, int k, vector<vector<int>>& friends) {
    vector<int> friendCounts(n, 0);
    for (auto& friendship : friends) {
        friendCounts[friendship[0]]++;
        friendCounts[friendship[1]]++;
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (friendCounts[i] == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of people and $m$ is the number of friendships. This is because we iterate over each friendship to update the friend counts, and then we iterate over each person to count the number of people with `k` friends.
> - **Space Complexity:** $O(n)$ where $n$ is the number of people. This is because we need to store the friend counts for each person.
> - **Why these complexities occur:** These complexities occur because we need to iterate over each friendship and each person to solve the problem.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we need to iterate over each friendship and each person to solve the problem. However, we can optimize the code by using a more efficient data structure, such as an unordered map, to store the friend counts.
- Detailed breakdown of the approach:
  1. Create an unordered map to store the friend counts for each person.
  2. Iterate over each friendship and update the friend counts in the map.
  3. Iterate over the map and count the number of people with `k` friends.
- Proof of optimality: This approach is optimal because we need to iterate over each friendship and each person to solve the problem. We cannot do better than $O(n + m)$ time complexity because we need to read the input.

```cpp
int countPeopleWithKFriends(int n, int k, vector<vector<int>>& friends) {
    unordered_map<int, int> friendCounts;
    for (auto& friendship : friends) {
        friendCounts[friendship[0]]++;
        friendCounts[friendship[1]]++;
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (friendCounts[i] == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of people and $m$ is the number of friendships. This is because we iterate over each friendship to update the friend counts, and then we iterate over each person to count the number of people with `k` friends.
> - **Space Complexity:** $O(n)$ where $n$ is the number of people. This is because we need to store the friend counts for each person.
> - **Optimality proof:** This approach is optimal because we need to iterate over each friendship and each person to solve the problem. We cannot do better than $O(n + m)$ time complexity because we need to read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, counting, and using data structures to solve problems.
- Problem-solving patterns identified: Using a data structure to store intermediate results and then iterating over the data structure to solve the problem.
- Optimization techniques learned: Using a more efficient data structure, such as an unordered map, to store intermediate results.
- Similar problems to practice: Other problems that involve counting and iterating over data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases, and not using efficient data structures.
- Edge cases to watch for: Empty input, invalid input, and cases where the number of friendships is much larger than the number of people.
- Performance pitfalls: Using inefficient data structures, not optimizing the code, and not considering the time and space complexity of the solution.
- Testing considerations: Testing the code with different inputs, edge cases, and large datasets to ensure that it works correctly and efficiently.