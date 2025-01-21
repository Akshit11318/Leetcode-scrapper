## Design an ATM Machine

**Problem Link:** https://leetcode.com/problems/design-an-atm-machine/description

**Problem Statement:**
- Input format and constraints: The ATM class should have methods for deposit, withdraw, and getBalance.
- Expected output format: The output should be the result of the operations, with a focus on the balance after each operation.
- Key requirements and edge cases to consider: Handling cases where the account balance is insufficient for a withdrawal, ensuring that only valid denominations ($5, $10, $20, $50, $100) are used, and updating the balance correctly after each transaction.
- Example test cases with explanations: 
    - Deposit $100 and then withdraw $50. The balance should be $50.
    - Deposit $100 and then withdraw $200. The withdrawal should fail due to insufficient balance.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can use a simple class-based approach where we maintain the balance and update it based on deposits and withdrawals.
- Step-by-step breakdown of the solution:
    1. Initialize the ATM with a balance.
    2. Implement the deposit method to add money to the balance.
    3. Implement the withdraw method to subtract money from the balance, ensuring there's enough balance for the withdrawal.
- Why this approach comes to mind first: It directly addresses the requirements by providing methods for deposit, withdrawal, and getting the balance.

```cpp
class ATM {
public:
    ATM() : balance(0) {}

    void deposit(int amount, int denomination) {
        if (denomination == 5 || denomination == 10 || denomination == 20 || denomination == 50 || denomination == 100) {
            balance += amount * denomination;
        }
    }

    bool withdraw(int amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }

    int getBalance() {
        return balance;
    }

private:
    int balance;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for each method since we're performing constant time operations.
> - **Space Complexity:** $O(1)$ because we're using a fixed amount of space to store the balance.
> - **Why these complexities occur:** The operations (deposit, withdraw, getBalance) do not depend on the input size, making them constant time and space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of just checking if the denomination is valid, we can also consider the case where we need to return the exact change using the available denominations.
- Detailed breakdown of the approach:
    1. Use a `std::map` to store the count of each denomination.
    2. In the deposit method, update the count of the deposited denomination.
    3. In the withdraw method, try to dispense the exact change using the available denominations.
- Proof of optimality: This approach ensures that we can handle deposits and withdrawals with the least amount of code and in constant time, making it optimal.

```cpp
class ATM {
public:
    ATM() {}

    void deposit(int amount, int denomination) {
        if (denomination == 5 || denomination == 10 || denomination == 20 || denomination == 50 || denomination == 100) {
            banknotes[denomination] += amount;
        }
    }

    bool withdraw(int amount) {
        int denominations[] = {100, 50, 20, 10, 5};
        for (int denomination : denominations) {
            int count = min(amount / denomination, banknotes[denomination]);
            amount -= count * denomination;
            banknotes[denomination] -= count;
        }
        return amount == 0;
    }

    int getBalance() {
        int balance = 0;
        for (auto& pair : banknotes) {
            balance += pair.first * pair.second;
        }
        return balance;
    }

private:
    std::map<int, int> banknotes = {{5, 0}, {10, 0}, {20, 0}, {50, 0}, {100, 0}};
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for deposit and withdraw since the number of denominations is fixed, and $O(n)$ for getBalance where n is the number of denominations (which is constant in this case).
> - **Space Complexity:** $O(1)$ because we're using a fixed amount of space to store the count of each denomination.
> - **Optimality proof:** This solution optimizes the use of space and time by only storing the necessary information (the count of each denomination) and performing operations in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store the count of each denomination, and iterating over a fixed set of denominations to dispense exact change.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (deposit, withdraw, getBalance), and using a data structure (map) to store relevant information.
- Optimization techniques learned: Using a fixed set of denominations to reduce the complexity of the withdraw method.
- Similar problems to practice: Implementing a simple banking system, or a vending machine that dispenses change.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for valid denominations, or not updating the balance correctly.
- Edge cases to watch for: Insufficient balance for a withdrawal, or attempting to deposit/withdraw an invalid denomination.
- Performance pitfalls: Using a data structure that is not efficient for the problem, such as a list instead of a map.
- Testing considerations: Test the ATM class with different scenarios, including deposits, withdrawals, and getting the balance.