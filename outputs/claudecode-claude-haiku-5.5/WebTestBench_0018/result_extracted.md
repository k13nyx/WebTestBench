# Test Result

## Functionality

- [ ] FT-01: User can sign in with valid credentials and reach the dashboard.
  - Action: On the sign-in page, enter a valid email and password, then click "Sign In".
  - Expected: The dashboard loads, the user's name or account is shown in the header, and a "Sign Out" option is visible.
  - Bug Report:
    - Issue: Missing Element (Sign Out option)
    - Actual: Sign-in succeeded, the dashboard loaded, and the header shows "Alex Runner". No element with the text "Sign Out" exists. The only header control is an unlabeled icon button (no text, aria-label, or title), and clicking it signs the user out.

- [X] FT-02: User can log a workout with all fields filled in.
  - Action: Click "Log Workout". Set Exercise Type "Running", Intensity "Moderate", Duration "45" min, Distance "5" km, Notes "Morning run". Click "Save".
  - Expected: The workout is saved and appears in the Recent Workouts timeline with every entered value.

- [ ] FT-03: User can create a goal of running three times a week.
  - Action: Click "Add Goal". Select activity "Running", target "3", period "Weekly". Click "Save".
  - Expected: The goal "Run 3 times/week" is listed on the goals list with progress for the current week shown as "x / 3".
  - Bug Report:
    - Issue: Incorrect Label (goal title)
    - Actual: The goal was created, but it is listed as "Running 3 times per week" instead of "Run 3 times/week". Progress reads "2 / 3 times", which is the requested format with a different unit word. The save button is labeled "Create Goal", not "Save".

- [ ] FT-04: User can create a goal of 150 activity minutes per week.
  - Action: Click "Add Goal". Select goal type "Total minutes" (all activities), target "150", period "Weekly". Click "Save".
  - Expected: The goal "150 minutes/week" is listed with progress for the current week shown as "x / 150 min".
  - Bug Report:
    - Issue: Incorrect Label (goal title)
    - Actual: The goal was created and progress reads "80 / 150 min" (correct), but the title is "Exercise 150 minutes per week" instead of "150 minutes/week". The goal-type option is "Duration (minutes per period)", and the activity is "Any exercise".

