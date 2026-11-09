All checklist items executed. Here is the complete test report.

# Test Result

## Functionality
- [ ] FT-01: User can register and sign in to a new account
  - Action: Open the registration page, create an account with valid credentials, then sign in with those credentials.
  - Expected: Account is created and sign-in succeeds, landing the user on the language selection/course area.
  - Bug Report:
    - Issue: Broken sign-in (registration itself works; account creation → auto-lands on /select-language ✅). However, signing in with the exact same valid credentials (`qa.tester@example.com` / `TestPass123!`) fails **every time** with "Invalid email or password" (tested 3 times, incl. in the same session right after registering and after a sign-out). Root cause observed in `localStorage["lingualearn_users"]`: the stored user record contains only `{id, name, email, selectedLanguage, progress, totalXP, streak, createdAt}` — **no password field**, so password verification can never succeed.
    - Actual: Toast "Invalid email or password" on every Log In attempt with the newly registered credentials; user stays on /login.

- [X] FT-02: User can pick a language and start its course
  - Action: From the language catalog, select a language (e.g., Spanish) and choose to start the course.
  - Expected: The course dashboard for that language opens, showing its levels and lessons.
  - Note: On /select-language, choosing Spanish enabled "Continue" (disabled before selection); the dashboard opened at /dashboard with "Continue learning Spanish", levels Beginner (3 lessons) and Elementary (2 lessons).

- [ ] FT-03: Course content is structured by level with lessons, exercises, and quizzes
  - Action: Open the course and inspect the curriculum layout.
  - Expected: Content is grouped into levels (e.g., Beginner → Intermediate) and each level contains lessons, exercises, and at least one quiz.
  - Bug Report:
    - Issue: Missing quiz content / structure incomplete. Levels exist (1 → Beginner, 2 → Elementary) and each contains lessons, but **no quizzes exist anywhere**. The string "quiz" appears only in marketing copy on the landing page ("Practice with quizzes…"); the curriculum data (`/src/data/courses.ts`) defines each level as `{id, name, description, lessons[]}` with lessons holding only `questions[]` (types: multiple-choice, translation, fill-blank). Even after completing the entire Beginner level (3/3), no level quiz card appears on the dashboard.
    - Actual: Dashboard shows only lessons per level; no "exercises" vs "quiz" separation and zero quiz items in any level; Beginner level fully completed with no quiz unlocked.

- [X] FT-04: User can complete a lesson with exercises
  - Action: Open the first available lesson, answer its exercises, and complete the lesson.
  - Expected: Lesson is marked complete and the next lesson in the sequence becomes available.
  - Note: Completed Greetings (4 questions) → "Lesson Complete! 75% — You got 3 out of 4 correct", +75 XP shown; back on dashboard Greetings shows a completed check-mark and the next lesson (Numbers 1-10) changed from locked to clickable (`cursor-pointer`). Repeated for Numbers 1-10 and Colors (each unlocked the next in sequence).

- [X] FT-05: User can answer multiple question types
  - Action: Within exercises/quizzes, identify and answer at least two different question formats (e.g., multiple choice and typing/translation).
  - Expected: Each question type can be answered and submitted successfully.
  - Note: Three formats answered and submitted successfully: Multiple Choice (Hola/Goodbye), Translation (typed "Buenos días" → "Correct!"), Fill in the Blank (typed "noches" → "Correct!").

- [ ] FT-06: User can submit a quiz and receive a score
  - Action: Open a level's quiz, answer all questions, and click the submit/finish button.
  - Expected: A score is displayed (e.g., "7/10" or percentage) reflecting the submitted answers.
  - Bug Report:
    - Issue: No quiz feature exists — the checklist step cannot be performed. There is no level quiz to open (confirmed on the dashboard, in the curriculum data `courses.ts`, and by module scan: only Landing.tsx mentions "quiz"). The lesson "Finish" screen does show a score ("75% — You got 3 out of 4 correct"), but this is not a quiz submission flow.
    - Actual: No quiz entry point exists anywhere in the course; additionally the score math is buggy (see FT-08 — dashboard recorded 100 for a 75% lesson and 125% for perfect lessons).

- [ ] FT-07: User can resume a course where they left off
  - Action: Complete part of a course, sign out, sign back in, and open the course.
  - Expected: A start/resume option continues from the first incomplete lesson; prior progress is preserved.
  - Bug Report:
    - Issue: Sign-in failure makes resume impossible (same root cause as FT-01). Completed 3 of 5 lessons (progress **is** preserved in `localStorage` — user record shows greetings/numbers/colors with `completed:true`), clicked the log-out header button → returned to landing page. Attempted to sign back in with the registered credentials → toast "Invalid email or password" every time; could never open the course again, so the start/resume behavior was unreachable.
    - Actual: Login rejects valid registered credentials ("Invalid email or password"); user permanently locked out of their saved progress after signing out.

- [ ] FT-08: User can view a progress summary across lessons
  - Action: Navigate to the progress/dashboard view for the enrolled course.
  - Expected: A summary shows per-lesson status (completed vs. not) and/or quiz scores across the levels.
  - Bug Report:
    - Issue: Incorrect score data in the progress summary (statuses/percentages themselves render). The dashboard summary shows Course Progress % , "3 of 5 lessons", per-level "3/3" / "0/2" progressbars, and per-lesson status — but the displayed scores are mathematically wrong: Greetings, scored "3 out of 4 correct (75%)" at completion, displays "Score: 100%"; perfect 4/4 lessons (Numbers, Colors) display "Score: 125%" — an impossible value. Saved records confirm inflation (`progress.spanish` stored `score:100/125/125`; formula matches (correct+1)/total). XP totals also inherit it (header "350 XP" = 100+125+125 instead of 75+100+100).
    - Actual: Dashboard renders "Score: 125%" for a lesson answered 4/4 and "Score: 100%" for a lesson answered 3/4 (75%).

