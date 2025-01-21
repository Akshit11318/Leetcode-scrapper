## Number of Calls Between Two Persons

**Problem Link:** https://leetcode.com/problems/number-of-calls-between-two-persons/description

**Problem Statement:**
- Input format and constraints: The problem involves analyzing a list of call logs where each log contains the caller, the receiver, and the duration of the call. The goal is to find the number of calls between two persons.
- Expected output format: The output should be the total number of calls between two persons.
- Key requirements and edge cases to consider: We need to consider all possible pairs of persons and count the number of calls between them. We should also handle cases where there are no calls between two persons.
- Example test cases with explanations:
  - Example 1: `calls = [[1, 2, 3], [2, 1, 1], [1, 3, 2], [3, 2, 1]]`, the output should be `3` because there are 3 calls between person 1 and person 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over all pairs of persons and count the number of calls between them.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the number of calls between each pair of persons.
  2. Iterate over each call log.
  3. For each call log, check if the caller and receiver are in the dictionary.
  4. If they are, increment the count of calls between them.
  5. If not, add them to the dictionary with a count of 1.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int numberOfCalls(vector<vector<int>>& calls) {
    unordered_map<string, int> callCount;
    for (auto& call : calls) {
        string key1 = to_string(call[0]) + "," + to_string(call[1]);
        string key2 = to_string(call[1]) + "," + to_string(call[0]);
        if (callCount.find(key1) != callCount.end()) {
            callCount[key1]++;
        } else if (callCount.find(key2) != callCount.end()) {
            callCount[key2]++;
        } else {
            callCount[key1] = 1;
        }
    }
    int maxCalls = 0;
    for (auto& pair : callCount) {
        maxCalls = max(maxCalls, pair.second);
    }
    return maxCalls;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of call logs, because in the worst case, we need to iterate over all pairs of persons.
> - **Space Complexity:** $O(n)$ where $n$ is the number of call logs, because we need to store the number of calls between each pair of persons.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are iterating over all pairs of persons, and the space complexity is $O(n)$ because we are storing the number of calls between each pair of persons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the number of calls between each pair of persons.
- Detailed breakdown of the approach:
  1. Create a hash map to store the number of calls between each pair of persons.
  2. Iterate over each call log.
  3. For each call log, check if the caller and receiver are in the hash map.
  4. If they are, increment the count of calls between them.
  5. If not, add them to the hash map with a count of 1.
- Proof of optimality: This approach is optimal because we are only iterating over each call log once, and we are using a hash map to store the number of calls between each pair of persons, which allows us to look up and update the count in constant time.
- Why further optimization is impossible: This approach is already optimal because we are only iterating over each call log once, and we are using a hash map to store the number of calls between each pair of persons.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int numberOfCalls(vector<vector<int>>& calls) {
    unordered_map<string, int> callCount;
    for (auto& call : calls) {
        string key = to_string(min(call[0], call[1])) + "," + to_string(max(call[0], call[1]));
        callCount[key]++;
    }
    int maxCalls = 0;
    for (auto& pair : callCount) {
        maxCalls = max(maxCalls, pair.second);
    }
    return maxCalls;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of call logs, because we are only iterating over each call log once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of call logs, because we are storing the number of calls between each pair of persons.
> - **Optimality proof:** This approach is optimal because we are only iterating over each call log once, and we are using a hash map to store the number of calls between each pair of persons, which allows us to look up and update the count in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hash map to store the number of calls between each pair of persons.
- Problem-solving patterns identified: Iterating over each call log and updating the count of calls between each pair of persons.
- Optimization techniques learned: Using a hash map to store the number of calls between each pair of persons, which allows us to look up and update the count in constant time.
- Similar problems to practice: Problems that involve counting the number of occurrences of each element in a list.

**Mistakes to Avoid:**
- Common implementation errors: Not using a hash map to store the number of calls between each pair of persons, which can lead to a time complexity of $O(n^2)$.
- Edge cases to watch for: Handling cases where there are no calls between two persons.
- Performance pitfalls: Not using a hash map to store the number of calls between each pair of persons, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different inputs to ensure that it is working correctly.