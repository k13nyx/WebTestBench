# Test Checklist

## Functionality
- [ ] FT-01: User can register for a new account
  - Action: Fill the registration form with a valid email and password, then click "Sign Up".
  - Expected: Account is created and the user is taken to the language selection screen.

- [ ] FT-02: User can select a language to learn
  - Action: On the language selection screen, click a language (e.g., "Spanish").
  - Expected: The selected language is set and its course/level structure is displayed.

- [ ] FT-03: User can view lessons, exercises, and quizzes organized by level
  - Action: After selecting a language, open the course page.
  - Expected: Lessons, exercises, and quizzes are listed in a sequence grouped by level (e.g., Level 1, Level 2).

- [ ] FT-04: User can start a course
  - Action: Click "Start Course" (or "Start Lesson") on the first lesson.
  - Expected: The first lesson/unit opens and is ready to use.

- [ ] FT-05: User can resume an in-progress course
  - Action: From the dashboard, click "Resume" on a partially completed course.
  - Expected: The app opens at the lesson/question where the user last stopped.

- [ ] FT-06: User can answer different types of questions
  - Action: In a lesson/quiz, complete a multiple-choice question and a fill-in-the-blank question, then submit each.
  - Expected: Both question types accept input and submit successfully.

- [ ] FT-07: User can view a progress summary across lessons
  - Action: Open the progress/summary page.
  - Expected: A basic summary of completed and remaining lessons (e.g., counts or a list) is displayed.

## Constraint
- [ ] CS-01: Registration requires valid, non-empty required fields
  - Action: Submit the registration form with an empty or invalid email, then click "Sign Up".
  - Expected: Registration is blocked and an error message (e.g., "Enter a valid email") is shown.

- [ ] CS-02: Lessons are locked sequentially
  - Action: Attempt to open a later lesson before completing earlier ones.
  - Expected: The later lesson is locked and cannot be accessed.

- [ ] CS-03: A language must be selected before lessons are accessible
  - Action: Try to access lessons without first selecting a language.
  - Expected: Lessons are not accessible; the user is directed to select a language first.

## Interaction
- [ ] IX-01: Instant feedback is shown after each answer
  - Action: Answer a question and submit it.
  - Expected: Feedback (correct/incorrect with explanation) appears immediately on the same screen.

- [ ] IX-02: A simple score is displayed after a question set/quiz
  - Action: Complete a set of questions or a quiz.
  - Expected: A simple score (e.g., "7/10") is displayed.

- [ ] IX-03: Progress indicator updates after completing a lesson
  - Action: Complete a lesson and return to the course page.
  - Expected: The lesson is marked complete and the progress indicator reflects the change.

## Content
- [ ] CT-01: Lesson, exercise, and quiz content matches the selected language
  - Action: Open lessons/exercises/quizzes for the selected language.
  - Expected: All displayed text, audio, and media are in or about the selected language.

- [ ] CT-02: Content difficulty matches its designated level
  - Action: Inspect lessons within a given level.
  - Expected: Topics and difficulty correspond to that level's designation within the structure.