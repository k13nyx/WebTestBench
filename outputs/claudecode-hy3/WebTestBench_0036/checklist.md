# Test Checklist

## Functionality
- [ ] FT-01: User can sign in to the application
  - Action: Click "Sign In", enter valid credentials, and submit.
  - Expected: User is authenticated and the dashboard loads.

- [ ] FT-02: Dashboard displays recommended meditations
  - Action: After signing in, view the dashboard.
  - Expected: A list/section of recommended meditations is visible.

- [ ] FT-03: Dashboard displays breathing exercises
  - Action: After signing in, view the dashboard.
  - Expected: A section of breathing exercises is visible.

- [ ] FT-04: Dashboard displays relaxation techniques
  - Action: After signing in, view the dashboard.
  - Expected: A section of relaxation techniques is visible.

- [ ] FT-05: User can start an interactive timed session
  - Action: Click "Start" (or equivalent) on an activity.
  - Expected: A timed session begins and counts down.

- [ ] FT-06: Active session shows step-by-step guidance
  - Action: Observe the screen during an active session.
  - Expected: Step-by-step instructions are displayed and advance as the session progresses.

- [ ] FT-07: User can filter activities by duration
  - Action: Select a duration filter (e.g., 5 / 10 / 20 min) and apply.
  - Expected: Only activities matching the selected duration are shown.

- [ ] FT-08: User can filter activities by goal
  - Action: Select a goal (Sleep, Focus, or Stress Relief) and apply.
  - Expected: Only activities matching the selected goal are shown.

- [ ] FT-09: System tracks completed sessions over time
  - Action: Complete a session, then open the stats/history view.
  - Expected: The completed-session count increases and is recorded over time.

- [ ] FT-10: User can save an activity to favorites
  - Action: Click the "Save" / favorite (heart) control on an activity.
  - Expected: The activity is added to the personal favorites list.

- [ ] FT-11: User can view the saved favorites list
  - Action: Navigate to the "Favorites" section.
  - Expected: The personal list shows all saved activities.

## Constraint
- [ ] CS-01: Invalid sign-in credentials are rejected
  - Action: Enter incorrect email/password and submit.
  - Expected: Access is denied and an error message is shown.

- [ ] CS-02: Signed-out users cannot access protected content
  - Action: Attempt to open the dashboard or Favorites while signed out.
  - Expected: User is redirected to sign-in or access is blocked.

## Interaction
- [ ] IX-01: Session displays live progress
  - Action: Start a session and observe the progress indicator over time.
  - Expected: The progress bar / timer updates continuously as time elapses.

- [ ] IX-02: Confirmation feedback when a favorite is saved
  - Action: Click "Save" on an activity.
  - Expected: A visual confirmation (toast or state change) indicates it was saved.

- [ ] IX-03: Completion feedback at end of session
  - Action: Let a timed session run to completion.
  - Expected: A completion message/screen is shown when the timer ends.

## Content
- [ ] CT-01: Dashboard media and text are relevant to the meditation theme
  - Action: Review images, icons, and descriptions on the dashboard.
  - Expected: All content directly relates to meditation, breathing, or relaxation.

- [ ] CT-02: Each activity shows accurate descriptive content
  - Action: Open an activity's details.
  - Expected: Title, duration, and goal are displayed and match the activity.