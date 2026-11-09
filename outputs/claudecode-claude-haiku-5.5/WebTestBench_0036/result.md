# Test Result

## Functionality
- [X] FT-01: Sign-in with valid credentials opens the dashboard
  - Action: Enter a valid email and password, then click "Sign In".
  - Expected: The dashboard loads and displays the signed-in user's name.
- [ ] FT-02: Dashboard shows the three recommendation sections
  - Action: Open the dashboard after signing in.
  - Expected: Sections labeled "Recommended Meditations", "Breathing Exercises", and "Relaxation Techniques" are visible, each with at least one default activity card.
  - Bug Report:
    - Issue: Missing Section Labels
    - Actual: The dashboard has no headings "Recommended Meditations", "Breathing Exercises", or "Relaxation Techniques". It shows "Featured for You" and "All Activities" instead, with Meditation/Breathing/Relaxation only as type filter chips.
- [ ] FT-03: Starting an activity opens a timed session
  - Action: Click "Start" on the first meditation card.
  - Expected: A session screen opens with a countdown timer that begins at the card's listed duration and decreases each second, plus the first step's guidance text.
  - Bug Report:
    - Issue: Incorrect Timer Behavior
    - Actual: The session opens with "Ready to begin?" and shows "Step 1 of 10" with the first guidance text, but the timer does not count down from the card's 10 min. After starting, it reads "0:01" and rises each second ("0:03"), against a fixed total of "3:07".
- [ ] FT-04: Step-by-step guidance advances through the session
  - Action: Click "Next" repeatedly during a session until the last step.
  - Expected: The step counter increments (e.g., "Step 2 of 5") and the guidance text changes at each step.
  - Bug Report:
    - Issue: Unresponsive Next Control
    - Actual: The step counter did advance from "Step 1 of 10" to "Step 2 of 10" on one click. Later Next clicks at "Step 2 of 10" and "Step 5 of 10" left the step counter unchanged (only the per-step seconds changed, e.g., "19" to "18"). Steps advanced on their own over time, so the Next control did not reliably move the session forward.
- [ ] FT-05: Completing a session increases the completed session count
  - Action: Note the count on the Progress page, complete a full session, then reopen the Progress page.
  - Expected: The total completed sessions count increases by exactly 1, and the session appears with today's date.
  - Bug Report:
    - Issue: Missing Progress Page
    - Actual: Navigating to /progress shows "404 Oops! Page not found", and no Progress link exists in the navigation. The dashboard "Sessions" count changed from 13 to 14 after one completed session, but no dated session history could be verified.
- [X] FT-06: Adding an activity to Favorites
  - Action: Click the heart icon on an activity card labeled "Save to Favorites".
  - Expected: The heart icon becomes filled, and the activity appears in the "Favorites" list.
- [X] FT-07: Removing an activity from Favorites
  - Action: Click the filled heart icon on a favorited activity.
  - Expected: The heart icon becomes empty, and the activity is removed from the "Favorites" list.
- [X] FT-08: Filtering activities by duration
  - Action: Select the "5 min" option in the Duration filter.
  - Expected: Only activities listed as 5 minutes are shown; all others are hidden.
- [ ] FT-09: Filtering activities by goal
  - Action: Select the "Sleep" option in the Goal filter.
  - Expected: Only activities tagged "Sleep" are shown; all others are hidden.
  - Bug Report:
    - Issue: Missing Filter Option
    - Actual: The Goal filter has no option labeled "Sleep". Its options are All, Find Calm, Improve Focus, Better Sleep, Reduce Stress, and Boost Energy. Selecting "Better Sleep" shows only the two activities tagged "Better Sleep" (Deep Sleep Journey, 4-7-8 Sleep Breathing) and hides the rest.
- [X] FT-10: Favorites persist after sign-out and sign-in
  - Action: Favorite one activity, click "Sign Out", then sign in with the same account and open the Favorites list.
  - Expected: The favorited activity is still listed.

## Constraint
- [X] CS-01: Sign-in is rejected with invalid credentials
  - Action: Enter a valid email with an incorrect password, then click "Sign In".
  - Expected: The message "Invalid email or password" appears, and the user remains on the sign-in page.
