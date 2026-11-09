All tests are complete. **FT-05** passed: "Exercise 150 minutes per week" goal created and displayed with "253 / 150 min" target, with "Goal created!" toast. Here is the full checklist with updated statuses:

# Test Result

## Functionality
- [X] FT-01: User can sign in with valid credentials and reach the main dashboard.
  - Action: Enter valid username and password, click "Sign In".
  - Expected: Sign-in succeeds and the dashboard (workout timeline / summary area) is displayed.
- [X] FT-02: User can log a workout with all detail fields and save it.
  - Action: Open the workout log form, fill Exercise Type ("Running"), Intensity ("Medium"), Duration (30), Distance (5), Notes ("Morning run"), click "Save Workout".
  - Expected: The workout is saved and appears as a new entry in the recent workouts timeline.
- [X] FT-03: Recent workouts timeline lists logged workouts in chronological order.
  - Action: View the recent workouts timeline after saving a workout.
  - Expected: The newly saved workout appears at the top of the timeline with older workouts ordered below it by date.
- [X] FT-04: User can create a frequency-based goal such as "run three times a week".
  - Action: Open goal creation, enter goal "Run 3 times per week" with target 3 and period "week", click "Save Goal".
  - Expected: The goal is saved and displayed in the goals list with its target (3 times/week).
- [X] FT-05: User can create a duration-based goal such as "exercise 150 minutes per week".
  - Action: Open goal creation, enter goal "Exercise 150 minutes per week" with target 150 minutes and period "week", click "Save Goal".
  - Expected: The goal is saved and displayed in the goals list with its target (150 minutes/week).
- [X] FT-06: Summary view compares logged activity against goals for the current week.
  - Action: Open the Summary view and inspect the "This Week" section.
  - Expected: Each weekly goal shows the goal target and the actual logged total for the current week side by side (e.g., 1 of 3 runs, 30 of 150 minutes).
- [ ] FT-07: Summary view compares logged activity against goals for the current month.
  - Action: Open the Summary view and inspect the "This Month" section.
  - Expected: Each goal shows the goal target and the actual logged total for the current month side by side.
  - Bug Report:
    - Issue: Missing monthly goal-vs-actual comparison in summary
    - Actual: The "This Month" area shows only aggregate stats ("This Month: 7 workouts", "Total Distance 46.7 km this month"). Every goal card is labeled "Weekly Goal" and shows only weekly progress ("Progress 3 / 3 times", "Progress 253 / 150 min"); no goal anywhere displays its target against the logged total for the current month.
- [X] FT-08: Logging a workout contributes to the matching goal's progress.
  - Action: Log a "Running" workout of 30 minutes, then open the Summary view.
  - Expected: The "Run 3 times per week" goal count and the weekly/monthly minute totals increase to include the new workout.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials.
  - Action: Enter a wrong password with a valid username, click "Sign In".
  - Expected: Sign-in fails, the user stays on the sign-in screen, and no dashboard data is shown.
  - Bug Report:
    - Issue: Invalid credentials accepted (missing credential validation)
    - Actual: Signing in with "alex@example.com" and wrong password "wrongpassword123" succeeds and the dashboard with workout/goal data is displayed. The form states "Use any email and password to sign in" — any non-empty credentials are accepted; the user is never kept on the sign-in screen.
- [ ] CS-02: A workout cannot be saved with missing required fields.
  - Action: Leave Exercise Type and Duration empty, click "Save Workout".
  - Expected: The workout is not saved and required-field errors are shown on the empty fields.
  - Bug Report:
    - Issue: Missing required-field error display / required state not testable on Exercise Type
    - Actual: Clicking "Save Workout" with empty fields blocks the save, but the page renders no error message at all (dialog contains no error text); only the browser-native tooltip "Please fill out this field." is attached to the empty required Duration field (input `:invalid`, validationMessage "Please fill out this field."). Exercise Type cannot be left empty — it is a preselected dropdown ("Running", no empty option) — so no required-field error is ever shown for it.
- [ ] CS-03: Numeric workout fields reject invalid values.
  - Action: Enter "-10" in Duration and "abc" in Distance, click "Save Workout".
  - Expected: The workout is not saved and errors indicate Duration and Distance must be valid positive numbers.
  - Bug Report:
    - Issue: No validation error for invalid numeric input; non-numeric text silently discarded
    - Actual: "-10" in Duration is stopped only by native HTML5 `min=1` validation (validationMessage "Value must be greater than or equal to 1."); "abc" cannot be entered into the numeric Distance input at all — the keystrokes are silently filtered, the field stays empty and shows no error. After clicking "Save Workout" no error text exists in the dialog indicating Duration and Distance must be valid positive numbers (Distance gets no feedback of any kind).
