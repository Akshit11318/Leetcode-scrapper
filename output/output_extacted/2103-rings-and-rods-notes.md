## Rings and Rods

**Problem Link:** https://leetcode.com/problems/rings-and-rods/description

**Problem Statement:**
- Input format and constraints: The input is a string `rings`, where each character is either 'R', 'G', or 'B', representing a ring of red, green, or blue color, respectively. The string will have a length of at least 1 and at most 100. Each rod can hold at most 10 rings.
- Expected output format: The function should return the number of rods that can hold all the rings.
- Key requirements and edge cases to consider: The function should handle cases where there are more rings than rods, and where there are multiple rods with the same color of rings.
- Example test cases with explanations:
  - Input: "BGBG" - Output: 2 (There are 2 rods, each with 2 rings of different colors)
  - Input: "R" - Output: 1 (There is 1 rod with 1 ring)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves counting the number of rods that can hold all the rings by iterating over the input string and checking each character.
- Step-by-step breakdown of the solution:
  1. Initialize an empty dictionary to store the count of each color of ring on each rod.
  2. Iterate over the input string, and for each character, increment the count of the corresponding color in the dictionary.
  3. If a rod already has a ring of the same color, increment the count of that color.
  4. If a rod does not have a ring of the same color, add a new rod with a count of 1 for that color.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

int countRods(const std::string& rings) {
    std::unordered_map<int, std::unordered_map<char, int>> rods;
    int rodCount = 0;
    for (int i = 0; i < rings.size(); i += 2) {
        int rodIndex = rings[i + 1] - '0';
        char color = rings[i];
        if (rods.find(rodIndex) == rods.end()) {
            rods[rodIndex] = {};
            rodCount++;
        }
        rods[rodIndex][color]++;
    }
    return rodCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all characters in the dictionary.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the input string once. The space complexity is also linear because in the worst case, we might need to store all characters in the dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a set to store the colors of rings on each rod, and then count the number of rods that have at least one ring.
- Detailed breakdown of the approach:
  1. Initialize an empty dictionary to store the set of colors for each rod.
  2. Iterate over the input string, and for each character, add the color to the set of colors for the corresponding rod.
  3. Count the number of rods that have at least one ring.
- Proof of optimality: This approach is optimal because it uses a set to store the colors of rings on each rod, which reduces the space complexity to $O(n)$.

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <unordered_set>

int countRods(const std::string& rings) {
    std::unordered_map<int, std::unordered_set<char>> rods;
    for (int i = 0; i < rings.size(); i += 2) {
        int rodIndex = rings[i + 1] - '0';
        char color = rings[i];
        rods[rodIndex].insert(color);
    }
    return rods.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all characters in the dictionary.
> - **Optimality proof:** This approach is optimal because it uses a set to store the colors of rings on each rod, which reduces the space complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store the count of each color of ring on each rod, and using a set to store the colors of rings on each rod.
- Problem-solving patterns identified: The problem can be solved by iterating over the input string and counting the number of rods that have at least one ring.
- Optimization techniques learned: Using a set to store the colors of rings on each rod reduces the space complexity to $O(n)$.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a rod already has a ring of the same color.
- Edge cases to watch for: The input string may be empty, or there may be more rings than rods.
- Performance pitfalls: Using a brute force approach can lead to a time complexity of $O(n^2)$.
- Testing considerations: The function should be tested with different input strings, including empty strings and strings with multiple rods and rings.