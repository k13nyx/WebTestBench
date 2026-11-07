# Test Result

## Functionality

- [X] FT-01: User can sign in with valid credentials
  - Action: Open the site, enter the default account's email and password, click the "Sign In" button.
  - Expected: Sign-in succeeds and the dashboard loads showing access to workout logging, goals, workout timeline, and summary.

- [X] FT-02: User can log a workout with all fields (type, intensity, duration, distance, notes)
  - Action: Open the "Log Workout" form, select an exercise type and intensity, enter a duration, distance and notes, then submit.
  - Expected: The workout is saved successfully and the entered values are retained (verified in the timeline entry).

- [X] FT-03: Logged workout appears in the recent workouts timeline
  - Action: Log a workout (e.g., Running / High / 30 minutes / 5 km / "Morning run"), then view the timeline section.
  - Expected: A new timeline entry appears showing that date plus its exercise type, intensity, duration, distance and notes.

- [X] FT-04: User can set a frequency goal such as "run three times a week"
  - Action: Open the Goals section, create a frequency goal: activity = Running, target = 3, period = per week, and save.
  - Expected: The goal is saved and displayed in the goals list with its activity (Running), target (3 times) and period (per week) visible.

- [X] FT-05: User can set a minutes goal such as "exercise 150 minutes per week"
  - Action: Create a duration goal: target = 150 minutes, period = per week, and save.
  - Expected: The goal is saved and displayed in the goals list with its target (150 minutes) and period (per week) visible.

