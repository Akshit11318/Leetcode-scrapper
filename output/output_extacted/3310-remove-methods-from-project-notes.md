## Remove Methods from Project
**Problem Link:** https://leetcode.com/problems/remove-methods-from-project/description

**Problem Statement:**
- Input format and constraints: 
  - The input will contain a list of strings, each representing a method in the project.
  - Each string will be in the format "method_name(class_name)".
  - The input will also contain a list of strings, each representing a method to be removed.
- Expected output format: 
  - The output should be a list of strings, each representing a method that is still in the project after removing the specified methods.
- Key requirements and edge cases to consider:
  - Methods with the same name but different classes should be treated as different methods.
  - If a method to be removed does not exist in the project, it should be ignored.
- Example test cases with explanations:
  - For example, if the input project methods are ["method1(class1)", "method2(class1)", "method1(class2)"] and the methods to be removed are ["method1(class1)"], the output should be ["method2(class1)", "method1(class2)"].

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves iterating over each method in the project and checking if it is in the list of methods to be removed.
- Step-by-step breakdown of the solution:
  1. Create a copy of the project methods list.
  2. Iterate over each method in the project methods list.
  3. For each method, check if it is in the list of methods to be removed.
  4. If a method is found in the list of methods to be removed, remove it from the copied list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> removeMethods(std::vector<std::string> projectMethods, std::vector<std::string> methodsToRemove) {
    // Create a copy of the project methods list
    std::vector<std::string> updatedMethods = projectMethods;

    // Iterate over each method in the project methods list
    for (auto it = updatedMethods.begin(); it != updatedMethods.end();) {
        // Check if the method is in the list of methods to be removed
        if (std::find(methodsToRemove.begin(), methodsToRemove.end(), *it) != methodsToRemove.end()) {
            // Remove the method from the copied list
            it = updatedMethods.erase(it);
        } else {
            ++it;
        }
    }

    return updatedMethods;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of project methods and $m$ is the number of methods to be removed. This is because for each project method, we are searching in the list of methods to be removed.
> - **Space Complexity:** $O(n)$, where $n$ is the number of project methods. This is because we are creating a copy of the project methods list.
> - **Why these complexities occur:** These complexities occur because we are using a linear search to find methods in the list of methods to be removed, and we are creating a copy of the project methods list.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use an unordered set to store the methods to be removed, allowing us to check for existence in constant time.
- Detailed breakdown of the approach:
  1. Create an unordered set from the list of methods to be removed.
  2. Iterate over each method in the project methods list.
  3. For each method, check if it is in the set of methods to be removed.
  4. If a method is not found in the set, add it to the result list.
- Proof of optimality: This approach is optimal because we are using a data structure that allows us to check for existence in constant time, and we are only iterating over the project methods list once.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

std::vector<std::string> removeMethods(std::vector<std::string> projectMethods, std::vector<std::string> methodsToRemove) {
    // Create an unordered set from the list of methods to be removed
    std::unordered_set<std::string> methodsToRemoveSet(methodsToRemove.begin(), methodsToRemove.end());

    // Create a result list
    std::vector<std::string> result;

    // Iterate over each method in the project methods list
    for (const auto& method : projectMethods) {
        // Check if the method is not in the set of methods to be removed
        if (methodsToRemoveSet.find(method) == methodsToRemoveSet.end()) {
            // Add the method to the result list
            result.push_back(method);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of project methods and $m$ is the number of methods to be removed. This is because we are creating an unordered set from the list of methods to be removed, and then iterating over the project methods list once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of project methods and $m$ is the number of methods to be removed. This is because we are creating an unordered set from the list of methods to be removed, and a result list.
> - **Optimality proof:** This approach is optimal because we are using a data structure that allows us to check for existence in constant time, and we are only iterating over the project methods list once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an unordered set to improve search efficiency.
- Problem-solving patterns identified: Using a set to store elements that need to be removed, and then iterating over the original list to filter out those elements.
- Optimization techniques learned: Using a data structure that allows for constant time search to improve the overall time complexity of the algorithm.
- Similar problems to practice: Other problems that involve filtering out elements from a list based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list.
- Edge cases to watch for: Handling cases where the input list is empty, or where the list of methods to be removed is empty.
- Performance pitfalls: Using a linear search to find elements in a list, which can lead to poor performance for large inputs.
- Testing considerations: Testing the algorithm with different input sizes and edge cases to ensure that it works correctly and efficiently.