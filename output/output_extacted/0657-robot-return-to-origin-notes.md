## Robot Return to Origin
**Problem Link:** https://leetcode.com/problems/robot-return-to-origin/description

**Problem Statement:**
- Input format: A string `moves` consisting of 'U', 'D', 'L', 'R' representing up, down, left, and right movements.
- Constraints: The string length is between 1 and 100.
- Expected output format: A boolean indicating whether the robot returns to the origin (0, 0).
- Key requirements and edge cases to consider: The robot starts at (0, 0) and moves according to the given string.
- Example test cases with explanations:
  - Input: "UD"
    - Explanation: The robot moves up and then down, so it returns to the origin.
  - Input: "LL"
    - Explanation: The robot moves left twice, so it does not return to the origin.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we can simulate the movements of the robot.
- Step-by-step breakdown of the solution:
  1. Initialize variables to keep track of the robot's position.
  2. Iterate over each character in the input string.
  3. Update the robot's position based on the current character.
  4. After iterating over all characters, check if the robot is back at the origin.

```cpp
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0; // Initialize variables to keep track of the robot's position
        for (char move : moves) { // Iterate over each character in the input string
            if (move == 'U') y++; // Update the robot's position based on the current character
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0; // Check if the robot is back at the origin
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we iterate over the string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the robot's position.
> - **Why these complexities occur:** The time complexity is linear because we process each character in the input string once. The space complexity is constant because we only use a fixed amount of space to store the robot's position.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The robot returns to the origin if and only if the number of 'U' movements equals the number of 'D' movements and the number of 'L' movements equals the number of 'R' movements.
- Detailed breakdown of the approach:
  1. Count the number of 'U', 'D', 'L', and 'R' movements.
  2. Check if the number of 'U' movements equals the number of 'D' movements and the number of 'L' movements equals the number of 'R' movements.

```cpp
class Solution {
public:
    bool judgeCircle(string moves) {
        int up = 0, down = 0, left = 0, right = 0; // Count the number of 'U', 'D', 'L', and 'R' movements
        for (char move : moves) {
            if (move == 'U') up++;
            else if (move == 'D') down++;
            else if (move == 'L') left++;
            else if (move == 'R') right++;
        }
        return up == down && left == right; // Check if the number of 'U' movements equals the number of 'D' movements and the number of 'L' movements equals the number of 'R' movements
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we iterate over the string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts of 'U', 'D', 'L', and 'R' movements.
> - **Optimality proof:** This is the optimal solution because we only need to iterate over the input string once to count the number of 'U', 'D', 'L', and 'R' movements. Any further optimization would not improve the time complexity.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Counting and comparison.
- Problem-solving patterns identified: Checking if the number of movements in one direction equals the number of movements in the opposite direction.
- Optimization techniques learned: Using a single pass through the input string to count the number of 'U', 'D', 'L', and 'R' movements.
- Similar problems to practice: Problems involving counting and comparison, such as checking if a string is a palindrome.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not checking for edge cases.
- Edge cases to watch for: Empty input string, input string with only one type of movement.
- Performance pitfalls: Using unnecessary data structures or algorithms that increase the time or space complexity.
- Testing considerations: Testing with different input strings, including edge cases and large inputs.