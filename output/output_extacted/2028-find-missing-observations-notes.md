## Find Missing Observations

**Problem Link:** https://leetcode.com/problems/find-missing-observations/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `lower` and `upper` bounds, find all missing integers in the range.
- Expected output format: Return a list of missing integers in the range.
- Key requirements and edge cases to consider: 
    - The input list `lower` and `upper` bounds are guaranteed to be non-empty.
    - The lower bound is inclusive, and the upper bound is inclusive.
    - The range of integers is from 1 to 10^5.
- Example test cases with explanations:
    - For `lower = [1, 3]` and `upper = [3, 4]`, the output should be `[2, 4]`.
    - For `lower = [1, 2, 3]` and `upper = [3, 4, 5]`, the output should be `[4, 5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible integers in the range and check if they exist in the given list.
- Step-by-step breakdown of the solution:
    1. Initialize an empty set to store the given integers.
    2. Iterate over the given list and add each integer to the set.
    3. Initialize an empty list to store the missing integers.
    4. Iterate over the range of integers from the minimum lower bound to the maximum upper bound.
    5. For each integer in the range, check if it exists in the set.
    6. If it does not exist, add it to the list of missing integers.
- Why this approach comes to mind first: It is a straightforward solution that checks every possible integer in the range.

```cpp
#include <vector>
#include <set>
#include <algorithm>

std::vector<int> findMissingObservations(std::vector<int>& lower, std::vector<int>& upper) {
    // Initialize an empty set to store the given integers
    std::set<int> givenIntegers;
    
    // Iterate over the given list and add each integer to the set
    for (int i = 0; i < lower.size(); i++) {
        for (int j = lower[i]; j <= upper[i]; j++) {
            givenIntegers.insert(j);
        }
    }
    
    // Initialize an empty list to store the missing integers
    std::vector<int> missingIntegers;
    
    // Find the minimum lower bound and the maximum upper bound
    int minLower = *std::min_element(lower.begin(), lower.end());
    int maxUpper = *std::max_element(upper.begin(), upper.end());
    
    // Iterate over the range of integers from the minimum lower bound to the maximum upper bound
    for (int i = minLower; i <= maxUpper; i++) {
        // Check if the integer exists in the set
        if (givenIntegers.find(i) == givenIntegers.end()) {
            // If it does not exist, add it to the list of missing integers
            missingIntegers.push_back(i);
        }
    }
    
    return missingIntegers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \cdot m \cdot k + k)$, where $n$ is the number of lower and upper bounds, $m$ is the average range of each bound, and $k$ is the total range of all bounds. The first term represents the time to populate the set of given integers, the second term represents the time to find the minimum and maximum bounds, and the third term represents the time to iterate over the range and find missing integers.
> - **Space Complexity:** $O(n \cdot m)$, which represents the space used to store the set of given integers.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it needs to iterate over all possible integers in the range and check if they exist in the set of given integers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over all possible integers in the range, we can use a set to store the given integers and then iterate over the range to find missing integers.
- Detailed breakdown of the approach:
    1. Initialize an empty set to store the given integers.
    2. Iterate over the given list and add each integer to the set.
    3. Initialize an empty list to store the missing integers.
    4. Find the minimum lower bound and the maximum upper bound.
    5. Iterate over the range of integers from the minimum lower bound to the maximum upper bound.
    6. For each integer in the range, check if it exists in the set.
    7. If it does not exist, add it to the list of missing integers.
- Proof of optimality: This approach is optimal because it only requires a single pass over the given list and the range of integers, resulting in a time complexity of $O(n \cdot m + k)$.

```cpp
#include <vector>
#include <set>
#include <algorithm>

std::vector<int> findMissingObservations(std::vector<int>& lower, std::vector<int>& upper) {
    // Initialize an empty set to store the given integers
    std::set<int> givenIntegers;
    
    // Iterate over the given list and add each integer to the set
    for (int i = 0; i < lower.size(); i++) {
        for (int j = lower[i]; j <= upper[i]; j++) {
            givenIntegers.insert(j);
        }
    }
    
    // Initialize an empty list to store the missing integers
    std::vector<int> missingIntegers;
    
    // Find the minimum lower bound and the maximum upper bound
    int minLower = *std::min_element(lower.begin(), lower.end());
    int maxUpper = *std::max_element(upper.begin(), upper.end());
    
    // Iterate over the range of integers from the minimum lower bound to the maximum upper bound
    for (int i = minLower; i <= maxUpper; i++) {
        // Check if the integer exists in the set
        if (givenIntegers.find(i) == givenIntegers.end()) {
            // If it does not exist, add it to the list of missing integers
            missingIntegers.push_back(i);
        }
    }
    
    return missingIntegers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + k)$, where $n$ is the number of lower and upper bounds, $m$ is the average range of each bound, and $k$ is the total range of all bounds. The first term represents the time to populate the set of given integers, and the second term represents the time to iterate over the range and find missing integers.
> - **Space Complexity:** $O(n \cdot m)$, which represents the space used to store the set of given integers.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the given list and the range of integers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to store given integers and iterating over the range to find missing integers.
- Problem-solving patterns identified: Finding the minimum and maximum bounds, and iterating over the range to find missing integers.
- Optimization techniques learned: Using a set to store given integers, and iterating over the range to find missing integers.
- Similar problems to practice: Finding missing integers in a list, finding the intersection of two lists, and finding the union of two lists.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the integer exists in the set before adding it to the list of missing integers.
- Edge cases to watch for: Handling empty input lists, and handling input lists with a single element.
- Performance pitfalls: Using a brute force approach that iterates over all possible integers in the range.
- Testing considerations: Testing the function with different input lists, and testing the function with edge cases.