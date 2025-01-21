## Number of Pairs of Interchangeable Rectangles

**Problem Link:** https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/description

**Problem Statement:**
- Input: A list of rectangles where each rectangle is represented as an array of two integers `[length, width]`.
- Constraints: `1 <= rectangles.length <= 10^5`, `1 <= length, width <= 10^5`.
- Expected Output: The number of pairs of interchangeable rectangles.
- Key Requirements and Edge Cases:
  - Two rectangles are interchangeable if they have the same area and the same orientation (i.e., length and width are the same).
  - The order of the rectangles does not matter.

**Example Test Cases:**
- Example 1:
  - Input: `rectangles = [[4,8],[3,6],[10,20],[6,12]]`
  - Output: `3`
  - Explanation: The three pairs of interchangeable rectangles are `[[4,8],[6,12]]`, `[[3,6],[6,12]]`, and `[[4,8],[6,12]]`.
- Example 2:
  - Input: `rectangles = [[4,5],[7,8]]`
  - Output: `0`
  - Explanation: There are no pairs of interchangeable rectangles.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each pair of rectangles to check if they are interchangeable.
- We will iterate over the list of rectangles and for each rectangle, we will compare it with every other rectangle.
- We will check if the areas and orientations of the two rectangles are the same.

```cpp
#include <iostream>
#include <vector>

int interchangeableRectangles(std::vector<std::vector<int>>& rectangles) {
    int count = 0;
    for (int i = 0; i < rectangles.size(); i++) {
        for (int j = i + 1; j < rectangles.size(); j++) {
            if (rectangles[i][0] * rectangles[i][1] == rectangles[j][0] * rectangles[j][1] &&
                (rectangles[i][0] == rectangles[j][0] && rectangles[i][1] == rectangles[j][1] ||
                 rectangles[i][0] == rectangles[j][1] && rectangles[i][1] == rectangles[j][0])) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rectangles. This is because we have two nested loops that iterate over the list of rectangles.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are comparing each pair of rectangles, and the space complexity occurs because we are only using a constant amount of space to store the count of interchangeable rectangles.

---

### Optimal Approach

**Explanation:**
- The key insight that leads to the optimal solution is to use a hashmap to store the frequency of each rectangle.
- We will iterate over the list of rectangles and for each rectangle, we will calculate its area and orientation.
- We will use a hashmap to store the frequency of each rectangle based on its area and orientation.
- Finally, we will calculate the number of pairs of interchangeable rectangles using the frequencies stored in the hashmap.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int interchangeableRectangles(std::vector<std::vector<int>>& rectangles) {
    std::unordered_map<std::pair<int, int>, int> freq;
    for (auto& rect : rectangles) {
        int area = rect[0] * rect[1];
        std::pair<int, int> orientation = {rect[0], rect[1]};
        if (rect[0] > rect[1]) {
            orientation = {rect[1], rect[0]};
        }
        freq[{area, orientation.first, orientation.second}]++;
    }
    int count = 0;
    for (auto& it : freq) {
        int f = it.second;
        count += f * (f - 1) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rectangles. This is because we are iterating over the list of rectangles once.
> - **Space Complexity:** $O(n)$ because we are using a hashmap to store the frequency of each rectangle.
> - **Optimality proof:** This is the optimal solution because we are only iterating over the list of rectangles once and using a hashmap to store the frequency of each rectangle. This reduces the time complexity from $O(n^2)$ to $O(n)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a hashmap to store the frequency of each rectangle.
- The problem-solving pattern identified is to use a hashmap to reduce the time complexity of the solution.
- The optimization technique learned is to use a hashmap to store the frequency of each rectangle and calculate the number of pairs of interchangeable rectangles using the frequencies stored in the hashmap.

**Mistakes to Avoid:**
- A common implementation error is to not handle the case where the length and width of a rectangle are the same.
- An edge case to watch for is when the input list of rectangles is empty.
- A performance pitfall is to use a brute force approach that has a time complexity of $O(n^2)$.
- A testing consideration is to test the solution with different input sizes and edge cases.