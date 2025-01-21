## Grand Slam Titles
**Problem Link:** https://leetcode.com/problems/grand-slam-titles/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `tournaments` where each element is an array of two integers representing the year and the type of the tournament. The constraints are that the number of tournaments will not exceed 1000 and the year range is from 1900 to 2016.
- Expected output format: The output should be the number of Grand Slam titles won by the player.
- Key requirements and edge cases to consider: A Grand Slam title is won if a player wins all four tournaments in the same year. The edge cases are when the input array is empty or when there are no Grand Slam titles won.
- Example test cases with explanations: 
  - For example, if the input is `[[1995,1],[1995,2],[1995,3],[1995,4]]`, the output should be `1` because the player won all four tournaments in the year 1995.
  - If the input is `[[1995,1],[1995,2],[1995,3]]`, the output should be `0` because the player did not win all four tournaments in the year 1995.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to iterate over all possible years and check if the player won all four tournaments in each year.
- Step-by-step breakdown of the solution: 
  1. Create a dictionary to store the tournaments won by the player for each year.
  2. Iterate over the input array and store the tournaments won by the player for each year in the dictionary.
  3. Iterate over the dictionary and check if the player won all four tournaments in each year.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large inputs.

```cpp
int grandSlamTitles(vector<vector<int>>& tournaments) {
    unordered_map<int, unordered_set<int>> yearTournaments;
    for (auto& tournament : tournaments) {
        int year = tournament[0];
        int type = tournament[1];
        yearTournaments[year].insert(type);
    }
    int count = 0;
    for (auto& year : yearTournaments) {
        if (year.second.size() == 4) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tournaments. This is because we iterate over the input array once to store the tournaments won by the player for each year, and then iterate over the dictionary once to check if the player won all four tournaments in each year.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tournaments. This is because we use a dictionary to store the tournaments won by the player for each year.
> - **Why these complexities occur:** These complexities occur because we use a dictionary to store the tournaments won by the player for each year, which requires $O(n)$ space. We also iterate over the input array and the dictionary once each, which requires $O(n)$ time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a hash set to store the tournaments won by the player for each year, and then check if the size of the hash set is equal to 4 for each year.
- Detailed breakdown of the approach: 
  1. Create a hash set to store the tournaments won by the player for each year.
  2. Iterate over the input array and store the tournaments won by the player for each year in the hash set.
  3. Check if the size of the hash set is equal to 4 for each year, and increment the count if it is.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

```cpp
int grandSlamTitles(vector<vector<int>>& tournaments) {
    unordered_map<int, unordered_set<int>> yearTournaments;
    for (auto& tournament : tournaments) {
        int year = tournament[0];
        int type = tournament[1];
        yearTournaments[year].insert(type);
    }
    int count = 0;
    for (auto& year : yearTournaments) {
        if (year.second.size() == 4) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tournaments. This is because we iterate over the input array once to store the tournaments won by the player for each year, and then iterate over the dictionary once to check if the player won all four tournaments in each year.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tournaments. This is because we use a dictionary to store the tournaments won by the player for each year.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated in this problem is the use of a hash set to store the tournaments won by the player for each year, and then checking if the size of the hash set is equal to 4 for each year.
- Problem-solving patterns identified: The problem-solving pattern identified in this problem is to use a dictionary to store the tournaments won by the player for each year, and then iterate over the dictionary to check if the player won all four tournaments in each year.
- Optimization techniques learned: The optimization technique learned in this problem is to use a hash set to store the tournaments won by the player for each year, which reduces the time complexity of the solution.
- Similar problems to practice: Similar problems to practice are problems that involve using a dictionary or a hash set to store data and then iterating over the data to find a solution.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a list or an array to store the tournaments won by the player for each year, which can lead to a time complexity of $O(n^2)$.
- Edge cases to watch for: An edge case to watch for is when the input array is empty, in which case the solution should return 0.
- Performance pitfalls: A performance pitfall is to use a nested loop to iterate over the input array, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: A testing consideration is to test the solution with different inputs, including an empty input array and an input array with multiple Grand Slam titles.