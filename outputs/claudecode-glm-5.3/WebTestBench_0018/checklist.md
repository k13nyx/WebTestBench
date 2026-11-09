# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Enter valid email/username and password on the sign-in form and click the "Sign In" button.
  - Expected: Sign-in succeeds and the user is taken to the main fitness tracker page (dashboard/workouts view); the user's data is visible.

- [ ] FT-02: User can log a workout with all detail fields
  - Action: Open the "Log Workout" form, fill in Exercise Type (e.g., "Running"), Intensity, Duration, Distance, and Notes, then submit.
  - Expected: Workout is saved and the confirmation reflects all entered values; no data loss in any of the five fields.

- [ ] FT-03: Logged workout appears in the recent workouts timeline
  - Action: After submitting a new workout, view the timeline section.
  - Expected: The newly logged workout appears in the timeline with its date and details.

- [ ] FT-04: Timeline lists workouts in reverse chronological order
  - Action: Compare the dates of the workouts shown in the recent workouts timeline (using default data plus any newly logged workout).
  - Expected: Most recent workout is listed first; older workouts follow in descending date order.

- [ ] FT-05: User can create a frequency-based goal ("run three times a week")
  - Action: In the goals section, create a goal equivalent to "Run three times a week" (activity "Run", target "3 times per week") and save it.
  - Expected: Goal is saved and displayed in the active goals list.

- [ ] FT-06: User can create a duration-based goal ("exercise 150 minutes per week")
  - Action: In the goals section, create a goal equivalent to "Exercise 150 minutes per week" (target "150 minutes per week") and save it.
  - Expected: Goal is saved and displayed in the active goals list.

- [ ] FT-07: Weekly summary compares logged activity against weekly goals
  - Action: Open the summary view for the current week.
  - Expected: Summary shows total logged activity for the current week side-by-side with each weekly goal's target (e.g., workouts count vs "3 times", minutes vs "150 minutes").

- [ ] FT-08: Monthly summary compares logged activity against goals for the current month
  - Action: Open the summary view for the current month.
  - Expected: Summary shows total logged activity for the current month compared against the monthly goal targets, including progress toward (or achievement of) each goal.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials
  - Action: Enter a wrong password (or unregistered email) on the sign-in form and click "Sign In".
  - Expected: Sign-in fails; the user remains on the sign-in page and an error message is shown; no user data is exposed.

- [ ] FT-09: Workouts page is inaccessible without signing in
  - Action: While signed out, attempt to open the workouts/dashboard page directly (e.g., via its menu link or URL).
  - Expected: User is not shown workout data; they are redirected to (or prompted with) the sign-in screen.

- [ ] CS-02: Workout form rejects empty required fields
  - Action: Open the "Log Workout" form and click the submit button without filling in required fields (e.g., exercise type, duration).
  - Expected: Form is not submitted; a validation message identifies the missing required fields.

- [ ] CS-03: Workout form rejects invalid numeric values
  - Action: In the "Log Workout" form, enter an invalid Duration (e.g., 0, negative, or non-numeric text) and submit.
  - Expected: Workout is not saved; a validation error for the invalid duration value is displayed.

- [ ] CS-04: Goal cannot be saved without required target parameters
  - Action: Open the goal-creation form and click save without selecting an activity or entering a target (e.g., blank times-per-week or minutes-per-week value).
  - Expected: Goal is not created; the form indicates which goal parameters are missing.

## Interaction
- [ ] IX-01: Success confirmation appears after a workout is logged
  - Action: Submit a fully filled, valid "Log Workout" form.
  - Expected: A visible success message (toast/banner) confirms the workout was logged, and it disappears or can be dismissed without breaking the page.

- [ ] IX-02: Inline error feedback appears when goal creation fails
  - Action: Attempt to save an invalid goal (see CS-04) and observe the goal form.
  - Expected: Error feedback appears near the relevant goal form field, and the form retains the user's other entered values.

- [ ] IX-03: Timeline entries respond to user interaction
  - Action: Click (or hover) a workout entry in the recent workouts timeline.
  - Expected: The entry visibly responds — e.g., expands or highlights to show full details including notes — confirming the timeline is interactive, not static.

- [ ] IX-04: Summary updates immediately after a new workout is logged
  - Action: Note the current weekly summary numbers, log one additional workout (e.g., a 30-minute run), then reopen the weekly summary without reloading.
  - Expected: Weekly totals and goal progress in the summary increase to reflect the new workout (e.g., +30 minutes toward the 150-minute goal).

## Content
- [ ] CT-01: Timeline entries display all five workout detail fields
  - Action: Inspect the entries in the recent workouts timeline (using default data).
  - Expected: Each entry shows its exercise type, intensity, duration, and distance, with notes visible (directly or on expand); values match what was logged.

- [ ] CT-02: All page labels and content are relevant to fitness tracking
  - Action: Review headings, form labels, buttons, and menu items across the sign-in, workout logging, goals, timeline, and summary views.
  - Expected: All text is fitness-tracker themed (e.g., "Log Workout", "Goals", "Weekly Summary") with no placeholder text, misspellings, or unrelated content.

- [ ] CT-03: Summary numbers are accurate and consistent with logged workouts
  - Action: Cross-check the weekly summary totals (workout count and total minutes) against the workouts shown in the timeline for the current week (default data).
  - Expected: Summary counts and minutes exactly match the timeline workouts for that week — no inflated, missing, or mismatched totals.