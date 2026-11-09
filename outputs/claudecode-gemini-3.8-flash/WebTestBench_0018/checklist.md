# Test Checklist

## Functionality
- [ ] FT-01: User Sign-in with Valid Credentials
  - Action: Enter valid credentials into the "Email/Username" and "Password" fields, then click the "Sign In" button.
  - Expected: User is successfully authenticated and redirected to the fitness dashboard.
- [ ] FT-02: Log Workout with All Details
  - Action: Select exercise type "Running", intensity "High", enter duration "45", distance "5", notes "Morning trail run", and click "Save Workout".
  - Expected: The workout is saved and appears immediately in the recent workouts timeline.
- [ ] FT-03: Set Weekly Frequency Fitness Goal
  - Action: In the goal creation section, select goal type "Frequency", enter target "3 times per week", activity "Run", and click "Save Goal".
  - Expected: The new frequency goal "Run 3 times a week" is created and listed in the active goals list.
- [ ] FT-04: Set Weekly Duration Fitness Goal
  - Action: In the goal creation section, select goal type "Duration", enter target "150 minutes per week", and click "Save Goal".
  - Expected: The new duration goal "Exercise 150 minutes per week" is created and listed in the active goals list.
- [ ] FT-05: Display Recent Workouts in Timeline
  - Action: Navigate to the "Recent Workouts" section on the dashboard.
  - Expected: Default and logged workouts are displayed in reverse chronological order along a timeline.
- [ ] FT-06: View Current Week Goal Comparison
  - Action: Click the "Weekly" filter/tab in the summary view section.
  - Expected: Summary displays current week's logged metrics compared directly against the weekly goals (e.g., actual vs. target minutes and sessions).
- [ ] FT-07: View Current Month Goal Comparison
  - Action: Click the "Monthly" filter/tab in the summary view section.
  - Expected: Summary displays aggregated monthly activity compared against the monthly goals.

## Constraint
- [ ] CS-01: Prevent Sign-in with Blank Credentials
  - Action: Leave "Email/Username" and "Password" fields empty and click the "Sign In" button.
  - Expected: Form submission is blocked, and validation messages appear under the required fields.
- [ ] CS-02: Prevent Workout Submission with Missing Required Fields
  - Action: Leave "Exercise Type" and "Duration" empty and click "Save Workout".
  - Expected: Workout is not saved, and inline error messages indicate that required fields are missing.
- [ ] CS-03: Restrict Negative or Non-numeric Values for Duration and Distance
  - Action: Enter "-30" in the duration field and "abc" in the distance field, then click "Save Workout".
  - Expected: Form rejects the invalid input with an error message and does not log the workout.
- [ ] CS-04: Prevent Creation of Incomplete Fitness Goals
  - Action: Attempt to click "Save Goal" without entering a target value or selecting a goal type.
  - Expected: Goal creation is blocked and an error alert prompts the user to specify all goal parameters.

## Interaction
- [ ] IX-01: Workout Submission Feedback
  - Action: Fill in all valid workout fields and click "Save Workout".
  - Expected: A confirmation toast or banner appears indicating "Workout logged successfully" and the form resets.
- [ ] IX-02: Timeframe Toggle in Summary View
  - Action: Click between "Current Week" and "Current Month" buttons in the summary view.
  - Expected: Active button toggles visual highlight and the comparison charts/metrics update smoothly without a page reload.
- [ ] IX-03: Expand Timeline Workout for Notes and Details
  - Action: Click on a workout item card in the timeline view.
  - Expected: Card expands to show the full workout notes and intensity level details.

## Content
- [ ] CT-01: Timeline Workout Entry Information Integrity
  - Action: Inspect any logged workout entry in the timeline.
  - Expected: Card clearly displays exercise type, intensity, duration, distance (with units), date/time, and notes.
- [ ] CT-02: Goal vs. Activity Metrics Display
  - Action: View the comparison cards in the summary view.
  - Expected: Each goal card shows both the target metric and the actual logged value (e.g., "90 / 150 mins" or percentage completed).
- [ ] CT-03: Relevant Predefined Exercise and Intensity Options
  - Action: Open the "Exercise Type" and "Intensity" dropdown menus in the workout form.
  - Expected: Exercise type includes standard fitness categories (e.g., Running, Cycling, Swimming) and intensity includes relevant levels (e.g., Low, Medium, High).