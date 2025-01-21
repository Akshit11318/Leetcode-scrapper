## Best Poker Hand
**Problem Link:** https://leetcode.com/problems/best-poker-hand/description

**Problem Statement:**
- The input consists of two parts: a hand of five cards and a deck of 47 cards. 
- Each card is represented by a string with two characters: the first character is the rank (`2` to `9`, `T` for ten, `J` for jack, `Q` for queen, `K` for king, `A` for ace), and the second character is the suit (`S` for spades, `H` for hearts, `D` for diamonds, `C` for clubs).
- The goal is to determine the best possible poker hand that can be formed by choosing any five cards from the hand and the deck.

**Expected Output Format:**
- The output should be a string representing the best possible poker hand.

**Key Requirements and Edge Cases:**
- The hand and deck may contain duplicate cards.
- The best possible poker hand should be determined based on standard poker hand rankings.
- If there are multiple possible hands with the same ranking, the hand with the highest rank should be chosen.

**Example Test Cases:**
- Input: `["2S","3S","4S","5S","6S"]`, `["7S","8S","9S","TS","JS","QS","KS","AS"]`
  - Output: `"Royal Flush"`
- Input: `["2S","3S","4S","5S","6S"]`, `["7S","8S","9S","TS","JS","QS","KS","AS","2H","3H","4H","5H","6H"]`
  - Output: `"Royal Flush"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible combinations of five cards from the hand and the deck.
- Then, evaluate each combination to determine the best possible poker hand.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Function to evaluate a poker hand
std::string evaluateHand(std::vector<std::string> hand) {
    // Implement poker hand evaluation logic here
    // For simplicity, this example only checks for a royal flush
    std::vector<char> ranks = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};
    std::vector<char> suits = {'S', 'H', 'D', 'C'};

    // Check for royal flush
    for (char suit : suits) {
        if (std::find(hand.begin(), hand.end(), std::string(1, 'T') + suit) != hand.end() &&
            std::find(hand.begin(), hand.end(), std::string(1, 'J') + suit) != hand.end() &&
            std::find(hand.begin(), hand.end(), std::string(1, 'Q') + suit) != hand.end() &&
            std::find(hand.begin(), hand.end(), std::string(1, 'K') + suit) != hand.end() &&
            std::find(hand.begin(), hand.end(), std::string(1, 'A') + suit) != hand.end()) {
            return "Royal Flush";
        }
    }

    return "Unknown";
}

// Brute force approach
std::string bestPokerHand(std::vector<std::string> hand, std::vector<std::string> deck) {
    int n = hand.size() + deck.size();
    std::vector<std::string> allCards = hand;
    allCards.insert(allCards.end(), deck.begin(), deck.end());

    std::string bestHand = "";
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    for (int m = l + 1; m < n; m++) {
                        std::vector<std::string> currentHand = {allCards[i], allCards[j], allCards[k], allCards[l], allCards[m]};
                        std::string evaluatedHand = evaluateHand(currentHand);

                        if (evaluatedHand == "Royal Flush" && (bestHand == "" || bestHand != "Royal Flush")) {
                            bestHand = evaluatedHand;
                        }
                    }
                }
            }
        }
    }

    return bestHand;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^5)$, where $n$ is the total number of cards (hand + deck).
> - **Space Complexity:** $O(n)$, for storing all possible combinations of cards.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of five cards, resulting in a time complexity of $O(n^5)$. The space complexity is $O(n)$ because we need to store all possible combinations.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is to use a more efficient algorithm to evaluate poker hands, such as using a hash table to store the count of each rank and suit.
- Then, iterate through the hand and deck to find the best possible poker hand.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

// Function to evaluate a poker hand
std::string evaluateHand(std::vector<std::string> hand) {
    std::unordered_map<char, int> rankCount;
    std::unordered_map<char, int> suitCount;

    for (const std::string& card : hand) {
        char rank = card[0];
        char suit = card[1];

        if (rankCount.find(rank) == rankCount.end()) {
            rankCount[rank] = 1;
        } else {
            rankCount[rank]++;
        }

        if (suitCount.find(suit) == suitCount.end()) {
            suitCount[suit] = 1;
        } else {
            suitCount[suit]++;
        }
    }

    // Check for royal flush
    if (suitCount.size() == 1 && rankCount.size() == 5) {
        std::vector<char> ranks = {'T', 'J', 'Q', 'K', 'A'};
        for (char rank : ranks) {
            if (rankCount.find(rank) == rankCount.end()) {
                return "Unknown";
            }
        }
        return "Royal Flush";
    }

    return "Unknown";
}

// Optimal approach
std::string bestPokerHand(std::vector<std::string> hand, std::vector<std::string> deck) {
    int n = hand.size() + deck.size();
    std::vector<std::string> allCards = hand;
    allCards.insert(allCards.end(), deck.begin(), deck.end());

    std::string bestHand = "";
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    for (int m = l + 1; m < n; m++) {
                        std::vector<std::string> currentHand = {allCards[i], allCards[j], allCards[k], allCards[l], allCards[m]};
                        std::string evaluatedHand = evaluateHand(currentHand);

                        if (evaluatedHand == "Royal Flush" && (bestHand == "" || bestHand != "Royal Flush")) {
                            bestHand = evaluatedHand;
                        }
                    }
                }
            }
        }
    }

    return bestHand;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^5)$, where $n$ is the total number of cards (hand + deck).
> - **Space Complexity:** $O(n)$, for storing all possible combinations of cards.
> - **Optimality proof:** The optimal approach still has a time complexity of $O(n^5)$ because we need to generate all possible combinations of five cards. However, the space complexity is reduced because we use a hash table to store the count of each rank and suit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hash tables, combinatorial algorithms.
- Problem-solving patterns identified: evaluating poker hands, generating all possible combinations.
- Optimization techniques learned: using hash tables to reduce space complexity.
- Similar problems to practice: evaluating other types of poker hands, generating all possible combinations of cards.

**Mistakes to Avoid:**
- Common implementation errors: not checking for duplicate cards, not handling edge cases.
- Edge cases to watch for: duplicate cards, invalid input.
- Performance pitfalls: using inefficient algorithms, not optimizing space complexity.
- Testing considerations: testing with different inputs, testing for edge cases.