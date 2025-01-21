## String Compression
**Problem Link:** https://leetcode.com/problems/string-compression/description

**Problem Statement:**
- Input format: A character array `chars`.
- Constraints: The input array will be modified in-place.
- Expected output format: The length of the modified array after compression.
- Key requirements and edge cases to consider: 
    - The input array should be compressed in-place.
    - The compressed array should be in the format of consecutive repeated characters followed by the count of repetition.
    - If the length of the compressed array is greater than or equal to the original length, return the original length.
- Example test cases with explanations:
    - `chars = ["a","a","b","b","c","c","c"]`, the compressed array will be `["a","2","b","2","c","3"]`.
    - `chars = ["a"]`, the compressed array will be `["a"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new array to store the compressed result and then replace the original array with the compressed one.
- Step-by-step breakdown of the solution:
    1. Initialize an empty array `compressed` to store the compressed result.
    2. Initialize variables `count` and `currentChar` to keep track of the current character and its count.
    3. Iterate through the input array `chars`. For each character, if it is the same as `currentChar`, increment `count`. Otherwise, append `currentChar` and `count` to `compressed`, and update `currentChar` and `count`.
    4. Append the last character and its count to `compressed`.
    5. Replace the original array `chars` with the compressed array `compressed`.
- Why this approach comes to mind first: It is straightforward to think of creating a new array to store the compressed result and then replacing the original array.

```cpp
void compress(vector<char>& chars) {
    vector<char> compressed;
    int count = 1;
    char currentChar = chars[0];
    
    for (int i = 1; i < chars.size(); i++) {
        if (chars[i] == currentChar) {
            count++;
        } else {
            compressed.push_back(currentChar);
            if (count > 1) {
                string countStr = to_string(count);
                for (char c : countStr) {
                    compressed.push_back(c);
                }
            }
            currentChar = chars[i];
            count = 1;
        }
    }
    
    compressed.push_back(currentChar);
    if (count > 1) {
        string countStr = to_string(count);
        for (char c : countStr) {
            compressed.push_back(c);
        }
    }
    
    if (compressed.size() >= chars.size()) {
        return;
    }
    
    chars.clear();
    for (char c : compressed) {
        chars.push_back(c);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate through the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we create a new array to store the compressed result.
> - **Why these complexities occur:** These complexities occur because we need to iterate through the input array to compress it, and we need to store the compressed result in a new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new array to store the compressed result, we can modify the original array in-place.
- Detailed breakdown of the approach:
    1. Initialize variables `count` and `currentChar` to keep track of the current character and its count.
    2. Initialize a variable `writeIndex` to keep track of the position where we should write the compressed result in the original array.
    3. Iterate through the input array `chars`. For each character, if it is the same as `currentChar`, increment `count`. Otherwise, write `currentChar` and `count` to the original array at the position `writeIndex`, and update `currentChar`, `count`, and `writeIndex`.
    4. Write the last character and its count to the original array at the position `writeIndex`.
- Proof of optimality: This solution is optimal because it only requires a single pass through the input array, and it modifies the original array in-place.

```cpp
int compress(vector<char>& chars) {
    int count = 1;
    char currentChar = chars[0];
    int writeIndex = 0;
    
    for (int i = 1; i < chars.size(); i++) {
        if (chars[i] == currentChar) {
            count++;
        } else {
            chars[writeIndex++] = currentChar;
            if (count > 1) {
                string countStr = to_string(count);
                for (char c : countStr) {
                    chars[writeIndex++] = c;
                }
            }
            currentChar = chars[i];
            count = 1;
        }
    }
    
    chars[writeIndex++] = currentChar;
    if (count > 1) {
        string countStr = to_string(count);
        for (char c : countStr) {
            chars[writeIndex++] = c;
        }
    }
    
    return writeIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate through the input array once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the input array, and it modifies the original array in-place.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, single pass through the input array.
- Problem-solving patterns identified: Using variables to keep track of the current character and its count, using a write index to keep track of the position where we should write the compressed result.
- Optimization techniques learned: Modifying the original array in-place instead of creating a new array.
- Similar problems to practice: Other string compression problems, such as Run-Length Encoding (RLE).

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the input array is empty, not handling the case where the compressed array is larger than the original array.
- Edge cases to watch for: The input array is empty, the compressed array is larger than the original array.
- Performance pitfalls: Creating a new array to store the compressed result instead of modifying the original array in-place.
- Testing considerations: Test the function with different input arrays, including empty arrays and arrays with repeated characters.