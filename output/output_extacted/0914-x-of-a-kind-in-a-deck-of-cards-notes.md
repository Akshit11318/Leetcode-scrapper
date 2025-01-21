## X of a Kind in a Deck of Cards

**Problem Link:** https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description

**Problem Statement:**
- Input: An integer array `deck` representing a deck of cards.
- Constraints: `1 <= deck.length <= 10000`, `1 <= deck[i] <= 10000`.
- Expected Output: The largest possible value of `x` such that there are at least `x` cards of each rank in the deck. If no such `x` exists, return `-1`.
- Key requirements: Find the largest possible value of `x` that satisfies the condition for all ranks in the deck.
- Example test cases:
  - Input: `deck = [1,2,3,4,4,3,2,1]`
    - Output: `2`
    - Explanation: We can have 2 cards of each rank 1, 2, and 3.
  - Input: `deck = [1,1,1,2,2,2,3,3]`
    - Output: `-1`
    - Explanation: We cannot have the same number of cards for each rank.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the occurrence of each card rank in the deck and find the minimum count.
- Step-by-step breakdown:
  1. Create a `map` to store the count of each card rank.
  2. Iterate through the deck to count the occurrence of each rank.
  3. Find the minimum count among all ranks.
- Why this approach comes to mind first: It directly addresses the requirement to find the largest possible value of `x` by counting the occurrence of each rank.

```cpp
#include <iostream>
#include <map>

int xOfAKind(int* deck, int deckSize) {
    std::map<int, int> countMap;
    for (int i = 0; i < deckSize; i++) {
        countMap[deck[i]]++;
    }

    int minCount = INT_MAX;
    for (auto& pair : countMap) {
        if (pair.second < minCount) {
            minCount = pair.second;
        }
    }

    // Check if the GCD of all counts is greater than 1
    int gcd = minCount;
    for (auto& pair : countMap) {
        gcd = gcdHelper(gcd, pair.second);
    }

    return gcd > 1 ? gcd : -1;
}

int gcdHelper(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcdHelper(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of the deck and $m$ is the number of unique ranks. This is because we iterate through the deck to count the occurrence of each rank and then iterate through the `map` to find the minimum count.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique ranks. This is because we use a `map` to store the count of each rank.
> - **Why these complexities occur:** The time complexity is linear with respect to the size of the input because we perform a constant amount of work for each element in the deck and each unique rank. The space complexity is linear with respect to the number of unique ranks because we store the count of each rank in the `map`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The largest possible value of `x` is the greatest common divisor (GCD) of the counts of all ranks.
- Detailed breakdown:
  1. Count the occurrence of each card rank in the deck.
  2. Calculate the GCD of the counts of all ranks.
- Proof of optimality: The GCD of the counts of all ranks represents the largest possible value of `x` that satisfies the condition for all ranks.

```cpp
#include <iostream>
#include <map>

int xOfAKind(int* deck, int deckSize) {
    std::map<int, int> countMap;
    for (int i = 0; i < deckSize; i++) {
        countMap[deck[i]]++;
    }

    int gcd = -1;
    for (auto& pair : countMap) {
        if (gcd == -1) {
            gcd = pair.second;
        } else {
            gcd = gcdHelper(gcd, pair.second);
        }
    }

    return gcd > 1 ? gcd : -1;
}

int gcdHelper(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcdHelper(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log m)$, where $n$ is the size of the deck and $m$ is the number of unique ranks. This is because we iterate through the deck to count the occurrence of each rank and then calculate the GCD of the counts.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique ranks. This is because we use a `map` to store the count of each rank.
> - **Optimality proof:** The GCD of the counts of all ranks represents the largest possible value of `x` that satisfies the condition for all ranks. This is because the GCD is the largest number that divides all counts without leaving a remainder.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, GCD calculation.
- Problem-solving patterns identified: Finding the minimum or maximum value, calculating the GCD.
- Optimization techniques learned: Using a `map` to store counts, calculating the GCD.
- Similar problems to practice: Other problems involving counting, GCD calculation, or optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling errors properly.
- Edge cases to watch for: Empty deck, deck with a single rank, deck with multiple ranks.
- Performance pitfalls: Using inefficient algorithms or data structures.
- Testing considerations: Test with different deck sizes, different numbers of unique ranks, and different counts for each rank.