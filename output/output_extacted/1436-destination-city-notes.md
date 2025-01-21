## Destination City

**Problem Link:** https://leetcode.com/problems/destination-city/description

**Problem Statement:**
- Input format and constraints: You are given a list of `paths` where each `path` is a pair of cities connected by a one-way road.
- Expected output format: The `destinationCity` is the city that is not the starting point of any path.
- Key requirements and edge cases to consider: 
  - All `paths[i] = [cityA, cityB]` indicates that there is a one-way road from `cityA` to `cityB`.
  - The destination city is guaranteed to exist.
- Example test cases with explanations: 
  - If `paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]`, the destination city is `"Sao Paulo"` because it is not the starting point of any path.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can create a `set` to store all the cities that are the starting point of any path, and then iterate over all the cities in the `paths` to find the city that is not in the `set`.
- Step-by-step breakdown of the solution:
  1. Create a `set` to store all the cities that are the starting point of any path.
  2. Iterate over all the paths and add the starting city of each path to the `set`.
  3. Create a `set` to store all the cities that are the ending point of any path.
  4. Iterate over all the paths and add the ending city of each path to the `set`.
  5. Iterate over all the cities in the `paths` and find the city that is in the `set` of ending cities but not in the `set` of starting cities.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity because it involves iterating over all the paths multiple times.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

string destCity(vector<vector<string>>& paths) {
    set<string> start;
    set<string> end;
    
    for (auto& path : paths) {
        start.insert(path[0]);
        end.insert(path[1]);
    }
    
    for (auto& path : paths) {
        if (end.find(path[1]) != end.end() && start.find(path[1]) == start.end()) {
            return path[1];
        }
    }
    
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of paths, because in the worst case, we need to iterate over all the paths to find the destination city.
> - **Space Complexity:** $O(n)$ where $n$ is the number of paths, because we need to store all the cities in the `set`.
> - **Why these complexities occur:** The time complexity is high because we are iterating over all the paths multiple times, and the space complexity is high because we are storing all the cities in the `set`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can create a `set` to store all the cities that are the starting point of any path, and then iterate over all the paths to find the city that is not in the `set`.
- Detailed breakdown of the approach:
  1. Create a `set` to store all the cities that are the starting point of any path.
  2. Iterate over all the paths and add the starting city of each path to the `set`.
  3. Iterate over all the paths and find the city that is not in the `set` of starting cities.
- Proof of optimality: This approach is optimal because it only involves iterating over all the paths once, which reduces the time complexity to $O(n)$.
- Why further optimization is impossible: This approach is already optimal because it only involves a single pass over the data.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

string destCity(vector<vector<string>>& paths) {
    set<string> start;
    
    for (auto& path : paths) {
        start.insert(path[0]);
    }
    
    for (auto& path : paths) {
        if (start.find(path[1]) == start.end()) {
            return path[1];
        }
    }
    
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of paths, because we only need to iterate over all the paths once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of paths, because we need to store all the cities in the `set`.
> - **Optimality proof:** This approach is optimal because it only involves a single pass over the data, which reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `set` to store unique elements and iterating over all the paths to find the destination city.
- Problem-solving patterns identified: Creating a `set` to store all the cities that are the starting point of any path and then iterating over all the paths to find the city that is not in the `set`.
- Optimization techniques learned: Reducing the time complexity by only iterating over all the paths once.
- Similar problems to practice: Problems that involve finding a unique element in a list of pairs.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the destination city is empty before returning it.
- Edge cases to watch for: If the input list of paths is empty, the function should return an empty string.
- Performance pitfalls: Iterating over all the paths multiple times, which increases the time complexity.
- Testing considerations: Testing the function with different inputs, including an empty list of paths, to ensure that it returns the correct destination city.