## Minimum Number of Frogs Croaking
**Problem Link:** https://leetcode.com/problems/minimum-number-of-frogs-croaking/description

**Problem Statement:**
- Input format: A string `croakOfFrogs` representing the sounds of frogs.
- Constraints: `1 <= croakOfFrogs.length <= 10^5`.
- Expected output format: The minimum number of frogs that can produce the sounds.
- Key requirements: Each frog can only croak once and can only produce the sounds in the order of "c-r-o-a-k".
- Example test cases:
  - Input: "croakcroak"
  - Output: 1
  - Explanation: One frog can produce the sounds.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of frogs and their sounds to find the minimum number of frogs.
- Step-by-step breakdown:
  1. Initialize a counter for the minimum number of frogs.
  2. Iterate over the string `croakOfFrogs`.
  3. For each character, try to find a frog that can produce the sound.
  4. If a frog is found, increment its sound counter.
  5. If a frog has produced all the sounds, increment the minimum number of frogs.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations.

```cpp
int minNumberOfFrogs(string croakOfFrogs) {
    int n = croakOfFrogs.length();
    int minFrogs = 0;
    int maxFrogs = 0;
    vector<int> soundCount(4, 0); // c, r, o, a
    
    for (int i = 0; i < n; i++) {
        char sound = croakOfFrogs[i];
        if (sound == 'c') {
            soundCount[0]++;
            maxFrogs = max(maxFrogs, soundCount[0]);
        } else if (sound == 'r') {
            if (soundCount[0] == 0) return -1;
            soundCount[0]--;
            soundCount[1]++;
        } else if (sound == 'o') {
            if (soundCount[1] == 0) return -1;
            soundCount[1]--;
            soundCount[2]++;
        } else if (sound == 'a') {
            if (soundCount[2] == 0) return -1;
            soundCount[2]--;
            soundCount[3]++;
        } else if (sound == 'k') {
            if (soundCount[3] == 0) return -1;
            soundCount[3]--;
        }
    }
    
    for (int i = 0; i < 4; i++) {
        if (soundCount[i] != 0) return -1;
    }
    
    return maxFrogs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `croakOfFrogs`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sound counts.
> - **Why these complexities occur:** The time complexity is linear because we iterate over the string once. The space complexity is constant because we only use a fixed amount of space to store the sound counts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a stack to keep track of the sounds produced by each frog.
- Detailed breakdown:
  1. Initialize a stack to store the sounds produced by each frog.
  2. Iterate over the string `croakOfFrogs`.
  3. For each character, check if it is a 'c' sound.
  4. If it is a 'c' sound, push it onto the stack.
  5. If it is not a 'c' sound, check if the top of the stack is the previous sound in the sequence.
  6. If it is, pop the top of the stack.
  7. If it is not, return -1 as the sequence is invalid.
- Proof of optimality: This approach is optimal because it only iterates over the string once and uses a constant amount of space.

```cpp
int minNumberOfFrogs(string croakOfFrogs) {
    int n = croakOfFrogs.length();
    int minFrogs = 0;
    int maxFrogs = 0;
    vector<int> soundCount(4, 0); // c, r, o, a
    
    for (int i = 0; i < n; i++) {
        char sound = croakOfFrogs[i];
        if (sound == 'c') {
            soundCount[0]++;
            maxFrogs = max(maxFrogs, soundCount[0]);
        } else if (sound == 'r') {
            if (soundCount[0] == 0) return -1;
            soundCount[0]--;
            soundCount[1]++;
        } else if (sound == 'o') {
            if (soundCount[1] == 0) return -1;
            soundCount[1]--;
            soundCount[2]++;
        } else if (sound == 'a') {
            if (soundCount[2] == 0) return -1;
            soundCount[2]--;
            soundCount[3]++;
        } else if (sound == 'k') {
            if (soundCount[3] == 0) return -1;
            soundCount[3]--;
        }
    }
    
    for (int i = 0; i < 4; i++) {
        if (soundCount[i] != 0) return -1;
    }
    
    return maxFrogs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `croakOfFrogs`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sound counts.
> - **Optimality proof:** This approach is optimal because it only iterates over the string once and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and constant space usage.
- Problem-solving patterns identified: Checking for valid sequences and using counters to track progress.
- Optimization techniques learned: Using constant space and iterating over the string only once.
- Similar problems to practice: Problems involving sequence validation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid sequences, not using constant space.
- Edge cases to watch for: Empty strings, strings with only one sound, strings with invalid sequences.
- Performance pitfalls: Using too much space, iterating over the string multiple times.
- Testing considerations: Test with different input sizes, test with different sound sequences.