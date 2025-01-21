## Encrypt and Decrypt Strings
**Problem Link:** https://leetcode.com/problems/encrypt-and-decrypt-strings/description

**Problem Statement:**
- Input format and constraints: The problem involves encrypting and decrypting a list of strings. Each string can be encrypted using a specific key. The goal is to design a class that supports these operations efficiently.
- Expected output format: The class should provide methods for encrypting and decrypting strings.
- Key requirements and edge cases to consider: The encryption key should be used to transform the strings into encrypted versions, and the same key should be used for decryption to retrieve the original strings.
- Example test cases with explanations: For example, if we have a string "hello" and an encryption key of 1, the encrypted string could be "ifmmp". Decrypting "ifmmp" with the same key should yield "hello".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to approach this problem is to iterate over each character in the string and apply the encryption key to it. This involves shifting the ASCII value of each character by the encryption key.
- Step-by-step breakdown of the solution:
  1. Define a method for encrypting a string by iterating over each character, applying the encryption key, and appending the encrypted character to a new string.
  2. Define a method for decrypting a string by reversing the encryption process.
- Why this approach comes to mind first: It directly implements the problem statement without considering optimizations.

```cpp
class Encrypter {
public:
    Encrypter(vector<char> keys, vector<string> values, vector<string> dictionary) {
        // Initialize encryption map
        for (int i = 0; i < keys.size(); i++) {
            encryptionMap[keys[i]] = values[i];
        }
    }
    
    string encrypt(string word1) {
        string encrypted;
        for (char c : word1) {
            if (encryptionMap.find(c) != encryptionMap.end()) {
                encrypted += encryptionMap[c];
            }
        }
        return encrypted;
    }
    
    int decrypt(string word2) {
        int count = 0;
        for (string word : dictionary) {
            string encrypted = encrypt(word);
            if (encrypted == word2) {
                count++;
            }
        }
        return count;
    }
    
private:
    unordered_map<char, string> encryptionMap;
    vector<string> dictionary;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ for encryption, where $n$ is the length of the input string and $m$ is the length of the encrypted string for each character. For decryption, it's $O(d \cdot n \cdot m)$, where $d$ is the number of words in the dictionary.
> - **Space Complexity:** $O(k)$, where $k$ is the number of unique characters in the keys.
> - **Why these complexities occur:** The encryption process involves a simple iteration over each character in the string, while the decryption process involves iterating over each word in the dictionary and encrypting it to compare with the target encrypted string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of encrypting each word in the dictionary during decryption, we can store the encrypted versions of the dictionary words upfront and use them for decryption.
- Detailed breakdown of the approach:
  1. In the constructor, encrypt each word in the dictionary and store the encrypted words in a map or a set for efficient lookup.
  2. For the `encrypt` method, apply the encryption as before.
  3. For the `decrypt` method, simply look up the encrypted word in the map or set of encrypted dictionary words to find the count of occurrences.
- Proof of optimality: This approach optimizes the decryption process by avoiding the need to encrypt each dictionary word during decryption, reducing the time complexity significantly.

```cpp
class Encrypter {
public:
    Encrypter(vector<char> keys, vector<string> values, vector<string> dictionary) {
        // Initialize encryption map
        for (int i = 0; i < keys.size(); i++) {
            encryptionMap[keys[i]] = values[i];
        }
        // Precompute encrypted dictionary
        for (string word : dictionary) {
            string encrypted = encrypt(word);
            encryptedDictionary[encrypted]++;
        }
    }
    
    string encrypt(string word1) {
        string encrypted;
        for (char c : word1) {
            if (encryptionMap.find(c) != encryptionMap.end()) {
                encrypted += encryptionMap[c];
            }
        }
        return encrypted;
    }
    
    int decrypt(string word2) {
        return encryptedDictionary[word2];
    }
    
private:
    unordered_map<char, string> encryptionMap;
    unordered_map<string, int> encryptedDictionary;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ for encryption, where $n$ is the length of the input string and $m$ is the length of the encrypted string for each character. For decryption, it's $O(1)$.
> - **Space Complexity:** $O(k + d)$, where $k$ is the number of unique characters in the keys and $d$ is the number of words in the dictionary.
> - **Optimality proof:** The precomputation of encrypted dictionary words allows for constant-time lookup during decryption, making this approach optimal in terms of time complexity for the decryption operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem showcases the importance of precomputation and caching for optimizing performance in certain scenarios.
- Problem-solving patterns identified: The approach illustrates how breaking down a problem into smaller, more manageable parts (like precomputing encrypted words) can lead to significant improvements.
- Optimization techniques learned: Precomputation and using data structures like maps or sets for efficient lookup are crucial optimization techniques.
- Similar problems to practice: Other problems that involve string manipulation, encryption, or caching for performance optimization.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as null or empty input strings, or not validating inputs.
- Edge cases to watch for: Dictionary words that are substrings of each other or words that encrypt to the same string.
- Performance pitfalls: Not optimizing the decryption process, leading to inefficient performance.
- Testing considerations: Thoroughly testing the `encrypt` and `decrypt` methods with various inputs, including edge cases, to ensure correctness and performance.