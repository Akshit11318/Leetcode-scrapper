## Find Servers That Handled Most Number of Requests
**Problem Link:** https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description

**Problem Statement:**
- Input: `k` (number of servers) and `requests` (list of requests where each request is a pair of start and end times)
- Expected output: List of server IDs that handled the most number of requests
- Key requirements and edge cases:
  - Each server can only handle one request at a time.
  - A server can handle a new request if it is not currently handling another request.
  - The goal is to find the server(s) that handled the most number of requests.

Example test cases:
- `k = 3`, `requests = [[0, 5], [1, 2], [1, 6]]`
- `k = 3`, `requests = [[0, 3], [5, 9], [1, 2]]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through each request and checking if any server is available to handle it.
- For each request, we check each server to see if it is available (not handling another request at the same time).
- If a server is available, we assign it to handle the request.

```cpp
#include <vector>
#include <queue>

using namespace std;

vector<int> busiestServers(int k, vector<vector<int>>& requests) {
    vector<int> serverRequests(k, 0); // Count of requests handled by each server
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> availableServers; // Available servers sorted by their next available time
    
    for (int i = 0; i < k; i++) {
        availableServers.push({0, i}); // Initialize all servers as available at time 0
    }
    
    for (auto& request : requests) {
        int start = request[0], end = request[1];
        while (!availableServers.empty() && availableServers.top().first <= start) {
            // Make the server available again after it finishes handling the previous request
            availableServers.pop();
            availableServers.push({end, availableServers.top().second});
        }
        
        if (!availableServers.empty()) {
            int serverId = availableServers.top().second;
            serverRequests[serverId]++;
            availableServers.pop();
            availableServers.push({end, serverId});
        }
    }
    
    int maxRequests = 0;
    for (int i = 0; i < k; i++) {
        maxRequests = max(maxRequests, serverRequests[i]);
    }
    
    vector<int> result;
    for (int i = 0; i < k; i++) {
        if (serverRequests[i] == maxRequests) {
            result.push_back(i);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$ where $n$ is the number of requests. This is because we perform a heap operation for each request, and heap operations take $O(\log k)$ time.
> - **Space Complexity:** $O(k + n)$ for storing the count of requests handled by each server and the heap of available servers.
> - **Why these complexities occur:** The time complexity is dominated by the heap operations, and the space complexity is due to the storage needed for the server counts and the heap.

---

### Optimal Approach (Required)
The provided brute force approach is already optimal for this problem as it efficiently utilizes a priority queue to manage server availability, ensuring that each request is handled by the first available server. The use of a priority queue allows for efficient management of server availability, making the solution optimal.

**Explanation:**
- The key insight is to use a priority queue to manage server availability, sorting servers by their next available time.
- This approach ensures that each request is handled by the first available server, which is the most efficient way to handle requests.

```cpp
// Same as the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$
> - **Space Complexity:** $O(k + n)$
> - **Optimality proof:** This approach is optimal because it ensures that each request is handled by the first available server, minimizing the time spent waiting for a server to become available.

---

### Final Notes

**Learning Points:**
- The importance of using data structures like priority queues to efficiently manage resources (in this case, server availability).
- How to approach problems involving scheduling and resource allocation.
- The value of breaking down complex problems into simpler, more manageable parts.

**Mistakes to Avoid:**
- Not considering the use of data structures like priority queues to improve efficiency.
- Failing to account for edge cases, such as when a server becomes available again after handling a request.
- Not optimizing the solution to minimize time complexity.