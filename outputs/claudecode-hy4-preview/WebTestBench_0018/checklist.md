# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Open the site, enter the default account's email and password, click the "Sign In" button.
  - Expected: Sign-in succeeds and the dashboard loads showing access to workout logging, goals, workout timeline, and summary.

- [ ] FT-02: User can log a workout with all fields (type, intensity, duration, distance, notes)
  - Action: Open the "Log Workout" form, select an exercise type and intensity, enter a duration, distance and notes, then submit.
  - Expected: The workout is saved successfully and the entered values are retained (verified in the timeline entry).

- [ ] FT-03: Logged workout appears in the recent workouts timeline
  - Action: Log a workout (e.g., Running / High / 30 minutes / 5 km / "Morning run"), then view the timeline section.
  - Expected: A new timeline entry appears showing that date plus its exercise type, intensity, duration, distance and notes.

- [ ] FT-04: User can set a frequency goal such as "run three times a week"
  - Action: Open the Goals section, create a frequency goal: activity = Running, target = 3, period = per week, and save.
  - Expected: The goal is saved and displayed in the goals list with its activity (Running), target (3 times) and period (per week) visible.

- [ ] FT-05: User can set a minutes goal such as "exercise 150 minutes per week"
  - Action: Create a duration goal: target = 150 minutes, period = per week, and save.
  - Expected: The goal is saved and displayed in the goals list with its target (150 minutes) and period (per week) visible.

- [ ] FT-06: Weekly summary compares logged activity against weekly goals
  - Action: Count the current week's workouts from the timeline, then open the Summary view and select "This Week".
  - Expected: For each weekly goal, the summary shows the achieved amount (matching the timeline count/total for Mon–today), the target, and a status (Met / Not met) consistent with achieved vs. target.

- [ ] FT-07: Monthly summary compares logged activity against goals for the current month
  - Action: Sum the current calendar month's workouts from the timeline, then open the Summary view and select "This Month".
  - Expected: Each goal displays the achieved amount for the current month (matching the timeline total) beside its monthly target, with a status consistent with the displayed achieved vs. target values.

## Constraint
- [ ] CS-01: Workout form cannot be submitted with required fields left empty
  - Action: Open "Log Workout", leave exercise type and duration empty, and submit.
  - Expected: Submission is blocked and validation messages appear for the required fields; no workout is added to the timeline.

- [ ] CS-02: Duration and distance reject non-numeric or negative values
  - Action: Enter "-30" in Duration and "abc" in Distance, then submit.
  - Expected: Submission is blocked with validation errors on both fields; no workout is added to the timeline.

- [ ] CS-03: Goal cannot be saved without all required goal details
  - Action: Open the goal form and save it with the target amount left empty.
  - Expected: Saving is blocked with a validation message, and no blank/incomplete goal is added to the goals list.

- [ ] CS-04: Workouts logged outside the current week/month are excluded from current period totals
  - Action: Compare the "This Week" totals against the timeline entries dated within the current week only.
  - Expected: Summary totals exclude any workout dated before the current week's Monday (or in a future/other month for the month view).

- [ ] CS-05: Workout, goal, and summary pages require an active session
  - Action: Sign out (or clear the session) and try to open the workout logging, goals, or summary page directly.
  - Expected: Access is denied and the user is redirected to the sign-in screen instead of seeing the content.

## Interaction
- [ ] IX-01: Confirmation is shown and the form resets after logging a workout
  - Action: Submit a valid workout through the "Log Workout" form.
  - Expected: A success confirmation message appears and the form fields return to their empty/default state.

- [ ] IX-02: New goal appears immediately with confirmation after saving
  - Action: Save a new goal in the Goals section.
  - Expected: A success confirmation appears and the new goal is visible in the goals list without a page reload.

- [ ] IX-03: Timeline is ordered from most recent to oldest
  - Action: View the timeline containing multiple workouts with different dates.
  - Expected: The newest workout is listed first and entries progress in descending date order.

- [ ] IX-04: Switching the summary period updates the comparison displayed
  - Action: In the Summary view, click "This Week", then click "This Month".
  - Expected: The panel content changes to the corresponding period, and the selected period control is visually indicated as active.

## Content
- [ ] CT-01: Workout form fields are labelled with the required field names
  - Action: Open the "Log Workout" form and read all visible field labels.
  - Expected: Labels include exactly "Exercise Type", "Intensity", "Duration", "Distance" and "Notes".

- [ ] CT-02: Exercise type and intensity options are fitness-related
  - Action: Open the Exercise Type and Intensity dropdowns and review all options.
  - Expected: Every option is a fitness activity (e.g., Running, Cycling, Swimming, Strength) or intensity level (e.g., Low, Moderate, High) — no unrelated or "Option 1 / Test" placeholders.

- [ ] CT-03: Saved goals are displayed as readable, complete text
  - Action: Save a goal such as "run three times a week" and view it in the goals list and summary.
  - Expected: The goal reads as plain language (e.g., "Run 3 times per week" / "Exercise 150 minutes per week") with no raw identifiers or codes shown.

- [ ] CT-04: Page content is consistent with a fitness tracker and free of placeholder content
  - Action: Review page headings, navigation labels, and all displayed images/icons.
  - Expected: All text and imagery relate to fitness tracking and load correctly — no "Lorem ipsum", no broken images, no unrelated stock content.