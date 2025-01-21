## High Five
**Problem Link:** https://leetcode.com/problems/high-five/description

**Problem Statement:**
- Input format and constraints: The input will be a list of records where each record is a list containing an ID and a score. The goal is to find the top 5 scores for each ID and calculate the average of these scores.
- Expected output format: The output should be a list of lists where each sublist contains an ID and the average of its top 5 scores. If an ID has less than 5 scores, all its scores should be used to calculate the average.
- Key requirements and edge cases to consider: 
  - Handling IDs with less than 5 scores.
  - IDs may not be consecutive or start from 1.
  - There may be duplicate IDs with the same score.
- Example test cases with explanations: 
  - For example, if the input is [[1,91],[1,92],[2,93],[2,99],[3,98],[3,100],[3,98],[4,99]], the output should be [[1,91.5],[2,96.0],[3,99.0],[4,99.0]].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through the records, sort the scores for each ID, select the top 5 scores, and then calculate the average.
- Step-by-step breakdown of the solution:
  1. Create a map to store scores for each ID.
  2. Iterate through the records and populate the map.
  3. For each ID in the map, sort its scores in descending order.
  4. Select the top 5 scores (or all scores if less than 5).
  5. Calculate the average of these top scores.
- Why this approach comes to mind first: It directly addresses the problem by considering all scores for each ID and then applying the required calculation.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<vector<double>> highFive(vector<vector<int>>& items) {
    map<int, vector<int>> idScores;
    
    // Populate the map with scores for each ID
    for (auto& item : items) {
        int id = item[0];
        int score = item[1];
        idScores[id].push_back(score);
    }
    
    vector<vector<double>> result;
    
    // For each ID, sort scores, select top 5, and calculate average
    for (auto& pair : idScores) {
        int id = pair.first;
        vector<int>& scores = pair.second;
        
        // Sort scores in descending order
        sort(scores.begin(), scores.end(), greater<int>());
        
        // Select top 5 scores (or all if less than 5)
        int count = min(5, (int)scores.size());
        double sum = 0.0;
        for (int i = 0; i < count; ++i) {
            sum += scores[i];
        }
        
        // Calculate average
        double average = sum / count;
        
        // Add result to output
        result.push_back({(double)id, average});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the scores for each ID, where $n$ is the maximum number of scores for any ID. However, considering the overall process, it's $O(N \log N)$ where $N$ is the total number of records because we iterate through all records once and then perform operations that depend on the number of unique IDs and their scores.
> - **Space Complexity:** $O(N)$ for storing scores in the map and the result vector, where $N$ is the total number of records.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation for each ID's scores, and the space complexity is due to storing all scores and the final result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all scores for each ID, we can maintain a priority queue (or a similar data structure like a multiset in C++) to keep track of the top 5 scores for each ID as we iterate through the records. This way, we avoid the sorting step and reduce the time complexity.
- Detailed breakdown of the approach:
  1. Create a map to store the top 5 scores for each ID.
  2. Iterate through the records, and for each record, insert the score into the appropriate ID's data structure, maintaining only the top 5 scores.
  3. After processing all records, calculate the average of the top 5 scores for each ID.
- Proof of optimality: This approach is optimal because it processes each record exactly once and uses a data structure that efficiently maintains the top scores without needing to sort all scores.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct ScoreComparator {
    bool operator()(const int& a, const int& b) {
        return a < b;
    }
};

vector<vector<double>> highFive(vector<vector<int>>& items) {
    map<int, priority_queue<int, vector<int>, ScoreComparator>> idScores;
    
    // Populate the map with top 5 scores for each ID
    for (auto& item : items) {
        int id = item[0];
        int score = item[1];
        
        if (idScores[id].size() < 5) {
            idScores[id].push(score);
        } else if (score > idScores[id].top()) {
            idScores[id].pop();
            idScores[id].push(score);
        }
    }
    
    vector<vector<double>> result;
    
    // For each ID, calculate average of top 5 scores
    for (auto& pair : idScores) {
        int id = pair.first;
        priority_queue<int, vector<int>, ScoreComparator> scores = pair.second;
        
        double sum = 0.0;
        int count = scores.size();
        for (int i = 0; i < count; ++i) {
            sum += scores.top();
            scores.pop();
        }
        
        // Calculate average
        double average = sum / count;
        
        // Add result to output
        result.push_back({(double)id, average});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log 5)$ because for each record, we might insert into or remove from the priority queue, and these operations take $\log k$ time where $k=5$ in our case. Since we do this for $N$ records, the overall time complexity simplifies to $O(N)$ because $\log 5$ is a constant.
> - **Space Complexity:** $O(N)$ for storing the top 5 scores for each ID.
> - **Optimality proof:** This approach is optimal because it processes each record once and maintains only the necessary information (top 5 scores) for each ID, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, maps, and efficient data structure choices.
- Problem-solving patterns identified: Maintaining a limited set of top elements, using data structures to reduce computational complexity.
- Optimization techniques learned: Avoiding unnecessary sorting, using priority queues for top-k problems.
- Similar problems to practice: Top-k elements in an array, median of two sorted arrays, etc.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of priority queues, not checking for edge cases like IDs with less than 5 scores.
- Edge cases to watch for: Handling IDs with duplicate scores, ensuring the data structure can handle a large number of unique IDs.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time or space complexity than necessary.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large datasets to ensure correctness and performance.