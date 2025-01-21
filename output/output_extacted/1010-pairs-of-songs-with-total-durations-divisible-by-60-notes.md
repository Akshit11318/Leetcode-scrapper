## Pairs of Songs With Total Durations Divisible by 60

**Problem Link:** https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `time` representing the duration of songs in seconds. The constraint is that the array length is between 1 and 10000, and each song duration is between 1 and 50000.
- Expected output format: The output should be the number of pairs of songs whose total duration is divisible by 60.
- Key requirements and edge cases to consider: The key requirement is to find all possible pairs of songs and check if their total duration is divisible by 60. An edge case could be when there are no pairs or when the total duration of all songs is less than 60.
- Example test cases with explanations: For example, given the input `[30,20,150,100,40]`, the output should be `3` because there are three pairs of songs whose total duration is divisible by 60: `(20, 40)`, `(30, 30)`, and `(150, 10)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use two nested loops to generate all possible pairs of songs and check if their total duration is divisible by 60.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to store the number of pairs.
  2. Use two nested loops to generate all possible pairs of songs.
  3. For each pair, calculate the total duration and check if it is divisible by 60.
  4. If it is, increment the `count`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large inputs.

```cpp
int numPairsDivisibleBy60(vector<int>& time) {
    int count = 0;
    int n = time.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((time[i] + time[j]) % 60 == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of songs. This is because we use two nested loops to generate all possible pairs of songs.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, so it's constant.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are generating all possible pairs of songs, and there are $n(n-1)/2$ pairs. The space complexity is $O(1)$ because we only use a constant amount of space to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the frequency of each remainder when divided by 60. Then, for each song, we can find its complement (60 - remainder) in the hashmap and add the frequency to the count.
- Detailed breakdown of the approach:
  1. Initialize a hashmap `freq` to store the frequency of each remainder.
  2. Initialize a variable `count` to store the number of pairs.
  3. Iterate over each song in the input array.
  4. For each song, calculate its remainder when divided by 60.
  5. Check if the complement (60 - remainder) is in the hashmap. If it is, add the frequency to the count.
  6. Increment the frequency of the remainder in the hashmap.
- Proof of optimality: This approach is optimal because we only need to iterate over the input array once, and we use a hashmap to store the frequency of each remainder, which allows us to find the complement in constant time.

```cpp
int numPairsDivisibleBy60(vector<int>& time) {
    int count = 0;
    unordered_map<int, int> freq;
    for (int t : time) {
        int remainder = t % 60;
        if (freq.find((60 - remainder) % 60) != freq.end()) {
            count += freq[(60 - remainder) % 60];
        }
        freq[remainder]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of songs. This is because we only need to iterate over the input array once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, so it's constant.
> - **Optimality proof:** The time complexity is $O(n)$ because we only need to iterate over the input array once. The space complexity is $O(1)$ because we only use a constant amount of space to store the hashmap and the count.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap, frequency counting, and complement finding.
- Problem-solving patterns identified: Using a hashmap to store frequency and finding complements to solve problems involving pairs.
- Optimization techniques learned: Using a hashmap to reduce time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Other problems involving pairs and frequency counting, such as finding pairs of numbers that sum to a target.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the hashmap or count variable, not checking for the complement in the hashmap, and not incrementing the frequency correctly.
- Edge cases to watch for: Handling empty input arrays, arrays with a single element, and arrays with all elements having the same remainder when divided by 60.
- Performance pitfalls: Using a brute force approach with two nested loops, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different input arrays, including edge cases, to ensure it returns the correct count of pairs.