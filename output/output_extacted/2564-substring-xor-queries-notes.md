## Substring Xor Queries

**Problem Link:** https://leetcode.com/problems/substring-xor-queries/description

**Problem Statement:**
- Given a binary string `s` and an array of queries where each query consists of a binary string `x` and an integer `id`.
- For each query, find the first substring in `s` that starts with the binary representation of `id` and ends with the binary representation of `id` XOR `x`.
- Return an array of the lengths of these substrings in the order of the queries.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each query and then over the entire string `s` to find the first matching substring that meets the condition.
- This involves converting each query's `id` and `x` into binary, then for each position in `s`, checking if the substring starting at that position and ending at a later position matches the condition.
- This approach comes to mind first because it directly implements the problem statement without considering optimizations.

```cpp
#include <vector>
#include <string>

std::vector<int> substringXorQueries(std::string s, std::vector<std::string>& queries) {
    int n = s.size();
    std::vector<int> results;
    
    for (auto& query : queries) {
        std::string x = query[0];
        int id = stoi(query[1], 0, 2);
        int xorVal = id ^ stoi(x, 0, 2);
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                std::string substr = s.substr(i, j - i);
                if (stoi(substr, 0, 2) == id && stoi(substr, 0, 2) ^ stoi(x, 0, 2) == xorVal) {
                    results.push_back(substr.size());
                    break;
                }
            }
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot q \cdot b)$, where $n$ is the length of string `s`, $q$ is the number of queries, and $b$ is the maximum length of a query string. This is because for each query, we potentially scan the entire string and its substrings.
> - **Space Complexity:** $O(q)$ for storing the results of each query.
> - **Why these complexities occur:** The nested loops over the string and its substrings, combined with the iteration over each query, lead to the high time complexity. The space complexity is due to storing the results.

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves creating a hashmap that maps the binary representation of `id` XOR `x` to its position in the string `s`.
- We iterate over the string `s` once to populate this hashmap.
- Then, for each query, we use the hashmap to find the position of the substring that starts with `id` and ends with `id` XOR `x`.
- This approach is optimal because it reduces the time complexity significantly by avoiding the need to scan the entire string for each query.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

std::vector<int> substringXorQueries(std::string s, std::vector<std::vector<std::string>>& queries) {
    int n = s.size();
    std::unordered_map<std::string, int> hashmap;
    std::vector<int> results(queries.size(), -1);
    
    // Populate hashmap
    for (int i = 0; i < n; ++i) {
        int val = 0;
        for (int j = i; j < n; ++j) {
            val = (val << 1) | (s[j] - '0');
            hashmap[std::to_string(val)] = i;
        }
    }
    
    // Process queries
    for (int i = 0; i < queries.size(); ++i) {
        int id = stoi(queries[i][0], 0, 2);
        int x = stoi(queries[i][1], 0, 2);
        int xorVal = id ^ x;
        std::string key = std::to_string(xorVal);
        if (hashmap.find(key) != hashmap.end()) {
            results[i] = hashmap[key] - id + 1;
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b + q)$, where $n$ is the length of string `s`, $b$ is the maximum length of a substring, and $q$ is the number of queries. This is because we make a single pass over the string to populate the hashmap and then process each query in constant time.
> - **Space Complexity:** $O(n \cdot b)$ for the hashmap, where each entry corresponds to a unique substring of `s`.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity by avoiding redundant scans of the string and using a hashmap for efficient lookups.

### Final Notes

**Learning Points:**
- The importance of using hashmaps for efficient lookups.
- How to approach problems involving substrings and queries.
- The value of reducing time complexity by pre-processing data.

**Mistakes to Avoid:**
- Failing to consider the impact of nested loops on time complexity.
- Not utilizing data structures like hashmaps for optimization.
- Overlooking the potential for pre-processing to reduce query time.