# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials
  - Action: Enter valid email/username and password into the sign-in form and click the sign-in button
  - Expected: User is authenticated and the dashboard page loads
- [ ] FT-02: Dashboard displays recommended content in all three categories
  - Action: Sign in and view the dashboard
  - Expected: Dashboard shows recommended meditations, breathing exercises, and relaxation techniques
- [ ] FT-03: User can start an interactive timed session
  - Action: Click the start button (e.g., "Start Session") on any activity card
  - Expected: A timed session screen opens and the countdown/timer begins running
- [ ] FT-04: Session displays step-by-step guidance
  - Action: Start any session and observe the screen
  - Expected: Sequential instruction steps are shown (e.g., "Inhale…", "Hold…", "Exhale…") and advance as the session proceeds
- [ ] FT-05: Session shows visible progress
  - Action: Start a session and let it run for several seconds
  - Expected: A progress indicator (progress bar, percentage, or elapsed/remaining time) visibly updates during the session
- [ ] FT-06: User can filter activities by duration
  - Action: Select a duration filter option (e.g., "5 min" or "Under 10 min")
  - Expected: Only activities matching the selected duration are displayed
- [ ] FT-07: User can filter activities by goal
  - Action: Select a goal filter option (Sleep, Focus, or Stress Relief)
  - Expected: Only activities tagged with the selected goal are displayed
- [ ] FT-08: Duration and goal filters work together
  - Action: Apply both a duration filter and a goal filter simultaneously
  - Expected: Only activities matching both criteria are displayed
- [ ] FT-09: User can save an activity to favorites
  - Action: Click the favorite/save control (e.g., heart icon) on an activity card
  - Expected: The activity is added to the personal favorites list
- [ ] FT-10: Favorites list displays saved activities
  - Action: Open the favorites section/list after saving at least one activity
  - Expected: All previously saved activities appear in the personal list
- [ ] FT-11: Completed sessions are tracked over time
  - Action: Complete at least one full session, then view the stats/progress/history section
  - Expected: The completed session count increases and the session appears in the tracking history (e.g., total sessions, streak, or per-day record)

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials
  - Action: Enter an incorrect password (or unknown username) and submit the sign-in form
  - Expected: Sign-in fails and an error message is shown; the dashboard does not load
- [ ] CS-02: Sign-in cannot be submitted with empty required fields
  - Action: Leave email/username and/or password empty and click the sign-in button
  - Expected: Submission is blocked and a validation message indicates the required field(s)
- [ ] CS-03: Session completion counts only after the session finishes
  - Action: Start a session and abandon/exit it before the timer ends, then check the stats section
  - Expected: The completed-session count does not increase for the abandoned session

## Interaction
- [ ] IX-01: Session completion is confirmed
  - Action: Let a session run until the timer ends
  - Expected: A completion indication appears (e.g., "Session Complete" message or celebration state)
- [ ] IX-02: Favorite toggle gives immediate visual feedback
  - Action: Click the favorite icon on an activity card
  - Expected: The icon changes state (e.g., outline → filled/colored) immediately to reflect the saved status
- [ ] IX-03: Filters update the activity list immediately
  - Action: Click a duration or goal filter option
  - Expected: The activity list refreshes immediately without requiring a page reload, reflecting the filter

## Content
- [ ] CT-01: All displayed activities are relevant to the meditation theme
  - Action: Browse the dashboard, filters, and favorites list
  - Expected: Every item shown is a meditation, breathing exercise, or relaxation technique — no irrelevant content
- [ ] CT-02: Activity cards show accurate duration and goal labels
  - Action: Open any activity and compare its displayed duration/goal tags with the filters it appears under
  - Expected: The stated duration matches the actual session length and the goal tag matches its assigned category (Sleep/Focus/Stress Relief)