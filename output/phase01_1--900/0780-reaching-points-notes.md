## Reaching Points
**Problem Link:** https://leetcode.com/problems/reaching-points/description

**Problem Statement:**
- Input format: Two integers `sx` and `sy` representing the starting point, and two integers `tx` and `ty` representing the target point.
- Constraints: `1 <= sx, sy, tx, ty <= 10^9`
- Expected output format: A boolean indicating whether it's possible to reach the target point from the starting point.
- Key requirements: The movement is restricted to either adding `sx` to `tx` or `sy` to `ty`.
- Example test cases:
  - Input: `sx = 1, sy = 1, tx = 3, ty = 5`
    - Output: `true`
    - Explanation: `1 -> 4 -> 8 -> 5` (by adding `sx` and `sy` to `tx` and `ty` respectively in each step)
  - Input: `sx = 2, sy = 3, tx = 8, ty = 4`
    - Output: `true`
    - Explanation: `2 -> 5 -> 8 -> 4` (by adding `sx` and `sy` to `tx` and `ty` respectively in each step)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of adding `sx` to `tx` and `sy` to `ty` until we reach or exceed the target point.
- Step-by-step breakdown:
  1. Start from the initial point `(sx, sy)`.
  2. At each step, try adding `sx` to `tx` and `sy` to `ty`.
  3. If the new point exceeds the target point, backtrack and try the other option.
  4. Continue until we reach the target point or all possible paths have been explored.

```cpp
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        if (tx < sx || ty < sy) return false;
        if (tx == sx && ty % sy == 0) return true;
        if (ty == sy && tx % sx == 0) return true;
        
        if (tx > ty) {
            int step = tx / sx;
            tx -= step * sx;
        } else {
            int step = ty / sy;
            ty -= step * sy;
        }
        
        return reachingPoints(sx, sy, tx, ty);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(min(tx, ty)))$ because in each recursive call, we reduce either `tx` or `ty` by a factor of `sx` or `sy` respectively.
> - **Space Complexity:** $O(log(min(tx, ty)))$ due to the recursive call stack.
> - **Why these complexities occur:** The recursive approach leads to these complexities because we are essentially performing a depth-first search with backtracking.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The problem can be solved using a mathematical approach based on the properties of the greatest common divisor (GCD).
- Detailed breakdown:
  1. If `tx` and `ty` are both divisible by `sx` and `sy` respectively, we can reduce the problem to a simpler form.
  2. We can use the property that `gcd(a, b) = gcd(a, b % a)` to simplify the problem.
  3. If `tx` and `ty` are not both divisible by `sx` and `sy`, we can reduce the problem to a simpler form by subtracting multiples of `sx` from `tx` and multiples of `sy` from `ty`.

```cpp
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy && tx != ty) {
            if (tx > ty) {
                if (ty == sy) return (tx - sx) % ty == 0;
                tx %= ty;
            } else {
                if (tx == sx) return (ty - sy) % tx == 0;
                ty %= tx;
            }
        }
        return tx == sx && ty == sy;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(min(tx, ty)))$ because in each iteration, we reduce either `tx` or `ty` by a factor of `ty` or `tx` respectively.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses a mathematical insight to simplify the problem and reduce the number of iterations required.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, mathematical insight, and iterative approach.
- Problem-solving patterns identified: Using GCD to simplify the problem and reducing the problem to a simpler form.
- Optimization techniques learned: Using mathematical insights to reduce the number of iterations required.
- Similar problems to practice: Problems involving GCD, recursive approach, and iterative approach.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base cases correctly, not reducing the problem to a simpler form.
- Edge cases to watch for: `tx` and `ty` being equal, `tx` and `ty` being both divisible by `sx` and `sy`.
- Performance pitfalls: Using a recursive approach without optimizing the problem.
- Testing considerations: Testing the function with different inputs, including edge cases.