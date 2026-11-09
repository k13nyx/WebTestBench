# Test Result

## Functionality
- [X] FT-01: User can sign in and reach the main app view
  - Action: Open the app, enter valid credentials in the sign-in form (e.g., email + password), and submit.
  - Expected: User is authenticated and lands on the main view showing workouts/goals/summary, with a signed-in indicator (user name or "Sign Out" control) visible.

- [X] FT-02: User can log a workout with all detail fields
  - Action: Open the "Log Workout" form, enter exercise type ("Running"), intensity ("Moderate"), duration ("30 min"), distance ("5 km"), and notes ("Morning run"), then submit.
  - Expected: The workout is saved and the form closes/resets.

- [X] FT-03: Logged workouts appear in the recent-workouts timeline
  - Action: After logging the FT-02 workout, view the timeline section.
  - Expected: The workout appears as a timeline entry, with the most recent entry listed first.

- [X] FT-04: User can create a fitness goal
  - Action: Open the goal form and create a goal such as "Run 3 times per week" (target value + period), then submit.
  - Expected: The goal is saved and listed in the goals section.

- [X] FT-05: Weekly summary compares logged activity against goals
  - Action: Open the summary view and select the current week.
  - Expected: Each weekly goal shows logged-vs-target progress for this week (e.g., "2/3 runs", "90/150 min"), computed from workouts dated in the current week.

- [ ] FT-06: Monthly summary compares logged activity against goals
  - Action: Switch the summary view to the current month.
  - Expected: Progress values change to month-to-date totals (e.g., "8/12 runs", "420/600 min"), computed from workouts in the current month.
  - Bug Report:
    - Issue: Missing Feature — no month-level goal comparison
    - Actual: There is no way to switch the summary to the current month. Goal progress always shows weekly-only values ("3 / 3 times", "253 / 150 min", "1 / 2 times", labeled "weekly goal"). Month figures exist only as raw stat tiles ("This Month: 7 workouts", "Total Distance: 46.7 km this month") with no logged-vs-target comparison. A dedicated summary route (/summary) returns a 404 "Oops! Page not found" page.

## Constraint
- [ ] CS-01: Invalid credentials are rejected at sign-in
  - Action: Submit the sign-in form with a wrong password or unknown account.
  - Expected: A visible error message appears and protected views remain inaccessible.
  - Bug Report:
    - Issue: No credential validation — invalid sign-in accepted
    - Actual: Submitting unknown account `unknown.account@example.com` / `wrongpassword` produced no error message and navigated directly into the protected main view (stats, workouts, goals). The sign-in page itself states "Use any email and password to sign in", so no login rejection path exists.

- [X] CS-02: Workout cannot be saved with missing required fields
  - Action: Submit the log-workout form with exercise type and duration empty.
  - Expected: Submission is blocked with inline validation errors, and no new timeline entry is created.

- [X] CS-03: Invalid numeric values are rejected
  - Action: Enter a negative or non-numeric duration or distance (e.g., "-5" or "abc").
  - Expected: A validation error is shown and the workout is not saved.

- [X] CS-04: App data is not accessible without signing in
  - Action: With a signed-out session, navigate directly to the timeline/summary/goals view (URL or reload).
  - Expected: The user is redirected to the sign-in screen; no workouts or goals are visible.

## Interaction
- [X] IX-01: Success feedback shown after logging a workout
  - Action: Successfully submit a valid workout form.
  - Expected: A confirmation appears (e.g., toast or "Workout logged" message) and the form closes/resets.

- [X] IX-02: Timeline and goal list update without a page reload
  - Action: Log a workout or create a goal while staying on the page.
  - Expected: The timeline/goals section updates immediately to include the new entry without a browser refresh.

- [ ] IX-03: Period switcher changes the summary comparison
  - Action: Toggle the summary view between "Week" and "Month".
  - Expected: The displayed actual-vs-target values update to match the selected period.
  - Bug Report:
    - Issue: Missing UI control — no Week/Month period switcher
    - Actual: A full DOM scan of buttons/text found no Week/Month toggle or tabs anywhere; the only controls are "Log Workout", "Add Goal", dialog buttons, card delete icons, and the header sign-out icon. Goal actual-vs-target values are fixed to the week and never update to a monthly period.

- [X] IX-04: Sign out returns to the sign-in screen
  - Action: Click "Sign Out".
  - Expected: The app shows the sign-in screen and previous workout/goal data is no longer displayed.

## Content
- [X] CT-01: Timeline entries display the full logged workout details
  - Action: View a timeline entry created with all fields filled.
  - Expected: The entry shows date/time, exercise type, intensity, duration, distance, and notes exactly as entered.

- [X] CT-02: Goals display their target, unit, and period
  - Action: View the goals list and summary labels.
  - Expected: Each goal shows its name with target and period matching what was created (e.g., "Run — 3 per week", "Exercise — 150 min/week").

- [X] CT-03: Content is fitness-relevant and unit-consistent
  - Action: Inspect form labels, timeline entries, and summary text.
  - Expected: Labels/units are appropriate and consistent (e.g., "Intensity", duration in minutes, distance in km or mi); no lorem ipsum, template placeholders, or off-topic text.

- [X] CT-04: Default data is present on first sign-in
  - Action: Sign in without adding any data.
  - Expected: At least one pre-existing workout appears in the timeline and at least one pre-existing goal is listed, so the summary renders with real values.
