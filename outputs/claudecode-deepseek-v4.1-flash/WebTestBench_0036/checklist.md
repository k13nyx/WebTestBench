# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Enter valid username/email and password on the sign-in page, click "Sign In".
  - Expected: User is authenticated and lands on the dashboard.

- [ ] FT-02: Dashboard shows recommended content across all three activity types
  - Action: Sign in and view the dashboard.
  - Expected: Recommended meditations, breathing exercises, and relaxation techniques are all displayed.

- [ ] FT-03: User can start an interactive timed session
  - Action: Click a recommended activity to start it.
  - Expected: The session opens and the timer begins counting.

- [ ] FT-04: Timed session shows step-by-step guidance
  - Action: Start any session and observe as it runs.
  - Expected: Sequential step-by-step instructions are shown for each stage of the session.

- [ ] FT-05: Session displays progress
  - Action: Start a session and observe the progress element.
  - Expected: A progress indicator reflects how far through the session the user is.

- [ ] FT-06: User can filter activities by duration
  - Action: Select a duration filter (e.g., "10 min").
  - Expected: Only activities matching the selected duration are listed.

- [ ] FT-07: User can filter activities by goal
  - Action: Select a goal filter (Sleep, Focus, or Stress Relief).
  - Expected: Only activities matching the selected goal are listed.

- [ ] FT-08: Session completion is tracked over time
  - Action: Complete a session, then open the progress/history view.
  - Expected: The completed session is counted and the running total updates.

- [ ] FT-09: User can save an activity to favorites
  - Action: Click the favorite/save control on any activity.
  - Expected: The activity is added to the user's personal favorites list.

- [ ] FT-10: User can view their personal favorites list
  - Action: Open the Favorites list.
  - Expected: All previously favorited activities are shown.

## Constraint
- [ ] CS-01: Sign-in rejects invalid credentials
  - Action: Enter an invalid email/password combination and click "Sign In".
  - Expected: Sign-in fails with an error message; no access to the dashboard.

- [ ] CS-02: Activities cannot be started without signing in
  - Action: Attempt to open the dashboard or start a session while signed out.
  - Expected: Access is blocked and the user is prompted to sign in.

- [ ] CS-03: Empty filter results show an empty state
  - Action: Apply a duration + goal filter combination that matches no activities.
  - Expected: A "no activities found" empty state is shown instead of stale results.

- [ ] CS-04: Favoriting the same activity twice does not create duplicates
  - Action: Favorite an activity, then favorite it again.
  - Expected: The list contains a single entry (toggle, not duplicate).

- [ ] CS-05: Duration and goal filters can be combined without conflict
  - Action: Apply one duration filter and one goal filter together.
  - Expected: Results match both conditions simultaneously.

## Interaction
- [ ] IX-01: Session timer updates live
  - Action: Start a timed session and watch the timer.
  - Expected: The timer counts down/up continuously in real time.

- [ ] IX-02: Progress indicator advances during the session
  - Action: Let a session run through several steps.
  - Expected: The progress indicator advances in step with the session, without manual refresh.

- [ ] IX-03: Favorite control reflects saved state
  - Action: Click the favorite control on an activity.
  - Expected: The control immediately toggles to a visually distinct "favorited" state.

- [ ] IX-04: Session completion gives confirmation feedback
  - Action: Complete a timed session to the end.
  - Expected: A completion message/toast confirms the session finished.

## Content
- [ ] CT-01: All activities are relevant to meditation and relaxation
  - Action: Review the titles/descriptions of meditations, breathing exercises, and relaxation techniques on the dashboard.
  - Expected: Every item is genuinely a meditation, breathing, or relaxation activity (no unrelated content).

- [ ] CT-02: Imagery and icons match the meditation theme
  - Action: Inspect the images and icons across the dashboard and activity cards.
  - Expected: All media is relevant to calm/meditation/wellness and loads correctly.

- [ ] CT-03: Goal labels match the specified goals
  - Action: Review the available goal filter labels.
  - Expected: Goals are labeled "Sleep", "Focus", and "Stress Relief" as specified.

- [ ] CT-04: Session guidance text is real instructional content
  - Action: Read the step-by-step guidance shown during a session.
  - Expected: Guidance provides coherent, on-theme instructions rather than placeholder text.