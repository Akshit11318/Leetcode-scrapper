## Maximum Number of Potholes That Can Be Fixed

**Problem Link:** https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/description

**Problem Statement:**
- Input format and constraints: Given a string `s` representing the road with potholes, where `#` denotes a pothole and `.` denotes a normal road cell. The goal is to find the maximum number of potholes that can be fixed by filling in the potholes with stones, considering that stones can only be placed in empty cells next to a pothole.
- Expected output format: The maximum number of potholes that can be fixed.
- Key requirements and edge cases to consider: The road is represented as a string, and stones can only be placed next to a pothole. If there are no potholes, the output should be 0.
- Example test cases with explanations:
  - Input: `s = "##..##"` Output: `2`
  - Input: `s = "#...#"` Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would involve checking every possible combination of placing stones next to potholes and counting the maximum number of potholes that can be fixed in each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of placing stones next to potholes.
  2. For each combination, count the number of potholes that can be fixed.
  3. Keep track of the maximum count across all combinations.

```cpp
#include <iostream>
#include <vector>
#include <string>

int maxPotholesFixed(const std::string& s) {
    int maxCount = 0;
    int n = s.size();
    
    // Generate all possible combinations of placing stones next to potholes
    for (int mask = 0; mask < (1 << n); mask++) {
        int count = 0;
        std::string temp = s;
        
        // For each combination, count the number of potholes that can be fixed
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) && temp[i] == '#') {
                // Check if there is an empty cell next to the pothole
                if (i > 0 && temp[i - 1] == '.') {
                    count++;
                    temp[i - 1] = '#'; // Mark the cell as fixed
                } else if (i < n - 1 && temp[i + 1] == '.') {
                    count++;
                    temp[i + 1] = '#'; // Mark the cell as fixed
                }
            }
        }
        
        // Keep track of the maximum count across all combinations
        maxCount = std::max(maxCount, count);
    }
    
    return maxCount;
}

int main() {
    std::string s;
    std::cin >> s;
    std::cout << maxPotholesFixed(s) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible combinations of placing stones next to potholes, which takes $O(2^n)$ time, and for each combination, we count the number of potholes that can be fixed, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the temporary string `temp` for each combination.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of placing stones next to potholes, which results in an exponential time complexity. The space complexity is linear because we only need to store a temporary string for each combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. We iterate through the string and for each pothole, we check if there is an empty cell next to it. If there is, we fix the pothole and mark the cell as fixed.
- Detailed breakdown of the approach:
  1. Initialize a count variable to keep track of the maximum number of potholes that can be fixed.
  2. Iterate through the string and for each pothole, check if there is an empty cell next to it.
  3. If there is, fix the pothole and mark the cell as fixed, and increment the count variable.

```cpp
#include <iostream>
#include <string>

int maxPotholesFixed(const std::string& s) {
    int count = 0;
    int n = s.size();
    std::string temp = s;
    
    for (int i = 0; i < n; i++) {
        if (temp[i] == '#') {
            // Check if there is an empty cell next to the pothole
            if (i > 0 && temp[i - 1] == '.') {
                count++;
                temp[i - 1] = '#'; // Mark the cell as fixed
            } else if (i < n - 1 && temp[i + 1] == '.') {
                count++;
                temp[i + 1] = '#'; // Mark the cell as fixed
            }
        }
    }
    
    return count;
}

int main() {
    std::string s;
    std::cin >> s;
    std::cout << maxPotholesFixed(s) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we only need to iterate through the string once to fix all the potholes.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the temporary string `temp`.
> - **Optimality proof:** This approach is optimal because we are using a greedy strategy to fix the potholes. We are fixing each pothole as soon as we encounter it, and we are not missing any opportunities to fix potholes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, string manipulation.
- Problem-solving patterns identified: Using a temporary string to keep track of changes, iterating through a string to find and fix potholes.
- Optimization techniques learned: Using a greedy approach to solve the problem in linear time complexity.
- Similar problems to practice: Other string manipulation problems, such as finding the longest palindromic substring or the shortest path in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string or a string with no potholes.
- Edge cases to watch for: An empty string, a string with no potholes, a string with only potholes.
- Performance pitfalls: Using an exponential time complexity approach, such as generating all possible combinations of placing stones next to potholes.
- Testing considerations: Test the function with different inputs, such as an empty string, a string with no potholes, a string with only potholes, and a string with a mix of potholes and empty cells.