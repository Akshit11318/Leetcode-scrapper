## Number of Divisible Triplet Sums

**Problem Link:** https://leetcode.com/problems/number-of-divisible-triplet-sums/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Output: The number of triplets `(i, j, l)` such that `i < j < l` and the sum of the elements at these indices is divisible by `k`.
- Key requirements and edge cases:
  - The array can be empty or contain a single element, in which case the number of triplets is 0.
  - The array can contain duplicate elements.
  - The divisor `k` can be any positive integer.
- Example test cases:
  - `nums = [2, 7, 9], k = 5` should return 1 because the triplet `(0, 1, 2)` has a sum of 18, which is divisible by 5.
  - `nums = [2, 7, 6, 1, 4], k = 3` should return 4 because the triplets `(0, 1, 3)`, `(0, 1, 4)`, `(0, 2, 4)`, and `(1, 2, 4)` have sums divisible by 3.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible triplet in the array.
- Step-by-step breakdown:
  1. Iterate over the array to consider each element as the first element of the triplet.
  2. For each first element, iterate over the remaining elements to consider each as the second element.
  3. For each pair of first and second elements, iterate over the remaining elements to consider each as the third element.
  4. For each triplet, calculate the sum and check if it is divisible by `k`.
- Why this approach comes to mind first: It is the most straightforward way to ensure all triplets are considered.

```cpp
int countTriplets(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int l = j + 1; l < nums.size(); l++) {
                if ((nums[i] + nums[j] + nums[l]) % k == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`. This is because we have three nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, excluding the input array, because we only use a constant amount of space to store the count and loop indices.
> - **Why these complexities occur:** The brute force approach requires checking every possible triplet, leading to cubic time complexity. The space complexity is constant because we do not use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every triplet, we can use a hashmap to store the cumulative sum modulo `k` and its frequency.
- Detailed breakdown:
  1. Initialize a hashmap with a cumulative sum of 0 and a frequency of 1 (to handle the case where the sum of the first two elements is divisible by `k`).
  2. Iterate over the array, maintaining a cumulative sum and its modulo `k`.
  3. For each element, calculate the new cumulative sum and its modulo `k`.
  4. Check if the hashmap contains a cumulative sum such that the difference between the current cumulative sum and the stored sum is divisible by `k`. If so, increment the count by the frequency of the stored sum.
  5. Update the frequency of the current cumulative sum in the hashmap.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal for this problem because we must consider at least two elements to form a triplet.

```cpp
int countTriplets(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> sumFreq;
    sumFreq[0] = 1; // Handle the case where the sum of the first two elements is divisible by k
    int cumSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        cumSum += nums[i];
        for (int j = i + 1; j < nums.size(); j++) {
            int sumIJ = cumSum - (i > 0 ? cumSum - nums[i - 1] : 0) + nums[j];
            if (sumIJ % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```
However, this solution does not utilize a hashmap effectively and still has a time complexity of $O(n^2)$. 

Let's use a prefix sum array and a hashmap to achieve $O(n^2)$ time complexity.

```cpp
int countTriplets(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> sumFreq;
    vector<int> prefixSum(nums.size() + 1, 0);
    for (int i = 0; i < nums.size(); i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int sumIJ = prefixSum[j + 1] - prefixSum[i];
            if (sumIJ % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```
However, the above solution still doesn't utilize a hashmap effectively.

Here is the correct solution that utilizes a hashmap:

```cpp
int countTriplets(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> sumFreq;
    vector<int> prefixSum(nums.size() + 1, 0);
    for (int i = 0; i <= nums.size(); i++) {
        if (i > 0) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
        }
        for (int j = i + 1; j <= nums.size(); j++) {
            int sumIJ = prefixSum[j] - prefixSum[i];
            if (sumIJ % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```
But, the solution above still doesn't utilize a hashmap.

```cpp
int countTriplets(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> sumFreq;
    vector<int> prefixSum(nums.size() + 1, 0);
    for (int i = 0; i <= nums.size(); i++) {
        if (i > 0) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
        }
        sumFreq[prefixSum[i] % k]++;
    }
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int sumIJ = prefixSum[j + 1] - prefixSum[i];
            if (sumIJ % k == 0) {
                count += sumFreq[0];
            } else {
                count += sumFreq[k - (sumIJ % k)];
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because we have two nested loops, each iterating over the array.
> - **Space Complexity:** $O(n)$, excluding the input array, because we use a hashmap to store the cumulative sum modulo `k` and its frequency.
> - **Optimality proof:** This approach is optimal because we must consider at least two elements to form a triplet, and we use a hashmap to efficiently count the frequency of each cumulative sum modulo `k`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Cumulative sum, hashmap, and modulo operation.
- Problem-solving patterns identified: Using a hashmap to efficiently count the frequency of each cumulative sum modulo `k`.
- Optimization techniques learned: Utilizing a hashmap to reduce the time complexity from $O(n^3)$ to $O(n^2)$.
- Similar problems to practice: Other problems involving cumulative sum, hashmap, and modulo operation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: Empty input array, single-element input array, and duplicate elements.
- Performance pitfalls: Using a brute force approach with a time complexity of $O(n^3)$.
- Testing considerations: Test the solution with different input sizes, including edge cases.