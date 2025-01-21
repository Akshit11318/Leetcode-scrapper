## Couples Holding Hands
**Problem Link:** https://leetcode.com/problems/couples-holding-hands/description

**Problem Statement:**
- Input format and constraints: The input is a vector of integers representing the row of seats, where each integer is the ID of the person sitting in that seat. The IDs are numbered from 0 to 2N-1, and each person has a partner with an ID that is the same but with a different parity (i.e., if the ID is even, the partner's ID is the same but odd, and vice versa). The output should be the minimum number of swaps required to arrange the seats so that every couple is holding hands.
- Expected output format: The output should be an integer representing the minimum number of swaps required.
- Key requirements and edge cases to consider: The input vector will have a length of 2N, where N is the number of couples. Each person will have a partner with a different parity, and the IDs will be numbered from 0 to 2N-1.
- Example test cases with explanations:
  - Input: `[0, 2, 1, 3]`
    Output: `1`
    Explanation: We can swap the second and third seats to get the desired arrangement.
  - Input: `[3, 2, 0, 1]`
    Output: `0`
    Explanation: The input is already in the desired arrangement.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible permutations of the input vector and checking each permutation to see if it satisfies the condition that every couple is holding hands.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of the input vector.
  2. For each permutation, check if every couple is holding hands.
  3. If a permutation satisfies the condition, count the number of swaps required to get to that permutation.
  4. Keep track of the minimum number of swaps required across all permutations.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible solutions, which guarantees that we will find the optimal solution if it exists.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minSwapsCouples(vector<int>& row) {
    int n = row.size();
    int minSwaps = INT_MAX;
    
    // Generate all permutations
    do {
        bool valid = true;
        for (int i = 0; i < n; i += 2) {
            if (row[i] % 2 == 0 && row[i + 1] != row[i] + 1) {
                valid = false;
                break;
            }
            if (row[i] % 2 == 1 && row[i + 1] != row[i] - 1) {
                valid = false;
                break;
            }
        }
        
        if (valid) {
            int swaps = 0;
            vector<int> temp = row;
            for (int i = 0; i < n; i++) {
                if (temp[i] != row[i]) {
                    swaps++;
                    // Find the position of temp[i] in row
                    int pos = -1;
                    for (int j = 0; j < n; j++) {
                        if (row[j] == temp[i]) {
                            pos = j;
                            break;
                        }
                    }
                    // Swap temp[i] and row[pos]
                    int t = temp[i];
                    temp[i] = temp[pos];
                    temp[pos] = t;
                }
            }
            minSwaps = min(minSwaps, swaps);
        }
    } while (next_permutation(row.begin(), row.end()));
    
    return minSwaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((2N)!) = O(2^{2N} \cdot N^{2N})$ [The time complexity is dominated by generating all permutations of the input vector, which has a time complexity of O((2N)!).]
> - **Space Complexity:** $O(2N)$ [The space complexity is dominated by storing the input vector and the temporary vector used to generate permutations.]
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations of the input vector, which results in an exponential time complexity. The space complexity is linear because we only need to store the input vector and a temporary vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of the connected components in the graph. Each couple forms a connected component, and we can use the union-find data structure to merge the components as we process the seats.
- Detailed breakdown of the approach:
  1. Create a union-find data structure with 2N elements, where each element represents a seat.
  2. Process the seats from left to right. For each seat, check if the person sitting in that seat is part of a couple that is already in the same connected component. If they are, we don't need to do anything.
  3. If the person sitting in the current seat is not part of a couple that is already in the same connected component, we need to merge the components. We can do this by finding the partner of the person sitting in the current seat and merging their components.
  4. After processing all seats, the number of connected components represents the minimum number of swaps required.
- Proof of optimality: The optimal approach has a time complexity of $O(N)$ because we only need to process each seat once. The space complexity is also $O(N)$ because we need to store the union-find data structure.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int minSwapsCouples(vector<int>& row) {
    int n = row.size();
    UnionFind uf(n);
    
    for (int i = 0; i < n; i += 2) {
        uf.unionSet(i, i + 1);
    }
    
    for (int i = 0; i < n; i++) {
        int partner = (row[i] % 2 == 0) ? row[i] + 1 : row[i] - 1;
        uf.unionSet(i, partner);
    }
    
    set<int> components;
    for (int i = 0; i < n; i++) {
        components.insert(uf.find(i));
    }
    
    return n / 2 - components.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ [The time complexity is dominated by processing each seat once.]
> - **Space Complexity:** $O(N)$ [The space complexity is dominated by storing the union-find data structure.]
> - **Optimality proof:** The optimal approach has a time complexity of $O(N)$ because we only need to process each seat once. The space complexity is also $O(N)$ because we need to store the union-find data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, connected components, and graph processing.
- Problem-solving patterns identified: Using a union-find data structure to keep track of connected components and merging components as we process the seats.
- Optimization techniques learned: Using a union-find data structure to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other problems that involve using a union-find data structure, such as finding connected components in a graph or solving the "Friend Circles" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the union-find data structure correctly or not merging components correctly.
- Edge cases to watch for: Handling the case where the input vector is empty or has only one element.
- Performance pitfalls: Using a brute force approach that has an exponential time complexity.
- Testing considerations: Testing the implementation with different input vectors, including edge cases and large inputs.