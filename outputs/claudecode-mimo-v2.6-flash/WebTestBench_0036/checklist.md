# Test Checklist

## Functionality
- [ ] FT-01: User can sign in and reaches the dashboard
  - Action: Enter valid credentials on the sign-in page and submit.
  - Expected: Sign-in succeeds and the dashboard page is displayed.
- [ ] FT-02: Dashboard shows recommended meditations, breathing exercises, and relaxation techniques
  - Action: After signing in, view the dashboard.
  - Expected: Dashboard lists recommended items in all three categories: meditations, breathing exercises, and relaxation techniques.
- [ ] FT-03: User can start an interactive timed session
  - Action: Click the start button on any activity card.
  - Expected: A timed session opens showing a countdown timer and step-by-step guidance.
- [ ] FT-04: Session displays step-by-step guidance and progress
  - Action: Start a session and observe it running.
  - Expected: Guidance steps advance sequentially, and a progress indicator (e.g., progress bar or step counter) updates as time passes.
- [ ] FT-05: User can filter activities by duration
  - Action: Select a duration filter (e.g., "5 min" or "10–15 min") on the activities list.
  - Expected: Only activities matching the selected duration are displayed.
- [ ] FT-06: User can filter activities by goal
  - Action: Select a goal filter such as Sleep, Focus, or Stress Relief.
  - Expected: Only activities matching the selected goal are displayed.
- [ ] FT-07: Completed sessions are counted over time
  - Action: Finish a full session, then view the session tracking/statistics area.
  - Expected: The completed-session count increases by 1 and reflects sessions completed over time (e.g., per day/week).
- [ ] FT-08: User can save an activity to favorites
  - Action: Click the favorite (heart/bookmark) control on an activity.
  - Expected: The activity is added to the personal favorites list.
- [ ] FT-09: User can view their personal favorites list
  - Action: Navigate to the favorites list after saving at least one activity.
  - Expected: The list displays all previously favorited activities.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials
  - Action: Submit the sign-in form with an incorrect password.
  - Expected: Access is denied and an error message is shown; the dashboard is not displayed.
- [ ] CS-02: Sign-in cannot be submitted with empty required fields
  - Action: Leave the email/username and/or password fields empty and submit.
  - Expected: Submission is blocked and a validation message indicates the required fields.
- [ ] CS-03: Duration and goal filters only show matching activities
  - Action: Apply a specific duration filter, then a specific goal filter.
  - Expected: Every listed activity matches the selected duration and goal; no non-matching activity appears.
- [ ] CS-04: An activity is not duplicated in the favorites list
  - Action: Click the favorite control on the same activity twice (or save it again after it is already favorited).
  - Expected: The favorites list contains the activity only once.
- [ ] CS-05: Session completion is only recorded when the session actually finishes
  - Action: Start a session and exit/stop it before the timer ends.
  - Expected: The completed-session count does not increase.

## Interaction
- [ ] IX-01: Session timer counts down and guidance advances interactively
  - Action: Start a timed session and let it run.
  - Expected: The timer visibly counts down in real time and the current guidance step changes as the session progresses.
- [ ] IX-02: Progress indicator updates live during the session
  - Action: Observe the progress indicator while a session runs.
  - Expected: Progress advances continuously toward 100% as the timer elapses.
- [ ] IX-03: A completion feedback is shown when a session ends
  - Action: Let a session run to completion.
  - Expected: A visible completion confirmation (e.g., "Session complete" message or summary) appears.
- [ ] IX-04: Favorite control reflects saved state
  - Action: Click the favorite control on an activity, then open the favorites list.
  - Expected: The control shows a selected/filled state, and the activity appears in the favorites list.

## Content
- [ ] CT-01: Recommended items and steps content is relevant to meditation
  - Action: Review dashboard recommendations and session guidance text.
  - Expected: All listed activities and guidance steps are on-theme (meditation, breathing, relaxation) with no irrelevant or placeholder content.
- [ ] CT-02: Goal labels correctly describe each activity
  - Action: Inspect activities tagged Sleep, Focus, and Stress Relief.
  - Expected: Each activity's title and description match its stated goal (e.g., sleep activities describe winding down/sleep).