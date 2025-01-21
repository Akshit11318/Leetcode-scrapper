## Construct the Lexicographically Largest Valid Sequence
**Problem Link:** https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description

**Problem Statement:**
- Input format: `n` - the number of elements in the sequence.
- Constraints: `1 <= n <= 500`.
- Expected output format: The lexicographically largest valid sequence of length `n`.
- Key requirements and edge cases to consider: A sequence is valid if it consists only of the digits `0` and `1`, and it contains at least one `0` and one `1`. The sequence must also be lexicographically largest, meaning it should be as large as possible when compared to other sequences of the same length.
- Example test cases with explanations:
  - For `n = 2`, the output should be `"10"`, as it is the lexicographically largest valid sequence of length 2.
  - For `n = 3`, the output should be `"110"`, as it is the lexicographically largest valid sequence of length 3.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible sequences of length `n` using the digits `0` and `1`, and then filter out the invalid sequences (those that do not contain at least one `0` and one `1`).
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of length `n` using the digits `0` and `1`.
  2. Filter out the invalid sequences (those that do not contain at least one `0` and one `1`).
  3. Sort the remaining sequences in lexicographically descending order.
  4. Return the first sequence in the sorted list, which is the lexicographically largest valid sequence.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible sequences and then filtering out the invalid ones.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

void generateSequences(std::vector<std::string>& sequences, std::string current, int n) {
    if (current.size() == n) {
        sequences.push_back(current);
        return;
    }
    generateSequences(sequences, current + "0", n);
    generateSequences(sequences, current + "1", n);
}

std::string constructLargestValidSequence(int n) {
    std::vector<std::string> sequences;
    generateSequences(sequences, "", n);
    std::vector<std::string> validSequences;
    for (const auto& sequence : sequences) {
        if (sequence.find('0') != std::string::npos && sequence.find('1') != std::string::npos) {
            validSequences.push_back(sequence);
        }
    }
    std::sort(validSequences.begin(), validSequences.end(), std::greater<std::string>());
    return validSequences[0];
}

int main() {
    int n;
    std::cin >> n;
    std::cout << constructLargestValidSequence(n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \log(2^n))$, as we generate all possible sequences of length `n` and then sort them.
> - **Space Complexity:** $O(2^n)$, as we store all possible sequences in memory.
> - **Why these complexities occur:** The time complexity is due to the generation of all possible sequences and the sorting operation, while the space complexity is due to the storage of all possible sequences.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since we want the lexicographically largest valid sequence, we can start by appending `1`s to the sequence until we have only one position left, which we will fill with a `0`. This approach ensures that the sequence is lexicographically largest while also being valid.
- Detailed breakdown of the approach:
  1. Initialize an empty sequence.
  2. Append `1`s to the sequence until we have only one position left.
  3. Fill the last position with a `0`.
- Proof of optimality: This approach is optimal because it ensures that the sequence is lexicographically largest while also being valid. By appending `1`s until we have only one position left, we maximize the number of `1`s in the sequence, which makes it lexicographically largest.
- Why further optimization is impossible: This approach is already optimal because it generates the lexicographically largest valid sequence in linear time.

```cpp
std::string constructLargestValidSequence(int n) {
    std::string sequence;
    for (int i = 0; i < n - 1; i++) {
        sequence += '1';
    }
    sequence += '0';
    return sequence;
}

int main() {
    int n;
    std::cin >> n;
    std::cout << constructLargestValidSequence(n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we append `1`s to the sequence until we have only one position left.
> - **Space Complexity:** $O(n)$, as we store the sequence in memory.
> - **Optimality proof:** This approach is optimal because it generates the lexicographically largest valid sequence in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Generation of all possible sequences, filtering out invalid sequences, sorting sequences in lexicographically descending order.
- Problem-solving patterns identified: Using recursion to generate all possible sequences, using sorting to find the lexicographically largest sequence.
- Optimization techniques learned: Starting with a brute force approach and then optimizing it by using a more efficient algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid sequences, not sorting the sequences in lexicographically descending order.
- Edge cases to watch for: Sequences of length 1, sequences that do not contain at least one `0` and one `1`.
- Performance pitfalls: Generating all possible sequences and then sorting them, which can be time-consuming for large sequences.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.