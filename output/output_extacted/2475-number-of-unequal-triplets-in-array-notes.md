## Number of Unequal Triplets in Array
**Problem Link:** https://leetcode.com/problems/number-of-unequal-triplets-in-array/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find the number of triplets that satisfy `nums[i] != nums[j]` and `nums[i] != nums[k]` and `nums[j] != nums[k]`.
- Expected output format: Return the number of unequal triplets.
- Key requirements and edge cases to consider: 
  - The array can contain duplicate elements.
  - The array can be empty or contain a single element.
  - The array can contain negative numbers and zero.
- Example test cases with explanations:
  - `nums = [4, 4, 2, 4, 3]`: There are 4 unequal triplets: `(4, 2, 3)`, `(4, 2, 4)`, `(4, 3, 4)`, `(2, 3, 4)`.
  - `nums = [1, 1, 1, 1]`: There are 0 unequal triplets.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to generate all possible triplets and check if they are unequal.
- Step-by-step breakdown of the solution:
  1. Generate all possible triplets using three nested loops.
  2. Check if the three elements of the triplet are unequal.
  3. If they are unequal, increment the count of unequal triplets.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient for large inputs.

```cpp
int countUnequalTriplets(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                if (nums[i] != nums[j] && nums[i] != nums[k] && nums[j] != nums[k]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we have three nested loops, each of which runs up to $n$ times.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count of unequal triplets.
> - **Why these complexities occur:** The time complexity is cubic because we generate all possible triplets, and the space complexity is constant because we only use a small amount of extra memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map` to count the frequency of each number in the array. Then, we can use the formula for combinations to calculate the number of unequal triplets.
- Detailed breakdown of the approach:
  1. Count the frequency of each number in the array using a `unordered_map`.
  2. Calculate the total number of triplets using the formula for combinations: $nC3 = \frac{n(n-1)(n-2)}{6}$.
  3. Calculate the number of triplets that contain at least two equal elements. This can be done by summing the number of triplets that contain two equal elements and the number of triplets that contain three equal elements.
  4. Subtract the number of triplets that contain at least two equal elements from the total number of triplets to get the number of unequal triplets.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array to count the frequency of each number, and then it uses a constant amount of time to calculate the number of unequal triplets.

```cpp
int countUnequalTriplets(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    int n = nums.size();
    int totalTriplets = n * (n - 1) * (n - 2) / 6;
    int equalTriplets = 0;
    for (auto& pair : freq) {
        int count = pair.second;
        if (count >= 2) {
            equalTriplets += count * (count - 1) * (count - 2) / 6;
        }
        if (count >= 3) {
            equalTriplets += count * (count - 1) / 2;
        }
    }
    return totalTriplets - equalTriplets;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we make a single pass through the input array to count the frequency of each number.
> - **Space Complexity:** $O(n)$, because we use a `unordered_map` to store the frequency of each number.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array, and then it uses a constant amount of time to calculate the number of unequal triplets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting the frequency of each number in an array, using the formula for combinations to calculate the number of triplets.
- Problem-solving patterns identified: Using a `unordered_map` to count the frequency of each number, calculating the number of triplets that contain at least two equal elements.
- Optimization techniques learned: Reducing the time complexity from $O(n^3)$ to $O(n)$ by using a `unordered_map` and the formula for combinations.
- Similar problems to practice: Counting the number of pairs or quadruplets that satisfy certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array or an array with a single element.
- Edge cases to watch for: An input array with duplicate elements, an input array with negative numbers or zero.
- Performance pitfalls: Using a brute force approach with a high time complexity, not using a `unordered_map` to count the frequency of each number.
- Testing considerations: Testing the function with different input arrays, including edge cases, to ensure it produces the correct output.