I've completed all 22 checklist items. Here are the results.

# Test Result

## Functionality

- [X] FT-01: User can sign in and land on the dashboard
  - Action: Open the app, enter valid credentials in the sign-in form (email + password), click "Sign In".
  - Expected: User is authenticated and the meditation dashboard page is displayed.

- [X] FT-02: Dashboard displays recommended meditations, breathing exercises, and relaxation techniques
  - Action: On the dashboard, locate the activity listings.
  - Expected: Recommended meditations, breathing exercises, and relaxation techniques are all present as separate sections/tabs, each containing at least one default activity.

- [X] FT-03: User can start an interactive timed session from an activity
  - Action: Click any default activity card (e.g., a meditation), then click the "Start" button.
  - Expected: An interactive session view opens and begins running.

- [X] FT-04: Session shows step-by-step guidance that advances
  - Action: During the session, observe the guidance text for the first 3 steps.
  - Expected: Numbered/ordered instructions are shown one at a time and automatically advance to the next step as the session progresses.

- [ ] FT-05: Session displays a live countdown timer and progress indicator
  - Action: Start a session and watch the timer and progress bar for ~10 seconds.
  - Expected: Remaining time counts down in real time and the progress indicator advances proportionally toward 100%.
  - Bug Report:
    - Issue: Missing live countdown timer (static "remaining" value)
    - Actual: The session footer shows two time values, e.g. `0:02 / 1:01`, `0:20 / 1:01`, `0:52 / 1:01` sampled over 50+ seconds. The left value counts **up** (elapsed) and the right value is frozen at `1:01` for the entire run — it never decrements. There is no displayed remaining-time countdown. (The progress bar does advance correctly: translateX went -88.52% → -78.69% → -62.30% → -47.54% → -14.75% → 0%.)

- [X] FT-06: User can filter activities by goal (sleep, focus, stress relief)
  - Action: Apply the goal filter "Sleep" to the activity list.
  - Expected: Only activities whose goal is Sleep are shown; every listed activity is tagged with the Sleep goal.

- [X] FT-07: User can filter activities by duration
  - Action: Apply a duration filter (e.g., "5–10 min") to the activity list.
  - Expected: Only activities whose displayed duration falls within the selected range are shown.

- [X] FT-08: User can save an activity to a personal favorites list
  - Action: On a default activity, click the favorite/heart icon, then open the "Favorites" list page.
  - Expected: The favorited activity appears in the personal favorites list with its name and duration.

- [ ] FT-09: Completed sessions are tracked over time
  - Action: Complete one full session (let the timer finish), then open the progress/stats view.
  - Expected: The completed-session count increases by exactly 1 and the completed session is recorded in the history.
  - Bug Report:
    - Issue: No session history view — completed session is not recorded in any history list
    - Actual: The count increments correctly (Sessions 15 → 16, Total Minutes 165 → 170, persisted across re-login) and the completion screen appears, but no history of completed sessions exists anywhere. The "Your Progress" panel (dashboard), the Profile page (`/profile`), and `/progress`, `/stats`, `/history` routes (all 404) expose only aggregate counters (Day Streak / Total Minutes / Sessions) plus a static "This Week" bar chart with fixed heights (75%, 50%, 50%, 37.5%, 87.5%). The completed "Quick Calm" session is never listed by name or date.

## Constraint

- [X] CS-01: Dashboard content is not accessible without signing in
  - Action: Sign out (or open the dashboard URL directly in a fresh session without credentials).
  - Expected: Access is blocked and the user is redirected to the sign-in page; no activity dashboard content is rendered.

- [X] CS-02: Invalid sign-in credentials are rejected
  - Action: Enter an incorrect password with a valid email and click "Sign In".
  - Expected: An error message is shown and the user remains on the sign-in page, not authenticated.

- [X] CS-03: Filter combination with no matches shows an empty state
  - Action: Apply a goal filter and a duration filter that no default activity satisfies.
  - Expected: An explicit "no results" / empty-state message is displayed and no stale activity cards remain.

- [X] CS-04: An abandoned session is not counted as completed
  - Action: Start a session, then exit/abandon it before the timer finishes. Open the progress/stats view.
  - Expected: The completed-session count is unchanged and the abandoned session is not listed as completed.

- [X] CS-05: Favoriting an already-saved activity does not create a duplicate
  - Action: Favorite an activity, return to it, and click the favorite control again; check the favorites list.
  - Expected: Only one entry for that activity exists in the favorites list at any time, and toggling off removes it.

## Interaction

- [X] IX-01: Session can be paused and resumed
  - Action: Start a session, click "Pause", wait 5 seconds, then click "Resume".
  - Expected: The countdown freezes while paused (no time decrease) and continues from the paused value after resuming.

- [X] IX-02: Favorite control reflects saved state immediately
  - Action: Click the favorite/heart icon on an activity card and observe the icon without navigating away.
  - Expected: The icon immediately changes to a filled/"saved" state indicating the activity is in favorites.

- [X] IX-03: Completing a session shows a completion confirmation
  - Action: Let a session run to completion (or use the shortest default activity).
  - Expected: A completion screen/message is displayed confirming the session finished.

- [X] IX-04: Active filters are visibly indicated and can be cleared
  - Action: Select a goal filter, note the filter control, then clear/deselect all filters.
  - Expected: The selected filter shows an active/selected state, and clearing filters restores the full unfiltered activity list.

## Content

- [X] CT-01: Each activity card shows name, duration, and goal
  - Action: Inspect 3 default activity cards on the dashboard.
  - Expected: Every card displays a non-empty title, a duration value, and a goal tag (e.g., Sleep, Focus, Stress Relief).

- [X] CT-02: All content and imagery are on-theme and load correctly
  - Action: Browse the dashboard and open 2 activity detail/session views.
  - Expected: All titles, descriptions, and images/icons relate to meditation, breathing, or relaxation; no broken/placeholder images and no off-theme content.

- [X] CT-03: Session guidance text is meaningful and correctly ordered
  - Action: Read through the full step list of one session from step 1 to the last step.
  - Expected: Every step contains real, actionable instruction text (no empty steps, lorem ipsum, or duplicate placeholders) and steps run in a logical 1→N sequence.

---

**Summary:** 20 of 22 items PASS; 2 FAIL.

**Notes on the two failures:**
- **FT-05** — the session UI only renders an elapsed timer (counting up) plus a fixed `1:01` total label; no remaining-time countdown exists. The progress bar itself behaves correctly.
- **FT-09** — aggregate tracking works (Sessions +1, minutes +5, persisted), but there is no itemized session history anywhere in the app (`/progress`, `/stats`, `/history` return the 404 page).

**Additional incidental finding (outside checklist scope):** the "Quick Calm" card advertises `5 min`, but the session engine ran the full 9-step session in ~61 seconds and the completion message states "You completed 5 minutes of quick calm" — the session length label does not match the actual runtime.