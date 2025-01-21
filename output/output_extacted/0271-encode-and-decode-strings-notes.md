## Encode and Decode Strings
**Problem Link:** https://leetcode.com/problems/encode-and-decode-strings/description

**Problem Statement:**
- Input format: A list of strings `strs`.
- Constraints: `1 <= strs.length <= 200`, `1 <= strs[i].length <= 6`, `strs[i]` consists of lowercase letters.
- Expected output format: A string representing the encoded version of the input strings.
- Key requirements: Design an algorithm to encode and decode a list of strings to and from a single string.
- Edge cases to consider: Empty input list, strings with varying lengths, and decoding the encoded string back to the original list of strings.

**Example Test Cases:**
- Input: `["leet","code","park","san francisco"]`
- Expected Output: `["leet","code","park","san francisco"]` after decoding the encoded string.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To encode the strings, we can concatenate all the strings with a delimiter (e.g., `#`) and their lengths (e.g., `5#hello`).
- Step-by-step breakdown of the solution:
  1. Encode each string by prefixing its length and appending a delimiter.
  2. Concatenate all the encoded strings into a single string.
  3. To decode, split the encoded string by the delimiter and extract the length of each string.
  4. Use the extracted length to slice the encoded string and retrieve the original string.

```cpp
class Codec {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded_str;
        for (const auto& str : strs) {
            encoded_str += to_string(str.length()) + "#" + str;
        }
        return encoded_str;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded_strs;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') j++;
            int length = stoi(s.substr(i, j - i));
            string str = s.substr(j + 1, length);
            decoded_strs.push_back(str);
            i = j + length + 1;
        }
        return decoded_strs;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the encoded string and the decoded strings.
> - **Why these complexities occur:** The encoding and decoding processes involve iterating over each character in the input strings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The brute force approach is already optimal in terms of time and space complexity, as we must read and process each character in the input strings.
- Proof of optimality: The encoding and decoding processes require at least $O(n \cdot m)$ time and space, as we need to read and write each character in the input strings.

```cpp
class Codec {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded_str;
        for (const auto& str : strs) {
            encoded_str += to_string(str.length()) + "#" + str;
        }
        return encoded_str;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded_strs;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') j++;
            int length = stoi(s.substr(i, j - i));
            string str = s.substr(j + 1, length);
            decoded_strs.push_back(str);
            i = j + length + 1;
        }
        return decoded_strs;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the encoded string and the decoded strings.
> - **Optimality proof:** The encoding and decoding processes require at least $O(n \cdot m)$ time and space, as we need to read and write each character in the input strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, encoding, and decoding.
- Problem-solving patterns identified: Using a delimiter to separate strings and their lengths.
- Optimization techniques learned: None, as the brute force approach is already optimal.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect delimiter usage, incorrect length extraction.
- Edge cases to watch for: Empty input list, strings with varying lengths.
- Performance pitfalls: None, as the optimal approach has a linear time and space complexity.
- Testing considerations: Test with different input cases, including empty strings and strings with varying lengths.