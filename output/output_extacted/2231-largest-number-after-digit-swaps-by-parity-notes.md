## Largest Number After Digit Swaps by Parity
**Problem Link:** https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description

**Problem Statement:**
- Input format: A string `num` representing a non-negative integer.
- Constraints: `1 <= num.length <= 1000`.
- Expected output format: The largest number that can be obtained after swapping digits of the same parity.
- Key requirements and edge cases to consider: The input string only contains digits, and the output should be the maximum possible number after swapping digits of the same parity.
- Example test cases with explanations:
  - Input: `num = "9973"`
    - Output: `"9973"`
    - Explanation: No swaps are needed as the number is already the maximum possible.
  - Input: `num = "309"`
    - Output: `"309"`
    - Explanation: No swaps are needed as there are no digits of the same parity that can be swapped to increase the number.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all permutations of the input string and check each permutation to see if it can be obtained by swapping digits of the same parity.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input string.
  2. For each permutation, check if it can be obtained by swapping digits of the same parity.
  3. If a permutation can be obtained by swapping digits of the same parity, compare it with the current maximum number.
  4. Update the maximum number if the current permutation is larger.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible permutations of the input string.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isSameParity(char a, char b) {
    return (a - '0') % 2 == (b - '0') % 2;
}

bool canBeObtained(string num, string perm) {
    int oddCount = 0, evenCount = 0;
    for (char c : num) {
        if ((c - '0') % 2 == 0) evenCount++;
        else oddCount++;
    }

    int permOddCount = 0, permEvenCount = 0;
    for (char c : perm) {
        if ((c - '0') % 2 == 0) permEvenCount++;
        else permOddCount++;
    }

    if (oddCount != permOddCount || evenCount != permEvenCount) return false;

    int numOddIndex = -1, numEvenIndex = -1;
    for (int i = 0; i < num.length(); i++) {
        if ((num[i] - '0') % 2 == 1) {
            if (numOddIndex == -1 || num[numOddIndex] > num[i]) numOddIndex = i;
        } else {
            if (numEvenIndex == -1 || num[numEvenIndex] > num[i]) numEvenIndex = i;
        }
    }

    int permOddIndex = -1, permEvenIndex = -1;
    for (int i = 0; i < perm.length(); i++) {
        if ((perm[i] - '0') % 2 == 1) {
            if (permOddIndex == -1 || perm[permOddIndex] > perm[i]) permOddIndex = i;
        } else {
            if (permEvenIndex == -1 || perm[permEvenIndex] > perm[i]) permEvenIndex = i;
        }
    }

    if (numOddIndex != -1 && permOddIndex != -1 && num[numOddIndex] != perm[permOddIndex]) return false;
    if (numEvenIndex != -1 && permEvenIndex != -1 && num[numEvenIndex] != perm[permEvenIndex]) return false;

    return true;
}

string largestNumberAfterDigitSwapsByParityBruteForce(string num) {
    string maxNum = num;
    sort(num.begin(), num.end());

    do {
        if (canBeObtained(num, maxNum)) {
            if (num > maxNum) maxNum = num;
        }
    } while (next_permutation(num.begin(), num.end()));

    return maxNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the input string. This is because we generate all permutations of the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the current permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations of the input string, which results in a time complexity of $O(n!)$. The space complexity is $O(n)$ because we need to store the current permutation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use two priority queues to store the digits of the same parity. We iterate through the input string and push the digits into the corresponding priority queue. Then, we iterate through the input string again and pop the largest digit from the corresponding priority queue.
- Detailed breakdown of the approach:
  1. Create two priority queues to store the digits of the same parity.
  2. Iterate through the input string and push the digits into the corresponding priority queue.
  3. Iterate through the input string again and pop the largest digit from the corresponding priority queue.
- Proof of optimality: This approach is optimal because it ensures that the largest possible number is obtained after swapping digits of the same parity.

```cpp
#include <iostream>
#include <string>
#include <queue>

using namespace std;

string largestNumberAfterDigitSwapsByParityOptimal(string num) {
    priority_queue<char> oddQueue, evenQueue;

    // Push digits into the corresponding priority queue
    for (char c : num) {
        if ((c - '0') % 2 == 1) {
            oddQueue.push(c);
        } else {
            evenQueue.push(c);
        }
    }

    // Pop the largest digit from the corresponding priority queue
    for (char& c : num) {
        if ((c - '0') % 2 == 1) {
            c = oddQueue.top();
            oddQueue.pop();
        } else {
            c = evenQueue.top();
            evenQueue.pop();
        }
    }

    return num;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input string. This is because we use priority queues to store the digits.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the digits in the priority queues.
> - **Optimality proof:** This approach is optimal because it ensures that the largest possible number is obtained after swapping digits of the same parity. The time complexity is $O(n \log n)$ because we use priority queues to store the digits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, swapping digits of the same parity.
- Problem-solving patterns identified: Using priority queues to store digits of the same parity.
- Optimization techniques learned: Using priority queues to ensure the largest possible number is obtained.
- Similar problems to practice: Other problems involving swapping digits or using priority queues.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the parity of the digits before swapping.
- Edge cases to watch for: Input strings with only one digit, input strings with all digits of the same parity.
- Performance pitfalls: Using a brute force approach that generates all permutations of the input string.
- Testing considerations: Test the function with input strings of different lengths and with different parities.