## Maximum Good People Based on Statements
**Problem Link:** https://leetcode.com/problems/maximum-good-people-based-on-statements/description

**Problem Statement:**
- Input format: `statements` - a 2D array where each subarray contains two integers representing a statement about the goodness of two people.
- Constraints: The length of `statements` will be in the range [1, 1000], and the values of `statements[i]` will be in the range [1, 1000].
- Expected output format: The maximum number of good people.
- Key requirements and edge cases to consider:
  - A person is considered good if they make a statement that is true and do not make any false statements.
  - If a person makes a statement that is false, they are considered bad, regardless of any true statements they make.
- Example test cases with explanations:
  - `statements = [[1,2],[1,3],[2,3]]` returns `3`, because all three people are good.
  - `statements = [[1,2],[2,1]]` returns `2`, because both people are good.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a person is good, we need to check all their statements.
- Step-by-step breakdown of the solution:
  1. Create a `isGood` function that checks if a person is good by verifying all their statements.
  2. Iterate through all people and use the `isGood` function to determine if they are good.
  3. Count the number of good people.

```cpp
class Solution {
public:
    int maximumGood(vector<vector<int>>& statements) {
        int n = statements.size();
        int maxGood = 0;
        
        // Iterate over all possible subsets of people
        for (int mask = 0; mask < (1 << n); mask++) {
            int goodCount = 0;
            bool isValid = true;
            
            // Check if the current subset is valid
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    goodCount++;
                    
                    // Check all statements made by person i
                    for (auto& statement : statements[i]) {
                        int person = statement[0] - 1;
                        bool isGood = statement[1] == 1;
                        
                        if (isGood) {
                            if ((mask & (1 << person)) == 0) {
                                isValid = false;
                                break;
                            }
                        } else {
                            if ((mask & (1 << person)) != 0) {
                                isValid = false;
                                break;
                            }
                        }
                    }
                    
                    if (!isValid) break;
                }
            }
            
            if (isValid) maxGood = max(maxGood, goodCount);
        }
        
        return maxGood;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of people and $m$ is the average number of statements made by each person. This is because we iterate over all possible subsets of people and check all their statements.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `maxGood` variable and other loop variables.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because we iterate over all possible subsets of people. The space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force, but with some optimizations.
- Detailed breakdown of the approach:
  1. Iterate over all possible subsets of people.
  2. For each subset, check if it is valid by verifying all statements made by people in the subset.
  3. If a subset is valid, update the maximum count of good people.

```cpp
class Solution {
public:
    int maximumGood(vector<vector<int>>& statements) {
        int n = statements.size();
        int maxGood = 0;
        
        // Iterate over all possible subsets of people
        for (int mask = 0; mask < (1 << n); mask++) {
            bool isValid = true;
            
            // Check if the current subset is valid
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    // Check all statements made by person i
                    for (auto& statement : statements[i]) {
                        int person = statement[0] - 1;
                        bool isGood = statement[1] == 1;
                        
                        if (isGood) {
                            if ((mask & (1 << person)) == 0) {
                                isValid = false;
                                break;
                            }
                        } else {
                            if ((mask & (1 << person)) != 0) {
                                isValid = false;
                                break;
                            }
                        }
                    }
                    
                    if (!isValid) break;
                }
            }
            
            if (isValid) {
                int goodCount = 0;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) != 0) goodCount++;
                }
                maxGood = max(maxGood, goodCount);
            }
        }
        
        return maxGood;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of people and $m$ is the average number of statements made by each person.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `maxGood` variable and other loop variables.
> - **Optimality proof:** This solution is optimal because it checks all possible subsets of people and verifies all their statements. Any further optimization would require reducing the number of subsets or statements to check, which is not possible in the general case.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterating over all possible subsets of people and verifying all their statements.
- Problem-solving patterns identified: Using a brute force approach and optimizing it to reduce the number of subsets or statements to check.
- Optimization techniques learned: Reducing the number of subsets or statements to check by using a more efficient algorithm or data structure.
- Similar problems to practice: Other problems that involve iterating over all possible subsets of people or verifying all statements made by people.

**Mistakes to Avoid:**
- Common implementation errors: Not checking all possible subsets of people or not verifying all statements made by people.
- Edge cases to watch for: Subsets with no people or subsets with all people.
- Performance pitfalls: Using an inefficient algorithm or data structure that has a high time or space complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.