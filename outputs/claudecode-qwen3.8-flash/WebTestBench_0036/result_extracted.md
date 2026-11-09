# Test Result

## Functionality
- [X] FT-01: User can sign in and reach the dashboard
  - Action: From the landing page, sign in with valid credentials (demo@mindful.com / demo123); verify the dashboard loads
  - Expected: Sign-in succeeds and the dashboard displaying recommended meditations, breathing exercises, and relaxation techniques is shown
  - Verified: URL became `/dashboard`, "Welcome back!" toast, "Featured for You" + "All Activities" with cards of all three types.

- [X] FT-02: Dashboard shows all three activity categories
  - Action: View the dashboard after signing in
  - Expected: Cards/entries exist for meditations, breathing exercises, and relaxation techniques (each category has at least one default item)
  - Verified: Type badges present — Meditation (Morning Calm, Deep Sleep Journey, Focus Flow, Gratitude Meditation), Breathing (Box Breathing, Energy Boost, 4-7-8 Sleep Breathing, Quick Calm), Relaxation (Body Scan Relaxation, Progressive Muscle Relaxation).

- [X] FT-03: User can start a timed session from an activity
  - Action: Clicked "Start" on the Box Breathing card, then "Start Session"
  - Expected: An interactive session screen begins with a visible countdown timer
  - Verified: `/session/box-breathing` opened with a live countdown (0:48 total) and elapsed timer (0:01…). Note: the on-card "Start" opens a "Ready to begin?" screen requiring a second "Start Session" click — an acceptable two-stage start.

- [X] FT-04: Session shows step-by-step guidance
  - Action: Observed the guidance area over time during a running session
  - Expected: Discrete steps/instructions appear sequentially (e.g., "Inhale", "Hold", "Exhale") rather than one static block of text
  - Verified: Header advanced "Step 1 of 12" → 2 → 3 → 5; guidance text changed sequentially: "breathe in" ("Breathe in slowly") → "breathe out" ("Exhale slowly").

- [X] FT-05: Session timer completes and marks the session complete
  - Action: Started the 5-min Box Breathing (runs as a compressed ~48 s countdown, well under 2 min) and let it reach 0
  - Expected: A completion state is shown (e.g., "Session complete") and the session is counted as completed
  - Verified: "Session Complete — Great job! You completed 5 minutes of box breathing." with Repeat / Back to Dashboard buttons; Sessions stat went 11 → 12 and Total Minutes 135 → 140.

- [X] FT-06: Session progress is displayed
  - Action: Watched the progress indicator while the session ran
  - Expected: A progress bar or percentage updates visibly as time elapses
  - Verified: `role="progressbar"` fill updated (translateX −85.42% at 0:07, −79.17% at 0:10) plus elapsed/remaining time labels (0:01 / 0:48).

- [X] FT-07: User can filter activities by duration
  - Action: Applied Duration = "5 min"
  - Expected: Only activities matching the selected duration remain listed
  - Verified: "Filtered Results (3)" — Box Breathing, Energy Boost, Quick Calm, each labeled "5 min".

- [X] FT-08: User can filter activities by goal
  - Action: Applied Goal = "Better Sleep"
  - Expected: Only activities tagged with that goal are shown
  - Verified: "Filtered Results (2)" — Deep Sleep Journey and 4-7-8 Sleep Breathing, both tagged "Better Sleep".

- [X] FT-09: Combined filters narrow results correctly
  - Action: Set Goal = "Better Sleep" + Duration = "10 min" simultaneously
  - Expected: Only activities matching both criteria are displayed
  - Verified: "Filtered Results (1)" — 4-7-8 Sleep Breathing (Better Sleep, 10 min) only.

- [X] FT-10: Completed-session count is tracked over time
  - Action: Noted Sessions = 11, completed one session, returned to dashboard
  - Expected: The count increases by exactly 1 (and a history/over-time view lists the sessions)
  - Verified: Sessions 11 → 12 (+1 exactly); over-time "This Week" bar chart updated with today's (Sun) bar at 33.3% height, and the app's `completedSessions` history record grew to 12 entries with timestamps. Note: the over-time view is a per-day bar chart, not an itemized textual session list.

