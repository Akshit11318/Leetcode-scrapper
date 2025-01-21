## Count Apples and Oranges

**Problem Link:** https://leetcode.com/problems/count-apples-and-oranges/description

**Problem Statement:**
- Input format and constraints: The problem takes seven integers as input: `s`, `t`, `a`, `b`, `apples`, and `oranges`. `s` and `t` represent the start and end of the house, `a` and `b` represent the positions of the apple and orange trees, and `apples` and `oranges` are arrays representing the distances at which the apples and oranges fall from their respective trees.
- Expected output format: The problem requires us to count the number of apples and oranges that fall within the range of the house (`s` to `t`).
- Key requirements and edge cases to consider: We need to calculate the positions where the apples and oranges fall by adding the tree positions to the distances in the `apples` and `oranges` arrays, then count how many of these positions fall within the house range.
- Example test cases with explanations: For example, if `s = 7`, `t = 11`, `a = 5`, `b = 15`, `apples = [-2, 2, 1]`, and `oranges = [5, -6]`, then the apples fall at positions `5 - 2 = 3`, `5 + 2 = 7`, and `5 + 1 = 6`, and the oranges fall at positions `15 + 5 = 20` and `15 - 6 = 9`. Only the apples at positions 6 and 7 fall within the house range.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to calculate the positions where the apples and oranges fall by adding the tree positions to the distances in the `apples` and `oranges` arrays.
- Step-by-step breakdown of the solution: Then, we iterate over these positions and count how many of them fall within the house range.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
#include <iostream>
using namespace std;

void countApplesAndOranges(int s, int t, int a, int b, int apples[], int applesSize, int oranges[], int orangesSize) {
    int appleCount = 0;
    int orangeCount = 0;

    // Calculate positions of apples and count those within the house range
    for (int i = 0; i < applesSize; i++) {
        int position = a + apples[i];
        if (position >= s && position <= t) {
            appleCount++;
        }
    }

    // Calculate positions of oranges and count those within the house range
    for (int i = 0; i < orangesSize; i++) {
        int position = b + oranges[i];
        if (position >= s && position <= t) {
            orangeCount++;
        }
    }

    cout << appleCount << endl;
    cout << orangeCount << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of apples and $m$ is the number of oranges. This is because we iterate over the apples and oranges once each.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts of apples and oranges within the house range.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each apple and orange. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach because we must examine each apple and orange at least once to determine if it falls within the house range.
- Detailed breakdown of the approach: The solution involves calculating the positions of the apples and oranges by adding the tree positions to their respective distances, then counting those positions that fall within the house range.
- Proof of optimality: This approach is optimal because it has a linear time complexity, which is the best we can achieve given that we must examine each apple and orange at least once.
- Why further optimization is impossible: Further optimization is impossible because we cannot avoid examining each apple and orange, and we must perform a constant amount of work for each one.

```cpp
#include <iostream>
using namespace std;

void countApplesAndOranges(int s, int t, int a, int b, int apples[], int applesSize, int oranges[], int orangesSize) {
    int appleCount = 0;
    int orangeCount = 0;

    // Calculate positions of apples and count those within the house range
    for (int i = 0; i < applesSize; i++) {
        if (a + apples[i] >= s && a + apples[i] <= t) {
            appleCount++;
        }
    }

    // Calculate positions of oranges and count those within the house range
    for (int i = 0; i < orangesSize; i++) {
        if (b + oranges[i] >= s && b + oranges[i] <= t) {
            orangeCount++;
        }
    }

    cout << appleCount << endl;
    cout << orangeCount << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of apples and $m$ is the number of oranges. This is because we iterate over the apples and oranges once each.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counts of apples and oranges within the house range.
> - **Optimality proof:** This approach is optimal because it has the best possible time complexity given the problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear iteration, conditional counting.
- Problem-solving patterns identified: Examining each element in a collection to determine if it meets a certain condition.
- Optimization techniques learned: Recognizing that sometimes the brute force approach is already optimal.
- Similar problems to practice: Other problems involving linear iteration and conditional counting.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, incorrect loop bounds.
- Edge cases to watch for: Empty input arrays, negative distances.
- Performance pitfalls: Using unnecessary data structures or algorithms that have higher time complexities.
- Testing considerations: Ensure that the solution works correctly for a variety of input sizes and edge cases.