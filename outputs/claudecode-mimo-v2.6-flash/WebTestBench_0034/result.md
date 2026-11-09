# Test Result

## Functionality
- [X] FT-01: Register a new account
  - Action: Navigate to the registration form, enter a valid email and password, and submit.
  - Expected: Account is created and the user is signed in, landing on a language selection or dashboard page.
  - *Note: Submitting valid Name/Email/Password on /register created the account, showed toast "Account created! Let's pick your language.", and landed on /select-language (signed in).*

- [X] FT-02: Choose a language to learn
  - Action: On the language selection screen, pick one of the offered languages and confirm.
  - Expected: The selected language becomes the user's active course and the course page for that language opens.
  - *Note: Picked Spanish, Continue (disabled until a card is selected) → toast "Great choice! Let's learn Spanish!" and dashboard opened as the active Spanish course ("Continue learning Spanish", 🇪🇸).*

- [X] FT-03: Course displays lessons grouped by level
  - Action: Open the selected language's course page.
  - Expected: Lessons are listed under distinct levels (e.g., Beginner, Intermediate) in a clear sequence.
  - *Note: Dashboard shows numbered levels "1 Beginner (Start your Spanish journey)" with Greetings → Numbers 1-10 → Colors, and "2 Elementary (Build your foundation)" with Family Members → Food & Drinks, each with 0/3, 0/2 progress bars.*

- [ ] FT-04: Start a course from the beginning
  - Action: Click the start/begin button on a course with no prior progress.
  - Expected: The first lesson opens, showing lesson content followed by exercises.
  - Bug Report:
    - Issue: Missing Lesson Content Section
    - Actual: There is no start/begin button (the lesson card is clicked instead), and the first lesson opens directly at the exercise "Question 1 of 4 (Multiple Choice: How do you say 'Hello' in Spanish?)" with no lesson content/intro/vocabulary section preceding the exercises — verified identically on 3 fresh accounts and across all 5 lessons.

- [ ] FT-05: Resume an in-progress course
  - Action: Leave a lesson mid-way, return to the course page, and click resume/continue.
  - Expected: The app reopens the lesson/step the user left off on, not the beginning.
  - Bug Report:
    - Issue: Lesson Position Not Restored on Resume
    - Actual: In "Numbers 1-10" I answered Question 1 correctly (feedback "Correct!", advanced to Question 2 of 4), exited via the header back button to the dashboard, then clicked the lesson card to resume — the lesson reopened at "Question 1 of 4" (the beginning), discarding in-lesson progress (stored progress only has `answeredQuestions: []`, written on lesson completion).

- [X] FT-06: Complete a lesson and advance to the next
  - Action: Finish all exercises in a lesson and submit/continue.
  - Expected: The lesson is marked complete and the next lesson in the sequence becomes accessible.
  - *Note: After finishing Greetings (Finish → "Lesson Complete! 100%"), "Continue Learning" returned to a dashboard showing Beginner 1/3, Greetings with a checkmark, and "Numbers 1-10" newly unlocked/clickable while "Colors" stayed locked; same unlock pattern continued through all 5 lessons (5/5, 100%).*

- [X] FT-07: Answer a multiple-choice question
  - Action: In an exercise, select an option and submit the answer.
  - Expected: The answer is accepted, recorded, and the exercise advances or accepts completion.
  - *Note: Selected "Hola" → "Check Answer" enabled → "Correct!" + Continue → Question 2 of 4; same for all MC items (e.g., Cinco, Red, Green, Agua, Fruit).*

- [X] FT-08: Answer a typed/text-input question
  - Action: Type an answer into a free-text exercise field and submit.
  - Expected: The response is accepted and evaluated rather than rejected as invalid input.
  - *Note: Typed "Buenos días" into Translation and "noches"/"café" into Fill-in-the-Blank → evaluated with "Correct!"; wrong inputs (e.g., "xxx") were also evaluated, not rejected, showing "Not quite right / Correct answer: X".*

- [ ] FT-09: Answer a matching or ordering-style question
  - Action: Complete an exercise requiring matching pairs or arranging items, then submit.
  - Expected: The arrangement/matching is accepted and evaluated.
  - Bug Report:
    - Issue: Matching/Ordering Exercise Type Does Not Exist
    - Actual: Every question in all 5 lessons (Greetings, Numbers, Colors, Family, Food) is only "Multiple Choice", "Translation", or "Fill in the Blank" — no matching-pairs or ordering/sequencing exercise was found anywhere in the app, so this action cannot be performed.

- [ ] FT-10: Take a quiz at the end of a lesson or level
  - Action: Navigate to a quiz and answer all questions, then submit.
  - Expected: The quiz submits successfully and produces a score result.
  - Bug Report:
    - Issue: No Quiz Feature Present
    - Actual: Lessons end with a "Lesson Complete / Keep Practicing" screen (no quiz); after completing all Beginner lessons (3/3) and all 5/5 lessons the dashboard shows no quiz entry (full page text contains no "Quiz"); routes /quiz and /quiz/spanish both render the app's 404 page — there is no quiz to navigate to, answer, or submit.

- [X] FT-11: View a progress summary
  - Action: Open the progress/summary view.
  - Expected: A summary shows completed vs. remaining lessons for the chosen language and overall progress.
  - *Note: The dashboard "Course Progress" panel is the progress summary: it showed "0% / 0 of 5" → "20% / 1 of 5" → "60% / 3 of 5" → "100% / 5 of 5", plus per-level completed/remaining bars (Beginner 3/3, Elementary 2/2) and completed lessons marked with checkmarks. (No dedicated /progress, /stats, /summary page exists — those routes 404 — and clicking the card opens no modal.)*

