## Course Schedule II
**Problem Link:** [https://leetcode.com/problems/course-schedule-ii/description](https://leetcode.com/problems/course-schedule-ii/description)

**Problem Statement:**
- Input format: `int numCourses`, `vector<vector<int>>& prerequisites`
- Constraints: `1 <= numCourses <= 2000`, `0 <= prerequisites.length <= numCourses * 10^5`
- Expected output format: `vector<int>` representing the course schedule
- Key requirements: Find a valid course schedule if possible, otherwise return an empty vector
- Edge cases to consider: Cycles in the graph, empty prerequisites list
- Example test cases:
  - `numCourses = 2`, `prerequisites = [[1,0]]`, expected output: `[0,1]`
  - `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`, expected output: `[0,1,2,3]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible permutations of courses and check if each permutation satisfies the prerequisites.
- This approach involves generating all permutations of `numCourses` and then validating each permutation against the `prerequisites`.
- This approach comes to mind first because it's a straightforward way to ensure that all possible orders are considered.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<int> result;
    vector<int> courses(numCourses);
    for (int i = 0; i < numCourses; i++) {
        courses[i] = i;
    }

    do {
        bool valid = true;
        for (auto& pair : prerequisites) {
            int course = pair[0], prerequisite = pair[1];
            if (find(courses.begin(), courses.begin() + course, prerequisite) == courses.begin() + course) {
                valid = false;
                break;
            }
        }
        if (valid) {
            result = courses;
            break;
        }
    } while (next_permutation(courses.begin(), courses.end()));

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of courses, because we're generating all permutations of courses.
> - **Space Complexity:** $O(n)$, where $n$ is the number of courses, because we're storing the current permutation of courses.
> - **Why these complexities occur:** The brute force approach is inefficient because it tries all possible permutations of courses, which leads to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using a topological sorting algorithm to find a valid course schedule.
- We create a graph where each course is a node, and there's a directed edge from course $i$ to course $j$ if $i$ is a prerequisite for $j$.
- We then perform a topological sort on this graph to find a valid order of courses.
- If the graph contains a cycle, we return an empty vector because there's no valid course schedule.

```cpp
#include <vector>
#include <queue>

using namespace std;

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> graph(numCourses);
    vector<int> indegree(numCourses, 0);

    for (auto& pair : prerequisites) {
        int course = pair[0], prerequisite = pair[1];
        graph[prerequisite].push_back(course);
        indegree[course]++;
    }

    queue<int> q;
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    vector<int> result;
    while (!q.empty()) {
        int course = q.front();
        q.pop();
        result.push_back(course);

        for (int neighbor : graph[course]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    if (result.size() != numCourses) {
        return {};
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of courses and $m$ is the number of prerequisites, because we're performing a constant amount of work for each course and each prerequisite.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of courses and $m$ is the number of prerequisites, because we're storing the graph and the indegree of each course.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the graph and the prerequisites, and it uses a efficient data structure (the queue) to keep track of the courses with no prerequisites.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sorting, graph traversal
- Problem-solving patterns identified: Finding a valid order in a directed acyclic graph (DAG)
- Optimization techniques learned: Using a queue to keep track of nodes with no incoming edges
- Similar problems to practice: Course Schedule, Alien Dictionary

**Mistakes to Avoid:**
- Not checking for cycles in the graph
- Not using a efficient data structure to keep track of the courses with no prerequisites
- Not handling edge cases correctly (e.g., empty prerequisites list)
- Not testing the solution thoroughly to ensure it works for all possible inputs.