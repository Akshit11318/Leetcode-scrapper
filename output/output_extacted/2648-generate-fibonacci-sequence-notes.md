## Generate Fibonacci Sequence
**Problem Link:** https://leetcode.com/problems/generate-fibonacci-sequence/description

**Problem Statement:**
- Input format and constraints: The function should take an integer `n` as input, representing the number of terms in the Fibonacci sequence to generate.
- Expected output format: The function should return a vector of integers representing the first `n` terms of the Fibonacci sequence.
- Key requirements and edge cases to consider: Handle cases where `n` is 0, 1, or negative. For `n` = 0, return an empty vector. For `n` = 1, return a vector with a single element, 0. For negative `n`, either return an empty vector or throw an exception, depending on the specific requirements.
- Example test cases with explanations:
  - `n` = 5 should return `[0, 1, 1, 2, 3]`.
  - `n` = 0 should return `[]`.
  - `n` = 1 should return `[0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to generate the Fibonacci sequence is to start with the first two terms (0 and 1) and then iteratively calculate each subsequent term as the sum of the previous two.
- Step-by-step breakdown of the solution:
  1. Initialize a vector with the first two terms of the sequence (0 and 1).
  2. If `n` is less than or equal to 2, return the vector (since it already contains the required number of terms).
  3. Otherwise, enter a loop that continues until the vector contains `n` terms.
  4. In each iteration of the loop, calculate the next term as the sum of the last two terms in the vector and append it to the vector.
- Why this approach comes to mind first: It directly follows the definition of the Fibonacci sequence and is easy to understand and implement.

```cpp
vector<int> generateFibonacciSequence(int n) {
    if (n <= 0) {
        return {}; // Return an empty vector for non-positive n
    }

    vector<int> sequence = {0, 1};
    while (sequence.size() < n) {
        int nextTerm = sequence.back() + sequence[sequence.size() - 2];
        sequence.push_back(nextTerm);
    }

    // If n is 1, return a vector with only the first term
    if (n == 1) {
        sequence.pop_back(); // Remove the second term
    }

    return sequence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we potentially iterate `n` times to generate the sequence.
> - **Space Complexity:** $O(n)$, since in the worst case, we store `n` terms in the sequence vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work in each iteration of the loop, which runs `n` times. The space complexity is also linear because we store each term of the sequence in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient for generating the Fibonacci sequence up to `n` terms. However, we can slightly optimize it by handling the base cases more efficiently and avoiding unnecessary iterations.
- Detailed breakdown of the approach:
  1. Handle base cases (`n` <= 0, `n` == 1) immediately and return the corresponding result.
  2. Initialize the sequence with the first two terms if `n` > 1.
  3. Use a loop to generate the rest of the sequence, but avoid calculating the next term if it's not needed (i.e., if we've already reached `n` terms).
- Proof of optimality: This approach is optimal because it generates the Fibonacci sequence in linear time and space, which is the best we can achieve given the need to store and calculate each term.
- Why further optimization is impossible: Any algorithm that generates the first `n` terms of the Fibonacci sequence must at least read the input and write the output, which takes linear time. Thus, our $O(n)$ time complexity is optimal.

```cpp
vector<int> generateFibonacciSequence(int n) {
    if (n <= 0) {
        return {};
    } else if (n == 1) {
        return {0};
    }

    vector<int> sequence = {0, 1};
    while (sequence.size() < n) {
        sequence.push_back(sequence.back() + sequence[sequence.size() - 2]);
    }

    return sequence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we iterate up to `n` times to generate the sequence.
> - **Space Complexity:** $O(n)$, since we store up to `n` terms in the sequence vector.
> - **Optimality proof:** The time complexity is optimal because we must generate each term at least once. The space complexity is also optimal because we need to store each term to calculate the next one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative approach to sequence generation, handling base cases efficiently.
- Problem-solving patterns identified: Directly applying the definition of a sequence to generate its terms.
- Optimization techniques learned: Avoiding unnecessary iterations, handling base cases efficiently.
- Similar problems to practice: Generating other sequences like the Catalan numbers or the Lucas sequence.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle base cases, incorrectly calculating the next term in the sequence.
- Edge cases to watch for: Negative input, input of 0 or 1.
- Performance pitfalls: Using recursive approaches without memoization, which can lead to exponential time complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases and larger values of `n`.