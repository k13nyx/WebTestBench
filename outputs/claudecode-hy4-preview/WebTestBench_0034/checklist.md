# Test Checklist

## Functionality
- [ ] FT-01: A new visitor can register an account
  - Action: Open the home page, click "Register" / "Sign Up", fill in a new name, unique email, password and matching password confirmation, then submit the form.
  - Expected: Account is created, the user is signed in automatically, and the page redirects to the language selection (or dashboard) view with the user's name/email visible in the header.

- [ ] FT-02: User can pick a language to learn
  - Action: On the language selection view, click one of the offered default languages (e.g. "Spanish") and confirm the selection.
  - Expected: The course page for that language opens, showing a heading/title naming that language and its learning content.

- [ ] FT-03: Course content is organized into levels containing lessons, exercises and quizzes
  - Action: View the course page for the selected language.
  - Expected: Content is grouped under at least two labelled levels, and each level contains a sequence that includes at least one lesson, one exercise and one quiz.

- [ ] FT-04: User can start a course from the first item
  - Action: On an untouched course, click "Start" on the first lesson of the first level.
  - Expected: The first lesson's content loads and a "Continue" / "Next" control is available.

- [ ] FT-05: User can resume a course in progress at the correct point
  - Action: Complete one exercise in a course, leave to another page, return to the course page, then click "Resume" / "Continue".
  - Expected: The course reopens at the next unanswered item in the sequence, not at the very first item.

- [ ] FT-06: Completing an item advances the user through the sequence
  - Action: Answer and submit all questions of an exercise, then confirm/continue.
  - Expected: The app moves to the next item in the structured sequence (next lesson or the quiz) without requiring manual navigation back to the course list.

- [ ] FT-07: Different question types can be answered
  - Action: Work through one exercise and one quiz in the default course content.
  - Expected: At least two distinct question formats are presented (e.g. multiple-choice, type-the-answer/fill-in, matching/translation) and each accepts a valid user answer.

- [ ] FT-08: A quiz returns a simple score
  - Action: Answer every question of a quiz and submit it.
  - Expected: A result screen shows a score expressed as correct-out-of-total and/or percentage (e.g. "3/5" or "60%").

- [ ] FT-09: User can view a basic summary of progress
  - Action: After completing at least one lesson, open the "Progress" / dashboard view.
  - Expected: The summary shows the number or percentage of lessons completed, and per-lesson completion status that matches the items actually completed.

## Constraint
- [ ] CS-01: Registration rejects invalid or duplicate credentials
  - Action: Submit the registration form with an empty email, a password that does not match the confirmation, and then retry with an email that already exists in the default data.
  - Expected: All three attempts are rejected with visible field-level error messages, no account is created, and the user remains on the registration form.

- [ ] CS-02: Lessons cannot be started out of sequence
  - Action: Sign in with a fresh account and click a lesson in a later level (e.g. the last lesson of the highest level).
  - Expected: The lesson cannot be started; it is shown as locked/unavailable and its content is not accessible.

- [ ] CS-03: A question cannot be submitted without an answer
  - Action: On an exercise question, click "Check" / "Submit" without selecting or typing an answer.
  - Expected: Submission is blocked with an inline prompt such as "Please select an answer", and no feedback or score is produced.

- [ ] CS-04: Course content requires a signed-in user
  - Action: Copy the URL of a lesson page while signed in, sign out, then paste that URL into the browser and load it.
  - Expected: The user is redirected to the sign-in / registration page and the lesson content is not displayed.

## Interaction
- [ ] IX-01: Instant feedback is shown per answered question
  - Action: Answer one question correctly and a second one incorrectly, submitting each.
  - Expected: Each answer shows immediate inline feedback on the same screen without a full page reload — "Correct" for the right answer, and "Incorrect" together with the correct answer for the wrong one.

- [ ] IX-02: Answer selection is visibly highlighted and changeable before submitting
  - Action: Click one answer option on a multiple-choice question, then click a different option.
  - Expected: The first option is highlighted while selected, the highlight moves to the second option, and only the last selection is submitted.

- [ ] IX-03: Progress indicator updates as soon as a lesson is completed
  - Action: Note the progress bar / completed count, then complete the current lesson.
  - Expected: The progress bar or completed count increases immediately, without a manual page refresh.

- [ ] IX-04: Completed items are visually marked in the course sequence
  - Action: Complete a lesson, then return to the course page.
  - Expected: That lesson displays a completed state (e.g. checkmark / "Completed" label) distinct from current and locked items.

## Content
- [ ] CT-01: Language options are real, relevant and render correctly
  - Action: View the language selection list.
  - Expected: Every entry is a real language name relevant to language learning, with no duplicates, no "Lorem ipsum"/"Test" placeholders, and every entry's icon/flag image loads without a broken-image icon.

- [ ] CT-02: All learning content belongs to the selected language
  - Action: Open the lessons, exercises and quizzes of the chosen language and inspect their text.
  - Expected: All vocabulary, sentences and instructions belong to that language (or its translation) — no content from an unrelated language, and no "TODO"/"placeholder" text.

- [ ] CT-03: Questions are complete and error-free
  - Action: Review every question in one exercise and one quiz, including any media they contain.
  - Expected: Each question has a non-empty prompt, a usable answer control (options or input), no "undefined"/"null"/"NaN" text, and any image/audio used loads and plays correctly.

- [ ] CT-04: Levels, lessons, exercises and quizzes have meaningful titles
  - Action: Read every level heading and item title in the course.
  - Expected: Each level has a meaningful name (e.g. "Beginner"/"A1"), and every lesson, exercise and quiz title is descriptive of a language-learning topic — no generic labels like "Item 1" or "Section".