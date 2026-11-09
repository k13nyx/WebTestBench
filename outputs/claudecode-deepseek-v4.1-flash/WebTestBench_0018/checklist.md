# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials and reach the workout dashboard
  - Action: Enter a valid username/email and password on the sign-in page, click "Sign In".
  - Expected: User is authenticated and the main dashboard (workout logging view) is displayed.
- [ ] FT-02: User can log a workout with all five fields populated
  - Action: Fill exercise type, intensity, duration, distance, and notes; click "Log Workout".
  - Expected: Workout is saved and a confirmation appears; no field errors are shown.
- [ ] FT-03: Newly logged workout appears in the recent workouts timeline
  - Action: Log a workout, then view the timeline.
  - Expected: The new workout appears as an entry in the timeline.
- [ ] FT-04: User can create a count-based goal (e.g., "run three times a week")
  - Action: Create a goal stating "run 3 times per week" and save it.
  - Expected: Goal is saved and listed among the user's active fitness goals.
- [ ] FT-05: User can create a duration-based goal (e.g., "exercise 150 minutes per week")
  - Action: Create a goal stating "exercise 150 minutes per week" and save it.
  - Expected: Goal is saved and listed among the user's active fitness goals.
- [ ] FT-06: Summary view compares logged activity against goals for the current week
  - Action: Log activity, then open the weekly summary view.
  - Expected: Weekly summary shows logged activity totals against each weekly goal.
- [ ] FT-07: Summary view compares logged activity against goals for the current month
  - Action: Open the monthly summary view.
  - Expected: Monthly summary shows logged activity totals against the applicable goals.
- [ ] FT-08: Timeline lists workouts in reverse-chronological order
  - Action: Log two workouts with different dates, then view the timeline.
  - Expected: The most recent workout is listed first.

## Constraint
- [ ] CS-01: Workout cannot be submitted with empty required fields
  - Action: Click "Log Workout" with the exercise type or duration left blank.
  - Expected: Submission is blocked and a required-field error is shown.
- [ ] CS-02: Numeric workout fields reject invalid values
  - Action: Enter a negative or non-numeric value for duration or distance.
  - Expected: Invalid input is rejected with an error; the workout is not saved.
- [ ] CS-03: Sign-in rejects invalid credentials
  - Action: Enter an incorrect password and click "Sign In".
  - Expected: Sign-in fails with an error message; the dashboard is not shown.
- [ ] CS-04: Goal cannot be saved without a target value and period
  - Action: Attempt to save a goal with a missing target (e.g., no number/period) .
  - Expected: Goal creation is blocked with a validation error.
- [ ] CS-05: Summary counts only activity within the current week/month
  - Action: Review the weekly summary when a workout exists in a prior week.
  - Expected: The prior-week workout is excluded from the current weekly totals.

## Interaction
- [ ] IX-01: Success message appears after a workout is logged
  - Action: Submit a valid workout.
  - Expected: A success confirmation/toast is displayed.
- [ ] IX-02: Summary view updates after a workout is logged
  - Action: Note summary totals, log a new workout, return to the summary.
  - Expected: Totals reflect the newly logged activity without a manual reload.
- [ ] IX-03: Goal progress visually distinguishes met vs. unmet goals
  - Action: Log activity such that one goal is met and another is not.
  - Expected: Met goal shows a distinct progress/complete state; unmet goal does not.

## Content
- [ ] CT-01: Exercise type field offers a relevant selection of exercises
  - Action: Open the exercise type dropdown when logging a workout.
  - Expected: Options are relevant fitness activities (e.g., run, cycle, swim) with no unrelated entries.
- [ ] CT-02: Summary and workout entries display correct measurement units
  - Action: View a logged workout and the summary view.
  - Expected: Duration is shown in minutes and distance in a labeled unit (km/mi) consistently.
- [ ] CT-03: Timeline entries display all logged workout details
  - Action: View a previously logged workout in the timeline.
  - Expected: Exercise type, intensity, duration, distance, and notes are all shown for that entry.