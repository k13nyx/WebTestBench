# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials.
  - Action: Enter valid default username and password on the sign-in form and click "Sign In".
  - Expected: User is authenticated and the dashboard page loads.
- [ ] FT-02: Dashboard shows recommended activities across all three types.
  - Action: Sign in and view the dashboard.
  - Expected: Recommended items are displayed under meditation, breathing exercises, and relaxation techniques sections.
- [ ] FT-03: User can start an interactive timed session from an activity.
  - Action: Click the start button on any recommended activity.
  - Expected: A session view opens with a running timer set to the activity's duration.
- [ ] FT-04: Session displays step-by-step guidance.
  - Action: Start any session and observe the session view.
  - Expected: Step-by-step instruction text is shown and advances through the session's steps.
- [ ] FT-05: Session runs to completion at the end of its duration.
  - Action: Start a short-duration session and let the timer reach zero.
  - Expected: Session ends and a completion state (e.g., "Session Complete") is displayed.
- [ ] FT-06: User can filter activities by duration.
  - Action: Select a duration filter (e.g., "5 min") on the dashboard.
  - Expected: Only activities matching the selected duration are listed.
- [ ] FT-07: User can filter activities by goal.
  - Action: Select each goal filter: "Sleep", "Focus", and "Stress Relief".
  - Expected: Each filter lists only activities tagged with that goal.
- [ ] FT-08: User can track completed sessions over time.
  - Action: Open the session tracking/statistics area after completing a session.
  - Expected: A completed-session count is displayed and reflects sessions completed over time (e.g., by day/week).
- [ ] FT-09: User can save an activity to favorites.
  - Action: Click the save/favorite (e.g., heart or bookmark) control on an activity.
  - Expected: The activity appears in the personal favorites list.
- [ ] FT-10: User can view and remove items from the favorites list.
  - Action: Open the favorites list and click the remove control on a saved item.
  - Expected: The favorites list shows saved items, and the removed item disappears from it.

## Constraint
- [ ] CS-01: Invalid credentials cannot sign in.
  - Action: Enter a wrong password with a valid username and click "Sign In".
  - Expected: Sign-in fails and the user remains on the sign-in page; the dashboard is not shown.
- [ ] CS-02: Dashboard and session pages are not accessible without signing in.
  - Action: Navigate directly to the dashboard/session URL while signed out.
  - Expected: Access is blocked and the user is redirected to the sign-in page.
- [ ] CS-03: Combined duration and goal filters only show matching activities.
  - Action: Apply a duration filter and a goal filter at the same time.
  - Expected: Only activities matching both criteria are listed; no non-matching activity is shown.
- [ ] CS-04: Aborted sessions do not count as completed.
  - Action: Start a session, then exit before the timer reaches zero; check the completed-session count.
  - Expected: The completed-session count is unchanged.

## Interaction
- [ ] IX-01: Session timer/progress indicator updates in real time.
  - Action: Start a session and watch the timer/progress indicator.
  - Expected: The remaining time counts down and the progress indicator advances continuously as the session runs.
- [ ] IX-02: Applying a filter immediately updates the activity list.
  - Action: Change the duration or goal filter selection.
  - Expected: The activity list refreshes to the filtered results without a manual reload.
- [ ] IX-03: Favorite control shows a saved/unsaved state change.
  - Action: Click the favorite control on an activity, then click it again.
  - Expected: The control visually toggles to a "saved" state (e.g., filled icon) and back to "unsaved".
- [ ] IX-04: Sign-in failure shows an error message.
  - Action: Submit the sign-in form with invalid credentials.
  - Expected: An error message (e.g., "Invalid username or password") is displayed near the form.

## Content
- [ ] CT-01: All dashboard activities are relevant to the meditation theme.
  - Action: Review the titles and descriptions of all listed activities.
  - Expected: Every activity relates to meditation, breathing exercises, or relaxation; no irrelevant items appear.
- [ ] CT-02: Session guidance content matches the selected activity.
  - Action: Start a specific activity and read the step-by-step guidance.
  - Expected: Guidance text corresponds to that activity (e.g., breathing steps for a breathing exercise).
- [ ] CT-03: Goal filter options are labeled "Sleep", "Focus", and "Stress Relief".
  - Action: Inspect the goal filter controls on the dashboard.
  - Expected: Exactly the goals Sleep, Focus, and Stress Relief are presented with those labels.