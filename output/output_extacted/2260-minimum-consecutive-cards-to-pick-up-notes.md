## Minimum Consecutive Cards to Pick Up
**Problem Link:** https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description

**Problem Statement:**
- Input: A deck of cards where each card is represented by an integer from 1 to 1000.
- Constraints: Each card appears at most once in the deck.
- Expected Output: The minimum number of consecutive cards that can be picked up from the deck to contain all the cards that have been seen so far.
- Key Requirements: The cards must be picked up in the order they appear in the deck, and once a card is picked up, it cannot be put back into the deck.
- Edge Cases: If it is impossible to pick up all the cards, return -1.

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each card in the deck and try to find the minimum number of consecutive cards that contain all the cards seen so far.
- Step-by-step breakdown:
  1. Initialize a `set` to store the unique cards seen so far.
  2. Iterate through each card in the deck.
  3. For each card, check if it is already in the set. If not, add it to the set.
  4. Try to find the minimum number of consecutive cards that contain all the cards in the set.

```cpp
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int minimumConsecutiveCards(vector<int>& deck) {
    set<int> uniqueCards;
    int minConsecutiveCards = INT_MAX;
    
    for (int i = 0; i < deck.size(); i++) {
        uniqueCards.insert(deck[i]);
        
        // Try to find the minimum number of consecutive cards
        for (int j = i; j < deck.size(); j++) {
            set<int> consecutiveCards;
            for (int k = i; k <= j; k++) {
                consecutiveCards.insert(deck[k]);
            }
            
            if (consecutiveCards.size() == uniqueCards.size()) {
                minConsecutiveCards = min(minConsecutiveCards, j - i + 1);
            }
        }
    }
    
    return minConsecutiveCards == INT_MAX ? -1 : minConsecutiveCards;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of cards in the deck. This is because we have three nested loops: one to iterate through each card, one to try to find the minimum number of consecutive cards, and one to check if the consecutive cards contain all the unique cards.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique cards in the deck. This is because we use a set to store the unique cards.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible combinations of consecutive cards. The space complexity is relatively low because we only store the unique cards.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a `set` to store the unique cards and a `deque` to store the indices of the cards in the current window.
- Detailed breakdown:
  1. Initialize a `set` to store the unique cards and a `deque` to store the indices of the cards in the current window.
  2. Iterate through each card in the deck.
  3. For each card, check if it is already in the set. If not, add it to the set.
  4. Add the current index to the deque.
  5. If the size of the set is equal to the size of the deque, update the minimum number of consecutive cards.
  6. If the size of the set is greater than the size of the deque, remove the oldest index from the deque.

```cpp
#include <iostream>
#include <set>
#include <deque>
using namespace std;

int minimumConsecutiveCards(vector<int>& deck) {
    set<int> uniqueCards;
    deque<int> indices;
    int minConsecutiveCards = INT_MAX;
    
    for (int i = 0; i < deck.size(); i++) {
        uniqueCards.insert(deck[i]);
        indices.push_back(i);
        
        while (uniqueCards.size() > indices.size()) {
            indices.pop_front();
        }
        
        if (uniqueCards.size() == indices.size()) {
            minConsecutiveCards = min(minConsecutiveCards, indices.back() - indices.front() + 1);
        }
    }
    
    return minConsecutiveCards == INT_MAX ? -1 : minConsecutiveCards;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cards in the deck. This is because we only iterate through each card once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique cards in the deck. This is because we use a set to store the unique cards and a deque to store the indices of the cards in the current window.
> - **Optimality proof:** This approach is optimal because we only iterate through each card once and use a set and deque to store the unique cards and indices, respectively. This minimizes the time and space complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to store unique cards and a deque to store indices of cards in the current window.
- Problem-solving patterns identified: Using a sliding window approach to find the minimum number of consecutive cards.
- Optimization techniques learned: Minimizing time and space complexity by using efficient data structures and algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty deck or a deck with duplicate cards.
- Edge cases to watch for: Handling cases where the minimum number of consecutive cards is not found.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Testing the implementation with different inputs and edge cases to ensure correctness.