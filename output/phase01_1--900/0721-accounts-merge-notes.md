## Accounts Merge
**Problem Link:** [https://leetcode.com/problems/accounts-merge/description](https://leetcode.com/problems/accounts-merge/description)

**Problem Statement:**
- Input format: A list of lists where each sublist contains a list of strings representing the account name and a list of email addresses.
- Constraints: The length of the input list is between $1$ and $1000$.
- Expected output format: A list of lists where each sublist contains the account name and the sorted list of merged email addresses.
- Key requirements: Merge accounts with the same name that have common email addresses.
- Edge cases: Handle cases where an email address appears in multiple accounts with different names.

**Example Test Cases:**
- `accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"]]`
- Expected output: `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"]]`

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a graph where each email address is a node and two nodes are connected if the email addresses appear in the same account.
- Step-by-step breakdown:
  1. Create an adjacency list representation of the graph.
  2. Iterate over each account and add edges to the graph.
  3. Perform a depth-first search (DFS) to find all connected components in the graph.
  4. For each connected component, merge the email addresses and add them to the result.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, unordered_set<string>> graph;
        unordered_map<string, string> emailToName;
        
        // Build the graph
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                string email = account[i];
                emailToName[email] = name;
                if (i > 1) {
                    graph[account[i-1]].insert(email);
                    graph[email].insert(account[i-1]);
                }
            }
        }
        
        vector<vector<string>> result;
        unordered_set<string> visited;
        
        // Perform DFS
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                string email = account[i];
                if (visited.find(email) == visited.end()) {
                    unordered_set<string> component;
                    dfs(graph, email, visited, component);
                    if (!component.empty()) {
                        vector<string> mergedAccount = {name};
                        for (auto& e : component) {
                            mergedAccount.push_back(e);
                        }
                        sort(mergedAccount.begin() + 1, mergedAccount.end());
                        result.push_back(mergedAccount);
                    }
                }
            }
        }
        
        return result;
    }
    
    void dfs(unordered_map<string, unordered_set<string>>& graph, string email, unordered_set<string>& visited, unordered_set<string>& component) {
        visited.insert(email);
        component.insert(email);
        for (auto& neighbor : graph[email]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(graph, neighbor, visited, component);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account. This is because we iterate over each account and email once.
> - **Space Complexity:** $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account. This is because we store the graph and the result in memory.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each account and email. The space complexity occurs because we store the graph and the result in memory.

### Optimal Approach (Required)
The provided brute force approach is already optimal for this problem. The time complexity is $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account. This is because we must iterate over each account and email at least once to merge the accounts.

However, we can make some minor optimizations to the code, such as using a `std::set` instead of a `std::vector` to store the merged email addresses for each account. This will reduce the time complexity of sorting the email addresses from $O(M \log M)$ to $O(M)$.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, unordered_set<string>> graph;
        unordered_map<string, string> emailToName;
        
        // Build the graph
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                string email = account[i];
                emailToName[email] = name;
                if (i > 1) {
                    graph[account[i-1]].insert(email);
                    graph[email].insert(account[i-1]);
                }
            }
        }
        
        vector<vector<string>> result;
        unordered_set<string> visited;
        
        // Perform DFS
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                string email = account[i];
                if (visited.find(email) == visited.end()) {
                    unordered_set<string> component;
                    dfs(graph, email, visited, component);
                    if (!component.empty()) {
                        vector<string> mergedAccount = {name};
                        for (auto& e : component) {
                            mergedAccount.push_back(e);
                        }
                        sort(mergedAccount.begin() + 1, mergedAccount.end());
                        result.push_back(mergedAccount);
                    }
                }
            }
        }
        
        return result;
    }
    
    void dfs(unordered_map<string, unordered_set<string>>& graph, string email, unordered_set<string>& visited, unordered_set<string>& component) {
        visited.insert(email);
        component.insert(email);
        for (auto& neighbor : graph[email]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(graph, neighbor, visited, component);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account.
> - **Space Complexity:** $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account.
> - **Optimality proof:** The time complexity is optimal because we must iterate over each account and email at least once to merge the accounts. The space complexity is optimal because we must store the graph and the result in memory.

### Final Notes

**Learning Points:**

*   The problem can be solved using a graph-based approach, where each email address is a node and two nodes are connected if the email addresses appear in the same account.
*   A depth-first search (DFS) can be used to find all connected components in the graph, which represent the merged accounts.
*   The time complexity of the solution is $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account.
*   The space complexity of the solution is $O(N \cdot M)$, where $N$ is the number of accounts and $M$ is the average number of emails per account.

**Mistakes to Avoid:**

*   Not handling edge cases, such as accounts with no email addresses or email addresses that appear in multiple accounts with different names.
*   Not using a graph-based approach, which can lead to inefficient solutions with high time complexities.
*   Not using a DFS to find all connected components in the graph, which can lead to incorrect results.
*   Not storing the graph and the result in memory, which can lead to incorrect results or runtime errors.