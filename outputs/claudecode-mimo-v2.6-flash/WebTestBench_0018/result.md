All tests executed. Here is the complete checklist with results.

# Test Result

## Functionality
- [X] FT-01: User can sign in with valid credentials
  - Action: Enter valid username and password on the sign-in page and submit.
  - Expected: User is authenticated and taken to the main fitness tracker page.
- [X] FT-02: User can log a workout with all detail fields
  - Action: Open the workout logging form, enter exercise type (e.g., "Running"), intensity, duration, distance, and notes, then save.
  - Expected: Workout is saved and all five entered values are stored with it.
- [X] FT-03: User can create a frequency-based goal
  - Action: Create a goal of the form "Run three times a week" via the goals section.
  - Expected: The goal is saved and listed among the user's active goals.
- [X] FT-04: User can create a duration-based goal
  - Action: Create a goal of the form "Exercise 150 minutes per week" via the goals section.
  - Expected: The goal is saved and listed among the user's active goals.
- [X] FT-05: Recent workouts timeline displays logged workouts
  - Action: After logging a workout, view the "Recent workouts" timeline.
  - Expected: The timeline shows the workout with its exercise type, duration, and date.
- [ ] FT-06: Summary view compares activity against goals for the current week
  - Action: Open the summary view and select the current-week period.
  - Expected: The view shows this week's logged totals alongside each goal's target (e.g., sessions count vs. 3/week, minutes vs. 150/week).
  - Bug Report:
    - Issue: Missing Summary View / Period Selector (Missing Element)
    - Actual: There is no summary view with a week/month period selector anywhere in the app (routes are only "/" and "*"; the only stats surface is the static "Your Stats" card grid: "This Week 1 workouts", "Week Duration 35 minutes"). The cards are non-clickable, contain no tab/toggle, and never display goal targets (no "vs 3/week" or "150/week"); goal targets appear only as progress bars in the separate Goals section, so the totals are never shown alongside the targets in a summary comparison.
- [ ] FT-07: Summary view compares activity against goals for the current month
  - Action: Open the summary view and select the current-month period.
  - Expected: The view shows this month's logged totals alongside the corresponding goal targets.
  - Bug Report:
    - Issue: Missing Summary View / Period Selector and No Monthly Goal Comparison (Missing Element)
    - Actual: No summary view or month-period selector exists; the static card "This Month 7 workouts" / "Total Distance 41.7 km this month" displays raw totals only. All goals are weekly ("weekly goal"), and no monthly goal target is displayed anywhere, so this month's totals are never compared against goal targets.
- [X] FT-08: User can sign out
  - Action: Click the sign-out control after signing in.
  - Expected: Session ends and the sign-in page is shown; protected pages are no longer accessible.

## Constraint
- [X] CS-01: Workout form cannot be submitted with empty required fields
  - Action: Leave exercise type, intensity, or duration blank and attempt to save the workout.
  - Expected: Submission is blocked and an error identifies the missing required field(s); no workout is created.
- [ ] CS-02: Invalid credentials are rejected
  - Action: Enter a wrong password on the sign-in page and submit.
  - Expected: Sign-in fails with an error message and the user remains on the sign-in page.
  - Bug Report:
    - Issue: No Credential Validation / Authentication Bypass (Invalid Credentials Accepted)
    - Actual: Submitting alex@example.com with the wrong password "WrongPassword123!" signed the user in immediately and rendered the main fitness tracker dashboard; no error message was displayed and the user did not remain on the sign-in page (the form states "Use any email and password to sign in", so no password can ever be rejected).
- [X] CS-03: Non-numeric or non-positive duration/distance is rejected
  - Action: Enter text or a negative number in the duration or distance field and save.
  - Expected: Validation error is shown, the invalid value is not saved, and no workout record is created.
- [X] CS-04: Goal cannot be saved without a valid target value
  - Action: Attempt to save a goal with a blank or zero target (e.g., blank times-per-week).
  - Expected: Submission is blocked with an error; the goal is not added to the list.
- [ ] CS-05: Duplicate sign-in does not occur after session established
  - Action: After signing in, attempt to navigate back to the sign-in page via browser back button.
  - Expected: User is redirected to the authenticated main page rather than being shown a usable sign-in form.
  - Bug Report:
    - Issue: Back Navigation Exits Application Instead of Redirecting (Incorrect History Handling)
    - Actual: Pressing the browser back button after signing in navigated to about:blank (the app leaves the site entirely). The user is never redirected to the authenticated main page as expected — the SPA never pushes history entries for sign-in/sign-out, so the expected in-app redirect cannot occur.

## Interaction
- [X] IX-01: Saving a workout shows a success confirmation
  - Action: Successfully submit a valid workout entry.
  - Expected: A success message/toast (e.g., "Workout saved") appears after submission.
- [X] IX-02: Newly logged workout appears immediately in the timeline
  - Action: Save a workout and return to the timeline without reloading the page.
  - Expected: The new workout is visible at the top of the timeline without a manual refresh.
- [X] IX-03: Creating a goal gives immediate feedback
  - Action: Successfully save a new fitness goal.
  - Expected: A confirmation appears and the new goal is instantly listed in the goals section.
- [ ] IX-04: Invalid sign-in attempt keeps the user in place with visible feedback
  - Action: Submit the sign-in form with an incorrect password.
  - Expected: An inline error or toast is displayed next to the form and form fields remain editable.
  - Bug Report:
    - Issue: Missing Error Feedback / Silent Authentication (No Validation Message)
    - Actual: Submitting an incorrect password produced no inline error and no toast; instead the form was accepted and the user was navigated to the authenticated dashboard, so the sign-in form was not kept in place at all.

## Content
- [X] CT-01: Timeline entries show workout details exactly as entered
  - Action: Log a workout with distinctive values (type "Cycling", intensity "High", duration "45", distance "12", notes "Evening ride") and inspect the timeline entry.
  - Expected: The timeline entry displays "Cycling", "High", "45", "12", and "Evening ride" matching the input, with correct units shown.
- [ ] CT-02: Summary displays the correct current period labels
  - Action: Open the summary view for week and month.
  - Expected: Labels show the actual current week date range and current month name, consistent with today's date.
  - Bug Report:
    - Issue: Missing Period Labels (Incorrect/Incomplete Text)
    - Actual: The stats/summary labels are only "This Week", "Week Duration", "This Month", and "Total Distance" (with units "workouts"/"minutes"/"km this month"). No current-week date range is shown (e.g., Nov 9 – Nov 15 for today, Mon Nov 09 2026) and the current month name ("November 2026") never appears anywhere in the view.
- [X] CT-03: Summary totals match the workouts actually logged
  - Action: Note the total minutes and session count of logged workouts for the current week, then compare with the summary's weekly figures.
  - Expected: The summary's totals equal the sum of the logged workouts (no mismatched or fabricated numbers).
- [X] CT-04: Page content is fitness-focused throughout
  - Action: Review the sign-in, logging, timeline, goals, and summary pages.
  - Expected: All visible headings, labels, and media relate to fitness tracking; no placeholder or off-topic text is displayed.

**Summary: 15/21 PASS, 6/21 FAIL** — failures: FT-06, FT-07 (no summary view with period selector or goal-target comparison), CS-02, IX-04 (any credentials accepted, no invalid-login error), CS-05 (back navigation exits the app instead of redirecting to the main page), CT-02 (no week date range or month name in labels).