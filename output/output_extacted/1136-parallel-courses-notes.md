## Parallel Courses
**Problem Link:** https://leetcode.com/problems/parallel-courses/description

**Problem Statement:**
- Input format: `n` (number of courses), `dependencies` (list of course prerequisites), `k` (number of parallel courses allowed)
- Constraints: `1 <= n <= 10^5`, `1 <= dependencies.length <= 10^5`, `1 <= k <= n`
- Expected output format: Minimum number of semesters required to complete all courses
- Key requirements and edge cases to consider: Handling cyclic dependencies, ensuring `k` parallel courses, and validating input
- Example test cases:
  - `n = 4`, `dependencies = [[1,0],[2,0],[3,1],[3,2]]`, `k = 2`: Expected output `3`
  - `n = 5`, `dependencies = [[1,0],[2,1],[3,2],[4,3]]`, `k = 3`: Expected output `4`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Enumerate all possible course schedules and check for validity
- Step-by-step breakdown of the solution:
  1. Generate all permutations of courses
  2. For each permutation, validate if it satisfies the dependencies and `k` parallel courses constraint
  3. Keep track of the minimum number of semesters required
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
    // Generate all permutations of courses
    vector<int> courses(n);
    for (int i = 0; i < n; i++) {
        courses[i] = i;
    }
    
    int minSemesters = INT_MAX;
    do {
        // Validate if the current permutation satisfies the dependencies and k parallel courses constraint
        bool valid = true;
        vector<int> semesterCourses;
        for (int i = 0; i < n; i++) {
            int course = courses[i];
            bool hasPrereq = false;
            for (auto& dependency : dependencies) {
                if (dependency[0] == course + 1) {
                    for (int j = 0; j < i; j++) {
                        if (courses[j] + 1 == dependency[1]) {
                            hasPrereq = true;
                            break;
                        }
                    }
                }
            }
            if (!hasPrereq) {
                semesterCourses.push_back(course);
                if (semesterCourses.size() > k) {
                    valid = false;
                    break;
                }
            }
        }
        
        if (valid) {
            // Calculate the number of semesters required for the current permutation
            int semesters = 0;
            while (!semesterCourses.empty()) {
                semesters++;
                vector<int> nextSemesterCourses;
                for (int i = 0; i < semesterCourses.size(); i++) {
                    for (auto& dependency : dependencies) {
                        if (dependency[1] == semesterCourses[i] + 1) {
                            nextSemesterCourses.push_back(dependency[0] - 1);
                        }
                    }
                }
                semesterCourses = nextSemesterCourses;
            }
            minSemesters = min(minSemesters, semesters);
        }
    } while (next_permutation(courses.begin(), courses.end()));
    
    return minSemesters;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot m)$, where $n$ is the number of courses and $m$ is the number of dependencies
> - **Space Complexity:** $O(n)$, for storing the courses and dependencies
> - **Why these complexities occur:** The brute force approach generates all permutations of courses, resulting in a high time complexity. The space complexity is relatively low, as we only need to store the courses and dependencies.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a topological sorting algorithm with a priority queue to efficiently schedule courses
- Detailed breakdown of the approach:
  1. Build a graph with courses as nodes and dependencies as edges
  2. Calculate the in-degree of each course
  3. Initialize a priority queue with courses having no prerequisites (in-degree 0)
  4. While the priority queue is not empty:
    - Dequeue `k` courses with the highest priority ( lowest in-degree)
    - Increment the semester counter
    - For each dequeued course, decrease the in-degree of its neighbors
    - Enqueue neighbors with in-degree 0
- Why this approach is optimal: It efficiently schedules courses while respecting dependencies and the `k` parallel courses constraint

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
    // Build the graph and calculate in-degrees
    vector<vector<int>> graph(n);
    vector<int> inDegree(n, 0);
    for (auto& dependency : dependencies) {
        graph[dependency[1] - 1].push_back(dependency[0] - 1);
        inDegree[dependency[0] - 1]++;
    }
    
    // Initialize the priority queue with courses having no prerequisites
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) {
            pq.push(i);
        }
    }
    
    int semesters = 0;
    while (!pq.empty()) {
        // Dequeue k courses with the highest priority
        vector<int> dequeuedCourses;
        for (int i = 0; i < k && !pq.empty(); i++) {
            int course = pq.top();
            pq.pop();
            dequeuedCourses.push_back(course);
        }
        
        // Increment the semester counter
        semesters++;
        
        // Decrease the in-degree of neighbors and enqueue them if in-degree becomes 0
        for (int course : dequeuedCourses) {
            for (int neighbor : graph[course]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    pq.push(neighbor);
                }
            }
        }
    }
    
    return semesters;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log k)$, where $n$ is the number of courses and $m$ is the number of dependencies
> - **Space Complexity:** $O(n + m)$, for storing the graph and priority queue
> - **Optimality proof:** The optimal approach efficiently schedules courses while respecting dependencies and the `k` parallel courses constraint, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sorting, priority queues, and graph traversal
- Problem-solving patterns identified: Using a priority queue to efficiently schedule tasks with dependencies
- Optimization techniques learned: Reducing time complexity by using a priority queue and avoiding unnecessary computations

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as cyclic dependencies or invalid input
- Edge cases to watch for: Handling cases where `k` is greater than the number of courses or where there are no dependencies
- Performance pitfalls: Using a brute force approach or failing to optimize the algorithm for large inputs
- Testing considerations: Thoroughly testing the implementation with various input scenarios to ensure correctness and efficiency.