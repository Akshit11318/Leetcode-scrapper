## Online Election
**Problem Link:** https://leetcode.com/problems/online-election/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a class `TopVotedCandidate` with methods `q` and `leaderBoard`. The `q` method takes an integer `t` and returns the candidate who is leading at time `t`, and the `leaderBoard` method returns a list of the leading candidates at each time point.
- Expected output format: The `q` method should return the candidate who is leading at time `t`, and the `leaderBoard` method should return a list of the leading candidates at each time point.
- Key requirements and edge cases to consider: The class should handle multiple queries and return the correct leading candidate at each time point. It should also handle edge cases such as an empty list of votes or an invalid time point.
- Example test cases with explanations:
    - `["TopVotedCandidate", "q", "q", "q", "q", "q", "q", "q", "leaderBoard"]`
      `[[[0,1,1,0,0,1,0]], [3], [12], [25], [15], [24], [8], [17], []]`
      The expected output is `[1, 1, 0, 0, 0, 1, 1, 1, [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through the list of votes and counting the votes for each candidate at each time point. The candidate with the most votes at each time point is considered the leading candidate.
- Step-by-step breakdown of the solution:
    1. Initialize a list to store the leading candidates at each time point.
    2. Iterate through the list of votes and count the votes for each candidate at each time point.
    3. At each time point, find the candidate with the most votes and add them to the list of leading candidates.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
class TopVotedCandidate {
public:
    vector<int> votes;
    TopVotedCandidate(vector<int> persons, vector<int> times) {
        votes = persons;
        // ...
    }
    
    int q(int t) {
        int time = 0;
        for (int i = 0; i < votes.size(); i++) {
            if (time == t) {
                int maxCount = 0;
                int leader = votes[i];
                for (int j = 0; j < votes.size(); j++) {
                    int count = 0;
                    for (int k = 0; k <= i; k++) {
                        if (votes[k] == votes[j]) {
                            count++;
                        }
                    }
                    if (count > maxCount) {
                        maxCount = count;
                        leader = votes[j];
                    }
                }
                return leader;
            }
            time++;
        }
        return -1; // time not found
    }
    
    vector<int> leaderBoard() {
        vector<int> leaders;
        for (int i = 0; i < votes.size(); i++) {
            int maxCount = 0;
            int leader = votes[i];
            for (int j = 0; j < votes.size(); j++) {
                int count = 0;
                for (int k = 0; k <= i; k++) {
                    if (votes[k] == votes[j]) {
                        count++;
                    }
                }
                if (count > maxCount) {
                    maxCount = count;
                    leader = votes[j];
                }
            }
            leaders.push_back(leader);
        }
        return leaders;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of votes, due to the nested loops in the `q` and `leaderBoard` methods.
> - **Space Complexity:** $O(n)$ where $n$ is the number of votes, for storing the list of leading candidates.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, and the space complexity is linear due to the storage of the leading candidates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `map` to store the count of votes for each candidate at each time point. This allows for efficient lookup and update of the vote counts.
- Detailed breakdown of the approach:
    1. Initialize a `map` to store the count of votes for each candidate at each time point.
    2. Iterate through the list of votes and update the vote counts in the `map`.
    3. At each time point, find the candidate with the most votes and add them to the list of leading candidates.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$ where $n$ is the number of votes, which is the best possible complexity for this problem.

```cpp
class TopVotedCandidate {
public:
    vector<int> votes;
    vector<int> times;
    map<int, int> voteCounts;
    vector<int> leaders;
    
    TopVotedCandidate(vector<int> persons, vector<int> times) {
        votes = persons;
        this->times = times;
        leaders.resize(times.size());
        int maxCount = 0;
        int leader = -1;
        for (int i = 0; i < votes.size(); i++) {
            voteCounts[votes[i]]++;
            if (voteCounts[votes[i]] >= maxCount) {
                maxCount = voteCounts[votes[i]];
                leader = votes[i];
            }
            leaders[i] = leader;
        }
    }
    
    int q(int t) {
        return leaders[lower_bound(times.begin(), times.end(), t) - times.begin()];
    }
    
    vector<int> leaderBoard() {
        return leaders;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of votes, for initializing the `map` and updating the vote counts.
> - **Space Complexity:** $O(n)$ where $n$ is the number of votes, for storing the `map` and the list of leading candidates.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a `map` to store and update vote counts, and the use of a `vector` to store the leading candidates.
- Problem-solving patterns identified: The problem requires identifying the leading candidate at each time point, and updating the vote counts accordingly.
- Optimization techniques learned: The optimal solution involves using a `map` to store and update vote counts, which reduces the time complexity from $O(n^3)$ to $O(n)$.
- Similar problems to practice: Problems that involve updating and querying data in real-time, such as stock prices or social media feeds.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the vote counts correctly, or failing to handle edge cases such as an empty list of votes.
- Edge cases to watch for: Handling edge cases such as an empty list of votes, or a time point that is not found in the list of times.
- Performance pitfalls: Using a brute force approach with a high time complexity, or failing to optimize the solution for large inputs.
- Testing considerations: Testing the solution with large inputs and edge cases to ensure that it performs correctly and efficiently.