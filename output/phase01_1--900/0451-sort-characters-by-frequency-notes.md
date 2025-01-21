## Sort Characters by Frequency
**Problem Link:** https://leetcode.com/problems/sort-characters-by-frequency/description

**Problem Statement:**
- Input: A string `s` containing various characters.
- Constraints: The string can contain any ASCII character, and its length is between 1 and 1000.
- Expected Output: A string where characters are sorted by their frequency in descending order. If two characters have the same frequency, the one that appears first in the original string should come first.
- Key Requirements and Edge Cases:
  - Handle cases where the string contains only one unique character.
  - Ensure the output maintains the relative order of characters with the same frequency based on their first occurrence in the input string.
- Example Test Cases:
  - Input: "tree"
    - Expected Output: "eert"
  - Input: "cccaaa"
    - Expected Output: "aaaccc"
  - Input: "Aabb"
    - Expected Output: "bbaA"

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves counting the frequency of each character and then sorting them based on this frequency. 
- A step-by-step breakdown:
  1. Create a frequency map to store the count of each character.
  2. Convert the frequency map into a vector of pairs (character, frequency) to facilitate sorting.
  3. Sort this vector based on the frequency of characters in descending order and then by the character's ASCII value to ensure stability for characters with the same frequency.
  4. Construct the output string by iterating over the sorted vector and appending each character a number of times equal to its frequency.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

string frequencySort(string s) {
    map<char, int> freqMap;
    for (char c : s) {
        freqMap[c]++;
    }
    
    vector<pair<char, int>> charFreq;
    for (auto& pair : freqMap) {
        charFreq.push_back(pair);
    }
    
    sort(charFreq.begin(), charFreq.end(), [](pair<char, int>& a, pair<char, int>& b) {
        if (a.second == b.second) {
            return s.find(a.first) < s.find(b.first); // Stability for same frequency
        }
        return a.second > b.second;
    });
    
    string result;
    for (auto& pair : charFreq) {
        result.append(pair.second, pair.first);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique characters in the string. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, for storing the frequency map and the vector of character-frequency pairs.
> - **Why these complexities occur:** The sorting step is the bottleneck, making the time complexity $O(n \log n)$. The space complexity is linear because we need to store all unique characters and their frequencies.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution utilizes a similar approach but focuses on directly leveraging the frequency counts to construct the output string without the need for sorting. Instead, it uses a priority queue to efficiently handle characters based on their frequency.
- Detailed breakdown:
  1. Count the frequency of each character using a map.
  2. Insert the characters and their frequencies into a priority queue, where the priority is based on the frequency.
  3. Dequeue characters from the priority queue and append them to the result string a number of times equal to their frequency.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

struct CharFreq {
    char c;
    int freq;
    bool operator<(const CharFreq& other) const {
        return freq < other.freq;
    }
};

string frequencySort(string s) {
    map<char, int> freqMap;
    for (char c : s) {
        freqMap[c]++;
    }
    
    priority_queue<CharFreq> pq;
    for (auto& pair : freqMap) {
        pq.push({pair.first, pair.second});
    }
    
    string result;
    while (!pq.empty()) {
        CharFreq cf = pq.top();
        pq.pop();
        result.append(cf.freq, cf.c);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the total number of characters and $k$ is the number of unique characters. This is because we push and pop each unique character from the priority queue once.
> - **Space Complexity:** $O(n)$, for storing the frequency map and the priority queue.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to sort characters by frequency. The use of a priority queue allows for efficient handling of characters based on their frequency.

---

### Final Notes

**Learning Points:**
- Utilizing a priority queue for efficient sorting based on frequency.
- Counting character frequencies using a map.
- Constructing the output string by iterating over the sorted characters.

**Mistakes to Avoid:**
- Not considering the stability of the sort for characters with the same frequency.
- Incorrectly handling edge cases, such as strings with a single unique character.
- Failing to validate the input string for null or empty conditions.