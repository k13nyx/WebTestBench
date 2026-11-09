# Test Result

## Functionality
- [X] FT-01: User Sign-in with Valid Credentials
  - Action: Enter valid credentials into the "Email/Username" and "Password" fields, then click the "Sign In" button.
  - Expected: User is successfully authenticated and redirected to the fitness dashboard.
- [X] FT-02: Log Workout with All Details
  - Action: Select exercise type "Running", intensity "High", enter duration "45", distance "5", notes "Morning trail run", and click "Save Workout".
  - Expected: The workout is saved and appears immediately in the recent workouts timeline.
- [X] FT-03: Set Weekly Frequency Fitness Goal
  - Action: In the goal creation section, select goal type "Frequency", enter target "3 times per week", activity "Run", and click "Save Goal".
  - Expected: The new frequency goal "Run 3 times a week" is created and listed in the active goals list.
- [X] FT-04: Set Weekly Duration Fitness Goal
  - Action: In the goal creation section, select goal type "Duration", enter target "150 minutes per week", and click "Save Goal".
  - Expected: The new duration goal "Exercise 150 minutes per week" is created and listed in the active goals list.
- [X] FT-05: Display Recent Workouts in Timeline
  - Action: Navigate to the "Recent Workouts" section on the dashboard.
  - Expected: Default and logged workouts are displayed in reverse chronological order along a timeline.
- [ ] FT-06: View Current Week Goal Comparison
  - Action: Click the "Weekly" filter/tab in the summary view section.
  - Expected: Summary displays current week's logged metrics compared directly against the weekly goals (e.g., actual vs. target minutes and sessions).
  - Bug Report:
    - Issue: Missing Feature / Element Not Found
    - Actual: There is no "Weekly" filter or tab in the summary view section; summary cards only present static aggregate metrics without a goal comparison view.
- [ ] FT-07: View Current Month Goal Comparison
  - Action: Click the "Monthly" filter/tab in the summary view section.
  - Expected: Summary displays aggregated monthly activity compared against the monthly goals.
  - Bug Report:
    - Issue: Missing Feature / Element Not Found
    - Actual: There is no "Monthly" filter or tab in the summary view section to view aggregated monthly activity compared against monthly goals.

## Constraint
- [X] CS-01: Prevent Sign-in with Blank Credentials
  - Action: Leave "Email/Username" and "Password" fields empty and click the "Sign In" button.
  - Expected: Form submission is blocked, and validation messages appear under the required fields.
- [ ] CS-02: Prevent Workout Submission with Missing Required Fields
  - Action: Leave "Exercise Type" and "Duration" empty and click "Save Workout".
  - Expected: Workout is not saved, and inline error messages indicate that required fields are missing.
  - Bug Report:
    - Issue: Missing Form Validation Messages
    - Actual: Exercise Type cannot be cleared or left empty (defaults to 'Running' with no blank option), and leaving Duration empty blocks submission without displaying any inline error messages under the required fields.
- [ ] CS-03: Restrict Negative or Non-numeric Values for Duration and Distance
  - Action: Enter "-30" in the duration field and "abc" in the distance field, then click "Save Workout".
  - Expected: Form rejects the invalid input with an error message and does not log the workout.
  - Bug Report:
    - Issue: Missing Error Message on Invalid Input
    - Actual: The form blocks workout logging when duration is -30 and HTML5 number constraints prevent typing letters in distance, but no visible error message or alert is rendered on the screen.
- [ ] CS-04: Prevent Creation of Incomplete Fitness Goals
  - Action: Attempt to click "Save Goal" without entering a target value or selecting a goal type.
  - Expected: Goal creation is blocked and an error alert prompts the user to specify all goal parameters.
  - Bug Report:
    - Issue: Missing Validation Alert
    - Actual: Clicking "Create Goal" without entering a target value prevents goal creation, but no error alert or visible notification prompts the user.

## Interaction
- [ ] IX-01: Workout Submission Feedback
  - Action: Fill in all valid workout fields and click "Save Workout".
  - Expected: A confirmation toast or banner appears indicating "Workout logged successfully" and the form resets.
  - Bug Report:
    - Issue: Missing Confirmation Toast / Banner
    - Actual: Saving a valid workout closes the dialog and resets the form, but no confirmation toast or banner appears in the interface.
- [ ] IX-02: Timeframe Toggle in Summary View
  - Action: Click between "Current Week" and "Current Month" buttons in the summary view.
  - Expected: Active button toggles visual highlight and the comparison charts/metrics update smoothly without a page reload.
  - Bug Report:
    - Issue: Missing Interactive Element
    - Actual: No "Current Week" or "Current Month" toggle buttons exist in the summary view section.
- [ ] IX-03: Expand Timeline Workout for Notes and Details
  - Action: Click on a workout item card in the timeline view.
  - Expected: Card expands to show the full workout notes and intensity level details.
  - Bug Report:
    - Issue: Unresponsive Element / Missing Expand Interaction
    - Actual: Clicking on a workout item card in the timeline does not expand the card or trigger any interactive state changes.

## Content
- [X] CT-01: Timeline Workout Entry Information Integrity
  - Action: Inspect any logged workout entry in the timeline.
  - Expected: Card clearly displays exercise type, intensity, duration, distance (with units), date/time, and notes.
- [X] CT-02: Goal vs. Activity Metrics Display
  - Action: View the comparison cards in the summary view.
  - Expected: Each goal card shows both the target metric and the actual logged value (e.g., "90 / 150 mins" or percentage completed).
- [X] CT-03: Relevant Predefined Exercise and Intensity Options
  - Action: Open the "Exercise Type" and "Intensity" dropdown menus in the workout form.
  - Expected: Exercise type includes standard fitness categories (e.g., Running, Cycling, Swimming) and intensity includes relevant levels (e.g., Low, Medium, High).