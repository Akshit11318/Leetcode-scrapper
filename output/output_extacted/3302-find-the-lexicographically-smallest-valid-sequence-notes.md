## Find the Lexicographically Smallest Valid Sequence
**Problem Link:** https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description

**Problem Statement:**
- Input: A list of `n` integers representing the lengths of `n` sequences.
- Constraints: Each sequence is composed of unique integers from 1 to its length.
- Expected Output: The lexicographically smallest valid sequence.
- Key Requirements: The sequence must be valid, meaning it does not contain any duplicates and is composed of unique integers from 1 to its length.
- Edge Cases: The input list can be empty, or it can contain sequences of varying lengths.

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible permutations of the given lengths and then checking each permutation to see if it forms a valid sequence.
- This approach is straightforward but inefficient due to the large number of permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Function to generate all permutations of a given list of lengths
void generatePermutations(std::vector<int>& lengths, int start, int end) {
    if (start == end) {
        // Check if the current permutation forms a valid sequence
        std::vector<int> sequence;
        for (int i = 0; i < lengths.size(); i++) {
            for (int j = 1; j <= lengths[i]; j++) {
                sequence.push_back(j);
            }
        }
        // Check for duplicates and lexicographical order
        std::sort(sequence.begin(), sequence.end());
        std::vector<int>::iterator it = std::unique(sequence.begin(), sequence.end());
        if (it == sequence.end()) {
            // Print the valid sequence
            for (int i = 0; i < sequence.size(); i++) {
                std::cout << sequence[i] << " ";
            }
            std::cout << std::endl;
        }
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(lengths[start], lengths[i]);
            generatePermutations(lengths, start + 1, end);
            std::swap(lengths[start], lengths[i]); // backtrack
        }
    }
}

int main() {
    std::vector<int> lengths = {2, 1, 2};
    generatePermutations(lengths, 0, lengths.size() - 1);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot log(n))$ where $n$ is the number of sequences. The $n!$ term comes from generating all permutations, and the $n \cdot log(n)$ term comes from sorting and checking for duplicates in each permutation.
> - **Space Complexity:** $O(n)$ for storing the current permutation and the sequence.
> - **Why these complexities occur:** The brute force approach generates all permutations, which leads to an exponential time complexity. The sorting and duplicate checking operations add to the time complexity.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a backtracking approach to generate the lexicographically smallest valid sequence.
- We start with an empty sequence and try to add the smallest possible integer to the sequence at each step.
- If adding an integer would result in a duplicate, we backtrack and try the next smallest integer.

```cpp
#include <iostream>
#include <vector>

// Function to generate the lexicographically smallest valid sequence
void generateSequence(std::vector<int>& lengths, std::vector<int>& sequence) {
    if (sequence.size() == lengths.size()) {
        // Print the valid sequence
        for (int i = 0; i < sequence.size(); i++) {
            std::cout << sequence[i] << " ";
        }
        std::cout << std::endl;
        return;
    }
    for (int i = 1; i <= lengths[sequence.size()]; i++) {
        bool found = false;
        for (int j = 0; j < sequence.size(); j++) {
            if (sequence[j] == i) {
                found = true;
                break;
            }
        }
        if (!found) {
            sequence.push_back(i);
            generateSequence(lengths, sequence);
            sequence.pop_back(); // backtrack
        }
    }
}

int main() {
    std::vector<int> lengths = {2, 1, 2};
    std::vector<int> sequence;
    generateSequence(lengths, sequence);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of sequences and $m$ is the maximum length of a sequence. The time complexity comes from generating the sequence and checking for duplicates.
> - **Space Complexity:** $O(n)$ for storing the current sequence.
> - **Optimality proof:** The optimal approach generates the lexicographically smallest valid sequence by trying the smallest possible integer at each step. This ensures that the generated sequence is the smallest possible.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, duplicate checking, and lexicographical ordering.
- Problem-solving patterns identified: using backtracking to generate the lexicographically smallest valid sequence.
- Optimization techniques learned: avoiding unnecessary computations by using a backtracking approach.

**Mistakes to Avoid:**
- Common implementation errors: not checking for duplicates, not using a backtracking approach.
- Edge cases to watch for: empty input list, sequences of varying lengths.
- Performance pitfalls: using an inefficient algorithm, not optimizing the solution.
- Testing considerations: testing the solution with different input lengths and sequences.