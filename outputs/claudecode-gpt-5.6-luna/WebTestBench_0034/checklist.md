# Test Checklist

## Functionality
- [ ] **FT-01: User can register for an account**
  - **Action:** Open **Register**, enter valid details in all required fields, and select **Create account**.
  - **Expected:** The account is created and the user is signed in or taken to the language-selection screen.

- [ ] **FT-02: User can select a language**
  - **Action:** Open the **Language selector**, choose any available language, and confirm the selection.
  - **Expected:** The selected language is displayed and its available course levels are shown.

- [ ] **FT-03: User can start an available course**
  - **Action:** Select an available level and choose **Start course**.
  - **Expected:** The first lesson in the selected language and level opens.

- [ ] **FT-04: Course content follows a structured sequence**
  - **Action:** From the course screen, progress through the displayed levels, lessons, exercises, and quizzes using **Next** or the provided navigation.
  - **Expected:** Content appears in the defined order: level → lessons → exercises/quizzes, and the next item opens after the current item is completed.

- [ ] **FT-05: User can resume an incomplete course**
  - **Action:** Start a course, complete part of a lesson, leave the course, reopen it, and select **Resume course**.
  - **Expected:** The course reopens at the saved lesson or exercise position rather than restarting from the beginning.

- [ ] **FT-06: User can submit answers to exercises and quizzes**
  - **Action:** Answer each available question type in the default course and select **Submit**, **Check answer**, or the equivalent answer-control button.
  - **Expected:** Each valid answer is accepted and the user can continue to the next question or activity.

- [ ] **FT-07: User can view a course progress summary**
  - **Action:** Open **Progress**, **My progress**, or the course summary from an enrolled course.
  - **Expected:** A summary shows the selected language, current level, and lesson completion status.

## Constraint
- [ ] **CS-01: Registration blocks incomplete required information**
  - **Action:** Open **Register**, leave at least one required field empty, and select **Create account**.
  - **Expected:** The account is not created and the missing field is identified with a validation message.

- [ ] **CS-02: Course selection is limited to available default data**
  - **Action:** Open the language and level selection screens without adding or creating course data.
  - **Expected:** Only languages and levels that exist in the application are selectable, and no empty or invalid course can be started.

- [ ] **CS-03: An unanswered activity cannot be submitted as completed**
  - **Action:** Open an exercise or quiz question, leave it unanswered, and select **Submit** or **Next**.
  - **Expected:** The activity is not marked complete and the user is prompted to provide an answer.

## Interaction
- [ ] **IX-01: Answer submission provides immediate correctness feedback**
  - **Action:** Submit both a correct answer and an incorrect answer in available exercises or quizzes.
  - **Expected:** Each submission immediately indicates whether the answer is correct or incorrect.

- [ ] **IX-02: The simple score updates after answered questions**
  - **Action:** Submit answers for multiple questions in one lesson or quiz.
  - **Expected:** The displayed score updates after each submitted answer and reflects the number of correct answers.

- [ ] **IX-03: Course state visibly changes after completion**
  - **Action:** Complete one lesson or quiz and return to the course overview.
  - **Expected:** The completed item is visibly marked as completed, and the next available item is identifiable.

## Content
- [ ] **CT-01: Course content matches the selected language and level**
  - **Action:** Select a language and level, then inspect the displayed course title, lesson names, exercises, and quizzes.
  - **Expected:** All displayed content is relevant to the selected language and is grouped under the correct level.

- [ ] **CT-02: Different question formats are clearly presented**
  - **Action:** Navigate through the default course until each available question format is displayed.
  - **Expected:** Each question has clear instructions and distinguishable answer controls appropriate to its format.

- [ ] **CT-03: Progress summary values match completed lessons**
  - **Action:** Complete a known number of lessons, open the progress summary, and compare it with the course overview.
  - **Expected:** Completed, current, and remaining lesson counts or status labels match the actual course state.