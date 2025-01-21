## Find the Number of Distinct Colors Among the Balls
**Problem Link:** https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description

**Problem Statement:**
- Input: An array of integers `balls` where each integer represents a ball, and each integer corresponds to a color.
- Constraints: $1 \leq balls.length \leq 10^5$.
- Expected output: The number of distinct colors among the balls.
- Key requirements: Count the number of unique colors.
- Edge cases: Empty array, array with one element, array with all elements being the same.

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over the array and check each element to see if it has been encountered before.
- Step-by-step breakdown:
  1. Initialize an empty set to store unique colors.
  2. Iterate over the array of balls.
  3. For each ball, check if its color is already in the set.
  4. If the color is not in the set, add it to the set.
  5. After iterating over all balls, return the size of the set, which represents the number of distinct colors.

```cpp
#include <iostream>
#include <set>
using namespace std;

int distinctColors(int* balls, int ballsSize) {
    set<int> uniqueColors;
    for (int i = 0; i < ballsSize; i++) {
        uniqueColors.insert(balls[i]);
    }
    return uniqueColors.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of balls. This is because we are doing a constant amount of work for each ball.
> - **Space Complexity:** $O(n)$ as in the worst case, all balls could have different colors, requiring a set of size $n$.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the array once. The space complexity is also linear because in the worst case, we might need to store all elements in the set.

### Optimal Approach (Required)
**Explanation:**
- The key insight is that a `set` in C++ is already an optimal data structure for storing unique elements.
- Detailed breakdown:
  1. Use the same approach as the brute force, but recognize that this is already the most efficient way to solve the problem given the constraints.
- Proof of optimality: Since we must examine each ball at least once to determine its color, the time complexity cannot be less than $O(n)$. The use of a `set` allows us to maintain a collection of unique colors in $O(n)$ time and space, which is optimal for this problem.

```cpp
#include <iostream>
#include <set>
using namespace std;

int distinctColors(int* balls, int ballsSize) {
    set<int> uniqueColors;
    for (int i = 0; i < ballsSize; i++) {
        uniqueColors.insert(balls[i]);
    }
    return uniqueColors.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of balls. This is because we are doing a constant amount of work for each ball.
> - **Space Complexity:** $O(n)$ as in the worst case, all balls could have different colors, requiring a set of size $n$.
> - **Optimality proof:** The time complexity is optimal because we must at least read the input once, resulting in a lower bound of $O(n)$. The space complexity is also optimal because we need to store all unique colors.

### Final Notes

**Learning Points:**
- The importance of using the right data structure for the problem. In this case, a `set` is ideal for storing unique elements.
- Understanding the trade-offs between time and space complexity.
- Recognizing when a brute force approach is already optimal due to the nature of the problem.

**Mistakes to Avoid:**
- Not considering the use of built-in data structures like `set` that can simplify the solution and improve efficiency.
- Overcomplicating the solution by trying to optimize beyond what is necessary for the given constraints.
- Not accounting for edge cases, such as an empty input array.