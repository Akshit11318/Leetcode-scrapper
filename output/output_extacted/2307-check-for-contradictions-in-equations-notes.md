## Check for Contradictions in Equations

**Problem Link:** https://leetcode.com/problems/check-for-contradictions-in-equations/description

**Problem Statement:**
- Input: A list of strings representing equations.
- Constraints: Each equation is in the format "a==b" or "a!=b", where 'a' and 'b' are lowercase letters.
- Expected output: True if there is a contradiction in the equations, False otherwise.
- Key requirements and edge cases to consider: Handling different cases of equality and inequality, ensuring no contradictions arise from the given equations.
- Example test cases:
  - Input: ["a==b","b!=a"] Output: True
  - Input: ["b==a","a==b"] Output: False

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can create all possible combinations of variable assignments (true or false) for each letter and check if any combination satisfies all equations without contradiction.
- Step-by-step breakdown of the solution:
  1. Generate all possible assignments of boolean values to variables.
  2. For each assignment, evaluate all equations.
  3. If any equation contradicts the assignment, mark it as invalid.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach but highly inefficient due to the exponential number of assignments.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

bool equationsPossible(vector<string>& equations) {
    unordered_map<char, bool> assignments;
    for (char c = 'a'; c <= 'z'; c++) {
        assignments[c] = true;
    }

    // Generate all possible assignments
    for (int mask = 0; mask < (1 << 26); mask++) {
        unordered_map<char, bool> currentAssignments;
        for (int i = 0; i < 26; i++) {
            char c = 'a' + i;
            currentAssignments[c] = (mask & (1 << i)) != 0;
        }

        bool validAssignment = true;
        for (const auto& equation : equations) {
            char a = equation[0], b = equation[3];
            if (equation[1] == '=') {
                if (currentAssignments[a] != currentAssignments[b]) {
                    validAssignment = false;
                    break;
                }
            } else {
                if (currentAssignments[a] == currentAssignments[b]) {
                    validAssignment = false;
                    break;
                }
            }
        }

        if (validAssignment) return false; // Found an assignment that satisfies all equations
    }

    return true; // No valid assignment found, implying a contradiction
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{26} \cdot n)$ where $n$ is the number of equations. This is because we generate all possible assignments and check each equation against each assignment.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store the assignments and equations, regardless of the input size.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible assignments, and the constant space complexity is due to only using a fixed amount of space to store the current assignment and iterate through equations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all possible assignments, we can use a union-find data structure to model the equality relationships and detect contradictions efficiently.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with each variable in its own set.
  2. Iterate through the equality equations and union the sets of variables that are equal.
  3. Then, iterate through the inequality equations. If two variables are in the same set, it's a contradiction.
- Proof of optimality: This approach ensures we only need to process each equation once, reducing the time complexity significantly.

```cpp
class UnionFind {
public:
    vector<int> parent, rank;
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unionSets(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
            else if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

bool equationsPossible(vector<string>& equations) {
    UnionFind uf(26);
    // First, union the sets of equal variables
    for (const auto& equation : equations) {
        if (equation[1] == '=') {
            uf.unionSets(equation[0] - 'a', equation[3] - 'a');
        }
    }
    // Then, check for contradictions among unequal variables
    for (const auto& equation : equations) {
        if (equation[1] == '!') {
            if (uf.find(equation[0] - 'a') == uf.find(equation[3] - 'a')) {
                return false; // Contradiction found
            }
        }
    }
    return true; // No contradiction found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \alpha(n))$ where $n$ is the number of equations and $\alpha(n)$ is the inverse Ackermann function, which grows very slowly. This is because we perform a constant amount of work for each equation and the union-find operations take almost constant time.
> - **Space Complexity:** $O(n)$, for storing the union-find data structure.
> - **Optimality proof:** This approach is optimal because it processes each equation exactly once and uses a data structure that supports very efficient set operations, making it impossible to improve the time complexity further for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, efficient handling of equality and inequality relationships.
- Problem-solving patterns identified: Using data structures to model relationships and detect contradictions efficiently.
- Optimization techniques learned: Reducing the problem to a simpler form by using a union-find data structure.
- Similar problems to practice: Other graph theory and data structure problems involving relationships and contradictions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the union-find data structure or not handling edge cases properly.
- Edge cases to watch for: Ensuring that the solution handles different types of equations and variable assignments correctly.
- Performance pitfalls: Using an inefficient algorithm or data structure, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with different types of input, including edge cases and large inputs.