## Count Collisions on a Road

**Problem Link:** https://leetcode.com/problems/count-collisions-on-a-road/description

**Problem Statement:**
- Input format: A string `directions` consisting of 'L', 'R', and 'S' characters, where 'L' denotes a car moving left, 'R' denotes a car moving right, and 'S' denotes a car that has stopped due to a collision.
- Constraints: The length of `directions` is in the range `[1, 1000]`.
- Expected output format: The total number of collisions that will occur on the road.
- Key requirements and edge cases to consider: Cars moving in opposite directions will collide and stop. Cars moving in the same direction will not collide.

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the movement of cars on the road and count the collisions as they occur.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for collisions.
  2. Iterate through the `directions` string from left to right, simulating the movement of cars.
  3. For each car, check if it will collide with any car to its right.
  4. If a collision occurs, increment the collision counter and mark the cars involved as stopped ('S').
  5. Continue the simulation until no more collisions can occur.

```cpp
int countCollisions(string directions) {
    int collisions = 0;
    for (int i = 0; i < directions.size(); i++) {
        if (directions[i] == 'R') {
            for (int j = i + 1; j < directions.size(); j++) {
                if (directions[j] == 'L') {
                    collisions++;
                    directions[i] = 'S';
                    directions[j] = 'S';
                    break;
                }
            }
        }
    }
    return collisions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `directions` string. This is because in the worst case, we are iterating through the string for each character.
> - **Space Complexity:** $O(1)$, as we are modifying the input string in-place and using a constant amount of space to store the collision counter.
> - **Why these complexities occur:** The nested loop structure causes the quadratic time complexity. The space complexity is constant because we are not using any data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a single pass through the `directions` string to count the collisions, rather than simulating the movement of cars.
- Detailed breakdown of the approach:
  1. Initialize a counter for collisions.
  2. Iterate through the `directions` string from left to right.
  3. For each 'R' character, check if there is an 'L' character to its right.
  4. If an 'L' character is found, increment the collision counter.
  5. Continue the iteration until the end of the string.

```cpp
int countCollisions(string directions) {
    int collisions = 0;
    for (int i = 0; i < directions.size(); i++) {
        if (directions[i] == 'R') {
            for (int j = i + 1; j < directions.size(); j++) {
                if (directions[j] == 'L') {
                    collisions++;
                    break;
                }
            }
        }
    }
    return collisions;
}
```

However, we can improve this further by using two pointers, one from the left and one from the right, to track the positions of 'R' and 'L' characters.

```cpp
int countCollisions(string directions) {
    int collisions = 0;
    int left = 0, right = directions.size() - 1;
    while (left < right) {
        if (directions[left] == 'R' && directions[right] == 'L') {
            collisions++;
            left++;
            right--;
        } else if (directions[left] == 'L') {
            left++;
        } else if (directions[right] == 'R') {
            right--;
        } else {
            left++;
            right--;
        }
    }
    return collisions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `directions` string. This is because we are making a single pass through the string.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the collision counter and pointers.
> - **Optimality proof:** This is the optimal solution because we are only iterating through the string once, which is the minimum number of iterations required to count the collisions.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, iteration through a string.
- Problem-solving patterns identified: Using a single pass through the input to count collisions.
- Optimization techniques learned: Reducing the number of iterations through the input.
- Similar problems to practice: Other string manipulation and iteration problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty strings or strings with only one character.
- Edge cases to watch for: Strings with only 'R' or only 'L' characters, strings with no collisions.
- Performance pitfalls: Using nested loops or recursive functions, which can lead to exponential time complexity.
- Testing considerations: Testing the function with different input strings, including edge cases and boundary cases.