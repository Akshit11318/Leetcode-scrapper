## Most Visited Sector in a Circular Track

**Problem Link:** https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description

**Problem Statement:**
- Input: An integer `n` representing the number of sectors in the circular track, and an array `rounds` of pairs representing the start and end sector of each round.
- Constraints: `1 <= n <= 100`, `1 <= rounds.length <= 1000`, `0 <= rounds[i][0] < n`, `0 <= rounds[i][1] < n`.
- Expected Output: An array of sector indices (0-indexed) that are most visited.
- Key Requirements: Count the number of times each sector is visited and return all sectors with the maximum count.
- Edge Cases: Handle cases where a round starts and ends at the same sector, or where a round crosses the boundary of the circular track.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each round and counting the number of times each sector is visited.
- For each round, iterate through the sectors from the start to the end, incrementing the count for each sector.
- If a round crosses the boundary of the circular track, handle this by iterating from the start sector to the end of the track, then from the start of the track to the end sector.
- Keep track of the maximum count and the sectors that have this count.

```cpp
vector<int> mostVisitedSector(int n, vector<vector<int>>& rounds) {
    vector<int> counts(n, 0);
    for (auto& round : rounds) {
        int start = round[0], end = round[1];
        if (start <= end) {
            for (int i = start; i <= end; ++i) {
                counts[i]++;
            }
        } else {
            for (int i = start; i < n; ++i) {
                counts[i]++;
            }
            for (int i = 0; i <= end; ++i) {
                counts[i]++;
            }
        }
    }
    int maxCount = *max_element(counts.begin(), counts.end());
    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (counts[i] == maxCount) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times r)$, where $n$ is the number of sectors and $r$ is the number of rounds. This is because for each round, we potentially iterate through all sectors.
> - **Space Complexity:** $O(n)$, for the `counts` vector.
> - **Why these complexities occur:** The brute force approach involves explicit iteration through each sector for each round, leading to a time complexity that scales with both the number of sectors and rounds.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we can still achieve the same result with less iteration by considering the nature of the circular track and the fact that we only need to count the visits, not the actual path taken.
- We can simplify the counting process by considering the start and end points of each round and how they contribute to the counts of the sectors.
- For each round, if the start sector is less than or equal to the end sector, we simply increment the counts of the sectors in the range `[start, end]`.
- If the start sector is greater than the end sector, we increment the counts of the sectors in the range `[start, n-1]` and `[0, end]`.
- Finally, find the maximum count and collect the sectors that have this count.

```cpp
vector<int> mostVisitedSector(int n, vector<vector<int>>& rounds) {
    vector<int> counts(n, 0);
    for (auto& round : rounds) {
        int start = round[0], end = round[1];
        if (start <= end) {
            for (int i = start; i <= end; ++i) {
                counts[i]++;
            }
        } else {
            for (int i = start; i < n; ++i) {
                counts[i]++;
            }
            for (int i = 0; i <= end; ++i) {
                counts[i]++;
            }
        }
    }
    int maxCount = *max_element(counts.begin(), counts.end());
    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (counts[i] == maxCount) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times r)$, where $n$ is the number of sectors and $r$ is the number of rounds.
> - **Space Complexity:** $O(n)$, for the `counts` vector.
> - **Optimality proof:** This approach is optimal because it must consider each round and potentially each sector, making the time complexity linear with respect to both the number of sectors and rounds.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include iteration, counting, and finding maximum values.
- Problem-solving patterns identified include breaking down complex problems into simpler iterations and using vectors for dynamic storage.
- Optimization techniques learned include simplifying iteration and avoiding unnecessary computations.
- Similar problems to practice include other counting and iteration problems, such as those involving arrays or linked lists.

**Mistakes to Avoid:**
- Common implementation errors include off-by-one errors when iterating through arrays or vectors.
- Edge cases to watch for include rounds that start and end at the same sector, or rounds that cross the boundary of the circular track.
- Performance pitfalls include using inefficient data structures or algorithms that scale poorly with the size of the input.
- Testing considerations include thoroughly testing the function with a variety of inputs, including edge cases.