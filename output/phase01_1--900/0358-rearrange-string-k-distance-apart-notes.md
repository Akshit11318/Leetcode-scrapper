## Rearrange String K Distance Apart

**Problem Link:** https://leetcode.com/problems/rearrange-string-k-distance-apart/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= 25`, `s` only contains lowercase English letters.
- Expected Output: A rearranged string `s` such that the same characters are at least `k` distance apart. If it's impossible, return an empty string.
- Key Requirements:
  - Rearrange the characters in the string `s` to meet the distance requirement.
  - If it's impossible to rearrange, return an empty string.
- Edge Cases:
  - When `k` is 0 or negative.
  - When the string `s` is empty.
  - When the frequency of a character exceeds the possible rearrangement.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible rearrangements of the string `s` and checking if any of them meet the distance requirement.
- Step-by-step breakdown:
  1. Generate all permutations of the string `s`.
  2. For each permutation, check if the same characters are at least `k` distance apart.
  3. If a valid rearrangement is found, return it. If not, continue checking other permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// Function to check if a rearrangement meets the distance requirement
bool isValidRearrangement(string s, int k) {
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j < s.size(); j++) {
            if (s[i] == s[j] && j - i <= k) {
                return false;
            }
        }
    }
    return true;
}

// Brute force approach to find a valid rearrangement
string rearrangeString(string s, int k) {
    if (k == 0) return s; // No need to rearrange if k is 0
    sort(s.begin(), s.end());
    do {
        if (isValidRearrangement(s, k)) {
            return s;
        }
    } while (next_permutation(s.begin(), s.end()));
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to generating all permutations of the string `s`, where $n$ is the length of `s`.
> - **Space Complexity:** $O(n)$ for storing the string `s`.
> - **Why these complexities occur:** The brute force approach involves trying all possible permutations, which leads to an exponential time complexity. The space complexity is linear because we only need to store the string `s`.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a priority queue to store characters and their frequencies, and a queue to store the characters that are waiting to be added back to the result.
- Step-by-step breakdown:
  1. Count the frequency of each character in the string `s`.
  2. Create a priority queue to store the characters and their frequencies.
  3. Create a queue to store the characters that are waiting to be added back to the result.
  4. While the priority queue is not empty, pop the character with the highest frequency and add it to the result.
  5. Add the character to the queue to wait for `k` steps before adding it back to the result.
  6. If the queue is not empty and the character at the front of the queue has waited for `k` steps, add it back to the priority queue.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>

using namespace std;

// Optimal approach to rearrange the string
string rearrangeString(string s, int k) {
    if (k == 0) return s; // No need to rearrange if k is 0
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    priority_queue<pair<int, char>> maxHeap;
    for (auto& it : freq) {
        maxHeap.push({it.second, it.first});
    }
    queue<pair<int, char>> waitQueue;
    string result;
    while (!maxHeap.empty()) {
        auto top = maxHeap.top();
        maxHeap.pop();
        result += top.second;
        waitQueue.push({top.first - 1, top.second});
        if (waitQueue.size() > k) {
            auto front = waitQueue.front();
            waitQueue.pop();
            if (front.first > 0) {
                maxHeap.push({front.first, front.second});
            }
        }
    }
    return result.size() == s.size() ? result : "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the priority queue operations, where $n$ is the length of `s`.
> - **Space Complexity:** $O(n)$ for storing the frequency map, priority queue, and queue.
> - **Optimality proof:** The optimal approach uses a priority queue to efficiently select the character with the highest frequency, and a queue to manage the waiting characters. This approach ensures that the same characters are at least `k` distance apart, and it does so in the most efficient way possible.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: priority queue, queue, frequency counting.
- Problem-solving patterns identified: using data structures to manage complex constraints.
- Optimization techniques learned: using priority queue to efficiently select the character with the highest frequency.
- Similar problems to practice: rearranging strings with other constraints.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling the waiting queue correctly.
- Edge cases to watch for: when `k` is 0 or negative, when the string `s` is empty.
- Performance pitfalls: using a brute force approach, not using a priority queue to select the character with the highest frequency.
- Testing considerations: testing with different input strings and values of `k`.