- [X] FT-11: User can save an activity to a personal favorites list
  - Action: Clicked the heart/favorite control on Morning Calm, then opened the Favorites view
  - Expected: The activity appears in the personal favorites list
  - Verified: Favorites page ("Your Favorites") showed the Morning Calm card.

- [X] FT-12: User can remove an activity from favorites
  - Action: Clicked the heart control on Morning Calm within Favorites
  - Expected: The item is removed from the favorites list
  - Verified: Morning Calm disappeared; only Box Breathing remained.

## Constraint
- [X] CS-01: Dashboard/session data requires sign-in
  - Action: Navigated directly to `/dashboard` (and `/favorites`) while signed out (after using "Log out")
  - Expected: User is redirected to sign-in; dashboard content is not viewable while signed out
  - Verified: Both URLs redirect to `/login`; no dashboard cards or stats rendered.

- [X] CS-02: Sign-in rejects invalid credentials
  - Action: Submitted sign-in with correct email + wrong password (`wrongpassword`)
  - Expected: An error message is shown and the user is not taken to the dashboard
  - Verified: Toast "Login failed — Invalid email or password. Try demo@mindful.com / demo123"; page stayed on `/login`.

- [X] CS-03: Favorites toggle is idempotent (no duplicates)
  - Action: Starred Morning Calm (which exists as two duplicate cards: Featured + All Activities), re-starred/unstarred repeatedly, and checked the Favorites list
  - Expected: The activity appears at most once in the favorites list
  - Verified: Favorites showed exactly one Morning Calm entry; the heart is a toggle (clicking a favorited item removes it — observed state flip filled ↔ outline); stored favorites array never gained a duplicate id.

- [X] CS-04: Filters never show non-matching activities
  - Action: Applied a non-matching combination: Duration "5 min" + Goal "Better Sleep" (no 5-min sleep activity exists)
  - Expected: An empty-results or "no activities found" state is shown; unrelated activities are NOT listed
  - Verified: "Filtered Results (0)" with paragraph "No activities match your filters." and a "Clear filters" button; no activity cards rendered.

- [X] CS-05: Session completion is counted only once
  - Action: Completed the Box Breathing session once, then navigated Dashboard → Favorites → Dashboard without starting another session
  - Expected: The completed-sessions counter increases by exactly 1, not more
  - Verified: Sessions stayed at 12 across navigations; data shows exactly one `box-breathing` completion dated today.

## Interaction
- [X] IX-01: Favorite control reflects current state
  - Action: Compared the heart control on a favorited vs. non-favorited activity via DOM inspection (hover to reveal)
  - Expected: The icon visibly distinguishes saved (filled/active) from unsaved (outline) state
  - Verified: Favorited heart SVG has class `lucide lucide-heart … fill-current text-destructive` (computed fill = rgb(239, 67, 67)); non-favorited heart is outline (`fill: none`, no `fill-current`). Cosmetic note (not a checklist violation): the control has no `aria-label`/`title` and stays at `opacity-0` until card hover.

- [X] IX-02: Pause/resume controls respond during a session
  - Action: Clicked the pause control mid-session (timer 0:10), waited ~4 s, clicked the same control (now a play icon) to resume
  - Expected: The countdown and progress indicator stop on pause and continue on resume
  - Verified: Timer frozen at 0:10 and progress bar unchanged (translateX −79.17%) during pause; after resume timer advanced 0:10 → 0:11 → 0:17 and step counter resumed (Step 5 of 12). Observation: the adjacent reset control (lucide-rotate-ccw) restarts the session to "Ready to begin?" and none of the session controls carry accessible names.

## Content
- [X] CT-01: All default content is meditation-relevant
  - Action: Browsed the landing page, dashboard (10 activities + goal/type filters), session guidance text ("breathe in", "Breathe in slowly", "Exhale slowly"), completion message, and DOM-checked for broken images and placeholder text
  - Expected: Every activity title, description, guidance step, and goal label relates to meditation/breathing/relaxation; no placeholder text (e.g., "lorem ipsum") or broken images
  - Verified: All copy is mindfulness-themed (goals: Find Calm, Reduce Stress, Better Sleep, Improve Focus, Boost Energy; durations in min); `/lorem/i` test returned false; zero images with `naturalWidth === 0` (icons are inline SVGs).
