## Election Results
**Problem Link:** https://leetcode.com/problems/election-results/description

**Problem Statement:**
- Input format and constraints: You are given a list of `candidates` where each element is a string representing a candidate's name and a list of `votes` where each element is an integer representing the index of the candidate that the corresponding voter voted for.
- Expected output format: Return the name of the candidate that is leading the election. If there is a tie for the most votes, return the lexicographically smallest name.
- Key requirements and edge cases to consider: There can be a tie for the most votes, and we should return the lexicographically smallest name in that case.
- Example test cases with explanations:
  - Example 1: 
    - Input: `candidates = ["Alice", "Bob", "Charlie"], votes = [0, 0, 1, 1, 2]`
    - Output: `"Alice"`
    - Explanation: Alice has 2 votes, Bob has 2 votes, and Charlie has 1 vote. Since Alice and Bob are tied for the most votes, we return the lexicographically smallest name, which is `"Alice"`.
  - Example 2: 
    - Input: `candidates = ["John", "Emma", "Michael"], votes = [0, 1, 0, 1, 0]`
    - Output: `"John"`
    - Explanation: John has 3 votes, Emma has 2 votes, and Michael has 0 votes. Since John has the most votes, we return his name.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the votes for each candidate by iterating through the `votes` list and incrementing the corresponding candidate's vote count.
- Step-by-step breakdown of the solution:
  1. Initialize a dictionary to store the vote count for each candidate.
  2. Iterate through the `votes` list and increment the vote count for the corresponding candidate in the dictionary.
  3. Find the maximum vote count.
  4. Find all candidates with the maximum vote count.
  5. Return the lexicographically smallest name among the candidates with the maximum vote count.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

string electionResults(vector<string>& candidates, vector<int>& votes) {
    // Initialize a dictionary to store the vote count for each candidate
    unordered_map<string, int> voteCount;
    for (const auto& candidate : candidates) {
        voteCount[candidate] = 0;
    }

    // Iterate through the votes list and increment the vote count for the corresponding candidate
    for (const auto& vote : votes) {
        voteCount[candidates[vote]]++;
    }

    // Find the maximum vote count
    int maxVotes = 0;
    for (const auto& pair : voteCount) {
        maxVotes = max(maxVotes, pair.second);
    }

    // Find all candidates with the maximum vote count
    vector<string> maxVoteCandidates;
    for (const auto& pair : voteCount) {
        if (pair.second == maxVotes) {
            maxVoteCandidates.push_back(pair.first);
        }
    }

    // Return the lexicographically smallest name among the candidates with the maximum vote count
    return *min_element(maxVoteCandidates.begin(), maxVoteCandidates.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of candidates and $m$ is the number of votes. This is because we iterate through the `candidates` list and the `votes` list once each.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candidates. This is because we store the vote count for each candidate in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the `candidates` list and the `votes` list once each. The space complexity occurs because we store the vote count for each candidate in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the vote count for each candidate and find the maximum vote count while iterating through the `votes` list.
- Detailed breakdown of the approach:
  1. Initialize a dictionary to store the vote count for each candidate.
  2. Initialize a variable to store the maximum vote count.
  3. Initialize a variable to store the lexicographically smallest name among the candidates with the maximum vote count.
  4. Iterate through the `votes` list and increment the vote count for the corresponding candidate in the dictionary.
  5. Update the maximum vote count and the lexicographically smallest name if necessary.
  6. Return the lexicographically smallest name among the candidates with the maximum vote count.
- Proof of optimality: This approach has the same time and space complexity as the brute force approach, but it avoids the need to iterate through the `voteCount` dictionary twice.
- Why further optimization is impossible: This approach has the optimal time and space complexity because it only iterates through the `votes` list once and stores the vote count for each candidate in a dictionary.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

string electionResults(vector<string>& candidates, vector<int>& votes) {
    // Initialize a dictionary to store the vote count for each candidate
    unordered_map<string, int> voteCount;
    for (const auto& candidate : candidates) {
        voteCount[candidate] = 0;
    }

    // Initialize a variable to store the maximum vote count
    int maxVotes = 0;

    // Initialize a variable to store the lexicographically smallest name among the candidates with the maximum vote count
    string maxVoteCandidate;

    // Iterate through the votes list and increment the vote count for the corresponding candidate
    for (const auto& vote : votes) {
        const auto& candidate = candidates[vote];
        voteCount[candidate]++;

        // Update the maximum vote count and the lexicographically smallest name if necessary
        if (voteCount[candidate] > maxVotes) {
            maxVotes = voteCount[candidate];
            maxVoteCandidate = candidate;
        } else if (voteCount[candidate] == maxVotes && candidate < maxVoteCandidate) {
            maxVoteCandidate = candidate;
        }
    }

    // Return the lexicographically smallest name among the candidates with the maximum vote count
    return maxVoteCandidate;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of candidates and $m$ is the number of votes. This is because we iterate through the `candidates` list and the `votes` list once each.
> - **Space Complexity:** $O(n)$, where $n$ is the number of candidates. This is because we store the vote count for each candidate in a dictionary.
> - **Optimality proof:** This approach has the optimal time and space complexity because it only iterates through the `votes` list once and stores the vote count for each candidate in a dictionary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store the vote count for each candidate, finding the maximum vote count, and finding the lexicographically smallest name among the candidates with the maximum vote count.
- Problem-solving patterns identified: Iterating through the `votes` list once and updating the maximum vote count and the lexicographically smallest name if necessary.
- Optimization techniques learned: Avoiding the need to iterate through the `voteCount` dictionary twice.
- Similar problems to practice: Other problems that involve finding the maximum or minimum value in a list or dictionary.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `voteCount` dictionary or the `maxVotes` variable correctly, not updating the `maxVotes` variable or the `maxVoteCandidate` variable correctly.
- Edge cases to watch for: Handling the case where there is a tie for the most votes, handling the case where the `votes` list is empty.
- Performance pitfalls: Iterating through the `voteCount` dictionary twice, not using a dictionary to store the vote count for each candidate.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.