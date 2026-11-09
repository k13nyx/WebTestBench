All checklist items have been executed. Here are the results:

# Test Result

**Environment note:** The app was reachable at `http://localhost:6034/`. Because logging in is broken (see FT‑02), a second account (`qa.tester2@example.com`) and later a third (`qa.tester3@example.com`) were registered through the working registration flow to be able to continue the session-dependent tests. Account `qa.tester@example.com` (FT‑01) was used for FT‑01, FT‑02, CS‑01, CS‑02, CS‑03 and the first pass of FT‑05/FT‑06/CS‑04.

## Functionality

- [X] FT-01: Register a new learner account
  - Action: Click the "Register"/"Sign up" entry point, enter a new email, a password (and name/username if the form asks for one), and submit the form.
  - Expected: The account is created, the app switches to a signed-in state (account name/email visible in the header), and no error is shown.
  - Note: Account created successfully ("Account created! Let's pick your language."), signed-in state reached, no error. The account name is shown in the dashboard greeting ("Welcome back, Test Learner 2!"), **not in the header** — the header only contains the logo, streak, XP and two icon buttons (language, logout).

- [ ] FT-02: Log in with an existing account
  - Action: Sign out if signed in, then use the "Log in"/"Sign in" form with the email and password from FT-01.
  - Expected: Login succeeds and the dashboard with the course list for that account is displayed.
  - Bug Report:
    - Issue: Broken authentication — valid credentials are always rejected
    - Actual: Submitting `qa.tester@example.com` / `Passw0rd!` (exactly the credentials used at registration) produces the toast **"Invalid email or password"**, the URL stays `/login` and the dashboard/course list is never rendered. Reproduced identically for `qa.tester2@example.com` / `Passw0rd!`. Root cause: registration writes `lingualearn_users[email] = {...newUser, password}` and then immediately calls `saveUser(newUser)`, which re-writes the same entry as `{...userData}` — i.e. **without the password** (verified: `'password' in storedUser === false` for every registered account), so the check `userData.password === password` in `login()` can never succeed.

- [X] FT-03: Choose a language to learn
  - Action: Open the language list on the dashboard and select one language (e.g., Spanish).
  - Expected: The chosen language becomes the active one, its levels/lessons/exercises/quizzes are shown, and any previously selected language is no longer active.
  - Note: Language list opens from the dashboard (header language icon → `/select-language`); the active-language checkmark moved from Spanish to French, the dashboard then showed French content ("Continue learning French", "Start your French journey", "0 of 2 lessons") and `selectedLanguage` was stored as `french`. Exercises/quizzes are not separate outline entries in this app (they exist as question types inside lessons).

- [X] FT-04: Course content is organized by level in a fixed sequence
  - Action: Open the course outline of the active language and expand each level.
  - Expected: Levels (e.g., Beginner, Intermediate, Advanced) appear in increasing difficulty order, and each level lists its lessons, exercises and quizzes in one fixed order.
  - Note: Outline is grouped in numbered, increasing-difficulty levels (Spanish: 1 Beginner → 2 Elementary; French/Japanese/German: Beginner) with each level listing its items in a fixed order (Greetings → Numbers 1-10 → Colors; Family Members → Food & Drinks). Levels are always rendered expanded — there is no collapse/expand control. The outline exposes only lesson entries; exercise/quiz content exists as question types inside the lessons (no separate exercise/quiz units, and no levels beyond Beginner/Elementary).

- [X] FT-05: Start a course from the beginning
  - Action: In the course outline, click "Start" (or the first lesson/exercise) of the first level.
  - Expected: The first lesson/exercise of that level opens with its content visible and a way to continue through its items.
  - Note: Clicking the first outline entry opened `/lesson/spanish/greetings` with the prompt "How do you say 'Hello' in Spanish?", the four options and a Check Answer → Continue flow ("Question 1 of 4").

- [ ] FT-06: Resume an in-progress course where it was left off
  - Action: Complete part of a lesson, leave it (back navigation or page reload), then return to the course outline and use "Resume"/"Continue".
  - Expected: The app reopens the last incomplete lesson/exercise of the active language at the exact item where the user stopped; already completed items are not replayed.
  - Bug Report:
    - Issue: In-progress state is never persisted — no resume possible
    - Actual: After answering Q1 and stopping at "Translation | Translate: 'Good morning' | Question 2 of 4", leaving via the header back button returns to the outline where the card shows only "Greetings | Learn basic Spanish greetings | 4 questions" — there is **no "Resume"/"Continue" control** (no element on the dashboard contains the word "resume") and the stored progress is still `{"spanish": []}` (the `answeredQuestions` field is always `[]`). Re-opening the lesson starts again at **"Question 1 of 4"**, replaying the already answered item. The "page reload" variant fails too: reloading `/lesson/spanish/greetings` or `/dashboard` redirects to `/login` although `lingualearn_user` exists in localStorage — the session is not restored on app boot.

