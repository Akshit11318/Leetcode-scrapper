## Relative Ranks
**Problem Link:** https://leetcode.com/problems/relative-ranks/description

**Problem Statement:**
- Input: An array of scores `scores` where each score is in the range `[1, 10^4]`.
- Constraints: The length of `scores` is between `1` and `10^4`.
- Expected Output: An array of strings where each string represents the relative rank of the corresponding score in the input array.
- Key Requirements: The relative rank is determined by the score's position in the sorted array of scores. If two scores are the same, they should have the same rank, and the next score should have a rank that is one more than the previous rank.
- Edge Cases: If the input array is empty, return an empty array. If the input array contains only one element, return an array with the string "Gold Medal".
- Example Test Cases:
  - Input: `scores = [10,3,8,9,4]`
  - Output: `["Gold Medal","5","Bronze Medal","Silver Medal","4"]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the scores in descending order and then iterate over the sorted array to assign ranks.
- Step-by-step breakdown of the solution:
  1. Sort the scores in descending order.
  2. Initialize an empty array to store the relative ranks.
  3. Initialize a variable to keep track of the current rank.
  4. Iterate over the sorted array. For each score, check if it is the first score or if it is different from the previous score. If it is, increment the current rank and assign the rank to the current score.
  5. Iterate over the original array and replace each score with its corresponding relative rank.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> findRelativeRanks(vector<int>& scores) {
    // Create a copy of the scores array
    vector<int> sortedScores = scores;
    // Sort the scores in descending order
    sort(sortedScores.begin(), sortedScores.end(), greater<int>());
    
    // Initialize an empty array to store the relative ranks
    vector<string> relativeRanks(scores.size());
    
    // Initialize a variable to keep track of the current rank
    int currentRank = 1;
    
    // Iterate over the sorted array
    for (int i = 0; i < sortedScores.size(); i++) {
        // Check if it is the first score or if it is different from the previous score
        if (i == 0 || sortedScores[i] != sortedScores[i-1]) {
            // Increment the current rank and assign the rank to the current score
            if (currentRank == 1) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Gold Medal";
            } else if (currentRank == 2) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Silver Medal";
            } else if (currentRank == 3) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Bronze Medal";
            } else {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = to_string(currentRank);
            }
            currentRank++;
        } else {
            // If the score is the same as the previous score, assign the same rank
            if (currentRank - 1 == 1) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Gold Medal";
            } else if (currentRank - 1 == 2) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Silver Medal";
            } else if (currentRank - 1 == 3) {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = "Bronze Medal";
            } else {
                relativeRanks[find(scores.begin(), scores.end(), sortedScores[i]) - scores.begin()] = to_string(currentRank - 1);
            }
        }
    }
    
    return relativeRanks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using a nested loop to find the index of each score in the original array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are creating a copy of the input array and an additional array to store the relative ranks.
> - **Why these complexities occur:** The nested loop causes the time complexity to be quadratic, and the additional arrays cause the space complexity to be linear.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a `map` to store the scores and their corresponding indices, and then iterate over the sorted array to assign ranks.
- Detailed breakdown of the approach:
  1. Create a `map` to store the scores and their corresponding indices.
  2. Sort the scores in descending order.
  3. Initialize an empty array to store the relative ranks.
  4. Iterate over the sorted array. For each score, find its index in the original array and assign the corresponding rank.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

vector<string> findRelativeRanks(vector<int>& scores) {
    // Create a map to store the scores and their corresponding indices
    map<int, int> scoreIndexMap;
    for (int i = 0; i < scores.size(); i++) {
        scoreIndexMap[scores[i]] = i;
    }
    
    // Sort the scores in descending order
    sort(scores.begin(), scores.end(), greater<int>());
    
    // Initialize an empty array to store the relative ranks
    vector<string> relativeRanks(scores.size());
    
    // Initialize a variable to keep track of the current rank
    int currentRank = 1;
    
    // Iterate over the sorted array
    for (int i = 0; i < scores.size(); i++) {
        // Check if it is the first score or if it is different from the previous score
        if (i == 0 || scores[i] != scores[i-1]) {
            // Increment the current rank and assign the rank to the current score
            if (currentRank == 1) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Gold Medal";
            } else if (currentRank == 2) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Silver Medal";
            } else if (currentRank == 3) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Bronze Medal";
            } else {
                relativeRanks[scoreIndexMap[scores[i]]] = to_string(currentRank);
            }
            currentRank++;
        } else {
            // If the score is the same as the previous score, assign the same rank
            if (currentRank - 1 == 1) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Gold Medal";
            } else if (currentRank - 1 == 2) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Silver Medal";
            } else if (currentRank - 1 == 3) {
                relativeRanks[scoreIndexMap[scores[i]]] = "Bronze Medal";
            } else {
                relativeRanks[scoreIndexMap[scores[i]]] = to_string(currentRank - 1);
            }
        }
    }
    
    return relativeRanks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we are using the `sort` function to sort the scores in descending order.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are creating a `map` to store the scores and their corresponding indices, and an additional array to store the relative ranks.
> - **Optimality proof:** This solution is optimal because we are using a `map` to store the scores and their corresponding indices, which allows us to assign ranks in a single pass over the sorted array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, maps, and iteration.
- Problem-solving patterns identified: using a `map` to store scores and their corresponding indices, and iterating over the sorted array to assign ranks.
- Optimization techniques learned: using a `map` to reduce the time complexity of finding the index of each score in the original array.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array or an array with only one element.
- Edge cases to watch for: handling the case where two scores are the same, and assigning the same rank to both scores.
- Performance pitfalls: using a nested loop to find the index of each score in the original array, which can result in a time complexity of $O(n^2)$.