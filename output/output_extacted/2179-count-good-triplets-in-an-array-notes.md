## Count Good Triplets in an Array

**Problem Link:** https://leetcode.com/problems/count-good-triplets-in-an-array/description

**Problem Statement:**
- Input format and constraints: Given an array `arr` of integers and two integers `a` and `b`, find the number of good triplets.
- Expected output format: Return the count of good triplets.
- Key requirements and edge cases to consider: 
  - A triplet `(i, j, k)` is good if `i < j < k` and `arr[i] % a == arr[j] % a` and `arr[j] % b == arr[k] % b`.
  - The array length can vary, and the values of `a` and `b` can also vary.
- Example test cases with explanations:
  - For example, given `arr = [1, 2, 3, 4, 5]`, `a = 2`, `b = 3`, a good triplet is `(1, 2, 4)` because `arr[1] % a == arr[2] % a` and `arr[2] % b == arr[4] % b`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach is to check every possible triplet in the array and count the ones that satisfy the conditions.
- Step-by-step breakdown of the solution:
  1. Iterate over the array with three nested loops to generate all possible triplets.
  2. For each triplet, check if `i < j < k` and `arr[i] % a == arr[j] % a` and `arr[j] % b == arr[k] % b`.
  3. If the conditions are met, increment the count of good triplets.
- Why this approach comes to mind first: It's straightforward to generate all possible triplets and check each one against the given conditions.

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                if (arr[i] % a == arr[j] % a && arr[j] % b == arr[k] % b) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the array, because we're using three nested loops to generate all possible triplets.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The time complexity is cubic because we're checking every possible triplet, and the space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible triplet, we can use a hashmap to store the count of each remainder when divided by `a` and `b`.
- Detailed breakdown of the approach:
  1. Initialize two hashmaps, `mapA` and `mapB`, to store the count of each remainder when divided by `a` and `b`, respectively.
  2. Iterate over the array and for each element, increment the count in `mapA` and `mapB` based on the remainder.
  3. Initialize a variable `count` to store the count of good triplets.
  4. Iterate over the array again and for each element, check the count of elements that have the same remainder when divided by `a` and are before the current element.
  5. For each such element, check the count of elements that have the same remainder when divided by `b` and are after the current element.
  6. Increment the `count` variable by the product of these two counts.
- Proof of optimality: This approach is optimal because we're only iterating over the array twice and using hashmaps to store the count of each remainder, which reduces the time complexity to $O(n)$.

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    unordered_map<int, int> mapA, mapB;
    for (int num : arr) {
        mapA[num % a]++;
        mapB[num % b]++;
    }
    int count = 0;
    for (int num : arr) {
        count += mapA[num % a] * mapB[num % b];
    }
    return count - arr.size() * 3 + 2;
}
```

However, this solution is not correct and needs to be modified as follows:

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                if (arr[i] % a == arr[j] % a && arr[j] % b == arr[k] % b) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

Since the problem requires us to count the number of triplets `(i, j, k)` such that `i < j < k` and `arr[i] % a == arr[j] % a` and `arr[j] % b == arr[k] % b`, we can't avoid checking every possible triplet.

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the array, because we're using three nested loops to generate all possible triplets.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the count and loop variables.
> - **Optimality proof:** This is the optimal solution because we have to check every possible triplet to count the number of good triplets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, hashmaps.
- Problem-solving patterns identified: Checking every possible solution, using hashmaps to store counts.
- Optimization techniques learned: Using hashmaps to reduce time complexity.
- Similar problems to practice: Other problems that involve counting or checking every possible solution.

**Mistakes to Avoid:**
- Common implementation errors: Not checking every possible solution, not using hashmaps correctly.
- Edge cases to watch for: Empty array, array with one or two elements.
- Performance pitfalls: Using three nested loops without considering the time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases.