## Frequency Tracker
**Problem Link:** https://leetcode.com/problems/frequency-tracker/description

**Problem Statement:**
- Input format and constraints: The problem requires implementing a `FrequencyTracker` class with methods to add and delete frequencies of numbers.
- Expected output format: The `hasFrequency` method should return whether a specific frequency exists.
- Key requirements and edge cases to consider: Handling cases where numbers are added or deleted when they don't exist, and checking for frequencies that don't exist.
- Example test cases with explanations:
  - Adding a number increases its frequency by 1.
  - Deleting a number decreases its frequency by 1.
  - Checking if a frequency exists after adding or deleting numbers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a data structure to store the frequency of each number and another to store the frequency of frequencies.
- Step-by-step breakdown of the solution:
  1. Create a map to store the frequency of each number.
  2. Create another map to store the frequency of frequencies.
  3. When adding a number, increment its frequency in the first map and update the frequency of frequencies in the second map.
  4. When deleting a number, decrement its frequency in the first map and update the frequency of frequencies in the second map.
- Why this approach comes to mind first: It directly addresses the problem statement by tracking frequencies and frequency of frequencies.

```cpp
class FrequencyTracker {
public:
    void add(int number) {
        if (freq.count(number)) {
            freqOfFreq[freq[number]]--;
            if (freqOfFreq[freq[number]] == 0) {
                freqOfFreq.erase(freq[number]);
            }
            freq[number]++;
            freqOfFreq[freq[number]]++;
        } else {
            freq[number] = 1;
            freqOfFreq[1]++;
        }
    }

    void deleteOne(int number) {
        if (freq.count(number)) {
            freqOfFreq[freq[number]]--;
            if (freqOfFreq[freq[number]] == 0) {
                freqOfFreq.erase(freq[number]);
            }
            freq[number]--;
            if (freq[number] > 0) {
                freqOfFreq[freq[number]]++;
            } else {
                freq.erase(number);
            }
        }
    }

    bool hasFrequency(int frequency) {
        return freqOfFreq.count(frequency);
    }
private:
    unordered_map<int, int> freq; // Number to frequency
    unordered_map<int, int> freqOfFreq; // Frequency to frequency of frequency
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations because we use hash maps for constant time lookups and updates.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique numbers added, because in the worst case, every number has a unique frequency.
> - **Why these complexities occur:** The use of hash maps allows for constant time operations, but the space required grows linearly with the number of unique elements.

---

### Optimal Approach (Required)

The provided brute force approach is already optimal in terms of time complexity for this problem. It achieves $O(1)$ time complexity for all operations using hash maps, which is the best we can do given the need to track and update frequencies dynamically.

However, for clarity and completeness, let's reiterate the optimal approach with a focus on why it's optimal:

**Explanation:**
- Key insight that leads to optimal solution: Using two hash maps to track the frequency of numbers and the frequency of frequencies allows for constant time updates and lookups.
- Detailed breakdown of the approach: The same as the brute force approach because it's already optimal.
- Proof of optimality: Any solution must at least read the input and write the output, which takes linear time. However, for the operations specified (add, delete, hasFrequency), $O(1)$ is optimal because we cannot do better than constant time for each operation given the need to dynamically update and query frequencies.

The code remains the same as in the brute force approach because it's already optimal.

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique numbers added.
> - **Optimality proof:** The use of hash maps for constant time lookups and updates, combined with the necessity of storing each unique number's frequency, makes this approach optimal for the given operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps for constant time operations, and the importance of choosing the right data structure for the problem.
- Problem-solving patterns identified: Breaking down the problem into smaller parts (tracking number frequencies and frequency of frequencies) and solving each part efficiently.
- Optimization techniques learned: Using the right data structure (hash maps) for constant time operations.
- Similar problems to practice: Other problems involving dynamic tracking and querying of data, such as LRU cache or similar frequency tracking problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., adding/deleting a number that doesn't exist), or not updating frequencies correctly.
- Edge cases to watch for: Adding or deleting numbers when they don't exist, and checking for frequencies that don't exist.
- Performance pitfalls: Using data structures that do not support constant time operations for lookups and updates.
- Testing considerations: Thoroughly testing with various sequences of add, delete, and hasFrequency operations to ensure correctness.