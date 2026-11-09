# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials and reach the main dashboard.
  - Action: Enter valid username and password, click "Sign In".
  - Expected: Sign-in succeeds and the dashboard (workout timeline / summary area) is displayed.
- [ ] FT-02: User can log a workout with all detail fields and save it.
  - Action: Open the workout log form, fill Exercise Type ("Running"), Intensity ("Medium"), Duration (30), Distance (5), Notes ("Morning run"), click "Save Workout".
  - Expected: The workout is saved and appears as a new entry in the recent workouts timeline.
- [ ] FT-03: Recent workouts timeline lists logged workouts in chronological order.
  - Action: View the recent workouts timeline after saving a workout.
  - Expected: The newly saved workout appears at the top of the timeline with older workouts ordered below it by date.
- [ ] FT-04: User can create a frequency-based goal such as "run three times a week".
  - Action: Open goal creation, enter goal "Run 3 times per week" with target 3 and period "week", click "Save Goal".
  - Expected: The goal is saved and displayed in the goals list with its target (3 times/week).
- [ ] FT-05: User can create a duration-based goal such as "exercise 150 minutes per week".
  - Action: Open goal creation, enter goal "Exercise 150 minutes per week" with target 150 minutes and period "week", click "Save Goal".
  - Expected: The goal is saved and displayed in the goals list with its target (150 minutes/week).
- [ ] FT-06: Summary view compares logged activity against goals for the current week.
  - Action: Open the Summary view and inspect the "This Week" section.
  - Expected: Each weekly goal shows the goal target and the actual logged total for the current week side by side (e.g., 1 of 3 runs, 30 of 150 minutes).
- [ ] FT-07: Summary view compares logged activity against goals for the current month.
  - Action: Open the Summary view and inspect the "This Month" section.
  - Expected: Each goal shows the goal target and the actual logged total for the current month side by side.
- [ ] FT-08: Logging a workout contributes to the matching goal's progress.
  - Action: Log a "Running" workout of 30 minutes, then open the Summary view.
  - Expected: The "Run 3 times per week" goal count and the weekly/monthly minute totals increase to include the new workout.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials.
  - Action: Enter a wrong password with a valid username, click "Sign In".
  - Expected: Sign-in fails, the user stays on the sign-in screen, and no dashboard data is shown.
- [ ] CS-02: A workout cannot be saved with missing required fields.
  - Action: Leave Exercise Type and Duration empty, click "Save Workout".
  - Expected: The workout is not saved and required-field errors are shown on the empty fields.
- [ ] CS-03: Numeric workout fields reject invalid values.
  - Action: Enter "-10" in Duration and "abc" in Distance, click "Save Workout".
  - Expected: The workout is not saved and errors indicate Duration and Distance must be valid positive numbers.
- [ ] CS-04: A goal cannot be saved with an empty name or non-positive target.
  - Action: Enter a blank goal name and target "0", click "Save Goal".
  - Expected: The goal is not saved and errors indicate a name and a target greater than zero are required.
- [ ] CS-05: Intensity only accepts the defined levels.
  - Action: Inspect the Intensity field options and attempt to submit a value outside them (e.g., "Extreme" typed into the field).
  - Expected: Only the defined intensity levels (e.g., Low / Medium / High) are selectable; any out-of-range value is rejected and the workout is not saved.

## Interaction
- [ ] IX-01: A success confirmation is shown after saving a workout or a goal.
  - Action: Save a workout, then save a goal.
  - Expected: Each save displays a visible success confirmation (e.g., "Workout logged" / "Goal saved") without reloading the page away from the current view.
- [ ] [ID IX-02]: The timeline updates immediately after a workout is logged.
  - Action: Log a workout and return to the recent workouts timeline without reloading the page.
  - Expected: The new workout entry appears in the timeline immediately after saving.
- [ ] IX-03: A clear error message is shown when sign-in fails.
  - Action: Submit invalid credentials on the sign-in screen.
  - Expected: An error message (e.g., "Invalid username or password") is displayed on the sign-in screen.
- [ ] IX-04: Validation errors are shown inline on invalid fields when saving a workout.
  - Action: Click "Save Workout" with empty required fields and invalid numbers.
  - Expected: Error messages appear directly next to each invalid field indicating what to correct.

## Content
- [ ] CT-01: The workout log form displays all required detail fields.
  - Action: Open the workout log form.
  - Expected: The form shows labeled fields for Exercise Type, Intensity, Duration, Distance, and Notes.
- [ ] CT-02: Timeline entries show the logged workout's details.
  - Action: Inspect a workout entry in the recent workouts timeline.
  - Expected: The entry displays the date, exercise type, intensity, duration, and distance (and notes when present) of that workout.
- [ ] CT-03: The Summary view shows both current-week and current-month comparisons.
  - Action: Open the Summary view.
  - Expected: The view contains distinct "This Week" and "This Month" sections, each listing goals alongside the corresponding logged totals.
- [ ] CT-04: Goal displays show the goal name and its target value.
  - Action: View the goals list in the Summary view.
  - Expected: Each goal shows its name and target as stated (e.g., "Run 3 times per week — 3", "Exercise 150 minutes per week — 150 min").