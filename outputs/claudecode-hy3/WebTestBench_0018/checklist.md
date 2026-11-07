# Test Checklist

## Functionality
- [ ] FT-01: User can sign in to the fitness tracker
  - Action: Enter valid credentials and submit the sign-in form.
  - Expected: User is authenticated and lands on the tracker dashboard.

- [ ] FT-02: User can log a detailed workout with all required fields
  - Action: Fill in exercise type, intensity, duration, distance, and notes, then submit.
  - Expected: Workout is saved and confirmed as recorded.

- [ ] FT-03: User can set a weekly frequency goal (e.g., "run 3 times a week")
  - Action: Create a goal of type "times per week" with a target count and submit.
  - Expected: Goal is saved and shown in the goals list.

- [ ] FT-04: User can set a weekly minutes goal (e.g., "exercise 150 minutes per week")
  - Action: Create a goal of type "minutes per week" with a target value and submit.
  - Expected: Goal is saved and shown in the goals list.

- [ ] FT-05: Recent workouts are displayed in a timeline
  - Action: Open the timeline/recent workouts view.
  - Expected: Logged workouts appear in chronological order (most recent first).

- [ ] FT-06: Summary view compares logged activity against goals for the current week
  - Action: Open the summary view and select the current week.
  - Expected: Progress for each goal is shown versus its weekly target.

- [ ] FT-07: Summary view compares logged activity against goals for the current month
  - Action: Open the summary view and select the current month.
  - Expected: Progress for each goal is shown versus its monthly rollup/target.

## Constraint
- [ ] CS-01: Sign-in rejects empty or invalid credentials
  - Action: Submit the sign-in form with blank or wrong credentials.
  - Expected: Access is denied and an error message is shown.

- [ ] CS-02: Workout form blocks submission with missing required fields
  - Action: Submit a workout form leaving required fields (e.g., exercise type, duration) empty.
  - Expected: Submission is prevented and a validation message identifies the missing fields.

- [ ] CS-03: Goal form requires valid positive numeric targets
  - Action: Submit a goal with zero, negative, or non-numeric values.
  - Expected: Submission is rejected with a validation message.

- [ ] CS-04: Goals are scoped to a weekly target only
  - Action: Attempt to set a goal without a weekly scope or with unsupported types.
  - Expected: Only weekly frequency or weekly minutes goals are accepted.

## Interaction
- [ ] IX-01: Success confirmation appears after logging a workout
  - Action: Submit a valid workout.
  - Expected: A success toast or message confirms the workout was saved.

- [ ] IX-02: Success confirmation appears after setting a goal
  - Action: Submit a valid goal.
  - Expected: A success toast or message confirms the goal was saved.

- [ ] IX-03: Timeline updates immediately after logging a workout
  - Action: Log a new workout and view the timeline.
  - Expected: The new workout appears at the top of the timeline without manual refresh.

## Content
- [ ] CT-01: Timeline displays relevant workout details
  - Action: Inspect a timeline entry.
  - Expected: Each entry shows exercise type, intensity, duration, distance, and notes.

- [ ] CT-02: Summary view clearly labels week and month goal comparisons
  - Action: Open the summary view.
  - Expected: Sections are clearly labeled "Week" and "Month" with logged vs. goal values.

- [ ] CT-03: Exercise type options are fitness-relevant
  - Action: Open the exercise type field on the workout form.
  - Expected: Options are valid fitness activities (e.g., run, cycle, swim) relevant to a fitness tracker.