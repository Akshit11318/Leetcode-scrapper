## Course Schedule
**Problem Link:** https://leetcode.com/problems/course-schedule/description

**Problem Statement:**
- Input format: `numCourses` and `prerequisites` where `prerequisites[i] = [ai, bi]` means to take course `ai`, you have to first take course `bi`.
- Constraints: `1 <= numCourses <= 2000`, `0 <= prerequisites.length <= numCourses * (numCourses - 1) / 2`, and `prerequisites[i].length == 2`.
- Expected output format: `bool` indicating whether it's possible to finish all courses.
- Key requirements: Determine if there's a valid order to take all courses without violating any prerequisites.
- Example test cases:
  - `numCourses = 2`, `prerequisites = [[1,0]]` returns `true`.
  - `numCourses = 2`, `prerequisites = [[1,0],[0,1]]` returns `false`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking all possible permutations of courses to see if any satisfy the prerequisites.
- This approach is straightforward but inefficient because it doesn't leverage any structural properties of the problem.
- We generate all permutations of courses and then check each permutation against the prerequisites.

```cpp
#include <iostream>
#include <vector>

bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
    // Generate all permutations
    std::vector<int> permutation(numCourses);
    for (int i = 0; i < numCourses; ++i) permutation[i] = i;
    
    do {
        bool valid = true;
        for (const auto& prerequisite : prerequisites) {
            int course = prerequisite[0];
            int pre = prerequisite[1];
            if (std::find(permutation.begin(), permutation.end(), course) < std::find(permutation.begin(), permutation.end(), pre)) {
                valid = false;
                break;
            }
        }
        if (valid) return true;
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$ where $n$ is the number of courses and $m$ is the number of prerequisites. This is because we generate all permutations of $n$ courses and for each permutation, we check against $m$ prerequisites.
> - **Space Complexity:** $O(n)$ for storing the permutation.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which leads to a factorial time complexity. Checking each permutation against the prerequisites adds a linear factor.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using a `topological sorting` algorithm to order the courses in a way that for every edge `(u,v)`, course `u` comes after `v` in the ordering.
- If such an ordering exists, it means we can finish all courses without violating any prerequisites.
- We use a `graph` to represent the courses and prerequisites, and then apply a depth-first search (`DFS`) to detect any cycles. If a cycle is found, it means we cannot finish all courses.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
    std::unordered_map<int, std::vector<int>> graph;
    std::vector<int> visited(numCourses, 0);
    
    // Build the graph
    for (const auto& prerequisite : prerequisites) {
        int course = prerequisite[0];
        int pre = prerequisite[1];
        graph[pre].push_back(course);
    }
    
    // DFS to detect cycles
    for (int i = 0; i < numCourses; ++i) {
        if (!visited[i] && hasCycle(graph, visited, i)) return false;
    }
    
    return true;
}

bool hasCycle(const std::unordered_map<int, std::vector<int>>& graph, std::vector<int>& visited, int course) {
    if (visited[course] == 1) return true; // Visiting a course that's currently being visited means a cycle
    if (visited[course] == 2) return false; // If we've already visited and left this course, no cycle
    
    visited[course] = 1; // Mark as visiting
    
    if (graph.find(course) != graph.end()) {
        for (int nextCourse : graph.at(course)) {
            if (hasCycle(graph, visited, nextCourse)) return true;
        }
    }
    
    visited[course] = 2; // Mark as visited and left
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of courses and $m$ is the number of prerequisites. This is because we visit each course and prerequisite once.
> - **Space Complexity:** $O(n + m)$ for storing the graph and visited status.
> - **Optimality proof:** This is optimal because we only visit each course and prerequisite once, leveraging the structural properties of the problem to avoid unnecessary work.

---

### Final Notes

**Learning Points:**
- Topological sorting is useful for ordering elements based on dependencies.
- DFS can be used to detect cycles in a graph.
- Avoid brute force approaches when a problem has structural properties that can be leveraged for efficiency.

**Mistakes to Avoid:**
- Not checking for cycles in the graph.
- Using an inefficient algorithm for detecting cycles.
- Not considering the structural properties of the problem when choosing an approach.