## Constraint
- [X] CS-01: Cannot register with missing required fields
  - Action: Submit the registration form with required fields (e.g., email/password) left empty.
  - Expected: Registration is blocked with a visible validation error; no account is created.
  - Note: Clicking "Create Account" with all fields empty → visible toast "Please fill in all fields", remained on /register, no account created, no redirect.

- [X] CS-02: Course content requires an authenticated account
  - Action: Without signing in, attempt to open a lesson or start a course.
  - Expected: The app does not allow starting lessons and directs the user to register/sign in.
  - Note: After signing out, direct navigation to /lesson/spanish/greetings redirected to /login ("Welcome back" page with Log In form and "Don't have an account? Sign up" link); /dashboard likewise redirected to /login.

- [X] CS-03: Lessons follow the structured sequence (no skipping locked items)
  - Action: Attempt to open a quiz or a later lesson before completing the preceding lesson(s) in the level.
  - Expected: The locked item is visibly marked as unavailable and cannot be started until the earlier item is completed.
  - Note: Before completing Greetings, the Numbers 1-10 card rendered with a `lucide-lock` icon, `opacity-60` and disabled cursor; clicking it did nothing (URL stayed /dashboard). Same for Colors and all Elementary lessons until their predecessor was completed (Food & Drinks remained locked while Family Members unlocked). (No quiz items exist to test locking on; lesson sequencing enforced.)

## Interaction
- [X] IX-01: Instant feedback on a correct answer
  - Action: In an exercise, select/type the correct answer and click Check/Submit.
  - Expected: The answer is immediately marked correct (e.g., green highlight / "Correct" message) without a full page reload.
  - Note: Typing "Buenos días" → Check Answer instantly displayed "Correct!" with icon, same URL / no page reload; repeated with "noches" and multiple-choice "Goodbye" (check icon on selected option).

- [X] IX-02: Instant feedback on a wrong answer
  - Action: In an exercise, provide an incorrect answer and click Check/Submit.
  - Expected: The answer is immediately marked wrong and the correct answer is shown.
  - Note: Selecting "Adiós" for "How do you say 'Hello'?" → instant "Not quite right" message; the chosen option was marked (X icon) and the correct option "Hola" was visibly marked with a check icon, all options disabled — no reload.

- [X] IX-03: Navigation between questions works
  - Action: After answering a question, click the Next button (repeat through a quiz).
  - Expected: The next question in sequence loads, and the question counter/position updates.
  - Note: "Continue" button after each check advanced through the lesson: counter updated "Question 1 of 4" → "Question 2 of 4" → "Question 3 of 4" → "Question 4 of 4", with new question loading each time; final step showed "Finish" → completion screen. (Quiz repeat not applicable — no quizzes exist.)

- [X] IX-04: Progress indicators update immediately after completing an item
  - Action: Complete a lesson or quiz, then return to the course dashboard.
  - Expected: The lesson shows as completed and any progress bar/percentage reflects the new state without manual reset.
  - Note: After each "Continue Learning" return to the dashboard (no manual refresh): Course Progress updated 0% → 20% ("1 of 5 lessons") → 40% → 60%, level bars updated 0/3 → 1/3 → 2/3 → 3/3, completed lessons gained status icons, and the next lesson became clickable immediately.

## Content
- [X] CT-01: Lesson content matches the selected language
  - Action: Enroll in a specific language course (e.g., Spanish) and review several lessons.
  - Expected: All vocabulary, prompts, and answer content are in/about the chosen language — no placeholder text (e.g., Lorem Ipsum) or content from a different language.
  - Note: Enrolled in Spanish and reviewed 3 lessons (Greetings, Numbers 1-10, Colors): all content is Spanish vocabulary/translations ("Hola", "Buenos días", "Buenas noches", "Cinco", "Uno, dos, tres", "Rojo", "Azul", "El cielo es azul"). No placeholder text; no French/Japanese/German content leaked into the Spanish course.

- [X] CT-02: Questions are complete and internally consistent
  - Action: Step through exercises and quiz questions in the course.
  - Expected: Every question has non-empty text, valid answer options, and options that match the question; no broken images or missing media.
  - Note: Across the 12 questions answered/seen (and verified against the question bank in `courses.ts`): every question has non-empty prompt text, 4 valid non-empty options that match the question (e.g., "What is 'five'?" → Cuatro/Cinco/Seis/Siete), and sensible single correct answers; fill-in-the-blank/translation items include correct answers (e.g., "One, two, ___" → "three") and hints where offered. All icons are inline SVGs (lucide); no broken images or missing media.

---

**Summary: 10 PASS / 8 FAIL.** Two core defects dominate: (1) **passwords are never stored on registration**, so sign-in (and therefore resume after sign-out) always fails — breaking FT-01 and FT-07; (2) **quizzes don't exist** despite the landing page advertising them — breaking FT-03 and FT-06; plus an **off-by-one score bug** ((correct+1)/total) that inflates dashboard lesson scores to impossible values like "125%" (FT-08).