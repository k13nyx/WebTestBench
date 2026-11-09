# Test Checklist

## Functionality
- [ ] FT-01: Sign-in with valid credentials opens the dashboard
  - Action: Enter a valid email and password, then click "Sign In".
  - Expected: The dashboard loads and displays the signed-in user's name.
- [ ] FT-02: Dashboard shows the three recommendation sections
  - Action: Open the dashboard after signing in.
  - Expected: Sections labeled "Recommended Meditations", "Breathing Exercises", and "Relaxation Techniques" are visible, each with at least one default activity card.
- [ ] FT-03: Starting an activity opens a timed session
  - Action: Click "Start" on the first meditation card.
  - Expected: A session screen opens with a countdown timer that begins at the card's listed duration and decreases each second, plus the first step's guidance text.
- [ ] FT-04: Step-by-step guidance advances through the session
  - Action: Click "Next" repeatedly during a session until the last step.
  - Expected: The step counter increments (e.g., "Step 2 of 5") and the guidance text changes at each step.
- [ ] FT-05: Completing a session increases the completed session count
  - Action: Note the count on the Progress page, complete a full session, then reopen the Progress page.
  - Expected: The total completed sessions count increases by exactly 1, and the session appears with today's date.
- [ ] FT-06: Adding an activity to Favorites
  - Action: Click the heart icon on an activity card labeled "Save to Favorites".
  - Expected: The heart icon becomes filled, and the activity appears in the "Favorites" list.
- [ ] FT-07: Removing an activity from Favorites
  - Action: Click the filled heart icon on a favorited activity.
  - Expected: The heart icon becomes empty, and the activity is removed from the "Favorites" list.
- [ ] FT-08: Filtering activities by duration
  - Action: Select the "5 min" option in the Duration filter.
  - Expected: Only activities listed as 5 minutes are shown; all others are hidden.
- [ ] FT-09: Filtering activities by goal
  - Action: Select the "Sleep" option in the Goal filter.
  - Expected: Only activities tagged "Sleep" are shown; all others are hidden.
- [ ] FT-10: Favorites persist after sign-out and sign-in
  - Action: Favorite one activity, click "Sign Out", then sign in with the same account and open the Favorites list.
  - Expected: The favorited activity is still listed.

## Constraint
- [ ] CS-01: Sign-in is rejected with invalid credentials
  - Action: Enter a valid email with an incorrect password, then click "Sign In".
  - Expected: The message "Invalid email or password" appears, and the user remains on the sign-in page.
- [ ] CS-02: Sign-in is blocked when required fields are empty
  - Action: Leave the Email field blank, enter any password, then click "Sign In".
  - Expected: The form is not submitted, and the Email field shows "Email is required".
- [ ] CS-03: Dashboard is inaccessible when signed out
  - Action: Click "Sign Out", then navigate directly to the dashboard address.
  - Expected: The user is redirected to the sign-in page, and no dashboard content is shown.
- [ ] CS-04: Exiting a session early does not count as a completed session
  - Action: Start a session, click "End Session" before the final step, then check the Progress page count.
  - Expected: The completed session count is unchanged, and no new entry is added to history.

## Interaction
- [ ] IX-01: Pause and resume control the session timer
  - Action: Start a session, click "Pause", wait 5 seconds, then click "Resume".
  - Expected: The timer stops while paused, the button label toggles between "Pause" and "Resume", and the timer continues from the paused value after resuming.
- [ ] IX-02: Favoriting shows a confirmation toast
  - Action: Click the heart icon on an unfavorited activity.
  - Expected: A toast reading "Added to Favorites" appears for about 3 seconds without a page reload.
- [ ] IX-03: Session completion screen appears automatically at zero
  - Action: Start a session and wait without interacting until the timer reaches 00:00.
  - Expected: A "Session Complete" screen appears automatically, without requiring any click.

## Content
- [ ] CT-01: Activity cards display complete information
  - Action: Review every activity card on the dashboard.
  - Expected: Each card shows a non-empty title, a duration in minutes, and a goal label; no card shows placeholder text such as "Lorem", "undefined", or "null".
- [ ] CT-02: Activity descriptions match their goal tags
  - Action: Filter by each goal (Sleep, Focus, Stress Relief) and read the description of each activity shown.
  - Expected: Each description relates to the selected goal (e.g., sleep-related wording for "Sleep" activities).
- [ ] CT-03: Images and icons are relevant to meditation and relaxation
  - Action: Review all images and icons on the dashboard and session screens.
  - Expected: Every image and icon relates to meditation, breathing, or relaxation, and none appear broken or missing.