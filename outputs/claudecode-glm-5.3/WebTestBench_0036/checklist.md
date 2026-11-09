# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Enter valid credentials on the sign-in page and click the "Sign In" button.
  - Expected: Sign-in succeeds and the user is taken to the dashboard of recommended activities.

- [ ] FT-02: Dashboard shows recommended activities of all three types
  - Action: Sign in and view the dashboard.
  - Expected: The dashboard displays recommended items of all three types: meditations, breathing exercises, and relaxation techniques.

- [ ] FT-03: User can start an interactive timed session
  - Action: Click the start button (e.g., "Start Session") on any activity card from the default data.
  - Expected: A timed session view opens for that activity with the session timer running.

- [ ] FT-04: Session displays step-by-step guidance
  - Action: Start a session and observe the session view.
  - Expected: The current step's instruction is clearly displayed (e.g., step name/text such as "Breathe in"), along with its step indicator.

- [ ] FT-05: Session shows progress toward completion
  - Action: Watch the session view during an active session.
  - Expected: A progress indicator (e.g., progress bar and/or countdown timer) continuously advances reflecting elapsed/remaining time.

- [ ] FT-06: Completed session is recorded in session tracking
  - Action: Note the current completed-sessions count, finish one session to the end, then check the tracking display (e.g., "Sessions completed").
  - Expected: The completed-sessions count increases by exactly 1 and reflects total sessions completed over time.

- [ ] FT-07: User can filter activities by duration
  - Action: Apply a duration filter (e.g., "5–10 min") on the dashboard.
  - Expected: Only activities whose duration falls within the selected range are displayed.

- [ ] FT-08: User can filter activities by goal
  - Action: Apply a goal filter for each of "Sleep", "Focus", and "Stress Relief" on the dashboard.
  - Expected: Only activities tagged with the selected goal are displayed for each filter value.

- [ ] FT-09: User can save an activity to personal favorites
  - Action: Click the favorite/save control (e.g., heart icon) on any activity card.
  - Expected: The activity is saved and appears in the user's personal favorites list.

- [ ] FT-10: User can open the personal favorites list
  - Action: Navigate to the favorites list (e.g., click a "Favorites" link/tab) after saving at least one activity.
  - Expected: The favorites page opens and lists exactly the activities the user saved.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid or empty credentials
  - Action: Submit the sign-in form with empty fields, then with an incorrect password.
  - Expected: Access is denied both times with a clear error message; the dashboard is not shown.

- [ ] CS-02: Dashboard cannot be accessed without signing in
  - Action: Open the dashboard URL directly while signed out (or sign out, then attempt to return).
  - Expected: The user is not shown the dashboard and is redirected to the sign-in page.

- [ ] CS-03: Combined filters return only activities matching both criteria
  - Action: Apply a duration filter and a goal filter (e.g., "5–10 min" + "Sleep") simultaneously.
  - Expected: Only activities matching BOTH the selected duration and goal are shown; no activity violating either filter appears.

## Interaction
- [ ] IX-01: Confirmation feedback appears when saving a favorite
  - Action: Click the favorite/save control on an activity card.
  - Expected: A visible confirmation appears (e.g., toast "Added to favorites" or the heart icon visibly switches to its active state).

- [ ] IX-02: Filter changes update results immediately
  - Action: Change or clear a filter on the dashboard.
  - Expected: The activity list updates to the new result set immediately, without requiring a page reload or extra submit action.

- [ ] IX-03: Step guidance advances automatically during the session
  - Action: Remain in an active session without interacting and observe the guidance area.
  - Expected: The step instruction advances to the next step automatically as each step's time elapses, with the step indicator updating.

- [ ] IX-04: Session completion state is shown when the timer ends
  - Action: Let a session run to the end of its timer.
  - Expected: A completion state is displayed (e.g., "Session complete" message with option to exit or return to the dashboard); the timer stops.

## Content
- [ ] CT-01: All activity content is relevant to the meditation theme
  - Action: Browse all activities on the dashboard, including their titles, descriptions, and images/icons.
  - Expected: Every item is directly relevant to meditation, breathing, or relaxation (no off-theme or placeholder content, no broken images).

- [ ] CT-02: Each activity card displays its duration and goal
  - Action: Inspect any activity card on the dashboard.
  - Expected: The card clearly shows the activity's duration (e.g., "10 min") and its goal tag (e.g., "Sleep", "Focus", or "Stress Relief"), and these match what the filters select.

- [ ] CT-03: Favorites list entries show complete activity details
  - Action: Open the favorites list and inspect a saved entry.
  - Expected: Each entry displays sufficient details to identify and start the activity (at minimum: title, type, duration, and goal), consistent with its dashboard card.