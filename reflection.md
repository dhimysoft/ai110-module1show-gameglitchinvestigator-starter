## 1. What was broken when you started?

The game had three major bugs when I first ran it.

Bug 1: The secret number converted to a string every other attempt.
Expected: the secret number stays as an integer throughout the game.
Actually happened: on even attempts the secret became a string so
comparing it to an integer guess always failed silently. For example
guessing 36 against a secret of "36" returned the wrong result
because Python treats 36 and "36" as different values.

Bug 2: The hints were backwards.
Expected: if my guess is higher than the secret it should say "Go LOWER".
Actually happened: it said "Go HIGHER" when I guessed too high and
"Go LOWER" when I guessed too low which was completely backwards and
made the game impossible to win by following the hints.

Bug 3: Wrong guesses sometimes increased the score.
Expected: wrong guesses should always decrease the score as a penalty.
Actually happened: on even attempts a Too High guess added 5 points
instead of subtracting them which rewarded wrong answers and made
the scoring system meaningless.

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot and Claude to help identify and fix the bugs.

Correct AI suggestion: Claude correctly identified that the secret
number was being converted to a string on even attempts using this
line in app.py:
secret = str(st.session_state.secret)
This caused the integer comparison to fail silently. I verified this
by opening the Developer Debug Info tab and observing the type
mismatch between my guess and the secret.

Incorrect AI suggestion: Copilot initially suggested rewriting the
entire check_guess function with extra type checking using try/except
blocks. This was unnecessary and overcomplicated the fix. The real
solution was simply removing the three lines in app.py that converted
the secret to a string on even attempts. I rejected Copilot's
suggestion because it added complexity without addressing the
root cause.

---

## 3. Debugging and testing your fixes

I verified my fixes by running the game manually and checking that:
- The secret number stayed the same across multiple submissions
- Guessing too high showed "Go LOWER" correctly
- Guessing too low showed "Go HIGHER" correctly
- Guessing the correct number ended the game with a win
- Wrong guesses always decreased the score

I then ran pytest to verify the logic functions worked correctly
with automated tests. All 6 tests passed confirming the fixes
worked as expected.

Fix 1: Replaced the conditional string conversion with:
secret = st.session_state.secret

Fix 2: Corrected the hint messages in check_guess so Too High
returns "Go LOWER" and Too Low returns "Go HIGHER".

Fix 3: Simplified update_score to always subtract 5 points
for wrong guesses instead of sometimes adding points.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire script every time a button is clicked.
This means any variable not stored in st.session_state gets reset
on every interaction. The secret number bug happened because the
secret variable was being recalculated inside the submit block
without using session state consistently.

I learned that in Streamlit you must store anything that needs to
persist between clicks inside st.session_state otherwise it will
be recreated on every rerun and cause unpredictable behavior.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is checking variable types carefully
when debugging. The hardest bug to find was the string conversion
because the game did not crash it just behaved incorrectly and
silently. This taught me that silent failures are harder to debug
than crashes.

Next time I would add type checks earlier and use the debug panel
more systematically from the start rather than guessing where
the problem might be.

This project changed how I think about AI generated code. It looks
correct at first glance but contains subtle logic errors that only
appear during actual use. The code was syntactically valid but
semantically broken. I now always test AI code manually and with
automated tests before trusting it in production.