- [ ] CS-04: A goal cannot be saved with an empty name or non-positive target.
  - Action: Enter a blank goal name and target "0", click "Save Goal".
  - Expected: The goal is not saved and errors indicate a name and a target greater than zero are required.
  - Bug Report:
    - Issue: Missing goal name field and name validation
    - Actual: The "New Goal" dialog contains only Goal Type, Exercise Type, Target and Period — there is no goal name input (names are auto-generated), so a blank name cannot be entered and no error can indicate a name is required. Target "0" is blocked only by native `min=1` validation ("Value must be greater than or equal to 1.") with no in-page error message; the dialog's submit button is labeled "Create Goal" (no "Save Goal").
- [X] CS-05: Intensity only accepts the defined levels.
  - Action: Inspect the Intensity field options and attempt to submit a value outside them (e.g., "Extreme" typed into the field).
  - Expected: Only the defined intensity levels (e.g., Low / Medium / High) are selectable; any out-of-range value is rejected and the workout is not saved.

## Interaction
- [X] IX-01: A success confirmation is shown after saving a workout or a goal.
  - Action: Save a workout, then save a goal.
  - Expected: Each save displays a visible success confirmation (e.g., "Workout logged" / "Goal saved") without reloading the page away from the current view.
- [X] [ID IX-02]: The timeline updates immediately after a workout is logged.
  - Action: Log a workout and return to the recent workouts timeline without reloading the page.
  - Expected: The new workout entry appears in the timeline immediately after saving.
- [ ] IX-03: A clear error message is shown when sign-in fails.
  - Action: Submit invalid credentials on the sign-in screen.
  - Expected: An error message (e.g., "Invalid username or password") is displayed on the sign-in screen.
  - Bug Report:
    - Issue: Missing invalid-credentials error message
    - Actual: Submitting invalid credentials ("alex@example.com" + "wrongpassword123") does not fail and no error message is displayed — sign-in proceeds straight to the dashboard. No "Invalid username or password" message ever appears; the only sign-in error in the app is "Please enter both email and password" (empty fields).
- [ ] IX-04: Validation errors are shown inline on invalid fields when saving a workout.
  - Action: Click "Save Workout" with empty required fields and invalid numbers.
  - Expected: Error messages appear directly next to each invalid field indicating what to correct.
  - Bug Report:
    - Issue: Missing inline validation error messages on workout form fields
    - Actual: After clicking "Save Workout" with empty required fields and invalid numbers, the dialog renders no error message elements next to any field (no error text in the DOM). Duration is flagged only by the browser-native tooltip ("Please fill out this field." / "Value must be greater than or equal to 1."), and the Distance field shows no error at all even after "abc" was entered — errors are not shown next to each invalid field.

## Content
- [X] CT-01: The workout log form displays all required detail fields.
  - Action: Open the workout log form.
  - Expected: The form shows labeled fields for Exercise Type, Intensity, Duration, Distance, and Notes.
- [X] CT-02: Timeline entries show the logged workout's details.
  - Action: Inspect a workout entry in the recent workouts timeline.
  - Expected: The entry displays the date, exercise type, intensity, duration, and distance (and notes when present) of that workout.
- [ ] CT-03: The Summary view shows both current-week and current-month comparisons.
  - Action: Open the Summary view.
  - Expected: The view contains distinct "This Week" and "This Month" sections, each listing goals alongside the corresponding logged totals.
  - Bug Report:
    - Issue: Missing "This Week" / "This Month" goal-comparison sections
    - Actual: "This Week" and "This Month" appear only as aggregate stat cards ("This Week: 6 workouts", "Week Duration: 253 minutes", "This Month: 7 workouts", "Total Distance: 46.7 km this month") that list no goals. Goals are shown in a separate "Goals" panel with weekly-only progress ("Weekly Goal — Progress 3 / 3 times", "253 / 150 min"); no section lists goals alongside the corresponding week/month logged totals.
- [X] CT-04: Goal displays show the goal name and its target value.
  - Action: View the goals list in the Summary view.
  - Expected: Each goal shows its name and target as stated (e.g., "Run 3 times per week — 3", "Exercise 150 minutes per week — 150 min").