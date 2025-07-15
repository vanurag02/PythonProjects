# 🧠 Mastermind – Number Guessing Game (Python CLI)

A simple command-line implementation of the classic **Mastermind** game in Python. The computer generates a random 4-digit number, and the player tries to guess it. After each attempt, the program gives hints about how many digits are correct and in the correct position.

Built using only **core Python** — no external libraries required.

---

## 🎮 Gameplay Overview

- The computer randomly generates a 4-digit number (no display)
- The user makes guesses one at a time
- After each incorrect guess:
  - The game tells how many digits were guessed correctly
  - It also shows which digits are in the correct position (rest marked as `X`)
- The game continues until the user guesses all 4 digits correctly
- Displays the number of attempts taken

---

---

## 🧠 Concepts Used

- Random number generation (`random.randrange`)
- Loops, conditionals, counters
- Type conversion between `int` and `str`
- List manipulation for feedback generation
- Clean CLI interaction and input handling

---

## 🚀 How to Run

### ▶️ Run the Script

```bash
python Mastermind.py
```

**Follow the on-screen instructions and try to become a Mastermind!**

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Libraries:** Standard Library Only (random)

---