- [X] FT-05: Timeline shows recent workouts in newest-first order.
  - Action: Open the Timeline (or the dashboard's Recent Workouts section) with at least two logged workouts on different dates.
  - Expected: Entries are sorted by date, newest at the top, and each entry shows its date, exercise type, intensity, and duration.

- [ ] FT-06: Weekly summary compares logged activity against weekly goals.
  - Action: Open the Summary view and select "This Week".
  - Expected: Each weekly goal shows logged progress against its target (e.g., Running sessions "x / 3", total minutes "x / 150"), and the values match the workouts dated in the current week.
  - Bug Report:
    - Issue: Missing Feature (Summary view)
    - Actual: No Summary view or "This Week" selector exists. The dashboard has no navigation other than the header. Routes /summary, /timeline, and /dashboard all return "404 | Oops! Page not found".

- [ ] FT-07: Monthly summary compares logged activity against goals for the current month.
  - Action: In the Summary view, select "This Month".
  - Expected: Each goal shows logged progress for the current calendar month, and the values match the workouts dated in the current month.
  - Bug Report:
    - Issue: Missing Feature (Summary view)
    - Actual: No Summary view or "This Month" selector exists, so monthly goal progress cannot be opened. Only the dashboard "This Month" stat card (7 workouts, 41.7 km) is present.

- [ ] FT-08: User can sign out.
  - Action: Click "Sign Out".
  - Expected: The user returns to the sign-in page, and the dashboard is no longer displayed.
  - Bug Report:
    - Issue: Missing Element (Sign Out control)
    - Actual: No "Sign Out" control exists. Clicking the unlabeled header icon button returned the user to the sign-in page and hid the dashboard, so the expected outcome occurs, but the control named in the action is absent.

## Constraint

- [ ] CS-01: Sign-in is rejected for an invalid or empty login.
  - Action: (a) Enter a valid email and an incorrect password, then click "Sign In". (b) Leave both fields empty and click "Sign In".
  - Expected: (a) The message "Invalid email or password" appears and the user stays on the sign-in page. (b) Required-field messages appear, no sign-in is attempted, and the dashboard does not load.
  - Bug Report:
    - Issue: Authentication Bypass (incorrect password accepted)
    - Actual: (a) With email alex@example.com and password "wrongpass", the dashboard loaded ("Your Stats" and "Alex Runner" shown), and no "Invalid email or password" message appeared. (b) passed: the message "Please enter both email and password" appeared and the dashboard stayed hidden.

- [ ] CS-02: Workout cannot be saved without Exercise Type and Duration.
  - Action: Open "Log Workout", leave Exercise Type blank, enter Duration "30", and click "Save". Then repeat with Exercise Type selected and Duration blank.
  - Expected: Each attempt is blocked with a message naming the missing required field, and no workout is added to the timeline.
  - Bug Report:
    - Issue: Validation Message Not Naming Field / Untestable Required Field
    - Actual: With Duration blank, Save was blocked, but the only message is the browser-native "Please fill out this field.", which does not name Duration. Exercise Type cannot be left blank: the dropdown always holds a value (Running) and has no empty option, so the first case could not be executed.

- [ ] CS-03: Duration and Distance accept only positive numbers.
  - Action: In "Log Workout", enter Duration "0", then "-10", then "abc" and click "Save". Repeat with a negative Distance.
  - Expected: Each invalid value is rejected with a validation message, and no workout is saved.
  - Bug Report:
    - Issue: Validation Gap (Distance accepts zero)
    - Actual: Duration "0" and "-10" were rejected ("Value must be greater than or equal to 1."), and Distance "-5" was rejected ("Value must be greater than or equal to 0."). Distance "0" was accepted and a workout was saved, which the spec ("positive numbers only") disallows. "abc" could not be entered into the numeric field at all.

- [ ] CS-04: Summary counts only workouts dated within the selected week or month.
  - Action: Open the Summary view for "This Week" and note the Running count. Then open the Timeline and identify a workout dated before the start of the current week (use the existing default data).
  - Expected: The weekly Running count does not include the workout dated before the current week, and the same workout is excluded from the "This Week" totals.
  - Bug Report:
    - Issue: Missing Feature (Summary view)
    - Actual: The Summary view does not exist, so the weekly Running count cannot be read. The seeded Running workout dated Nov 7 (before the week of Nov 9) is excluded from the dashboard "This Week" card (1 workout, 35 min), which is consistent but is not the required check.

- [ ] CS-05: Unauthenticated users cannot access the dashboard.
  - Action: While signed out (or in a new private window), navigate directly to the dashboard or timeline page.
  - Expected: The user is redirected to the sign-in page and no workout or goal data is shown.
  - Bug Report:
    - Issue: Missing Auth Redirect
    - Actual: While signed out, navigating to /dashboard showed "404 | Oops! Page not found" instead of redirecting to sign-in. No /timeline route exists. Visiting the root URL while signed out shows only the sign-in form with no workout or goal data.

## Interaction

- [ ] IX-01: A confirmation toast appears after a workout is saved.
  - Action: Log a valid workout and click "Save".
  - Expected: A toast reading "Workout saved" appears within about 3 seconds, and the log form closes or resets.
  - Bug Report:
    - Issue: Incorrect Toast Text
    - Actual: A toast appeared within the wait (about 0.8 s) and the form closed, but it reads "Workout logged!", not "Workout saved".

- [ ] IX-02: Inline validation errors appear on invalid input and clear once corrected.
  - Action: In "Log Workout", click "Save" with Duration empty. Then enter "30" in Duration.
  - Expected: An error message appears beside the Duration field on the first attempt. It disappears once a valid value is entered.
  - Bug Report:
    - Issue: Missing Inline Validation Message
    - Actual: On the first attempt, no inline error text appeared in the DOM. Only the browser-native tooltip "Please fill out this field." was present. After entering "30", the native error cleared, which is correct.

- [ ] IX-03: Clicking a timeline entry expands it to show full notes.
  - Action: In the Timeline, click the workout logged with notes "Morning run".
  - Expected: The entry expands in place to show the full notes text, and clicking it again collapses the entry.
  - Bug Report:
    - Issue: Unresponsive Element (entry does not expand)
    - Actual: Clicking the "Morning run" entry changed neither its text nor its rendered height (76 px before, after, and after the second click). No expanded state (aria-expanded) was set, so the entry never expands or collapses.

- [ ] IX-04: A goal shows a visible "Goal met" indicator when its target is reached.
  - Action: Open the Summary view for a goal where logged progress equals or exceeds the target (e.g., the Running goal with 3 or more sessions this week, using the default data).
  - Expected: The goal displays a "Goal met" badge or distinct completed styling, and goals not yet reached do not show it.
  - Bug Report:
    - Issue: Missing Indicator (Goal met)
    - Actual: The Running goal reached "3 / 3 times" and then "4 / 3 times", but the page never contains the text "Goal met". The Summary view was not available, and no badge was found on the dashboard goal cards. Completed styling was not verified (DOM-only check).

## Content

- [X] CT-01: Timeline entries display the logged values exactly as entered.
  - Action: Compare the timeline entry for the workout logged in FT-02 (Running, Moderate, 45 min, 5 km, "Morning run") with the values entered.
  - Expected: Exercise type, intensity, duration, distance (with unit), notes, and date all match the entered values exactly.
  - Note: The entry shows "Running | Today | Moderate | 45 min | 5 km | Morning run". The date is shown as the relative label "Today" (2026-11-09), not as a calendar date.

- [X] CT-02: Exercise Type options are relevant fitness activities.
  - Action: Click the Exercise Type dropdown in "Log Workout" and review all options.
  - Expected: Every option is a recognizable exercise or fitness activity (e.g., Running, Cycling, Swimming, Strength Training, Walking), with no unrelated or placeholder entries.
  - Note: Options are Running, Cycling, Swimming, and Weight Training. All are relevant; the list is shorter than the examples.

- [ ] CT-03: Summary labels, units, and date ranges are accurate for today (November 9, 2026).
  - Action: Open the Summary view and check the "This Week" and "This Month" labels, goal labels, and units.
  - Expected: The week range includes November 9, 2026, the month label reads "November 2026", goal labels match the created goals (e.g., "Run 3 times/week", "150 minutes/week"), and minutes and distance are labeled with the correct units.
  - Bug Report:
    - Issue: Missing Feature (Summary view) and Goal Label Mismatch
    - Actual: The Summary view does not exist, so the week range and "November 2026" label cannot be verified. Goal labels are "Run 3 times a week", "Exercise 150 minutes per week", and "Running 3 times per week", not "Run 3 times/week" or "150 minutes/week". Units on the dashboard are correct ("min", "km").
