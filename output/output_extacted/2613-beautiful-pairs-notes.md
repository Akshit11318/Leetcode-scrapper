## Beautiful Pairs
**Problem Link:** https://leetcode.com/problems/beautiful-pairs/description

**Problem Statement:**
- Given two arrays `nums` and `n`, find the number of beautiful pairs. A beautiful pair is a pair of indices `(i, j)` where `nums[i] + nums[j] == n`.
- Input format and constraints: The input arrays `nums` will have a length of at most 100, and `n` will be an integer.
- Expected output format: The number of beautiful pairs.
- Key requirements and edge cases to consider: We need to consider all pairs of indices and check if their sum equals `n`.
- Example test cases with explanations:
    - For example, if `nums = [1, 2, 3, 4, 5]` and `n = 7`, then the beautiful pairs are `(2, 4)`, `(3, 3)`, and `(4, 2)`, so the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of beautiful pairs, we can simply iterate over all pairs of indices in the `nums` array and check if the sum of the elements at those indices equals `n`.
- Step-by-step breakdown of the solution:
    1. Initialize a variable `count` to store the number of beautiful pairs.
    2. Iterate over all pairs of indices `(i, j)` in the `nums` array.
    3. For each pair, check if `nums[i] + nums[j] == n`.
    4. If the condition is true, increment the `count` variable.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible pairs, making it easy to understand and implement.

```cpp
int beautifulPair(int* nums, int numsSize, int n) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < numsSize; j++) {
            if (nums[i] + nums[j] == n) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(numsSize^2)$, where `numsSize` is the length of the `nums` array. This is because we have two nested loops that iterate over all pairs of indices.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` variable.
> - **Why these complexities occur:** The time complexity is quadratic because we check all pairs of indices, and the space complexity is constant because we only use a single variable to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all pairs of indices, we can use a hash map to store the elements of the `nums` array and their counts. Then, for each element, we can check if `n - nums[i]` is in the hash map.
- Detailed breakdown of the approach:
    1. Create a hash map `freq` to store the elements of the `nums` array and their counts.
    2. Iterate over the `nums` array and update the `freq` hash map.
    3. Initialize a variable `count` to store the number of beautiful pairs.
    4. Iterate over the `nums` array again, and for each element, check if `n - nums[i]` is in the `freq` hash map.
    5. If the condition is true, increment the `count` variable by the count of `n - nums[i]` in the `freq` hash map.
- Proof of optimality: This approach has a time complexity of $O(numsSize)$, which is optimal because we need to iterate over the `nums` array at least once to find the beautiful pairs.

```cpp
int beautifulPair(int* nums, int numsSize, int n) {
    unordered_map<int, int> freq;
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
    }
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (freq.find(n - nums[i]) != freq.end()) {
            count += freq[n - nums[i]];
            if (n - nums[i] == nums[i]) {
                count--;
            }
        }
    }
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(numsSize)$, where `numsSize` is the length of the `nums` array. This is because we iterate over the `nums` array twice: once to update the `freq` hash map and once to find the beautiful pairs.
> - **Space Complexity:** $O(numsSize)$, as we use a hash map to store the elements of the `nums` array and their counts.
> - **Optimality proof:** The time complexity is linear because we iterate over the `nums` array twice, and the space complexity is linear because we use a hash map to store the elements and their counts.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash map, frequency counting, and iteration over arrays.
- Problem-solving patterns identified: Using a hash map to store elements and their counts, and iterating over arrays to find pairs.
- Optimization techniques learned: Reducing the time complexity from quadratic to linear by using a hash map.
- Similar problems to practice: Other problems that involve finding pairs or counting frequencies, such as two-sum or anagram problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty `nums` array or a non-integer value of `n`.
- Edge cases to watch for: Handling cases where `n` is not an integer or where the `nums` array is empty.
- Performance pitfalls: Not using a hash map to store elements and their counts, which can lead to a quadratic time complexity.
- Testing considerations: Testing the function with different input cases, including edge cases, to ensure it works correctly.