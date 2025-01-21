## Unique Number of Occurrences
**Problem Link:** https://leetcode.com/problems/unique-number-of-occurrences/description

**Problem Statement:**
- Input format: An array of integers `arr`.
- Constraints: `1 <= arr.length <= 1000`, `0 <= arr[i] <= 1000`.
- Expected output format: A boolean value indicating whether the number of occurrences of each element is unique.
- Key requirements and edge cases to consider: 
    - The array may contain duplicate elements.
    - The array may contain a single unique element.
    - The array may be empty.
- Example test cases with explanations:
    - Input: `arr = [1,2,2,1,1,3]`. Output: `false`. Explanation: The number 1 occurs three times and the number 2 occurs twice, so the number of occurrences of each element is not unique.
    - Input: `arr = [1,2]`. Output: `true`. Explanation: The number 1 occurs once and the number 2 occurs once, so the number of occurrences of each element is unique.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if the number of occurrences of each element is unique, we can count the occurrences of each element and store them in a separate data structure.
- Step-by-step breakdown of the solution:
    1. Create a frequency map to store the count of each element in the array.
    2. Iterate over the frequency map and store the counts in a separate data structure (e.g., a set or a list).
    3. Check if the size of the set/list is equal to the number of unique elements in the frequency map. If they are equal, return true; otherwise, return false.
- Why this approach comes to mind first: It is a straightforward solution that involves counting the occurrences of each element and checking if these counts are unique.

```cpp
#include <iostream>
#include <unordered_map>
#include <set>

bool uniqueOccurrences(int* arr, int arrSize) {
    // Create a frequency map to store the count of each element
    std::unordered_map<int, int> frequencyMap;
    for (int i = 0; i < arrSize; i++) {
        if (frequencyMap.find(arr[i]) != frequencyMap.end()) {
            frequencyMap[arr[i]]++;
        } else {
            frequencyMap[arr[i]] = 1;
        }
    }
    
    // Store the counts in a set
    std::set<int> counts;
    for (auto& pair : frequencyMap) {
        counts.insert(pair.second);
    }
    
    // Check if the size of the set is equal to the number of unique elements
    return counts.size() == frequencyMap.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the array once to create the frequency map and then iterate over the frequency map to store the counts in a set.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because in the worst case, we may need to store every element in the frequency map and the set.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the input array. The space complexity is also linear because we may need to store every element in the frequency map and the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the array to count the occurrences of each element and store the counts in a set.
- Detailed breakdown of the approach:
    1. Create an unordered map to store the count of each element.
    2. Create a set to store unique counts.
    3. Iterate over the array, updating the count of each element in the map and adding the count to the set if it's not already present.
    4. If we encounter a count that's already in the set, return false.
- Proof of optimality: This solution has the same time and space complexity as the brute force approach but is more efficient in practice because it uses a single pass over the array and avoids unnecessary iterations.
- Why further optimization is impossible: We must iterate over the array at least once to count the occurrences of each element, and we must store these counts in a data structure to check for uniqueness. Therefore, the time and space complexities of this solution are optimal.

```cpp
#include <iostream>
#include <unordered_map>
#include <set>

bool uniqueOccurrences(int* arr, int arrSize) {
    // Create a frequency map and a set to store unique counts
    std::unordered_map<int, int> frequencyMap;
    std::set<int> counts;
    
    // Iterate over the array, updating the count of each element and adding it to the set
    for (int i = 0; i < arrSize; i++) {
        if (frequencyMap.find(arr[i]) != frequencyMap.end()) {
            frequencyMap[arr[i]]++;
        } else {
            frequencyMap[arr[i]] = 1;
        }
        
        // If the count is already in the set, return false
        if (counts.find(frequencyMap[arr[i]]) != counts.end()) {
            return false;
        }
        
        // Add the count to the set
        counts.insert(frequencyMap[arr[i]]);
    }
    
    // If we've iterated over the entire array without returning false, return true
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the array once, updating the count of each element and adding it to the set.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because in the worst case, we may need to store every element in the frequency map and the set.
> - **Optimality proof:** This solution is optimal because it uses a single pass over the array and avoids unnecessary iterations. The time and space complexities are optimal because we must iterate over the array at least once to count the occurrences of each element and store these counts in a data structure to check for uniqueness.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, set operations, and frequency counting.
- Problem-solving patterns identified: Using a single pass over the array to count occurrences and check for uniqueness.
- Optimization techniques learned: Avoiding unnecessary iterations and using a single data structure to store counts.
- Similar problems to practice: Other problems involving frequency counting and set operations, such as finding the most frequent element in an array or checking if two arrays have the same frequency distribution.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty array or an array with a single unique element.
- Edge cases to watch for: Arrays with duplicate elements, arrays with a single unique element, and empty arrays.
- Performance pitfalls: Using unnecessary iterations or data structures, which can increase the time and space complexity of the solution.
- Testing considerations: Testing the solution with a variety of input arrays, including edge cases and arrays with different frequency distributions.