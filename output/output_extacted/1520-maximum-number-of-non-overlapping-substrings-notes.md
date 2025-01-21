## Maximum Number of Non-Overlapping Substrings

**Problem Link:** https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `text` and a list of strings `words` as input. The goal is to find the maximum number of non-overlapping occurrences of the words in the text.
- Expected output format: The function should return the maximum number of non-overlapping occurrences.
- Key requirements and edge cases to consider: The function should handle cases where the input text or words are empty, and it should also handle cases where there are multiple occurrences of the same word.
- Example test cases with explanations:
  - Example 1: Input: `text = "abcde", words = ["a","b","c"]`, Output: `3`
  - Example 2: Input: `text = "abcde", words = ["a","aa","aaa"]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each word in the list and checking if it occurs in the text. If it does, we mark the occurrence as used and continue checking for the next occurrence.
- Step-by-step breakdown of the solution:
  1. Iterate over each word in the list.
  2. For each word, iterate over the text to find occurrences of the word.
  3. If an occurrence is found, mark the occurrence as used and continue checking for the next occurrence.
  4. Keep track of the maximum number of non-overlapping occurrences found.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
class Solution {
public:
    int maxNumberOfSubstrings(string text, vector<string>& words) {
        int maxCount = 0;
        int n = text.size();
        int m = words.size();
        
        // Iterate over each word in the list
        for (int i = 0; i < m; i++) {
            int count = 0;
            string tempText = text;
            
            // Iterate over the text to find occurrences of the word
            while (true) {
                int index = tempText.find(words[i]);
                
                // If the word is not found, break the loop
                if (index == string::npos) {
                    break;
                }
                
                // Mark the occurrence as used
                tempText.replace(index, words[i].size(), "");
                
                // Increment the count
                count++;
            }
            
            // Update the maximum count
            maxCount = max(maxCount, count);
        }
        
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ is the number of words, $n$ is the length of the text, and $k$ is the maximum length of a word. This is because we have a nested loop structure, where we iterate over each word and then iterate over the text to find occurrences of the word.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the text. This is because we create a temporary copy of the text to mark occurrences as used.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, and the space complexity is moderate due to the temporary copy of the text.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to find non-overlapping occurrences of the words in the text. We can maintain a frequency count of the words and update it as we slide the window.
- Detailed breakdown of the approach:
  1. Initialize a frequency count of the words.
  2. Initialize a sliding window with a size equal to the length of the longest word.
  3. Iterate over the text using the sliding window.
  4. For each window, check if the word at the start of the window is in the frequency count.
  5. If it is, decrement the frequency count and increment the count of non-overlapping occurrences.
  6. If the frequency count is zero, slide the window to the next position.
- Proof of optimality: This approach has a time complexity of $O(n \cdot k)$, where $n$ is the length of the text and $k$ is the maximum length of a word. This is because we only iterate over the text once and use a constant amount of extra space to store the frequency count.

```cpp
class Solution {
public:
    int maxNumberOfSubstrings(string text, vector<string>& words) {
        int maxCount = 0;
        int n = text.size();
        int m = words.size();
        
        // Initialize a frequency count of the words
        unordered_map<string, int> freq;
        for (int i = 0; i < m; i++) {
            freq[words[i]]++;
        }
        
        // Initialize a sliding window with a size equal to the length of the longest word
        int windowSize = 0;
        for (int i = 0; i < m; i++) {
            windowSize = max(windowSize, (int)words[i].size());
        }
        
        // Iterate over the text using the sliding window
        for (int i = 0; i <= n - windowSize; i++) {
            int count = 0;
            unordered_map<string, int> tempFreq = freq;
            
            // Iterate over the window to find occurrences of the words
            for (int j = i; j < n; j += windowSize) {
                string word = text.substr(j, windowSize);
                
                // If the word is in the frequency count, decrement the frequency count and increment the count
                if (tempFreq.find(word) != tempFreq.end()) {
                    tempFreq[word]--;
                    count++;
                } else {
                    break;
                }
            }
            
            // Update the maximum count
            maxCount = max(maxCount, count);
        }
        
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the text and $k$ is the maximum length of a word. This is because we iterate over the text once and use a constant amount of extra space to store the frequency count.
> - **Space Complexity:** $O(m)$, where $m$ is the number of words. This is because we store the frequency count of the words.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity with respect to the length of the text, and it uses a constant amount of extra space to store the frequency count.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency count, and optimization techniques.
- Problem-solving patterns identified: Using a frequency count to keep track of the words and updating it as we slide the window.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity and using a frequency count to reduce the space complexity.
- Similar problems to practice: Other problems that involve finding non-overlapping occurrences of words in a text, such as the "Substring with Concatenation of All Words" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the frequency count correctly, not updating the frequency count correctly, and not handling edge cases correctly.
- Edge cases to watch for: Handling cases where the input text or words are empty, and handling cases where there are multiple occurrences of the same word.
- Performance pitfalls: Not using a sliding window approach, not using a frequency count, and not optimizing the time and space complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, and testing the function with different types of words and texts.