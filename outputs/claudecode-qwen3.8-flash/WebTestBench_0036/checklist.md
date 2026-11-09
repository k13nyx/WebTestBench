# Test Checklist

## Functionality
- [ ] FT-01: User can sign in and reach the dashboard
  - Action: From the landing page, sign in with valid credentials; verify the dashboard loads
  - Expected: Sign-in succeeds and the dashboard displaying recommended meditations, breathing exercises, and relaxation techniques is shown

- [ ] FT-02: Dashboard shows all three activity categories
  - Action: View the dashboard after signing in
  - Expected: Cards/entries exist for meditations, breathing exercises, and relaxation techniques (each category has at least one default item)

- [ ] FT-03: User can start a timed session from an activity
  - Action: Click a default activity (e.g., a meditation card) and its Start button
  - Expected: An interactive session screen begins with a visible countdown timer

- [ ] FT-04: Session shows step-by-step guidance
  - Action: During a running session, observe the guidance area over time
  - Expected: Discrete steps/instructions appear sequentially (e.g., "Inhale", "Hold", "Exhale") rather than one static block of text

- [ ] FT-05: Session timer completes and marks the session complete
  - Action: Start a short (≤2 min) session and let the countdown reach 0
  - Expected: A completion state is shown (e.g., "Session complete") and the session is counted as completed

- [ ] FT-06: Session progress is displayed
  - Action: While a session is running, watch the progress indicator
  - Expected: A progress bar or percentage updates visibly as time elapses

- [ ] FT-07: User can filter activities by duration
  - Action: Apply a duration filter (e.g., "5 min") on the dashboard
  - Expected: Only activities matching the selected duration remain listed

- [ ] FT-08: User can filter activities by goal
  - Action: Apply a goal filter such as "Sleep", "Focus", or "Stress Relief"
  - Expected: Only activities tagged with that goal are shown

- [ ] FT-09: Combined filters narrow results correctly
  - Action: Set both a duration and a goal filter simultaneously
  - Expected: Only activities matching both criteria are displayed

- [ ] FT-10: Completed-session count is tracked over time
  - Action: Note the completed-sessions statistic, complete one more session, return to the dashboard/stats view
  - Expected: The count increases by exactly 1 (and a history/over-time view lists the sessions)

- [ ] FT-11: User can save an activity to a personal favorites list
  - Action: Click the favorite/star control on an activity, then open the Favorites view
  - Expected: The activity appears in the personal favorites list

- [ ] FT-12: User can remove an activity from favorites
  - Action: In Favorites, use the remove/unstar control on a favorited item
  - Expected: The item is removed from the favorites list

## Constraint
- [ ] CS-01: Dashboard/session data requires sign-in
  - Action: Navigate directly to the dashboard URL (or after signing out)
  - Expected: User is redirected to sign-in; dashboard content is not viewable while signed out

- [ ] CS-02: Sign-in rejects invalid credentials
  - Action: Submit the sign-in form with an empty or wrong password
  - Expected: An error message is shown and the user is not taken to the dashboard

- [ ] CS-03: Favorites toggle is idempotent (no duplicates)
  - Action: Click the favorite control on the same activity twice (star, then in list view confirm) and re-star it
  - Expected: The activity appears at most once in the favorites list

- [ ] CS-04: Filters never show non-matching activities
  - Action: Apply a duration/goal combination with no matching activities (e.g., "60 min" + an unused goal)
  - Expected: An empty-results or "no activities found" state is shown; unrelated activities are NOT listed

- [ ] CS-05: Session completion is counted only once
  - Action: Complete one session, then navigate back and forth without starting another
  - Expected: The completed-sessions counter increases by exactly 1, not more

## Interaction
- [ ] IX-01: Favorite control reflects current state
  - Action: Hover/observe the star control on a favorited vs. non-favorited activity
  - Expected: The icon visibly distinguishes saved (filled/active) from unsaved (outline) state

- [ ] IX-02: Pause/resume controls respond during a session
  - Action: Click Pause mid-session, wait a few seconds, then click Resume
  - Expected: The countdown and progress indicator stop on pause and continue on resume

## Content
- [ ] CT-01: All default content is meditation-relevant
  - Action: Browse the dashboard, a session's guidance text, and filter labels
  - Expected: Every activity title, description, guidance step, and goal label relates to meditation/breathing/relaxation; no placeholder text (e.g., "lorem ipsum") or broken images