## Constraint
- [X] CS-01: Registration blocked with invalid or empty credentials
  - Action: Submit the registration form with an empty email/password or malformed email.
  - Expected: Submission is blocked and a validation error is displayed; no account is created.
  - *Note: Empty submit → toast "Please fill in all fields", stayed on /register. Malformed email "not-an-email" → form submission blocked by native validation (invalid field kept focus), page stayed on /register, no account created.*

- [X] CS-02: Cannot skip ahead to locked lessons
  - Action: Attempt to open a lesson that comes after an incomplete prior lesson.
  - Expected: Access is prevented (locked state or error) until prerequisite lessons are completed.
  - *Note: With 0 completed, clicking the locked "Colors" card (lock icon, no pointer cursor) did nothing — no navigation occurred; "Numbers" stayed locked until Greetings was completed, and Elementary lessons stayed locked until Beginner 3/3. Locked state is rendered and enforced.*

- [ ] CS-03: Cannot submit an exercise or quiz question with no answer selected/entered
  - Action: Leave a question unanswered and click submit/next.
  - Expected: The app blocks advancement and prompts the user to answer.
  - Bug Report:
    - Issue: No Validation Prompt on Unanswered Submission
    - Actual: Advancement is blocked — "Check Answer" is disabled while no option is selected and while text inputs are empty (verified on MC, Translation, and Fill-in-the-Blank) — but clicking/attempting submission produces no prompt/message asking the user to answer (no toast, inline error, or guidance appears; only the placeholder text is shown).

- [X] CS-04: Duplicate registration with an existing email is rejected
  - Action: Register using an email already registered.
  - Expected: Registration fails with an "already exists" style error message.
  - *Note: Registering again with tester.qa@example.com (valid credentials) → toast "An account with this email already exists", remained on /register, no second account created (localStorage `lingualearn_users` still holds one entry for that email).*

## Interaction
- [X] IX-01: Instant feedback shown after each answer
  - Action: Submit an answer to any exercise or quiz question.
  - Expected: Immediate visual feedback appears indicating correct or incorrect, before moving on.
  - *Note: After every "Check Answer" the feedback renders before advancing: "Correct!" with a checkmark on right answers; "Not quite right" plus "Correct answer: X" on wrong ones (options/text become disabled and "Continue/Finish" appears only after feedback).*

- [X] IX-02: Score updates after answering questions
  - Action: Answer questions in a quiz/exercise set.
  - Expected: A visible score/points indicator reflects the results of answered questions.
  - *Note: Header XP updated with results (0 → 125 → 350 → 600 XP), each result screen showed a score ("100% — 4 out of 4 — +100 XP", "75% — 3 out of 4 — +75 XP", "0% — Keep Practicing"), and per-lesson "Score: X%" badges appeared on completed lessons; the lesson progress bar advances per answered question. (Note: badge values are inaccurate — see CT-03.)*

- [ ] IX-03: Course state reflects progress after leaving and returning
  - Action: Complete part of a course, refresh or revisit the course page.
  - Expected: The UI shows updated progress (e.g., completed lessons marked, continue option present) without loss of state.
  - Bug Report:
    - Issue: Session Lost on Refresh with Broken Login (State Inaccessible)
    - Actual: In-app revisit works (dashboard correctly showed "1 of 5", checkmarks, continue option), but any full page refresh/navigation forces redirect to /login, and logging back in always fails with toast "Invalid email or password" for accounts created in this app (registration never stores a password — `lingualearn_user`/`lingualearn_users` contain no password field). Reproduced for two separate accounts: after a refresh the user can never return to see their progress → loss of state.

## Content
- [X] CT-01: Lesson content matches the selected language and level
  - Action: Open lessons at different levels of the chosen language.
  - Expected: All lesson text, vocabulary, and questions are in/about the selected language and appropriate to the stated level.
  - *Note: Spanish selected → all content is Spanish-focused. Beginner: greetings (Hola/Adiós), numbers (tres/diez), colors (rojo/azul/verde). Elementary: family (madre/abuelo/hermana, "Mi padre") and food (agua/pan/café/manzana). Instructions in English, vocabulary/questions in Spanish, difficulty fits each level.*

- [X] CT-02: Answer options and quiz content are relevant and non-duplicated
  - Action: Review multiple-choice options and quiz questions across exercises.
  - Expected: Options are plausible, distinct, and on-topic; no lorem-ipsum or off-theme placeholder content appears.
  - *Note: All reviewed options are distinct, on-topic Spanish/English vocabulary: Cuatro/Cinco/Seis/Siete; Leche/Jugo/Agua/Café; Padre/Madre/Hermano/Hermana; Blue/Green/Red/Yellow; Vegetable/Fruit/Drink/Meat. No placeholder/lorem text found. (No quiz content exists to review — see FT-10.)*

- [ ] CT-03: Progress summary values are accurate
  - Action: Compare the progress summary against actual completed lessons.
  - Expected: Counts of completed/remaining lessons and score shown match what the user actually finished.
  - Bug Report:
    - Issue: Incorrect Score Calculation (Scores Inflated by +25%, Can Exceed 100%)
    - Actual: Lesson counts are accurate (5 of 5, Beginner 3/3, Elementary 2/2), but score badges are wrong: Greetings shows "Score: 125%" for an actual 4/4 = 100%, Colors "Score: 125%" for 100%, Family/Food "Score: 125%" for 100%, and Numbers shows "Score: 100%" for an actual 3/4 = 75% (verified result screens: "100%, 4 out of 4", "75%, 3 out of 4"). Stored score in localStorage is literally 125 — every score = actual + 25, producing impossible values >100%.