- [ ] FT-07: Answer each type of question
  - Action: Work through a quiz/exercise containing multiple choice, fill-in-the-blank and matching items; select an option, type text, and pair the matches respectively.
  - Expected: Each item renders its own input control, accepts the user's input, and the answer is registered for that item.
  - Bug Report:
    - Issue: Missing question type — "matching" items do not exist anywhere in the app
    - Actual: Only three question types exist (`multiple-choice`, `translation`, `fill-blank`); the type list of every one of the 9 lessons in all 4 languages is `[multiple-choice, translation, fill-blank, multiple-choice]`. No matching question, no pair list and no match/pair component exist (no "match"/"pair" occurrence in the course data or in the lesson renderer). The lesson screen therefore only ever renders option buttons or a single free-text input, so a matching item can neither be displayed nor answered. (Multiple-choice, translation and fill-in-the-blank themselves work: each renders its own control, accepts input, grades and registers the answer.)

- [X] FT-08: Finishing an item records it as completed
  - Action: Answer the final question of a lesson/exercise and finish it.
  - Expected: The item shows a completed state (e.g., checkmark / "Completed") and is counted as completed in the progress summary.
  - Note: After "Finish" on the last question the screen shows "Lesson Complete!"; back on the outline the lesson card carries a `lucide-circle-check` icon and the counters updated (Beginner 1/3 → 2/3, "1 of 5 lessons" → "2 of 5 lessons", 20% → 40%). Note: the score shown on that card is wrong (see FT-09).

- [X] FT-09: A simple score is shown after a quiz
  - Action: Answer every question of a quiz and submit it.
  - Expected: A simple score (e.g., "8/10" or "80%") is displayed, and the number matches the count of answers graded correct.
  - Note: The end-of-lesson screen displays **"100%"** and **"You got 4 out of 4 correct"**, which matches the 4 graded-correct answers. **However the persisted score and XP are wrong:** the same perfect run stored `score: 125` for the lesson and awarded `totalXP: 250` after two lessons (the last correct answer is counted twice — `(score + isCorrect) / total`), and the outline card consequently shows "Score: 125%" for a 4/4 lesson.

- [X] FT-10: View a progress summary across lessons
  - Action: Open the "Progress"/"My Progress" entry in the navigation.
  - Expected: A summary lists the lessons of the active language with their completion state (and per-level totals), including every lesson completed so far.
  - Note: The summary is the dashboard's "Course Progress" panel: overall "40%", "2 of 5 lessons", per-level totals (Beginner 2/3, Elementary 0/2) and each lesson of the active language listed with its completion state (check icon + score for finished ones, lock icon for the rest) — every completed lesson is included. There is **no separate "Progress"/"My Progress" nav entry or `/progress` route** (the header holds only the language and logout icon buttons and the app renders no nav links).

## Constraint

- [ ] CS-01: Registration rejects invalid input
  - Action: Submit the registration form with a blank required field, then with a malformed email, then with a mismatched password confirmation.
  - Expected: Each invalid submission is rejected with a clear inline error message next to the offending field, and no account is created.
  - Bug Report:
    - Issue: Missing inline field validation and missing password-confirmation field
    - Actual: Blank form → the only feedback is the global toast **"Please fill in all fields"** rendered in the notification region at the top of the page; no error element is rendered next to the Name/Email/Password fields (inputs carry no `aria-invalid`, no error styling and no `required` attribute). Malformed email `not-an-email` → the submission never reaches the app because the native HTML5 validation of `<input type="email">` blocks it ("Please include an '@' in the email address"); the app renders no error message of its own in the DOM. Mismatched password confirmation → **not possible at all**: the form contains exactly three inputs (Name, Email, Password) with no confirmation field. No account was created by any invalid submission (the users list stayed empty).

- [X] CS-02: A duplicate account cannot be registered
  - Action: Register again using the email address of the account created in FT-01.
  - Expected: Registration is refused with an "already registered/exists" message, and no second account is created.
  - Note: Toast "An account with this email already exists", the app stayed on `/register`, and the stored users list still contained exactly one entry for that email.

