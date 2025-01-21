## Determine if String Halves Are Alike
**Problem Link:** https://leetcode.com/problems/determine-if-string-halves-are-alike/description

**Problem Statement:**
- Input format: A string `s` consisting of lowercase letters.
- Constraints: The length of `s` is an even number.
- Expected output format: A boolean indicating whether the two halves of `s` have the same number of vowels.
- Key requirements and edge cases to consider: Handling strings of varying lengths, ensuring accurate vowel counting, and correctly splitting the string into halves.
- Example test cases with explanations:
  - For the input `"AbCdEfGh"`, the halves `"AbCdEf"` and `"Gh"` have the same number of vowels (`1` in each), so the output should be `true`.
  - For the input `"MerryChristmas"`, the halves `"Merry"` and `"Christmas"` have different numbers of vowels, so the output should be `false`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Split the string into two halves and count the vowels in each half.
- Step-by-step breakdown of the solution:
  1. Find the middle index of the string.
  2. Split the string into two halves using the middle index.
  3. Initialize counters for vowels in each half.
  4. Iterate through each character in both halves, incrementing the vowel counter when a vowel is encountered.
  5. Compare the vowel counts for both halves and return `true` if they are equal, `false` otherwise.
- Why this approach comes to mind first: It directly addresses the problem statement by splitting the string and comparing vowel counts.

```cpp
#include <string>
using namespace std;

bool halvesAreAlike(string s) {
    int n = s.length();
    int mid = n / 2;
    int vowels1 = 0, vowels2 = 0;
    
    // Count vowels in the first half
    for (int i = 0; i < mid; i++) {
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels1++;
        }
    }
    
    // Count vowels in the second half
    for (int i = mid; i < n; i++) {
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels2++;
        }
    }
    
    return vowels1 == vowels2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are potentially scanning through the entire string once to count the vowels.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the vowel counts and indices.
> - **Why these complexities occur:** The time complexity is linear due to the iteration over the string, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over both halves separately, we can iterate over the string once and use a single loop to count the vowels in both halves.
- Detailed breakdown of the approach:
  1. Find the middle index of the string.
  2. Initialize counters for vowels in the first and second halves.
  3. Iterate through the string, incrementing the appropriate vowel counter based on whether the index is before or after the middle.
  4. Return `true` if the vowel counts are equal, `false` otherwise.
- Proof of optimality: This approach still has a linear time complexity but reduces the number of iterations and comparisons needed, making it slightly more efficient than the brute force approach.

```cpp
#include <string>
using namespace std;

bool halvesAreAlike(string s) {
    int n = s.length();
    int mid = n / 2;
    int vowels1 = 0, vowels2 = 0;
    
    for (int i = 0; i < n; i++) {
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            if (i < mid) {
                vowels1++;
            } else {
                vowels2++;
            }
        }
    }
    
    return vowels1 == vowels2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This remains linear because we still iterate over the entire string.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space for the vowel counts and indices.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations (comparisons and increments) needed to solve the problem, all while maintaining a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and basic string manipulation.
- Problem-solving patterns identified: Splitting a problem into smaller parts (halves of the string) and comparing results.
- Optimization techniques learned: Reducing the number of iterations and comparisons.
- Similar problems to practice: Other string manipulation and comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to convert characters to lowercase for vowel comparison.
- Edge cases to watch for: Empty strings, strings with an odd length (though the problem statement specifies even lengths).
- Performance pitfalls: Using inefficient string manipulation methods or unnecessary iterations.
- Testing considerations: Ensuring the function works correctly for strings of varying lengths and vowel distributions.