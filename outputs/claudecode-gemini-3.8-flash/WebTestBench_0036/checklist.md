# Test Checklist

## Functionality
- [ ] FT-01: User sign in with valid credentials
  - Action: Enter valid username and password into the sign-in form and click "Sign In".
  - Expected: User is authenticated and redirected to the personal meditation dashboard.
- [ ] FT-02: Filter activities by duration and goal
  - Action: Select a duration (e.g., "10 min") and a goal (e.g., "Stress Relief") from the filter options.
  - Expected: The activity list updates to display only items that match both selected criteria.
- [ ] FT-03: Launch an interactive timed session
  - Action: Click "Start Session" on any activity card.
  - Expected: Session view opens with an active countdown timer, step-by-step guidance instructions, and a progress indicator.
- [ ] FT-04: Complete a session and update tracking history
  - Action: Allow a session timer to finish (or click "Complete Session") and return to the dashboard.
  - Expected: Session ends successfully, and the total completed sessions counter increases by 1.
- [ ] FT-05: Add activity to personal favorites list
  - Action: Click the "Favorite" heart icon on an activity card.
  - Expected: Activity is saved and appears within the "My Favorites" dashboard section.
- [ ] FT-06: Remove activity from personal favorites list
  - Action: Click the active "Favorite" icon on an activity within the "My Favorites" list.
  - Expected: Activity is immediately removed from the "My Favorites" list.

## Constraint
- [ ] CS-01: Prevent sign-in submission with empty fields
  - Action: Click "Sign In" leaving username and password input fields blank.
  - Expected: Form submission is blocked, and validation messages prompt the user to enter required credentials.
- [ ] CS-02: Handle filter combinations yielding no matches
  - Action: Select duration and goal filter combinations that have no matching content.
  - Expected: Displays a "No activities found" empty state message without breaking the page layout.
- [ ] CS-03: Maintain timer state upon pause and resume
  - Action: Start a timed session, click "Pause", wait 3 seconds, and click "Resume".
  - Expected: Timer pauses countdown accurately and resumes counting down from the paused timestamp without resetting.
- [ ] CS-04: Incomplete session does not increment completion tracker
  - Action: Start a session and click "Exit Session" before completing the guided steps.
  - Expected: Session closes, user returns to dashboard, and the completed sessions count remains unchanged.

## Interaction
- [ ] IX-01: Toggle visual state of favorite button
  - Action: Click the "Favorite" icon on an unselected activity card.
  - Expected: Icon state immediately updates from outline to filled with an updated active status.
- [ ] IX-02: Dynamic progress bar update during session guidance
  - Action: Advance to the next step during an active guided session.
  - Expected: The guidance text updates smoothly, and the session progress bar visually advances proportionally.
- [ ] IX-03: Reset applied filters to default state
  - Action: Click "Clear Filters" after applying duration and goal criteria.
  - Expected: All filter selectors return to their default unselected state, and all recommended activities reappear.

## Content
- [ ] CT-01: Activity category presence on dashboard
  - Action: Inspect the recommended activity sections on the dashboard.
  - Expected: Clear sections or tags for "Meditations", "Breathing Exercises", and "Relaxation Techniques" are visible.
- [ ] CT-02: Relevant wellness goal filter options
  - Action: Open the goal filter options menu.
  - Expected: Filter options include "Sleep", "Focus", and "Stress Relief".
- [ ] CT-03: Completed session statistics display
  - Action: View the session tracking widget on the user dashboard.
  - Expected: Displays a labeled summary of completed sessions over time (e.g., total sessions completed count and weekly activity summary).