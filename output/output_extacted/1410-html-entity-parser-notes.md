## HTML Entity Parser
**Problem Link:** https://leetcode.com/problems/html-entity-parser/description

**Problem Statement:**
- Input format and constraints: The input string will be a valid HTML entity, and the task is to parse it into a string without HTML entities.
- Expected output format: The output should be a string where all HTML entities are replaced with their corresponding characters.
- Key requirements and edge cases to consider: Handling of nested entities, handling of unknown entities, and handling of edge cases like empty strings or strings with no entities.
- Example test cases with explanations:
  - Input: `"&amp;"` Output: `"&"`
  - Input: `"&lt;"` Output: `"<"`
  - Input: `"&gt;"` Output: `">"`
  - Input: `"&quot;"` Output: `"""`
  - Input: `"&apos;"` Output: `"'"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach to solve this problem is to manually check for each entity in the input string and replace it with its corresponding character.
- Step-by-step breakdown of the solution:
  1. Create a dictionary that maps each entity to its corresponding character.
  2. Iterate over the input string, checking for the start of an entity (`"&"`) and then the corresponding character(s) that define the entity.
  3. If an entity is found, replace it with its corresponding character from the dictionary.
- Why this approach comes to mind first: It directly addresses the problem by checking for each entity and replacing it, which is a straightforward but potentially inefficient approach due to the manual checking and replacement process.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, char> entities = {
            {"&amp;", '&'},
            {"&lt;", '<'},
            {"&gt;", '>'},
            {"&quot;", '\"'},
            {"&apos;", '\''}
        };
        
        string result;
        int i = 0;
        while (i < text.size()) {
            if (text[i] == '&') {
                int j = i + 1;
                while (j < text.size() && text[j] != ';') {
                    j++;
                }
                if (j < text.size() && text[j] == ';') {
                    string entity = text.substr(i, j - i + 1);
                    if (entities.find(entity) != entities.end()) {
                        result += entities[entity];
                    } else {
                        result += entity;
                    }
                    i = j + 1;
                } else {
                    result += text[i];
                    i++;
                }
            } else {
                result += text[i];
                i++;
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because in the worst case, we might need to iterate over the entire string once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, because the space used does not grow with the size of the input, given that the number of entities is constant.
> - **Why these complexities occur:** The time complexity is linear because we only need to make a single pass through the input string. The space complexity is constant because we use a fixed amount of space to store the entities and their corresponding characters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilizing a similar approach to the brute force but optimizing it by directly iterating over the string and using a more efficient data structure to store the entities.
- Detailed breakdown of the approach: The optimal approach involves creating a dictionary that maps entities to their corresponding characters and then iterating over the input string, checking for entities and replacing them.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string and uses a constant amount of space to store the entities, resulting in a linear time complexity.
- Why further optimization is impossible: Further optimization is not possible because we must at least read the input string once, which already requires $O(n)$ time.

```cpp
class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, char> entities = {
            {"&amp;", '&'},
            {"&lt;", '<'},
            {"&gt;", '>'},
            {"&quot;", '\"'},
            {"&apos;", '\''}
        };
        
        string result;
        int i = 0;
        while (i < text.size()) {
            if (text[i] == '&') {
                int j = i + 1;
                while (j < text.size() && text[j] != ';') {
                    j++;
                }
                if (j < text.size() && text[j] == ';') {
                    string entity = text.substr(i, j - i + 1);
                    if (entities.find(entity) != entities.end()) {
                        result += entities[entity];
                    } else {
                        result += entity;
                    }
                    i = j + 1;
                } else {
                    result += text[i];
                    i++;
                }
            } else {
                result += text[i];
                i++;
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, because we use a constant amount of space to store the entities.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a constant amount of space, which are the minimum requirements for solving this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and the use of dictionaries for efficient lookups.
- Problem-solving patterns identified: Directly addressing the problem by checking for entities and replacing them, optimizing the approach by using efficient data structures.
- Optimization techniques learned: Using a dictionary for constant time lookups, minimizing the number of iterations over the input string.
- Similar problems to practice: Other string manipulation problems that involve replacing substrings or characters based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for the end of an entity (`";"`) or incorrectly handling unknown entities.
- Edge cases to watch for: Empty strings, strings with no entities, and strings with nested entities.
- Performance pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexities.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure it works correctly in all scenarios.