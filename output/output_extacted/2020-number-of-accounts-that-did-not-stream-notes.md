## Number of Accounts That Did Not Stream

**Problem Link:** https://leetcode.com/problems/number-of-accounts-that-did-not-stream/description

**Problem Statement:**
- Input: A list of integers `accounts` where each integer represents an account ID and a list of integers `streamed` where each integer represents an account ID that streamed.
- Constraints: 
  - `1 <= accounts.length <= 100`
  - `1 <= streamed.length <= 100`
- Expected Output: The number of account IDs that did not stream.
- Key Requirements and Edge Cases:
  - Handle cases where `accounts` or `streamed` lists are empty.
  - Ensure the comparison between account IDs is case-sensitive if applicable.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each account ID in `accounts` and check if it exists in the `streamed` list.
- Step-by-step breakdown:
  1. Initialize a counter to store the number of accounts that did not stream.
  2. Iterate through each account ID in `accounts`.
  3. For each account ID, check if it exists in the `streamed` list.
  4. If it does not exist, increment the counter.
  5. Return the counter at the end.

```cpp
class Solution {
public:
    int numberOfAccountsThatDidNotStream(vector<int>& accounts, vector<int>& streamed) {
        int count = 0;
        for (int account : accounts) {
            bool found = false;
            for (int stream : streamed) {
                if (account == stream) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n*m)$ where $n$ is the number of accounts and $m$ is the number of streamed accounts. This is because for each account, we potentially iterate through all streamed accounts.
> - **Space Complexity:** $O(1)$, excluding the space needed for input and output, since we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loop structure, which checks each account against each streamed account.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Convert the `streamed` list into a `set` for efficient lookups. Checking membership in a set is an $O(1)$ operation on average.
- Detailed breakdown:
  1. Convert the `streamed` list into a set.
  2. Iterate through each account ID in `accounts`.
  3. For each account ID, check if it exists in the `streamed` set.
  4. If it does not exist, increment the counter.
  5. Return the counter at the end.

```cpp
class Solution {
public:
    int numberOfAccountsThatDidNotStream(vector<int>& accounts, vector<int>& streamed) {
        unordered_set<int> streamedSet(streamed.begin(), streamed.end());
        int count = 0;
        for (int account : accounts) {
            if (streamedSet.find(account) == streamedSet.end()) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of accounts and $m$ is the number of streamed accounts. This is because we first convert the `streamed` list into a set ($O(m)$), and then iterate through each account ($O(n)$).
> - **Space Complexity:** $O(m)$, excluding the space needed for input and output, since we store the `streamed` accounts in a set.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by utilizing a data structure (set) that allows for constant time membership tests, reducing the overall time complexity from $O(n*m)$ to $O(n + m)$.

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem. In this case, using a `set` for the `streamed` accounts significantly improves the efficiency of the solution.
- Understanding the trade-offs between different approaches, including time and space complexity.
- Recognizing that sometimes, a small optimization (like using a set for lookup) can significantly improve the performance of an algorithm.

**Mistakes to Avoid:**
- Not considering the impact of data structure choice on algorithm performance.
- Failing to analyze the time and space complexity of an algorithm.
- Not testing edge cases, such as empty input lists.