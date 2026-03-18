# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.  
It wrote the code, ran away, and left behind a game that doesn’t really work.

- You can't win consistently  
- The hints are misleading  
- The secret number seems to change randomly  

---

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python -m streamlit run app.py
```

---

## ▶️ Running the Application

I ran the app locally using the command above, and it successfully opened in the browser.

To debug the issues, I used the **Developer Debug Info** tab in the app to view the secret number and compare it with my guesses. This helped me reproduce and understand the bugs.

---

## 🎯 Game Purpose

This is a number guessing game where the player tries to guess a randomly generated number within a limited number of attempts.

The game:
- Provides hints ("Higher" or "Lower")
- Tracks score based on performance
- Ends when the correct number is guessed

---

## 🐛 Bugs Found

### Bug 1 – Secret Number Reset
- The secret number changed every time I clicked "Submit"  
- I noticed this when I guessed the same number twice and got different results  
- Cause: Streamlit reruns the script on every interaction and the value was not stored in `st.session_state`  

---

### Bug 2 – Type Mismatch
- The secret number was sometimes converted into a string  
- This caused comparisons to fail even when the values looked correct  

**Cause:**
```python
secret = str(st.session_state.secret)
```

---

### Bug 3 – Incorrect Hint Logic
- The game gave incorrect hints  
- Example: it would say "Go Higher" when the guess was already too high  
- Cause: The conditional logic in `check_guess()` was reversed  

---

### Bug 4 – Score Bug
- Some incorrect guesses increased the score instead of decreasing it  
- Cause: Incorrect condition in the scoring logic  

---

## 🔧 Fixes Applied

### Fix 1 – Persist Secret Number
- Stored the secret number in `st.session_state`  
- This prevents it from resetting on every interaction  

---

### Fix 2 – Removed String Conversion
- Removed:
```python
secret = str(st.session_state.secret)
```
- Keeping the value as an integer ensures correct comparisons  

---

### Fix 3 – Corrected Hint Logic
- Updated conditions in `check_guess()`:
  - Too high → "Go LOWER"  
  - Too low → "Go HIGHER"  

---

### Fix 4 – Fixed Score Logic
- Updated scoring so incorrect guesses always subtract points  
- This makes scoring consistent  

---

## 🧪 Testing

I ran automated tests using:

```bash
pytest
```

- All tests passed successfully  
- This confirmed that the fixes work correctly  

---

## 📸 Demo

![Winning Game](screenshot.png)

The game now:
- Maintains a consistent secret number
- Provides correct hints
- Updates score properly
- Can be won normally

---

## 🧠 Reflection (Summary)

This project showed me that even if code runs, it can still have logical issues that make it unusable.

The biggest issue came from how Streamlit reruns the script on every interaction. Once I understood how `st.session_state` works, the behavior of the game made a lot more sense.

I also learned that AI-generated code can look correct at first glance but still contain subtle bugs. It’s helpful for getting started, but it still needs to be tested and verified carefully.