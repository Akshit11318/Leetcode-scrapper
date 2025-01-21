## Number of Unique Categories

**Problem Link:** https://leetcode.com/problems/number-of-unique-categories/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `categories`, where each string is a category name, and a string `sentence`, find the number of unique categories that are mentioned in the sentence.
- Expected output format: The function should return the number of unique categories.
- Key requirements and edge cases to consider: The input array `categories` can be empty, and the `sentence` can be empty as well. The categories in the `sentence` can appear in any order and can be separated by any number of spaces.
- Example test cases with explanations:
  - `categories = ["tech", "science", "history"], sentence = "tech science history"` should return `3` because all three categories are mentioned in the sentence.
  - `categories = ["tech", "science", "history"], sentence = "tech tech"` should return `1` because only one category ("tech") is mentioned in the sentence.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate over each category and check if it exists in the sentence. If it does, we increment a counter to keep track of the number of unique categories found.
- Step-by-step breakdown of the solution:
  1. Initialize a counter `uniqueCategories` to 0.
  2. Iterate over each category in the `categories` array.
  3. For each category, check if it exists in the `sentence`.
  4. If a category is found in the sentence and has not been counted before, increment the `uniqueCategories` counter.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It directly checks for the presence of each category in the sentence.

```cpp
int numberOfUniqueCategories(vector<string>& categories, string sentence) {
    unordered_set<string> unique;
    for (const auto& category : categories) {
        if (sentence.find(category) != string::npos && unique.find(category) == unique.end()) {
            unique.insert(category);
        }
    }
    return unique.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of categories and $m$ is the length of the sentence. This is because for each category, we are potentially scanning the entire sentence.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique categories. This is for storing the unique categories found in the sentence.
> - **Why these complexities occur:** The time complexity is due to the nested operations of iterating over categories and searching within the sentence. The space complexity is due to storing unique categories.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each category against the entire sentence, we can preprocess the sentence to make lookups more efficient. We can split the sentence into words and store them in a set for constant time lookup.
- Detailed breakdown of the approach:
  1. Split the sentence into words and store them in a set.
  2. Initialize a counter `uniqueCategories` to 0.
  3. Iterate over each category in the `categories` array.
  4. For each category, check if it exists in the set of words from the sentence. If it does and has not been counted before, increment the `uniqueCategories` counter.
- Proof of optimality: This approach optimizes the lookup time within the sentence from linear to constant, significantly improving the performance for large sentences.

```cpp
int numberOfUniqueCategories(vector<string>& categories, string sentence) {
    unordered_set<string> words;
    istringstream iss(sentence);
    string word;
    while (iss >> word) {
        words.insert(word);
    }
    
    unordered_set<string> unique;
    for (const auto& category : categories) {
        if (words.find(category) != words.end() && unique.find(category) == unique.end()) {
            unique.insert(category);
        }
    }
    return unique.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of categories and $m$ is the number of words in the sentence. This is because we are doing a constant time lookup for each category in the set of words.
> - **Space Complexity:** $O(n + m)$, for storing the words from the sentence and the unique categories.
> - **Optimality proof:** This is optimal because we have reduced the time complexity of checking each category against the sentence from linear to constant, leveraging the efficiency of set lookups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of preprocessing data to improve lookup efficiency, and the use of sets for constant time membership testing.
- Problem-solving patterns identified: Improving performance by reducing the complexity of nested operations.
- Optimization techniques learned: Preprocessing data to enable faster lookups, and leveraging data structures like sets for efficient membership testing.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases such as empty input arrays or sentences.
- Edge cases to watch for: Categories or sentences with leading or trailing spaces, and categories that are substrings of other categories.
- Performance pitfalls: Using linear search within the sentence for each category, leading to high time complexity.
- Testing considerations: Ensuring that the solution works correctly for a variety of inputs, including different lengths of sentences and categories, and different numbers of unique categories.