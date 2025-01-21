## Largest Component Size by Common Factor

**Problem Link:** https://leetcode.com/problems/largest-component-size-by-common-factor/description

**Problem Statement:**
- Input format: `nums`, a list of integers
- Constraints: `1 <= nums.length <= 10^4`, `1 <= nums[i] <= 10^6`
- Expected output format: The size of the largest component
- Key requirements and edge cases to consider:
  - A component is a group of numbers that share a common factor
  - The common factor should be greater than 1
  - Example test cases: `[4,6,15,35]`, `[20,50,10,100]`, `[2,3,6]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible factor for each number
- Step-by-step breakdown of the solution:
  1. Iterate over each number in the input list
  2. For each number, find all its factors
  3. For each factor, check if it is also a factor of any other number in the list
  4. Group numbers that share a common factor into components
  5. Find the size of the largest component
- Why this approach comes to mind first: It directly addresses the problem statement

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int largestComponentSize(std::vector<int>& nums) {
    int maxComponentSize = 0;
    std::unordered_set<int> visited;

    for (int num : nums) {
        for (int factor = 2; factor * factor <= num; factor++) {
            if (num % factor == 0) {
                int componentSize = 0;
                std::unordered_set<int> component;
                for (int otherNum : nums) {
                    if (otherNum % factor == 0 && visited.find(otherNum) == visited.end()) {
                        component.insert(otherNum);
                        visited.insert(otherNum);
                        componentSize++;
                    }
                }
                maxComponentSize = std::max(maxComponentSize, componentSize);
            }
        }
    }

    return maxComponentSize;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{n} \cdot m)$, where $n$ is the length of the input list and $m$ is the maximum value in the list
> - **Space Complexity:** $O(n)$, for storing the visited numbers
> - **Why these complexities occur:** The outer loop iterates over each number, the middle loop checks for factors, and the inner loop checks for other numbers with the same factor, leading to the time complexity. The space complexity is due to storing visited numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use the concept of `union-find` to group numbers that share a common factor
- Detailed breakdown of the approach:
  1. Initialize a `union-find` data structure
  2. Iterate over each number in the input list
  3. For each number, find its prime factors
  4. For each prime factor, union the current number with all other numbers that have the same prime factor
  5. Find the size of the largest component
- Proof of optimality: This approach has a better time complexity than the brute force approach because it uses a more efficient data structure and avoids redundant calculations

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

class UnionFind {
public:
    std::unordered_map<int, int> parent;
    std::unordered_map<int, int> size;

    int find(int x) {
        if (parent.find(x) == parent.end()) {
            parent[x] = x;
            size[x] = 1;
            return x;
        }
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        }
    }
};

int largestComponentSize(std::vector<int>& nums) {
    UnionFind uf;
    for (int num : nums) {
        for (int factor = 2; factor * factor <= num; factor++) {
            if (num % factor == 0) {
                uf.union_(num, factor);
            }
        }
    }

    int maxComponentSize = 0;
    for (auto& pair : uf.size) {
        maxComponentSize = std::max(maxComponentSize, pair.second);
    }

    return maxComponentSize;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{m})$, where $n$ is the length of the input list and $m$ is the maximum value in the list
> - **Space Complexity:** $O(n)$, for storing the `union-find` data structure
> - **Optimality proof:** This approach is optimal because it uses a more efficient data structure and avoids redundant calculations, resulting in a better time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `union-find` data structure, prime factorization
- Problem-solving patterns identified: using a more efficient data structure to improve time complexity
- Optimization techniques learned: avoiding redundant calculations, using a `union-find` data structure
- Similar problems to practice: problems involving graph traversal, clustering, or community detection

**Mistakes to Avoid:**
- Common implementation errors: incorrect usage of the `union-find` data structure, incorrect calculation of prime factors
- Edge cases to watch for: handling duplicate numbers, handling numbers with no common factors
- Performance pitfalls: using a brute force approach, using an inefficient data structure
- Testing considerations: testing with large input lists, testing with numbers that have many common factors.