- [ ] FT-06: Weekly summary compares logged activity against weekly goals
  - Action: Count the current week's workouts from the timeline, then open the Summary view and select "This Week".
  - Expected: For each weekly goal, the summary shows the achieved amount (matching the timeline count/total for Mon–today), the target, and a status (Met / Not met) consistent with achieved vs. target.
  - Bug Report:
    - Issue: Missing summary period view and missing "Not met" status
    - Actual: No "Summary view" with a period selector exists — the dashboard has only two buttons ("Log Workout", "Add Goal"); "This Week" and "This Month" are static labels on the stat cards, not selectable controls, so the action "open the Summary view and select 'This Week'" cannot be performed. The Goals panel does show achieved vs. target correctly (e.g., "Exercise 150 minutes per week … 278 / 150 min", "Run 3 times a week … 4 / 3 times", matching the timeline's 7 workouts / 278 minutes for Mon Nov 2–today), and met goals show "🎉 Goal achieved!", but unmet goals show no status at all: "Strength training twice a week … 1 / 2 times" displays only a progress bar with no "Not met" indicator.

- [ ] FT-07: Monthly summary compares logged activity against goals for the current month
  - Action: Sum the current calendar month's workouts from the timeline, then open the Summary view and select "This Month".
  - Expected: Each goal displays the achieved amount for the current month (matching the timeline total) beside its monthly target, with a status consistent with the displayed achieved vs. target values.
  - Bug Report:
    - Issue: No monthly comparison view; weekly goals never show current-month figures
    - Actual: There is no Summary view with a "This Month" control to select (the whole dashboard exposes only the "Log Workout" and "Add Goal" buttons; "This Month" is a static stat-card label). Every weekly goal keeps displaying week-scoped numbers regardless of any month selection — "Exercise 150 minutes per week … 278 / 150 min" and "Run 3 times a week … 4 / 3 times" while the current month total is 8 workouts / 320 minutes. Only a goal explicitly created with Period = Month is scoped to the month (a test goal "Exercise 300 minutes per month" correctly showed "320 / 300 min"), so existing/weekly goals cannot be compared against a monthly target.

## Constraint

- [X] CS-01: Workout form cannot be submitted with required fields left empty
  - Action: Open "Log Workout", leave exercise type and duration empty, and submit.
  - Expected: Submission is blocked and validation messages appear for the required fields; no workout is added to the timeline.

- [ ] CS-02: Duration and distance reject non-numeric or negative values
  - Action: Enter "-30" in Duration and "abc" in Distance, then submit.
  - Expected: Submission is blocked with validation errors on both fields; no workout is added to the timeline.
  - Bug Report:
    - Issue: Distance field does not reject non-numeric input
    - Actual: Duration "-30" is correctly blocked (number input, min="1" → native message "Value must be greater than or equal to 1."), but Distance accepts non-numeric text silently: typing "abc" into the Distance field leaves it empty with `checkValidity() === true` and no validation message, and submitting with Duration "25" + Distance "abc" succeeded ("Workout logged!"), adding a tenth timeline entry ("Running … Moderate … 25 min") with no distance value. No error is reported for the Distance field.

- [X] CS-03: Goal cannot be saved without all required goal details
  - Action: Open the goal form and save it with the target amount left empty.
  - Expected: Saving is blocked with a validation message, and no blank/incomplete goal is added to the goals list.

- [X] CS-04: Workouts logged outside the current week/month are excluded from current period totals
  - Action: Compare the "This Week" totals against the timeline entries dated within the current week only.
  - Expected: Summary totals exclude any workout dated before the current week's Monday (or in a future/other month for the month view).

- [X] CS-05: Workout, goal, and summary pages require an active session
  - Action: Sign out (or clear the session) and try to open the workout logging, goals, or summary page directly.
  - Expected: Access is denied and the user is redirected to the sign-in screen instead of seeing the content.

## Interaction

- [X] IX-01: Confirmation is shown and the form resets after logging a workout
  - Action: Submit a valid workout through the "Log Workout" form.
  - Expected: A success confirmation message appears and the form fields return to their empty/default state.

- [X] IX-02: New goal appears immediately with confirmation after saving
  - Action: Save a new goal in the Goals section.
  - Expected: A success confirmation appears and the new goal is visible in the goals list without a page reload.

- [ ] IX-03: Timeline is ordered from most recent to oldest
  - Action: View the timeline containing multiple workouts with different dates.
  - Expected: The newest workout is listed first and entries progress in descending date order.
  - Bug Report:
    - Issue: Newly logged workout is inserted at the top regardless of its date
    - Actual: After logging two workouts (default form date 2026-11-07, while the browser's current date is 2026-11-08), the timeline reads: "Running — Yesterday — 25 min", "Running — Yesterday — High — 30 min", "Running — Today — 35 min", "Weight Training — Yesterday — 55 min", then "Nov 6, Nov 5, Nov 3, Nov 1, Oct 31, Oct 29". The newest entry ("Today", Nov 8) is listed third, behind two Nov 7 entries, so the list is not in descending date order. Contributing detail: the Date field defaults to the UTC date (2026-11-07) instead of the local date (2026-11-08).

- [ ] IX-04: Switching the summary period updates the comparison displayed
  - Action: In the Summary view, click "This Week", then click "This Month".
  - Expected: The panel content changes to the corresponding period, and the selected period control is visually indicated as active.
  - Bug Report:
    - Issue: No period-switch control exists in the summary
    - Actual: The dashboard contains no summary period toggle. "This Week" and "This Month" are plain labels of two static stat cards ("This Week 7 workouts", "This Month 8 workouts"); the only clickable controls anywhere on the page are "Log Workout", "Add Goal", the per-card delete icons, and the sign-out icon. Clicking the "This Week"/"This Month" text does nothing, so the panel cannot change period and no control can be visually indicated as active.

## Content

- [X] CT-01: Workout form fields are labelled with the required field names
  - Action: Open the "Log Workout" form and read all visible field labels.
  - Expected: Labels include exactly "Exercise Type", "Intensity", "Duration", "Distance" and "Notes".

- [X] CT-02: Exercise type and intensity options are fitness-related
  - Action: Open the Exercise Type and Intensity dropdowns and review all options.
  - Expected: Every option is a fitness activity (e.g., Running, Cycling, Swimming, Strength) or intensity level (e.g., Low, Moderate, High) — no unrelated or "Option 1 / Test" placeholders.

- [X] CT-03: Saved goals are displayed as readable, complete text
  - Action: Save a goal such as "run three times a week" and view it in the goals list and summary.
  - Expected: The goal reads as plain language (e.g., "Run 3 times per week" / "Exercise 150 minutes per week") with no raw identifiers or codes shown.

- [X] CT-04: Page content is consistent with a fitness tracker and free of placeholder content
  - Action: Review page headings, navigation labels, and all displayed images/icons.
  - Expected: All text and imagery relate to fitness tracking and load correctly — no "Lorem ipsum", no broken images, no unrelated stock content.
