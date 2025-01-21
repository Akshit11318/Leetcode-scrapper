## Count Zero Request Servers
**Problem Link:** https://leetcode.com/problems/count-zero-request-servers/description

**Problem Statement:**
- Input: `k` (number of servers), `maxRequests` (maximum number of requests per server), `requests` (array of server indices that will receive a request)
- Expected output: Number of servers that will receive zero requests after processing all requests
- Key requirements:
  - Each server can only handle a limited number of requests (`maxRequests`).
  - If a server receives more requests than it can handle, it will receive zero requests (i.e., it will not process any requests).
- Edge cases:
  - Empty `requests` array.
  - `k` or `maxRequests` is zero.
- Example test cases:
  - `k = 3`, `maxRequests = 3`, `requests = [0,1,0,2,1,0]`. Expected output: 1 (server 2 will receive zero requests).

---

### Brute Force Approach

**Explanation:**
- Initialize an array to track the number of requests each server receives.
- Iterate through the `requests` array and increment the corresponding server's request count.
- If a server's request count exceeds `maxRequests`, set its request count to zero (since it will not process any requests).
- Finally, count the number of servers with zero requests.

```cpp
int countZeroRequests(int k, int maxRequests, vector<int>& requests) {
    vector<int> requestCounts(k, 0);
    for (int request : requests) {
        if (requestCounts[request] < maxRequests) {
            requestCounts[request]++;
        } else {
            requestCounts[request] = 0;
        }
    }
    int zeroRequests = 0;
    for (int count : requestCounts) {
        if (count == 0) {
            zeroRequests++;
        }
    }
    return zeroRequests;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the number of requests and $k$ is the number of servers. We iterate through the `requests` array and then through the `requestCounts` array.
> - **Space Complexity:** $O(k)$, where $k$ is the number of servers. We need to store the request counts for each server.
> - **Why these complexities occur:** We need to process each request and keep track of the request counts for each server, resulting in linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- We can improve the brute force approach by using a more efficient data structure to track the request counts. A `map` or `unordered_map` can be used to store the request counts, allowing us to look up and update the counts in constant time.
- However, since the problem statement guarantees that the `requests` array only contains indices between 0 and `k-1`, we can use a simple array to store the request counts, which is more efficient than a `map`.
- The optimal approach is to use a single pass through the `requests` array to update the request counts and count the number of servers with zero requests.

```cpp
int countZeroRequests(int k, int maxRequests, vector<int>& requests) {
    vector<int> requestCounts(k, 0);
    for (int request : requests) {
        requestCounts[request]++;
    }
    int zeroRequests = 0;
    for (int& count : requestCounts) {
        if (count == 0 || count > maxRequests) {
            zeroRequests++;
        }
    }
    return zeroRequests;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the number of requests and $k$ is the number of servers. We iterate through the `requests` array and then through the `requestCounts` array.
> - **Space Complexity:** $O(k)$, where $k$ is the number of servers. We need to store the request counts for each server.
> - **Optimality proof:** This is the most efficient approach because we only need to make a single pass through the `requests` array and then through the `requestCounts` array. We cannot reduce the time complexity further because we must process each request and count the number of servers with zero requests.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem (in this case, a simple array).
- How to optimize the brute force approach by reducing the number of iterations and using more efficient data structures.
- The trade-offs between time and space complexity.

**Mistakes to Avoid:**
- Not considering the constraints of the problem (e.g., the range of values in the `requests` array).
- Not optimizing the brute force approach to reduce the time complexity.
- Not considering the edge cases (e.g., empty `requests` array, `k` or `maxRequests` is zero).