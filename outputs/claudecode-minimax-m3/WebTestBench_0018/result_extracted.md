# Test Result

## Functionality

- [X] FT-01: Sign in with valid default credentials
  - Action: Open the app, enter the default username/email and password in the Sign In form, click **Sign In**.
  - Expected: Login succeeds, the sign-in form is replaced by the signed-in app (Timeline/Goals/Summary are reachable), and the signed-in user is shown.

- [X] FT-02: Log a workout with all detail fields
  - Action: Open the Log Workout form; enter Exercise Type = "Running", Intensity = "High", Duration = 45, Distance = 8.5, Notes = "Felt strong"; click **Log Workout**.
  - Expected: The workout is saved with all five field values and a success confirmation is shown (no error message).

- [X] FT-03: Timeline lists recent workouts from default data
  - Action: Open the Timeline section.
  - Expected: A chronological list of recent workouts is displayed, with the most recently logged workout first, and each entry shows at least exercise type and date.

- [ ] FT-04: Create a count-based goal ("run three times a week")
  - Action: In the Goals section, choose a goal type of workouts/times per week, set the target to 3, and save the goal.
  - Expected: The goal is saved and listed with a target of 3 times per week and appears in the Summary view for the current week and month.
  - Bug Report:
    - Issue: Missing Monthly Summary View
    - Actual: The goal is created and listed correctly, and the Goals section shows the weekly progress (e.g., "3 / 3 times" with progress bar), but there is no separate or inline monthly summary view that compares goals against current-month activity. The page only exposes weekly progress for each goal, and "Your Stats" shows monthly totals (workouts/distance) without any goal comparison.

- [ ] FT-05: Create a duration-based goal ("exercise 150 minutes per week")
  - Action: In the Goals section, choose a goal type of exercise minutes per week, set the target to 150, and save the goal.
  - Expected: The goal is saved and listed with a target of 150 minutes per week and appears in the Summary view for the current week and month.
  - Bug Report:
    - Issue: Missing Monthly Summary View
    - Actual: The goal is created and listed correctly with weekly progress shown (e.g., "298 / 150 min" with "🎉 Goal achieved!"), but no monthly summary view exists for goal comparison.

- [X] FT-06: Summary compares current-week activity against goals
  - Action: Open the Summary view and locate the current-week section.
  - Expected: For each active goal the current week shows the target value, the amount actually logged this week, and a met/not-met status consistent with the logged data.

- [ ] FT-07: Summary compares current-month activity against goals
  - Action: Open the Summary view and locate the current-month section.
  - Expected: For each active goal the current month shows the target value, the amount actually logged this month, and a met/not-met status consistent with the logged data.
  - Bug Report:
    - Issue: No monthly goal comparison exists
    - Actual: There is no current-month section that shows goal target vs. actuals. The "Your Stats" cards show "This Month: 7 workouts" and "Total Distance: 43.2 km this month" but never compare these to any goal target or status. Goals are only tracked against the current week.

## Constraint

- [X] CS-01: Workout form cannot be submitted with required fields empty
  - Action: Open the Log Workout form, leave Exercise Type and Duration empty, fill only Notes, click **Log Workout**.
  - Expected: The workout is not saved, and a validation error is shown for each missing required field.

- [X] CS-02: Duration and Distance accept only valid non-negative numbers
  - Action: Submit a workout with Duration = "abc" and Distance = -5 (other fields valid).
  - Expected: The workout is not saved and an error identifies the invalid duration/distance entry.

- [X] CS-03: Unauthenticated access is blocked
  - Action: Sign out or open the app in a fresh browser session/incognito window and try to reach the Log Workout, Goals, and Summary pages directly.
  - Expected: The user is redirected to the Sign In form and no workout, goal, or summary data is displayed.

- [ ] CS-04: Invalid sign-in credentials are rejected
  - Action: Enter a wrong password with the default username/email and click **Sign In**.
  - Expected: Sign-in is refused, an error message is displayed, and no signed-in app view is shown.
  - Bug Report:
    - Issue: No credential validation
    - Actual: The app accepts any email/password combination (the Sign In screen itself states "Use any email and password to sign in"). Entering "alex@example.com" / "wrongpassword" successfully signed the user in with no error message — the dashboard, default workouts, and goals all loaded as if login were valid.

- [X] CS-05: Goal progress counts only matching workouts
  - Action: With the "3 times per week" goal from FT-04 active, log one workout of type "Running" and one of type "Cycling", then check the weekly run-count progress.
  - Expected: The run count increases by exactly 1 (the Running workout); the Cycling workout does not increment the run goal, while it does count toward the 150-minute goal.

## Interaction

- [X] IX-01: Successful workout submission shows a confirmation
  - Action: Log a valid workout as in FT-02.
  - Expected: A success/confirmation message or toast appears indicating the workout was saved, and the form resets or closes.

- [X] IX-02: Invalid input shows an inline error on the offending field
  - Action: Submit the Log Workout form with an empty Exercise Type (other fields valid).
  - Expected: An error message appears next to or associated with the Exercise Type field and the form stays open with the other entered values intact.

- [X] IX-03: Summary reflects a newly logged workout immediately
  - Action: Note the current week's minutes and run count in Summary, then log a 45-minute Running workout, then reopen/refresh the Summary view.
  - Expected: The current-week minutes increase by 45 and the run count increases by 1, without needing to log in again or reload the page from scratch.

- [ ] IX-04: Sections navigate without errors
  - Action: Use the navigation/tabs to move between Timeline, Goals, and Summary, and back again.
  - Expected: Each click switches the displayed content to that section, no error page or blank screen appears, and the current section is indicated as active.
  - Bug Report:
    - Issue: Missing section navigation
    - Actual: There are no tabs, links, or any other navigation controls between Timeline, Goals, and Summary. The page renders all sections ("Your Stats", "Recent Workouts", "Goals") in a single scrollable view; clicking any element cannot switch the displayed content to a different section. There is also no separate Summary view to navigate to.

## Content

- [X] CT-01: Logged workout displays the exact values entered
  - Action: Open the Timeline and inspect the entry for the workout logged in FT-02.
  - Expected: It shows Exercise Type "Running", Intensity "High", Duration 45, Distance 8.5, and Notes "Felt strong" — no field blank, truncated, or replaced by a generic label.

- [X] CT-02: Goals display their type and target clearly
  - Action: Open the Goals section and read the two goals created in FT-04 and FT-05.
  - Expected: One goal reads as running/workouts 3 times per week and the other as 150 minutes of exercise per week, with target numbers matching what was entered.

- [ ] CT-03: Summary headings and figures are correct and legible
  - Action: Read the Summary view end to end.
  - Expected: The current week and current month are each distinctly labelled, and each goal row shows a target figure, an actual logged figure, and a status; figures are numeric and consistent with the Timeline data.
  - Bug Report:
    - Issue: No monthly summary figures for goals
    - Actual: "Your Stats" shows clearly labeled "This Week" (workouts/duration) and "This Month" (workouts/distance) figures, and each weekly goal row shows a numeric target, an actual logged figure, and a status (progress bar + "🎉 Goal achieved!" where met). However, there is no monthly summary at all — no row, status, or progress figure for the current month against any goal, so the month portion of the summary is missing.

- [X] CT-04: Timeline entries show workout details with no placeholder content
  - Action: Read each entry in the Timeline list.
  - Expected: Every entry shows a date/time, exercise type, and duration (plus distance where applicable), all content is fitness-related, and no lorem-ipsum, "N/A" for provided values, or dummy text appears.
