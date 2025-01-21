## Optimal Account Balancing
**Problem Link:** https://leetcode.com/problems/optimal-account-balancing/description

**Problem Statement:**
- Input format: A 2D array `transactions` where `transactions[i]` represents a transaction, with `transactions[i][0]` being the account ID and `transactions[i][1]` being the transaction amount.
- Constraints: Each account ID is a unique integer, and the transaction amount can be positive (representing a deposit) or negative (representing a withdrawal).
- Expected output format: The minimum number of transactions required to balance all accounts.
- Key requirements and edge cases to consider:
  - Handling cases with no transactions.
  - Handling cases where it's impossible to balance all accounts (e.g., if the total of all transaction amounts is not zero).
- Example test cases with explanations:
  - `transactions = [[1,2],[2,1],[1,-2]]`: This should return `2` because we can balance accounts by moving `2` from account `1` to account `2`, and then moving `1` from account `2` back to account `1`, effectively cancelling out the initial transactions.
  - `transactions = [[1,5],[2,3],[3,4]]`: This should return `3` because we need at least three transactions to balance these accounts, considering the amounts and the requirement to minimize the number of transactions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of transactions to find the minimum number required to balance all accounts.
- Step-by-step breakdown of the solution:
  1. Calculate the net balance for each account by summing up all transaction amounts associated with that account.
  2. Attempt to find combinations of transactions that can balance the accounts by moving funds from accounts with a positive balance to those with a negative balance.
  3. Since this approach involves trying all possible combinations, it can be extremely inefficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int minTransfers(std::vector<std::vector<int>>& transactions) {
    std::vector<int> balances;
    // Calculate net balance for each account
    for (auto& transaction : transactions) {
        int account = transaction[0];
        int amount = transaction[1];
        // Simplified for explanation; actual implementation needs to handle account indexing correctly
        if (balances.size() <= account) {
            balances.resize(account + 1);
        }
        balances[account] += amount;
    }
    
    // Remove zero balances as they do not affect the minimum number of transactions
    std::vector<int> nonZeroBalances;
    for (int balance : balances) {
        if (balance != 0) {
            nonZeroBalances.push_back(balance);
        }
    }
    
    // Brute force approach to find minimum transactions
    int minTransactions = INT_MAX;
    // This part is highly inefficient and not practical for large inputs
    // It's meant to illustrate the brute force thought process rather than be implemented as is.
    return minTransactions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of non-zero balances, because in the worst case, we might have to consider all possible subsets of transactions.
> - **Space Complexity:** $O(n)$, for storing the non-zero balances.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of transactions, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a graph theory approach, specifically by constructing a flow network where each account is a node, and the edges represent possible transactions between accounts. The minimum number of transactions corresponds to the maximum flow in this network, with each transaction being a unit of flow.
- Detailed breakdown of the approach:
  1. Construct a flow network with a source node connected to all accounts with a positive balance and a sink node connected to all accounts with a negative balance.
  2. The capacity of each edge from the source to an account is the account's positive balance, and the capacity of each edge from an account to the sink is the account's negative balance.
  3. Find the maximum flow in this network, which represents the maximum amount that can be transferred in a single transaction.
  4. The minimum number of transactions is then the total sum of all balances divided by the maximum flow, considering that each transaction can transfer up to the maximum flow amount.

```cpp
#include <vector>
#include <queue>
#include <limits>

struct Edge {
    int to, capacity, rev;
};

int minTransfers(std::vector<std::vector<int>>& transactions) {
    // Calculate net balance for each account
    std::vector<int> balances;
    for (auto& transaction : transactions) {
        int account = transaction[0];
        int amount = transaction[1];
        if (balances.size() <= account) {
            balances.resize(account + 1, 0);
        }
        balances[account] += amount;
    }
    
    // Remove zero balances
    std::vector<int> nonZeroBalances;
    for (int balance : balances) {
        if (balance != 0) {
            nonZeroBalances.push_back(balance);
        }
    }
    
    int source = nonZeroBalances.size();
    int sink = nonZeroBalances.size() + 1;
    std::vector<std::vector<Edge>> graph(sink + 1);
    
    // Construct flow network
    for (int i = 0; i < nonZeroBalances.size(); ++i) {
        if (nonZeroBalances[i] > 0) {
            // Edge from source to account
            graph[source].push_back({i, nonZeroBalances[i], graph[i].size()});
            graph[i].push_back({source, 0, graph[source].size() - 1});
        } else {
            // Edge from account to sink
            graph[i].push_back({sink, -nonZeroBalances[i], graph[sink].size()});
            graph[sink].push_back({i, 0, graph[i].size() - 1});
        }
    }
    
    for (int i = 0; i < nonZeroBalances.size(); ++i) {
        for (int j = 0; j < nonZeroBalances.size(); ++j) {
            if (nonZeroBalances[i] > 0 && nonZeroBalances[j] < 0) {
                // Edge from account i to account j
                graph[i].push_back({j, std::min(nonZeroBalances[i], -nonZeroBalances[j]), graph[j].size()});
                graph[j].push_back({i, 0, graph[i].size() - 1});
            }
        }
    }
    
    int maxFlow = 0;
    while (true) {
        std::vector<int> level(sink + 1, -1);
        level[source] = 0;
        std::queue<int> queue;
        queue.push(source);
        
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (auto& edge : graph[u]) {
                if (edge.capacity > 0 && level[edge.to] < 0) {
                    level[edge.to] = level[u] + 1;
                    queue.push(edge.to);
                }
            }
        }
        
        if (level[sink] < 0) {
            break;
        }
        
        std::vector<int> start(sink + 1, 0);
        int pathFlow = INT_MAX;
        std::vector<int> path;
        int u = sink;
        while (u != source) {
            for (int i = 0; i < graph[u].size(); ++i) {
                if (graph[u][i].capacity > 0 && level[graph[u][i].to] + 1 == level[u]) {
                    path.push_back(i);
                    pathFlow = std::min(pathFlow, graph[u][i].capacity);
                    u = graph[u][i].to;
                    break;
                }
            }
        }
        
        for (int i = path.size() - 1; i >= 0; --i) {
            graph[path[i]].capacity -= pathFlow;
            graph[graph[path[i]].to][graph[path[i]].rev].capacity += pathFlow;
        }
        
        maxFlow += pathFlow;
    }
    
    return nonZeroBalances.size() - maxFlow;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of non-zero balances and $m$ is the total amount of money, because in the worst case, we might have to augment the flow $m$ times, and each augmentation can take up to $O(n^2)$ time in the worst case due to the BFS and path finding.
> - **Space Complexity:** $O(n^2)$, for the adjacency list representation of the flow network.
> - **Optimality proof:** This approach is optimal because it constructs a flow network that accurately models the problem and then finds the maximum flow in this network, which corresponds to the minimum number of transactions required to balance all accounts. The use of the Ford-Fulkerson method with BFS for finding augmenting paths ensures that the maximum flow is found efficiently.