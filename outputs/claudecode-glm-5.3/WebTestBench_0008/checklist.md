# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Navigate to the registration page, fill in username, email, and password with valid values, and click the "Register" (or "Sign Up") button.
  - Expected: Account is created, the user is logged in (or redirected to login), and subsequent login with the same credentials succeeds.

- [ ] FT-02: Challenge catalog displays predefined challenges
  - Action: Open the challenge catalog page.
  - Expected: A list of pre-existing programming challenges is displayed, each showing at least a title, difficulty level, and topic.

- [ ] FT-03: Catalog can be filtered by difficulty
  - Action: On the catalog page, apply a difficulty filter (e.g., "Easy").
  - Expected: Only challenges with the selected difficulty are shown; all displayed challenges are labeled with that difficulty.

- [ ] FT-04: Catalog can be filtered by topic
  - Action: On the catalog page, apply a topic filter (e.g., "Arrays").
  - Expected: Only challenges belonging to the selected topic are shown.

- [ ] FT-05: Challenge detail page shows description and embedded code editor
  - Action: Click any challenge title in the catalog.
  - Expected: A detail page opens showing the challenge description, the predefined test cases (or their count), and an embedded code editor ready for input.

- [ ] FT-06: User can submit a correct solution that passes all test cases
  - Action: Open a default challenge, type a known-correct solution into the embedded editor, and click "Submit".
  - Expected: The system runs the solution against the predefined test cases and displays a "Passed" (accepted) result.

- [ ] FT-07: User can submit an incorrect solution that fails test cases
  - Action: Open a default challenge, type a known-wrong solution (e.g., returns a wrong value), and click "Submit".
  - Expected: The system displays a "Failed" result indicating the solution did not pass the test cases, with basic feedback (e.g., which test case failed or expected vs. actual output).

- [ ] FT-08: Dashboard tracks progress after solving a challenge
  - Action: Solve one default challenge successfully, then open the personal dashboard.
  - Expected: The dashboard reflects the newly solved challenge in progress stats (e.g., solved count or completion percentage increases).

- [ ] FT-09: Dashboard shows statistics of challenges completed by difficulty
  - Action: Open the personal dashboard.
  - Expected: A breakdown of solved challenges per difficulty level (e.g., Easy / Medium / Hard counts) is displayed and matches the user's actual solved challenges.

- [ ] FT-10: User can review past submissions
  - Action: Open the submissions (submission history) page after having made at least one submission.
  - Expected: A list of past submissions is shown, each including at least the challenge name, submission time, and pass/fail result.

- [ ] FT-11: Leaderboard ranks users by earned points
  - Action: Open the leaderboard page after solving at least one challenge.
  - Expected: Users are listed with their earned points and ranked in descending order of points; the current user appears with points consistent with their solved challenges.

## Constraint
- [ ] CS-01: Registration cannot submit with empty required fields
  - Action: On the registration page, leave one or more required fields (username/email/password) empty and click "Register".
  - Expected: The account is not created and a validation message identifies the missing required fields.

- [ ] CS-02: Registration rejects duplicate credentials
  - Action: Attempt to register a new account using the username or email of an existing default user.
  - Expected: Registration is rejected with an error message indicating the username or email is already taken.

- [ ] CS-03: Code submission cannot be empty
  - Action: Open a challenge, leave the embedded editor empty, and click "Submit".
  - Expected: The submission is not executed and a message prompts the user to enter code before submitting.

- [ ] CS-04: Unauthenticated user cannot access personal pages
  - Action: While logged out, attempt to access the personal dashboard or submission history (e.g., by URL or navigation link).
  - Expected: Access is denied and the user is redirected to the login/registration page.

## Interaction
- [ ] IX-01: Submission result feedback appears after automatic test run
  - Action: Submit any solution from the challenge editor.
  - Expected: The page shows a running/evaluating state and then updates in place with the pass/fail outcome and basic feedback, without requiring a manual page reload.

- [ ] IX-02: Leaderboard updates after a challenge is solved
  - Action: Solve a default challenge successfully, then navigate to the leaderboard.
  - Expected: The current user's points and rank on the leaderboard increase to reflect the newly solved challenge.

## Content
- [ ] CT-01: Challenge content is relevant to programming topics
  - Action: Browse the catalog and open at least two different challenges.
  - Expected: Each challenge's title, description, and test cases are clearly a programming task consistent with its labeled topic and difficulty (no off-theme or placeholder content).

- [ ] CT-02: Difficulty labels on challenges are valid values
  - Action: Inspect all challenges in the catalog and on their detail pages.
  - Expected: Every challenge displays exactly one difficulty from the expected set (e.g., Easy, Medium, Hard) — no missing, misspelled, or contradictory labels.