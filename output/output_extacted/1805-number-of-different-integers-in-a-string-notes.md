## Number of Different Integers in a String
**Problem Link:** https://leetcode.com/problems/number-of-different-integers-in-a-string/description

**Problem Statement:**
- Input: A string `word` containing only digits and lowercase English letters.
- Constraints: $1 \leq \text{length of } word \leq 2 \times 10^5$
- Expected Output: The number of different integers that can be extracted from `word`.
- Key requirements and edge cases:
  - Non-numeric characters separate integers.
  - Leading zeros are ignored, e.g., "001" is considered as "1".
- Example test cases:
  - Input: "a123b456"
    - Expected Output: 2
  - Input: "000000001"
    - Expected Output: 1

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Extract all substrings that contain digits and consider them as integers.
- Step-by-step breakdown:
  1. Iterate over the string to find substrings containing digits.
  2. For each digit-containing substring, remove leading zeros and consider it as an integer.
  3. Store these integers in a set to eliminate duplicates.
  4. Return the size of the set as the number of different integers.
- Why this approach comes to mind first: It directly addresses the problem statement by extracting integers and counting unique ones.

```cpp
#include <iostream>
#include <string>
#include <set>

int numDifferentIntegers(string word) {
    set<int> uniqueIntegers;
    string currentInteger = "";
    
    for (char c : word) {
        if (isdigit(c)) {
            currentInteger += c;
        } else if (!currentInteger.empty()) {
            // Remove leading zeros
            while (currentInteger.size() > 1 && currentInteger[0] == '0') {
                currentInteger.erase(0, 1);
            }
            uniqueIntegers.insert(stoi(currentInteger));
            currentInteger.clear();
        }
    }
    
    // Handle the last integer in the string
    if (!currentInteger.empty()) {
        while (currentInteger.size() > 1 && currentInteger[0] == '0') {
            currentInteger.erase(0, 1);
        }
        uniqueIntegers.insert(stoi(currentInteger));
    }
    
    return uniqueIntegers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the maximum length of a digit substring, because we iterate over the string and for each integer found, we potentially remove leading zeros.
> - **Space Complexity:** $O(n)$, as in the worst case, every character could be a separate integer, and we store them in a set.
> - **Why these complexities occur:** The time complexity is due to the iteration and potential string manipulation (removing leading zeros), while the space complexity is due to storing unique integers in a set.

---

### Optimal Approach

**Explanation:**
- Key insight: Utilize a more efficient method to handle leading zeros and integer extraction.
- Detailed breakdown:
  1. Iterate over the string, identifying substrings that are digits.
  2. For each digit substring, find the first non-zero digit (if any) to handle leading zeros efficiently.
  3. Extract the integer by parsing the substring starting from the first non-zero digit (or '0' if all digits are zero).
  4. Use a set to store unique integers.
- Proof of optimality: This approach optimizes the handling of leading zeros and integer extraction without unnecessary string manipulations, making it more efficient than the brute force approach.

```cpp
#include <iostream>
#include <string>
#include <set>

int numDifferentIntegers(string word) {
    set<int> uniqueIntegers;
    int start = 0;
    
    for (int i = 0; i < word.size(); ++i) {
        if (isdigit(word[i])) {
            if (start == 0 || !isdigit(word[start])) {
                start = i;
            }
        } else {
            if (start != 0) {
                int end = i;
                // Find the first non-zero digit
                int nonZeroStart = start;
                while (nonZeroStart < end && word[nonZeroStart] == '0') {
                    nonZeroStart++;
                }
                // If all digits are zero, consider it as "0"
                if (nonZeroStart == end) {
                    nonZeroStart = start;
                }
                uniqueIntegers.insert(stoi(word.substr(nonZeroStart, end - nonZeroStart)));
                start = 0;
            }
        }
    }
    
    // Handle the last integer in the string
    if (start != 0) {
        int end = word.size();
        int nonZeroStart = start;
        while (nonZeroStart < end && word[nonZeroStart] == '0') {
            nonZeroStart++;
        }
        if (nonZeroStart == end) {
            nonZeroStart = start;
        }
        uniqueIntegers.insert(stoi(word.substr(nonZeroStart, end - nonZeroStart)));
    }
    
    return uniqueIntegers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as in the worst case, every character could contribute to a unique integer stored in the set.
> - **Optimality proof:** This approach is optimal because it makes a single pass through the input string and uses a set for efficient storage and lookup of unique integers, minimizing both time and space complexities.

---

### Final Notes

**Learning Points:**
- Efficient handling of strings and integers.
- Use of sets for storing unique elements.
- Optimization techniques for reducing unnecessary string manipulations.

**Mistakes to Avoid:**
- Inefficient handling of leading zeros.
- Unnecessary string manipulations.
- Not considering edge cases, such as all zeros or non-digit characters separating integers.
- Inadequate testing for various input scenarios.