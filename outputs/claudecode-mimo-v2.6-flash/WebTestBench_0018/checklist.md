# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Enter valid username and password on the sign-in page and submit.
  - Expected: User is authenticated and taken to the main fitness tracker page.

- [ ] FT-02: User can log a workout with all detail fields
  - Action: Open the workout logging form, enter exercise type (e.g., "Running"), intensity, duration, distance, and notes, then save.
  - Expected: Workout is saved and all five entered values are stored with it.

- [ ] FT-03: User can create a frequency-based goal
  - Action: Create a goal of the form "Run three times a week" via the goals section.
  - Expected: The goal is saved and listed among the user's active goals.

- [ ] FT-04: User can create a duration-based goal
  - Action: Create a goal of the form "Exercise 150 minutes per week" via the goals section.
  - Expected: The goal is saved and listed among the user's active goals.

- [ ] FT-05: Recent workouts timeline displays logged workouts
  - Action: After logging a workout, view the "Recent workouts" timeline.
  - Expected: The timeline shows the workout with its exercise type, duration, and date.

- [ ] FT-06: Summary view compares activity against goals for the current week
  - Action: Open the summary view and select the current-week period.
  - Expected: The view shows this week's logged totals alongside each goal's target (e.g., sessions count vs. 3/week, minutes vs. 150/week).

- [ ] FT-07: Summary view compares activity against goals for the current month
  - Action: Open the summary view and select the current-month period.
  - Expected: The view shows this month's logged totals alongside the corresponding goal targets.

- [ ] FT-08: User can sign out
  - Action: Click the sign-out control after signing in.
  - Expected: Session ends and the sign-in page is shown; protected pages are no longer accessible.

## Constraint
- [ ] CS-01: Workout form cannot be submitted with empty required fields
  - Action: Leave exercise type, intensity, or duration blank and attempt to save the workout.
  - Expected: Submission is blocked and an error identifies the missing required field(s); no workout is created.

- [ ] CS-02: Invalid credentials are rejected
  - Action: Enter a wrong password on the sign-in page and submit.
  - Expected: Sign-in fails with an error message and the user remains on the sign-in page.

- [ ] CS-03: Non-numeric or non-positive duration/distance is rejected
  - Action: Enter text or a negative number in the duration or distance field and save.
  - Expected: Validation error is shown, the invalid value is not saved, and no workout record is created.

- [ ] CS-04: Goal cannot be saved without a valid target value
  - Action: Attempt to save a goal with a blank or zero target (e.g., blank times-per-week).
  - Expected: Submission is blocked with an error; the goal is not added to the list.

- [ ] CS-05: Duplicate sign-in does not occur after session established
  - Action: After signing in, attempt to navigate back to the sign-in page via browser back button.
  - Expected: User is redirected to the authenticated main page rather than being shown a usable sign-in form.

## Interaction
- [ ] IX-01: Saving a workout shows a success confirmation
  - Action: Successfully submit a valid workout entry.
  - Expected: A success message/toast (e.g., "Workout saved") appears after submission.

- [ ] IX-02: Newly logged workout appears immediately in the timeline
  - Action: Save a workout and return to the timeline without reloading the page.
  - Expected: The new workout is visible at the top of the timeline without a manual refresh.

- [ ] IX-03: Creating a goal gives immediate feedback
  - Action: Successfully save a new fitness goal.
  - Expected: A confirmation appears and the new goal is instantly listed in the goals section.

- [ ] IX-04: Invalid sign-in attempt keeps the user in place with visible feedback
  - Action: Submit the sign-in form with an incorrect password.
  - Expected: An inline error or toast is displayed next to the form and form fields remain editable.

## Content
- [ ] CT-01: Timeline entries show workout details exactly as entered
  - Action: Log a workout with distinctive values (type "Cycling", intensity "High", duration "45", distance "12", notes "Evening ride") and inspect the timeline entry.
  - Expected: The timeline entry displays "Cycling", "High", "45", "12", and "Evening ride" matching the input, with correct units shown.

- [ ] CT-02: Summary displays the correct current period labels
  - Action: Open the summary view for week and month.
  - Expected: Labels show the actual current week date range and current month name, consistent with today's date.

- [ ] CT-03: Summary totals match the workouts actually logged
  - Action: Note the total minutes and session count of logged workouts for the current week, then compare with the summary's weekly figures.
  - Expected: The summary's totals equal the sum of the logged workouts (no mismatched or fabricated numbers).

- [ ] CT-04: Page content is fitness-focused throughout
  - Action: Review the sign-in, logging, timeline, goals, and summary pages.
  - Expected: All visible headings, labels, and media relate to fitness tracking; no placeholder or off-topic text is displayed.