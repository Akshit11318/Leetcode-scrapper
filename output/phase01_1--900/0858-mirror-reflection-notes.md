## Mirror Reflection

**Problem Link:** https://leetcode.com/problems/mirror-reflection/description

**Problem Statement:**
- Input format: Two integers `p` and `q` representing the number of units the laser beam travels.
- Constraints: `1 <= p <= 1000`, `1 <= q <= 1000`.
- Expected output format: The location where the laser beam stops, either `0` (top left corner), `1` (top right corner), or `2` (bottom left corner).
- Key requirements: Determine the final position of the laser beam after reflecting off the mirrors.
- Example test cases:
  - `p = 2`, `q = 1`: The laser beam travels `2` units and reflects off the top mirror, then travels `1` unit and reflects off the bottom mirror, ending at the top left corner (`0`).
  - `p = 3`, `q = 1`: The laser beam travels `3` units and reflects off the top mirror, then travels `1` unit and reflects off the bottom mirror, ending at the top right corner (`1`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves simulating the movement of the laser beam and counting the number of reflections off the top and bottom mirrors.
- We can use a simple loop to simulate the movement and reflections.
- This approach comes to mind first because it directly models the problem statement.

```cpp
int mirrorReflection(int p, int q) {
    int reflections = 0;
    while (p > 0 && q > 0) {
        if (p > q) {
            p -= q;
            reflections++;
        } else if (p < q) {
            q -= p;
            reflections++;
        } else {
            return reflections % 2 == 0 ? 0 : 1;
        }
    }
    return reflections % 2 == 0 ? 0 : 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(p + q)$, where $p$ and $q$ are the input integers. This is because in the worst case, we need to simulate $p + q$ reflections.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the reflections and the remaining distances.
> - **Why these complexities occur:** The time complexity occurs because we need to simulate each reflection, and the space complexity is constant because we only use a fixed amount of space to store the state.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that the final position of the laser beam only depends on the parity of `p` and `q`.
- If `p` is even and `q` is odd, the laser beam will end at the top left corner (`0`).
- If `p` is odd and `q` is odd, the laser beam will end at the top right corner (`1`).
- If `p` is odd and `q` is even, the laser beam will end at the bottom left corner (`2`).
- We can directly calculate the final position based on the parity of `p` and `q`.

```cpp
int mirrorReflection(int p, int q) {
    if (p % 2 == 0 && q % 2 == 1) {
        return 0;
    } else if (p % 2 == 1 && q % 2 == 1) {
        return 1;
    } else {
        return 2;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only need to perform a constant number of operations to calculate the final position.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Optimality proof:** This solution is optimal because we directly calculate the final position based on the parity of `p` and `q`, without simulating any reflections.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: parity analysis, direct calculation.
- Problem-solving patterns identified: reducing the problem to a simpler case, using parity analysis to simplify the solution.
- Optimization techniques learned: eliminating unnecessary simulations, using direct calculations.
- Similar problems to practice: other problems that involve parity analysis or direct calculations.

**Mistakes to Avoid:**
- Common implementation errors: incorrect parity analysis, incorrect simulation of reflections.
- Edge cases to watch for: `p = 0`, `q = 0`, `p = q`.
- Performance pitfalls: simulating unnecessary reflections, using excessive memory.
- Testing considerations: test cases with different parities of `p` and `q`, test cases with edge values of `p` and `q`.