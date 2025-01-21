## Queries on a Permutation with Key
**Problem Link:** https://leetcode.com/problems/queries-on-a-permutation-with-key/description

**Problem Statement:**
- Input format: An integer `n` and a 2D array `queries` where each query is in the format `[key, value]`.
- Constraints: `1 <= n <= 100`, `1 <= queries.length <= 100`, and `1 <= key, value <= n`.
- Expected output format: An array of integers representing the result of each query.
- Key requirements: For each query, find the index `k` in the permutation such that `permutation[k] = key`. Then, move the element at index `k` to the front of the permutation.
- Edge cases: If `key` does not exist in the permutation, the query is ignored.

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a permutation array and for each query, find the index of the key in the permutation and move it to the front.
- Step-by-step breakdown of the solution:
  1. Create a permutation array from 1 to `n`.
  2. For each query, iterate through the permutation to find the index `k` where `permutation[k] = key`.
  3. If `key` is found, remove it from the permutation at index `k` and insert it at the front of the permutation.
  4. After each query, record the value at the index `value - 1` in the modified permutation.

```cpp
#include <vector>
using namespace std;

vector<int> processQueries(int n, vector<vector<int>>& queries) {
    vector<int> permutation(n);
    for (int i = 0; i < n; i++) {
        permutation[i] = i + 1;
    }
    
    vector<int> results;
    for (auto& query : queries) {
        int key = query[0];
        int value = query[1];
        
        // Find the index of the key in the permutation
        int index = -1;
        for (int i = 0; i < n; i++) {
            if (permutation[i] == key) {
                index = i;
                break;
            }
        }
        
        // If key is found, move it to the front
        if (index != -1) {
            int temp = permutation[index];
            for (int i = index; i > 0; i--) {
                permutation[i] = permutation[i - 1];
            }
            permutation[0] = temp;
        }
        
        // Record the value at the index value - 1
        results.push_back(permutation[value - 1]);
    }
    
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n)$ where $q$ is the number of queries and $n$ is the size of the permutation. This is because for each query, we potentially scan the entire permutation.
> - **Space Complexity:** $O(n + q)$ for storing the permutation and the results of the queries.
> - **Why these complexities occur:** The brute force approach involves scanning the permutation for each query, leading to high time complexity. The space complexity is linear due to the storage of the permutation and the results.

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of physically moving elements in the permutation array for each query, we can maintain the order of elements using a different data structure, such as a `deque`, which supports efficient insertion and removal at any position.
- Detailed breakdown of the approach:
  1. Create a `deque` to represent the permutation.
  2. For each query, find the element corresponding to the key in the `deque`.
  3. Remove the found element from its current position in the `deque` and insert it at the front.
  4. After each query, access the element at the index `value - 1` in the `deque`.

```cpp
#include <deque>
#include <vector>
using namespace std;

vector<int> processQueries(int n, vector<vector<int>>& queries) {
    deque<int> permutation;
    for (int i = 1; i <= n; i++) {
        permutation.push_back(i);
    }
    
    vector<int> results;
    for (auto& query : queries) {
        int key = query[0];
        int value = query[1];
        
        // Find the element corresponding to the key in the deque
        for (auto it = permutation.begin(); it != permutation.end(); ++it) {
            if (*it == key) {
                // Remove the found element and insert it at the front
                permutation.erase(it);
                permutation.push_front(key);
                break;
            }
        }
        
        // Access the element at the index value - 1
        results.push_back(permutation[value - 1]);
    }
    
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n)$ where $q$ is the number of queries and $n$ is the size of the permutation. Although the use of a `deque` improves efficiency in insertion and removal, the overall time complexity remains the same due to the potential need to scan the entire `deque` for each query.
> - **Space Complexity:** $O(n + q)$ for storing the permutation and the results of the queries.
> - **Optimality proof:** The optimal approach still involves scanning the permutation for each query in the worst case. However, using a `deque` reduces the overhead of shifting elements during insertion and removal, making it more efficient in practice.

### Final Notes
**Learning Points:**
- Using the right data structure (e.g., `deque`) can significantly improve the efficiency of certain operations.
- The choice of data structure depends on the specific requirements of the problem (e.g., frequent insertion/removal at arbitrary positions).

**Mistakes to Avoid:**
- Not considering the trade-offs of different data structures for the problem at hand.
- Failing to optimize operations based on the problem's specific requirements.