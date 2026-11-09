# Test Checklist

## Functionality

- [ ] **FT-01: User can sign in with a valid pre-existing account**
  - **Action:** Enter valid default account credentials and select **“Sign In.”**
  - **Expected:** The user is authenticated and taken to the fitness tracker dashboard.

- [ ] **FT-02: User can log a complete workout**
  - **Action:** Open **“Log Workout,”** select an **Exercise Type**, choose an **Intensity**, enter **Duration**, enter **Distance**, add **Notes**, and select **“Save Workout.”**
  - **Expected:** The workout is saved and includes every entered field.

- [ ] **FT-03: User can set a workout-frequency goal**
  - **Action:** Open **“Goals,”** create or select a goal with the target **“Run three times a week,”** and save it.
  - **Expected:** The goal is displayed in the user’s goals list with its weekly frequency target.

- [ ] **FT-04: User can set a weekly-duration goal**
  - **Action:** Create or select a goal with the target **“Exercise 150 minutes per week”** and save it.
  - **Expected:** The goal is displayed with a 150-minute weekly target.

- [ ] **FT-05: User can view recent workouts in a timeline**
  - **Action:** Navigate to the **“Recent Workouts”** or **“Timeline”** view after a workout is present.
  - **Expected:** Workouts appear in timeline order with their exercise type, intensity, duration, distance, notes, and workout date.

- [ ] **FT-06: User can view activity compared with goals**
  - **Action:** Open the **“Summary”** view and inspect both the **Current Week** and **Current Month** sections.
  - **Expected:** The summary shows logged activity and compares it with the configured goals for each period.

- [ ] **FT-07: Logged workout data is retained when revisiting the dashboard**
  - **Action:** Save a valid workout, navigate away from the dashboard, then return to **“Recent Workouts.”**
  - **Expected:** The saved workout remains visible with the same field values.

## Constraint

- [ ] **CS-01: Required workout fields prevent incomplete submissions**
  - **Action:** Open **“Log Workout,”** leave one or more required fields empty, and select **“Save Workout.”**
  - **Expected:** The workout is not saved, and each missing required field is identified for correction.

- [ ] **CS-02: Workout numeric fields accept only valid numeric values**
  - **Action:** Enter non-numeric, negative, or otherwise invalid values in **Duration** and **Distance**, then attempt to save.
  - **Expected:** The form rejects each invalid value and does not create a workout.

- [ ] **CS-03: Goal targets cannot be saved without a valid target**
  - **Action:** In **“Goals,”** attempt to save a goal with an empty, zero, negative, or non-numeric target.
  - **Expected:** The goal is not saved, and the invalid target is identified for correction.

- [ ] **CS-04: Invalid sign-in credentials do not authenticate the user**
  - **Action:** Enter an invalid email, username, or password and select **“Sign In.”**
  - **Expected:** The user remains signed out and receives a clear invalid-credentials error.

- [ ] **CS-05: Summary calculations use only workouts in the selected period**
  - **Action:** Compare the **Current Week** and **Current Month** summary totals with the dates of the workouts shown in the timeline.
  - **Expected:** Weekly totals include only workouts from the current week, and monthly totals include only workouts from the current month.

## Interaction

- [ ] **IX-01: Workout save provides visible completion feedback**
  - **Action:** Save a valid workout.
  - **Expected:** The interface visibly confirms that the workout was saved and updates the relevant workout view without requiring a page refresh.

- [ ] **IX-02: Goal save updates the goals and summary views**
  - **Action:** Save a valid goal, then open or refresh **“Summary.”**
  - **Expected:** The new goal appears in the goals list and is reflected in the applicable current-week or current-month comparison.

- [ ] **IX-03: Summary period controls update displayed data**
  - **Action:** Switch between **“Current Week”** and **“Current Month”** in the summary.
  - **Expected:** The selected period is visibly indicated, and the activity totals and goal comparison update to match that period.

## Content

- [ ] **CT-01: Workout timeline presents complete and relevant workout information**
  - **Action:** Review each workout entry in **“Recent Workouts”** or **“Timeline.”**
  - **Expected:** Every entry displays readable, accurate information for exercise type, intensity, duration, distance, notes, and date; no unrelated or placeholder workout content is shown.

- [ ] **CT-02: Goal summary uses clear labels and accurate comparison values**
  - **Action:** Review the goal cards or metrics in **“Summary”** for the current week and month.
  - **Expected:** Each goal is labeled with its target, completed activity, remaining amount or status, and period; displayed values match the logged workouts.