## Parallel Courses III
**Problem Link:** https://leetcode.com/problems/parallel-courses-iii/description

**Problem Statement:**
- Given an integer `n` representing the number of courses, a list of pairs `dependencies` where each pair `[x, y]` means course `x` must be taken before course `y`, and a list of `prerequisites` where `prerequisites[i]` is a list of courses that must be taken before course `i`, find the minimum number of semesters required to complete all courses.
- Input format: `n`, `dependencies`, `prerequisites`
- Constraints: `1 <= n <= 1000`, `0 <= dependencies.length <= 10^5`, `0 <= prerequisites.length <= 10^5`
- Expected output format: Minimum number of semesters required to complete all courses.
- Key requirements and edge cases to consider:
  - Handling cyclic dependencies
  - Courses with no prerequisites
  - Courses that cannot be taken in parallel
- Example test cases with explanations:
  - Test case 1: `n = 3`, `dependencies = [[0, 1], [1, 2]]`, `prerequisites = [[], [], []]`. Expected output: `3`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves creating a graph from the given dependencies and then trying to find a topological sorting of the graph. However, the brute force approach would involve trying all possible orderings of courses and checking if they satisfy the dependencies.
- Step-by-step breakdown:
  1. Create a graph from the dependencies.
  2. Generate all permutations of courses.
  3. For each permutation, check if it satisfies the dependencies.
  4. If a permutation satisfies the dependencies, calculate the minimum number of semesters required based on the prerequisites.
- Why this approach comes to mind first: It's a straightforward approach that tries to brute force all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSemesters(int n, vector<vector<int>>& dependencies, vector<vector<int>>& prerequisites) {
    // Generate all permutations of courses
    vector<int> courses(n);
    for (int i = 0; i < n; i++) {
        courses[i] = i;
    }

    int minSemesters = INT_MAX;
    do {
        // Check if the current permutation satisfies the dependencies
        bool satisfiesDependencies = true;
        for (const auto& dependency : dependencies) {
            if (find(courses.begin(), courses.end(), dependency[1]) < find(courses.begin(), courses.end(), dependency[0])) {
                satisfiesDependencies = false;
                break;
            }
        }

        if (satisfiesDependencies) {
            // Calculate the minimum number of semesters required based on the prerequisites
            int semesters = 0;
            vector<int> taken(n, 0);
            for (int i = 0; i < n; i++) {
                if (taken[courses[i]]) {
                    continue;
                }

                int semester = 0;
                vector<int> stack;
                stack.push_back(courses[i]);
                taken[courses[i]] = 1;

                while (!stack.empty()) {
                    semester++;
                    vector<int> newStack;
                    for (int course : stack) {
                        for (int nextCourse : prerequisites[course]) {
                            if (!taken[nextCourse]) {
                                newStack.push_back(nextCourse);
                                taken[nextCourse] = 1;
                            }
                        }
                    }
                    stack = newStack;
                }

                semesters = max(semesters, semester);
            }

            minSemesters = min(minSemesters, semesters);
        }
    } while (next_permutation(courses.begin(), courses.end()));

    return minSemesters;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of courses and $m$ is the number of dependencies. This is because we generate all permutations of courses and check each permutation against the dependencies.
> - **Space Complexity:** $O(n)$, as we need to store the permutations of courses.
> - **Why these complexities occur:** The brute force approach tries all possible orderings of courses, which leads to a factorial time complexity. The space complexity is linear because we only need to store the current permutation of courses.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using topological sorting to find a valid ordering of courses that satisfies the dependencies.
- Key insight: We can use a topological sorting algorithm to find a valid ordering of courses in $O(n + m)$ time complexity.
- Detailed breakdown:
  1. Create a graph from the dependencies.
  2. Perform a topological sorting on the graph to find a valid ordering of courses.
  3. Calculate the minimum number of semesters required based on the prerequisites.
- Why further optimization is impossible: The topological sorting algorithm has a linear time complexity, which is optimal for this problem.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int minSemesters(int n, vector<vector<int>>& dependencies, vector<vector<int>>& prerequisites) {
    // Create a graph from the dependencies
    vector<vector<int>> graph(n);
    vector<int> inDegree(n, 0);
    for (const auto& dependency : dependencies) {
        graph[dependency[0]].push_back(dependency[1]);
        inDegree[dependency[1]]++;
    }

    // Perform a topological sorting on the graph
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    vector<int> order;
    while (!q.empty()) {
        int course = q.front();
        q.pop();
        order.push_back(course);

        for (int nextCourse : graph[course]) {
            inDegree[nextCourse]--;
            if (inDegree[nextCourse] == 0) {
                q.push(nextCourse);
            }
        }
    }

    // Calculate the minimum number of semesters required based on the prerequisites
    int semesters = 0;
    vector<int> taken(n, 0);
    for (int course : order) {
        if (taken[course]) {
            continue;
        }

        int semester = 0;
        vector<int> stack;
        stack.push_back(course);
        taken[course] = 1;

        while (!stack.empty()) {
            semester++;
            vector<int> newStack;
            for (int c : stack) {
                for (int nextCourse : prerequisites[c]) {
                    if (!taken[nextCourse]) {
                        newStack.push_back(nextCourse);
                        taken[nextCourse] = 1;
                    }
                }
            }
            stack = newStack;
        }

        semesters = max(semesters, semester);
    }

    return semesters;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of courses and $m$ is the number of dependencies. This is because we perform a topological sorting on the graph.
> - **Space Complexity:** $O(n)$, as we need to store the graph and the in-degrees of the courses.
> - **Optimality proof:** The topological sorting algorithm has a linear time complexity, which is optimal for this problem. We cannot do better than this because we need to at least read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sorting, graph theory
- Problem-solving patterns identified: Using graph theory to solve dependency problems
- Optimization techniques learned: Using topological sorting to reduce time complexity
- Similar problems to practice: Topological sorting, graph theory problems

**Mistakes to Avoid:**
- Common implementation errors: Not handling cyclic dependencies correctly
- Edge cases to watch for: Courses with no prerequisites, courses that cannot be taken in parallel
- Performance pitfalls: Using brute force approaches for large inputs
- Testing considerations: Test cases with cyclic dependencies, courses with no prerequisites, courses that cannot be taken in parallel.