- [X] CS-03: Login with a wrong password is rejected
  - Action: On the login form, enter the registered email with an incorrect password and submit.
  - Expected: An error message is displayed and the dashboard/course content is not shown.
  - Note: Toast "Invalid email or password" was displayed, the URL stayed `/login` and no course content was rendered.

- [X] CS-04: The lesson sequence is enforced
  - Action: On a course where the first lesson is not yet completed, attempt to open the second lesson/exercise/quiz of that level from the outline.
  - Expected: The later item stays locked (disabled or blocked with a "complete the previous item first" message) and its content does not open.
  - Note: "Numbers 1-10" (2nd item) was rendered with a `lucide-lock` icon and no clickable card; clicking it left the URL at `/dashboard` and no lesson content opened. Re-verified later on the second level ("Family Members" stayed locked with a lock icon and did not open while "Colors" was still unfinished).

## Interaction

- [X] IX-01: Instant feedback for a correct answer
  - Action: Answer a question correctly and submit.
  - Expected: Immediately, without leaving the item or reloading the page, a positive feedback message (e.g., "Correct!") and correct-answer styling appear.
  - Note: "Correct!" appeared immediately after Check Answer (no navigation/reload); the chosen option got `border-success bg-success/10 text-success` plus a `lucide-circle-check` icon.

- [X] IX-02: Instant feedback for an incorrect answer
  - Action: Answer a question incorrectly and submit.
  - Expected: Immediately a "Incorrect"/"Try again" message appears, the chosen option is marked as wrong, and the correct answer is revealed.
  - Note: "Not quite right" appeared immediately; the selected option turned `border-destructive bg-destructive/10 text-destructive` with a `lucide-circle-x` icon, the correct option was revealed in green with a check icon, and for the text questions "Correct answer: Buenos días" / "Correct answer: revoir" was shown.

- [X] IX-03: Continue is gated until an answer is given
  - Action: Open a question and inspect the Continue/Next/Submit control before answering, then select an answer and inspect it again.
  - Expected: The control is disabled (or does nothing when clicked) until an answer is provided, and becomes enabled as soon as an answer is given.
  - Note: "Check Answer" was `disabled` on every question before input (multiple-choice, translation, fill-in-the-blank) and became enabled immediately after selecting an option / typing text.

## Content

- [X] CT-01: Content matches the selected language and lesson topic
  - Action: Open a lesson, an exercise and a quiz in the active language and read the prompts, options and vocabulary.
  - Expected: All content is about the selected language (e.g., a Spanish lesson contains Spanish words/phrases with translations), and no content from another language appears.
  - Note: Spanish → "How do you say 'Hello' in Spanish?" (Hola/Adiós/Gracias/Por favor), "Complete: 'Buenas ___'", "Translate: 'Good morning'"; French → Bonjour/Au revoir/Merci, "Goodbye: Au ___"; Japanese → Konnichiwa/Sayonara/Arigatou/Sumimasen; German → Hallo/Tschüss/Danke/Bitte. A scan of all course data found no word from another language in any course. There are no separate exercise/quiz units to read — the content types are multiple-choice, translation and fill-in-the-blank.

- [X] CT-02: Content is complete, with no placeholders
  - Action: Inspect question options, lesson instructions, feedback messages and button labels across several levels.
  - Expected: Every option, instruction and message has real meaningful text — no empty options and no "Lorem ipsum", "TODO", "undefined" or truncated sentences.
  - Note: Checked across Spanish Beginner + Elementary, French, Japanese and German (all 9 lessons / 36 questions): every option, description, hint, feedback message ("Correct!", "Not quite right", "Correct answer: …", "Lesson Complete!", "Keep Practicing!", "You got 4 out of 4 correct") and button label ("Check Answer", "Continue", "Finish", "Continue Learning", "Try Again", "Show hint", "Create Account", "Log In") carries real text; zero empty options/questions/answers and no placeholder strings.

- [X] CT-03: The summary shows the learner's real data
  - Action: Complete two lessons in the active language, then open the progress summary.
  - Expected: The summary lists exactly the lessons/levels actually completed with their real completion state and counts, and shows no placeholder or zero values for work already completed.
  - Note: After completing Greetings and Numbers 1-10 the summary showed exactly those two lessons with check icons, "2 of 5 lessons", 40%, per-level "2/3" and "0/2" — no placeholder/zero values for completed work. Caveat: the per-lesson score values are wrong ("Score: 125%" for a 4/4 lesson) — see the FT-09 note.