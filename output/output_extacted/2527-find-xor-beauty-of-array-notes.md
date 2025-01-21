## Find XOR Beauty of Array
**Problem Link:** https://leetcode.com/problems/find-xor-beauty-of-array/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of size `n`, find the XOR beauty of the array, which is the number of pairs `(i, j)` such that `i < j` and `nums[i] XOR nums[j]` equals `0`.
- Expected output format: The XOR beauty of the array.
- Key requirements and edge cases to consider: The array can contain duplicate elements, and the XOR operation has the property that `a XOR a = 0` and `a XOR 0 = a`.
- Example test cases with explanations: For example, given `nums = [1, 2, 3, 1]`, the XOR beauty of the array is `1`, because there is only one pair `(i, j)` such that `i < j` and `nums[i] XOR nums[j]` equals `0`, which is `(0, 3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the XOR beauty of the array, we can iterate over all pairs of elements in the array and check if their XOR is equal to `0`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `beauty` to `0`.
  2. Iterate over all pairs of elements in the array using two nested loops.
  3. For each pair, calculate the XOR of the two elements.
  4. If the XOR is equal to `0`, increment the `beauty` variable.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the nested loops.

```cpp
int findXorBeauty(vector<int>& nums) {
    int beauty = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if ((nums[i] ^ nums[j]) == 0) {
                beauty++;
            }
        }
    }
    return beauty;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array, because we are using two nested loops to iterate over all pairs of elements.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the `beauty` variable.
> - **Why these complexities occur:** The time complexity is high because we are iterating over all pairs of elements, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over all pairs of elements, we can use a `unordered_map` to store the frequency of each element in the array. Then, we can calculate the XOR beauty by iterating over the `unordered_map` and summing up the number of pairs that have an XOR of `0`.
- Detailed breakdown of the approach:
  1. Initialize an `unordered_map` to store the frequency of each element in the array.
  2. Iterate over the array and update the frequency of each element in the `unordered_map`.
  3. Initialize a variable `beauty` to `0`.
  4. Iterate over the `unordered_map` and for each element, calculate the number of pairs that have an XOR of `0` by using the formula `freq * (freq - 1) / 2`.
  5. Sum up the number of pairs for each element to get the total XOR beauty.
- Proof of optimality: This approach is optimal because we are only iterating over the array once to update the frequency of each element, and then iterating over the `unordered_map` to calculate the XOR beauty. This reduces the time complexity from $O(n^2)$ to $O(n)$.

```cpp
int findXorBeauty(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    int beauty = 0;
    for (auto& pair : freq) {
        int freqVal = pair.second;
        beauty += freqVal * (freqVal - 1) / 2;
    }
    return beauty;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we are only iterating over the array once to update the frequency of each element, and then iterating over the `unordered_map` to calculate the XOR beauty.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store the frequency of each element in the `unordered_map`.
> - **Optimality proof:** This approach is optimal because we are only iterating over the array once to update the frequency of each element, and then iterating over the `unordered_map` to calculate the XOR beauty, which reduces the time complexity from $O(n^2)$ to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `unordered_map` to store the frequency of each element, and then calculating the XOR beauty by iterating over the `unordered_map`.
- Problem-solving patterns identified: Reducing the time complexity by using a `unordered_map` to store the frequency of each element, and then iterating over the `unordered_map` to calculate the XOR beauty.
- Optimization techniques learned: Using a `unordered_map` to reduce the time complexity from $O(n^2)$ to $O(n)$.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `unordered_map` correctly, or not updating the frequency of each element correctly.
- Edge cases to watch for: When the input array is empty, or when the input array contains duplicate elements.
- Performance pitfalls: Using a nested loop to iterate over all pairs of elements, which can lead to a high time complexity.
- Testing considerations: Testing the function with different input arrays, including empty arrays and arrays with duplicate elements.