## Decode Xored Array
**Problem Link:** https://leetcode.com/problems/decode-xored-array/description

**Problem Statement:**
- Input: An array of integers `encoded` where `encoded[i] = original[i] XOR original[i + 1]`, and an integer `first`, which is the first element of the original array.
- Constraints: `2 <= encoded.length <= 10^5`, `encoded[i] >= 0`, `0 <= first <= 10^5`.
- Expected Output: The decoded original array.
- Key Requirements: The original array must be decoded using the XOR operation and the given `first` element.
- Example Test Cases:
  - Input: `encoded = [1,2,3], first = 1`
    Output: `[1,0,2,1]`
  - Input: `encoded = [6,2,7,3], first = 4`
    Output: `[4,2,0,7,4]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over the `encoded` array and use the XOR operation to find each element of the original array.
- Start with the `first` element as the initial value.
- For each `encoded[i]`, calculate `original[i + 1]` by performing `encoded[i] XOR original[i]`.
- This approach seems straightforward but let's analyze its complexity.

```cpp
vector<int> decode(vector<int>& encoded, int first) {
    vector<int> original;
    original.push_back(first);
    for (int i = 0; i < encoded.size(); i++) {
        int next = encoded[i] ^ original.back();
        original.push_back(next);
    }
    return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the `encoded` array. This is because we iterate over the array once.
> - **Space Complexity:** $O(n)$, as we store the decoded array of the same size as the input array plus one for the `first` element.
> - **Why these complexities occur:** The iteration over the `encoded` array and the storage of the `original` array cause these linear complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the XOR operation is its own inverse, meaning `a XOR b XOR b = a`. This property allows us to directly calculate each element of the original array without needing to store the entire array as we go, but since we need to return the entire array, we have to store it anyway.
- The approach remains similar to the brute force, as it's already quite efficient given the need to examine each element of the `encoded` array and the requirement to return the entire decoded array.
- Proof of optimality: Since we must examine each element of the `encoded` array at least once to decode it and we must store the decoded array, the time and space complexities of $O(n)$ are optimal.

```cpp
vector<int> decode(vector<int>& encoded, int first) {
    vector<int> original = {first};
    for (int encoded_val : encoded) {
        original.push_back(encoded_val ^ original.back());
    }
    return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the `encoded` array.
> - **Space Complexity:** $O(n)$, for storing the decoded array.
> - **Optimality proof:** Given the necessity of examining each `encoded` value and storing the result, these complexities are the best achievable.

---

### Final Notes

**Learning Points:**
- The XOR operation's properties, especially being its own inverse, are crucial in solving this problem efficiently.
- Understanding the requirements of the problem, such as needing to return the entire decoded array, helps in determining the optimal approach.
- The problem demonstrates a scenario where a brute force approach is already quite efficient due to the nature of the problem.

**Mistakes to Avoid:**
- Not considering the properties of the XOR operation, which could lead to overcomplicating the solution.
- Failing to recognize the need to store the entire decoded array, which affects space complexity.
- Overlooking the simplicity of the problem and attempting overly complex solutions.