- [ ] CS-02: Sign-in is blocked when required fields are empty
  - Action: Leave the Email field blank, enter any password, then click "Sign In".
  - Expected: The form is not submitted, and the Email field shows "Email is required".
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: The form was not submitted and the user stayed on /login. The Email field showed the browser's native message "Please fill out this field." and did not show "Email is required".
- [X] CS-03: Dashboard is inaccessible when signed out
  - Action: Click "Sign Out", then navigate directly to the dashboard address.
  - Expected: The user is redirected to the sign-in page, and no dashboard content is shown.
- [ ] CS-04: Exiting a session early does not count as a completed session
  - Action: Start a session, click "End Session" before the final step, then check the Progress page count.
  - Expected: The completed session count is unchanged, and no new entry is added to history.
  - Bug Report:
    - Issue: Unverifiable Progress History
    - Actual: Early exit worked in the sense that the unlabeled left session control (no "End Session" label) returned the screen to "Ready to begin?" at step 1. The Progress page does not exist (404), so no history entry could be checked. The dashboard count was not read immediately after the early exit. The later count of 13 → 14 after one full completion is consistent with the early exit not being counted, but this is not verified.

## Interaction
- [ ] IX-01: Pause and resume control the session timer
  - Action: Start a session, click "Pause", wait 5 seconds, then click "Resume".
  - Expected: The timer stops while paused, the button label toggles between "Pause" and "Resume", and the timer continues from the paused value after resuming.
  - Bug Report:
    - Issue: Missing Pause Control
    - Actual: The session screen has no Pause or Resume control. It has three unlabeled buttons: back, an end/exit control, and Next. The timer keeps running during the session.
- [ ] IX-02: Favoriting shows a confirmation toast
  - Action: Click the heart icon on an unfavorited activity.
  - Expected: A toast reading "Added to Favorites" appears for about 3 seconds without a page reload.
  - Bug Report:
    - Issue: Missing Confirmation Toast
    - Actual: After favoriting Morning Calm and Energy Boost, no "Added to Favorites" text or status notification appeared (checked at 300 ms and 1.2 s after the click). The page did not reload. Other toasts, such as "Welcome back!" and "Login failed", do render.
- [X] IX-03: Session completion screen appears automatically at zero
  - Action: Start a session and wait without interacting until the timer reaches 00:00.
  - Expected: A "Session Complete" screen appears automatically, without requiring any click.

## Content
- [X] CT-01: Activity cards display complete information
  - Action: Review every activity card on the dashboard.
  - Expected: Each card shows a non-empty title, a duration in minutes, and a goal label; no card shows placeholder text such as "Lorem", "undefined", or "null".
- [X] CT-02: Activity descriptions match their goal tags
  - Action: Filter by each goal (Sleep, Focus, Stress Relief) and read the description of each activity shown.
  - Expected: Each description relates to the selected goal (e.g., sleep-related wording for "Sleep" activities).
- [ ] CT-03: Images and icons are relevant to meditation and relaxation
  - Action: Review all images and icons on the dashboard and session screens.
  - Expected: Every image and icon relates to meditation, breathing, or relaxation, and none appear broken or missing.
  - Bug Report:
    - Issue: Irrelevant Generic Icons
    - Actual: The dashboard has no img elements, and none are broken. Its icons are Lucide SVGs: leaf, heart, clock, play, target, sparkles, plus generic UI or progress icons (chart-column, trending-up, flame, trophy, filter) that do not relate to meditation, breathing, or relaxation.

---

**Notes on this run:**
- Sign-in used the demo account printed on the login page (demo@mindful.com / demo123). The button is labeled "Sign in", and the account menu item is "Log out", not "Sign Out". I treated these as the same controls.
- The Goal filter labels differ from the checklist ("Better Sleep", "Improve Focus", "Reduce Stress" versus "Sleep", "Focus", "Stress Relief"). CT-02 was judged on whether the descriptions match their goal tags.
- IX-03 passed on the completion screen itself. The timer counted up to the 3:07 total rather than down to 00:00, which is the same root cause as FT-03.
- Session screen icons were only partly reviewed for CT-03 (the start screen and dashboard were covered).
- About 80 tool calls were used of the 100 budget.