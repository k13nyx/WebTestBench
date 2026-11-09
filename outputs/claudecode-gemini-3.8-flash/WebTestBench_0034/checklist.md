# Test Checklist

## Functionality
- [ ] FT-01: Register a new user account
  - Action: Enter a valid username, email, and password in the registration form and click "Register".
  - Expected: Account is created successfully and the user is redirected to the language selection page.
- [ ] FT-02: Select a target language
  - Action: Click on a language card (e.g., "Spanish") from the available language options.
  - Expected: The chosen language is set as active and the course overview screen for that language is displayed.
- [ ] FT-03: Start an initial lesson
  - Action: Click the "Start" button on Lesson 1 under Level 1.
  - Expected: The lesson player launches and displays the first exercise of Lesson 1.
- [ ] FT-04: Answer a multiple-choice exercise
  - Action: Select an answer option in a multiple-choice question and click "Check".
  - Expected: The answer is submitted, evaluated immediately, and the option to proceed becomes active.
- [ ] FT-05: Answer a text-input exercise
  - Action: Type the translation into the text input field in a fill-in-the-blank question and click "Check".
  - Expected: The typed response is evaluated and instant correctness feedback is displayed.
- [ ] FT-06: Complete a quiz and view score
  - Action: Answer the final question of a level quiz and click "Submit Quiz".
  - Expected: The quiz ends and a summary screen displays the user's final score and total correct answers.
- [ ] FT-07: Resume an in-progress course
  - Action: Exit an ongoing lesson, return to the main dashboard, and click "Resume Course".
  - Expected: The application opens directly to the last uncompleted lesson or exercise the user was working on.
- [ ] FT-08: View lesson progress summary
  - Action: Navigate to the "Progress" dashboard.
  - Expected: Displays an overview showing completed lessons, current active level, and total completion percentage.

## Constraint
- [ ] CS-01: Prevent registration with empty fields
  - Action: Leave the registration fields blank and click "Register".
  - Expected: Registration is blocked, and validation error messages appear under all required fields.
- [ ] CS-02: Enforce sequential progression for locked lessons
  - Action: Click on an uncompleted, locked lesson (e.g., Lesson 3 while Lesson 1 is incomplete).
  - Expected: The lesson remains locked and cannot be started until previous prerequisites are completed.
- [ ] CS-03: Block submission when no answer is provided
  - Action: Click "Check" on an exercise without selecting an option or entering any text.
  - Expected: Submission is prevented (button remains disabled or an alert prompts the user to provide an answer).

## Interaction
- [ ] IX-01: Display instant feedback for correct answer
  - Action: Select the correct answer option in an exercise and click "Check".
  - Expected: A green banner appears displaying "Correct!", plays a success chime, and reveals the "Continue" button.
- [ ] IX-02: Display instant feedback for incorrect answer
  - Action: Select an incorrect answer option in an exercise and click "Check".
  - Expected: A red banner appears displaying "Incorrect" alongside the correct solution, and reveals the "Continue" button.
- [ ] IX-03: Dynamic lesson progress bar update
  - Action: Complete an exercise item within a lesson and click "Continue".
  - Expected: The top progress bar increments smoothly to reflect the updated fraction of completed exercises in the lesson.

## Content
- [ ] CT-01: Structured curriculum hierarchy display
  - Action: Open the course curriculum page.
  - Expected: Content is clearly grouped into distinct levels (e.g., Level 1, Level 2), each containing ordered sequences of lessons, exercises, and a concluding quiz.
- [ ] CT-02: Target language content alignment
  - Action: Inspect the vocabulary, question prompts, and options within the selected language course.
  - Expected: All lesson texts, exercise prompts, and answer choices match the selected target language without untranslated placeholders or broken strings.