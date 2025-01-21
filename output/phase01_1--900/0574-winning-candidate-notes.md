## Winning Candidate

**Problem Link:** https://leetcode.com/problems/winning-candidate/description

**Problem Statement:**
- Input format: `votes` array where `votes[i]` is the candidate's id
- Constraints: `1 <= votes.length <= 5 * 10^4`, `1 <= votes[i] <= votes.length`
- Expected output format: The id of the winning candidate
- Key requirements: Determine the candidate with the most votes
- Edge cases to consider: Multiple candidates with the same number of votes, a single candidate with all the votes
- Example test cases:
  - Input: `votes = [1, 1, 1, 3, 3]`
  - Output: `1`
  - Explanation: Candidate `1` has 3 votes, which is more than candidate `3` with 2 votes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the votes for each candidate by iterating through the `votes` array.
- Step-by-step breakdown:
  1. Initialize a `votesCount` array with zeros, where `votesCount[i]` represents the number of votes for candidate `i`.
  2. Iterate through the `votes` array and increment the corresponding count in `votesCount`.
  3. Find the maximum count in `votesCount` and return the corresponding candidate id.
- Why this approach comes to mind first: It directly addresses the problem statement by counting votes for each candidate.

```cpp
vector<int> votesCount(votes.size() + 1, 0);
for (int vote : votes) {
    votesCount[vote]++;
}
int maxVotes = 0, winningCandidate = 0;
for (int i = 1; i <= votes.size(); i++) {
    if (votesCount[i] > maxVotes) {
        maxVotes = votesCount[i];
        winningCandidate = i;
    }
}
return winningCandidate;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `votes` array. This is because we iterate through the `votes` array twice: once to count the votes and once to find the maximum count.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `votes` array. This is because we use a `votesCount` array of size $n+1$ to store the vote counts.
> - **Why these complexities occur:** The iteration through the `votes` array and the use of the `votesCount` array cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use an unordered map to store the vote counts, which allows for efficient lookup and update of vote counts.
- Detailed breakdown:
  1. Initialize an unordered map `voteCounts` to store the vote counts for each candidate.
  2. Iterate through the `votes` array and update the vote count for each candidate in `voteCounts`.
  3. Find the candidate with the maximum vote count in `voteCounts` and return their id.
- Proof of optimality: This approach has the same time complexity as the brute force approach but uses less space when the number of unique candidates is much smaller than the total number of votes.

```cpp
unordered_map<int, int> voteCounts;
int maxVotes = 0, winningCandidate = 0;
for (int vote : votes) {
    voteCounts[vote]++;
    if (voteCounts[vote] > maxVotes) {
        maxVotes = voteCounts[vote];
        winningCandidate = vote;
    }
}
return winningCandidate;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `votes` array. This is because we iterate through the `votes` array once.
> - **Space Complexity:** $O(k)$, where $k$ is the number of unique candidates. This is because we use an unordered map to store the vote counts for each candidate.
> - **Optimality proof:** This approach is optimal because it uses the minimum amount of space necessary to store the vote counts and has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Vote counting, use of unordered maps for efficient lookup and update.
- Problem-solving patterns identified: Iterating through an array and updating counts in a separate data structure.
- Optimization techniques learned: Using unordered maps to reduce space complexity.
- Similar problems to practice: Other problems involving vote counting or frequency analysis.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `votesCount` array or `voteCounts` map correctly.
- Edge cases to watch for: Multiple candidates with the same number of votes, a single candidate with all the votes.
- Performance pitfalls: Using a data structure with high overhead, such as a vector of vectors, to store the vote counts.
- Testing considerations: Test the function with different inputs, including edge cases and large inputs.