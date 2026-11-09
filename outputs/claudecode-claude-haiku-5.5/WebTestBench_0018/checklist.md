# Test Checklist

## Functionality
- [ ] FT-01: User can sign in with valid credentials and reach the dashboard.
  - Action: On the sign-in page, enter a valid email and password, then click "Sign In".
  - Expected: The dashboard loads, the user's name or account is shown in the header, and a "Sign Out" option is visible.
- [ ] FT-02: User can log a workout with all fields filled in.
  - Action: Click "Log Workout". Set Exercise Type "Running", Intensity "Moderate", Duration "45" min, Distance "5" km, Notes "Morning run". Click "Save".
  - Expected: The workout is saved and appears in the Recent Workouts timeline with every entered value.
- [ ] FT-03: User can create a goal of running three times a week.
  - Action: Click "Add Goal". Select activity "Running", target "3", period "Weekly". Click "Save".
  - Expected: The goal "Run 3 times/week" is listed on the goals list with progress for the current week shown as "x / 3".
- [ ] FT-04: User can create a goal of 150 activity minutes per week.
  - Action: Click "Add Goal". Select goal type "Total minutes" (all activities), target "150", period "Weekly". Click "Save".
  - Expected: The goal "150 minutes/week" is listed with progress for the current week shown as "x / 150 min".
- [ ] FT-05: Timeline shows recent workouts in newest-first order.
  - Action: Open the Timeline (or the dashboard's Recent Workouts section) with at least two logged workouts on different dates.
  - Expected: Entries are sorted by date, newest at the top, and each entry shows its date, exercise type, intensity, and duration.
- [ ] FT-06: Weekly summary compares logged activity against weekly goals.
  - Action: Open the Summary view and select "This Week".
  - Expected: Each weekly goal shows logged progress against its target (e.g., Running sessions "x / 3", total minutes "x / 150"), and the values match the workouts dated in the current week.
- [ ] FT-07: Monthly summary compares logged activity against goals for the current month.
  - Action: In the Summary view, select "This Month".
  - Expected: Each goal shows logged progress for the current calendar month, and the values match the workouts dated in the current month.
- [ ] FT-08: User can sign out.
  - Action: Click "Sign Out".
  - Expected: The user returns to the sign-in page, and the dashboard is no longer displayed.

## Constraint
- [ ] CS-01: Sign-in is rejected for an invalid or empty login.
  - Action: (a) Enter a valid email and an incorrect password, then click "Sign In". (b) Leave both fields empty and click "Sign In".
  - Expected: (a) The message "Invalid email or password" appears and the user stays on the sign-in page. (b) Required-field messages appear, no sign-in is attempted, and the dashboard does not load.
- [ ] CS-02: Workout cannot be saved without Exercise Type and Duration.
  - Action: Open "Log Workout", leave Exercise Type blank, enter Duration "30", and click "Save". Then repeat with Exercise Type selected and Duration blank.
  - Expected: Each attempt is blocked with a message naming the missing required field, and no workout is added to the timeline.
- [ ] CS-03: Duration and Distance accept only positive numbers.
  - Action: In "Log Workout", enter Duration "0", then "-10", then "abc" and click "Save". Repeat with a negative Distance.
  - Expected: Each invalid value is rejected with a validation message, and no workout is saved.
- [ ] CS-04: Summary counts only workouts dated within the selected week or month.
  - Action: Open the Summary view for "This Week" and note the Running count. Then open the Timeline and identify a workout dated before the start of the current week (use the existing default data).
  - Expected: The weekly Running count does not include the workout dated before the current week, and the same workout is excluded from the "This Week" totals.
- [ ] CS-05: Unauthenticated users cannot access the dashboard.
  - Action: While signed out (or in a new private window), navigate directly to the dashboard or timeline page.
  - Expected: The user is redirected to the sign-in page and no workout or goal data is shown.

## Interaction
- [ ] IX-01: A confirmation toast appears after a workout is saved.
  - Action: Log a valid workout and click "Save".
  - Expected: A toast reading "Workout saved" appears within about 3 seconds, and the log form closes or resets.
- [ ] IX-02: Inline validation errors appear on invalid input and clear once corrected.
  - Action: In "Log Workout", click "Save" with Duration empty. Then enter "30" in Duration.
  - Expected: An error message appears beside the Duration field on the first attempt. It disappears once a valid value is entered.
- [ ] IX-03: Clicking a timeline entry expands it to show full notes.
  - Action: In the Timeline, click the workout logged with notes "Morning run".
  - Expected: The entry expands in place to show the full notes text, and clicking it again collapses the entry.
- [ ] IX-04: A goal shows a visible "Goal met" indicator when its target is reached.
  - Action: Open the Summary view for a goal where logged progress equals or exceeds the target (e.g., the Running goal with 3 or more sessions this week, using the default data).
  - Expected: The goal displays a "Goal met" badge or distinct completed styling, and goals not yet reached do not show it.

## Content
- [ ] CT-01: Timeline entries display the logged values exactly as entered.
  - Action: Compare the timeline entry for the workout logged in FT-02 (Running, Moderate, 45 min, 5 km, "Morning run") with the values entered.
  - Expected: Exercise type, intensity, duration, distance (with unit), notes, and date all match the entered values exactly.
- [ ] CT-02: Exercise Type options are relevant fitness activities.
  - Action: Click the Exercise Type dropdown in "Log Workout" and review all options.
  - Expected: Every option is a recognizable exercise or fitness activity (e.g., Running, Cycling, Swimming, Strength Training, Walking), with no unrelated or placeholder entries.
- [ ] CT-03: Summary labels, units, and date ranges are accurate for today (November 9, 2026).
  - Action: Open the Summary view and check the "This Week" and "This Month" labels, goal labels, and units.
  - Expected: The week range includes November 9, 2026, the month label reads "November 2026", goal labels match the created goals (e.g., "Run 3 times/week", "150 minutes/week"), and minutes and distance are labeled with the correct units.