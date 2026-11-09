# Test Result

## Functionality

- [X] FT-01: User can sign in with a valid pre-existing account
  - Action: Enter valid default account credentials and select **“Sign In.”**
  - Expected: The user is authenticated and taken to the fitness tracker dashboard.

- [X] FT-02: User can log a complete workout
  - Action: Open **“Log Workout,”** select an **Exercise Type**, choose an **Intensity**, enter **Duration**, enter **Distance**, add **Notes**, and select **“Save Workout.”**
  - Expected: The workout is saved and includes every entered field.

- [X] FT-03: User can set a workout-frequency goal
  - Action: Open **“Goals,”** create or select a goal with the target **“Run three times a week,”** and save it.
  - Expected: The goal is displayed in the user’s goals list with its weekly frequency target.

- [X] FT-04: User can set a weekly-duration goal
  - Action: Create or select a goal with the target **“Exercise 150 minutes per week”** and save it.
  - Expected: The goal is displayed with a 150-minute weekly target.

- [X] FT-05: User can view recent workouts in a timeline
  - Action: Navigate to the **“Recent Workouts”** or **“Timeline”** view after a workout is present.
  - Expected: Workouts appear in timeline order with their exercise type, intensity, duration, distance, notes, and workout date.

- [ ] FT-06: User can view activity compared with goals
  - Action: Open the **“Summary”** view and inspect both the **Current Week** and **Current Month** sections.
  - Expected: The summary shows logged activity and compares it with the configured goals for each period.
  - Bug Report:
    - Issue: Missing Summary view
    - Actual: The dashboard contains no **“Summary”** control or **Current Week/Current Month** comparison sections. It only displays dashboard statistics and goal progress cards.

- [ ] FT-07: Logged workout data is retained when revisiting the dashboard
  - Action: Save a valid workout, navigate away from the dashboard, then return to **“Recent Workouts.”**
  - Expected: The saved workout remains visible with the same field values.
  - Bug Report:
    - Issue: Workout data is not retained after revisiting
    - Actual: After saving the Cycling workout and leaving the dashboard through the account/sign-in flow, signing in again restored the original workout list; the saved **“QA workout entry”** workout was no longer visible.

## Constraint

- [ ] CS-01: Required workout fields prevent incomplete submissions
  - Action: Open **“Log Workout,”** leave one or more required fields empty, and select **“Save Workout.”**
  - Expected: The workout is not saved, and each missing required field is identified for correction.
  - Bug Report:
    - Issue: Missing required-field feedback
    - Actual: The incomplete workout was not saved and the dialog remained open, but no visible validation message identified the missing fields for correction.

- [X] CS-02: Workout numeric fields accept only valid numeric values
  - Action: Enter non-numeric, negative, or otherwise invalid values in **Duration** and **Distance**, then attempt to save.
  - Expected: The form rejects each invalid value and does not create a workout.

- [ ] CS-03: Goal targets cannot be saved without a valid target
  - Action: In **“Goals,”** attempt to save a goal with an empty, zero, negative, or non-numeric target.
  - Expected: The goal is not saved, and the invalid target is identified for correction.
  - Bug Report:
    - Issue: Missing invalid-target feedback
    - Actual: Empty and zero targets left the dialog open and did not create a goal, but no visible validation message identified the invalid target for correction.

- [ ] CS-04: Invalid sign-in credentials do not authenticate the user
  - Action: Enter an invalid email, username, or password and select **“Sign In.”**
  - Expected: The user remains signed out and receives a clear invalid-credentials error.
  - Bug Report:
    - Issue: Invalid credentials are accepted
    - Actual: Signing in with `invalid@example.com` and `wrong` authenticated the user and displayed the fitness tracker dashboard instead of showing an invalid-credentials error.

- [ ] CS-05: Summary calculations use only workouts in the selected period
  - Action: Compare the **Current Week** and **Current Month** summary totals with the dates of the workouts shown in the timeline.
  - Expected: Weekly totals include only workouts from the current week, and monthly totals include only workouts from the current month.
  - Bug Report:
    - Issue: Missing period-based summary
    - Actual: No Summary view or Current Week/Current Month comparison controls are available, so period-specific calculations cannot be inspected.

## Interaction

- [X] IX-01: Workout save provides visible completion feedback
  - Action: Save a valid workout.
  - Expected: The interface visibly confirms that the workout was saved and updates the relevant workout view without requiring a page refresh.

- [ ] IX-02: Goal save updates the goals and summary views
  - Action: Save a valid goal, then open or refresh **“Summary.”**
  - Expected: The new goal appears in the goals list and is reflected in the applicable current-week or current-month comparison.
  - Bug Report:
    - Issue: Missing Summary view
    - Actual: The new goal appeared in the goals list with progress, but there is no **“Summary”** view or current-week/current-month comparison to update.

- [ ] IX-03: Summary period controls update displayed data
  - Action: Switch between **“Current Week”** and **“Current Month”** in the summary.
  - Expected: The selected period is visibly indicated, and the activity totals and goal comparison update to match that period.
  - Bug Report:
    - Issue: Missing summary period controls
    - Actual: No Summary view or **“Current Week”**/**“Current Month”** controls are present.

## Content

- [ ] CT-01: Workout timeline presents complete and relevant workout information
  - Action: Review each workout entry in **“Recent Workouts”** or **“Timeline.”**
  - Expected: Every entry displays readable, accurate information for exercise type, intensity, duration, distance, notes, and date; no unrelated or placeholder workout content is shown.
  - Bug Report:
    - Issue: Incomplete workout entry information
    - Actual: Several existing entries, including **Weight Training**, **Yoga**, and **HIIT**, display exercise type, intensity, duration, notes, and date but do not display a distance value.

- [ ] CT-02: Goal summary uses clear labels and accurate comparison values
  - Action: Review the goal cards or metrics in **“Summary”** for the current week and month.
  - Expected: Each goal is labeled with its target, completed activity, remaining amount or status, and period; displayed values match the logged workouts.
  - Bug Report:
    - Issue: Missing goal summary
    - Actual: The dashboard goal cards show labels, weekly targets, and progress values, but no Summary view provides current-week and current-month comparison values, remaining amounts, or period-specific status.
