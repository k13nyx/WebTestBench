# Test Result

## Functionality

- [X] **FT-01: User can sign in to the meditation application.**
  - **Action:** Enter valid credentials for a preconfigured account and select **“Sign in.”**
  - **Expected:** The user is authenticated and taken to the meditation dashboard.

- [X] **FT-02: Dashboard displays recommended meditation activities.**
  - **Action:** Open the dashboard after signing in.
  - **Expected:** The dashboard displays recommended activities including meditations, breathing exercises, and relaxation techniques.

- [X] **FT-03: User can filter activities by duration.**
  - **Action:** Select an available duration filter.
  - **Expected:** Only activities matching the selected duration are displayed.

- [X] **FT-04: User can filter activities by goal.**
  - **Action:** Select each available goal filter, including **Sleep**, **Focus**, and **Stress Relief**.
  - **Expected:** Only activities matching the selected goal are displayed.

- [X] **FT-05: User can combine duration and goal filters.**
  - **Action:** Select one duration filter and one goal filter.
  - **Expected:** Every displayed activity matches both the selected duration and selected goal.

- [X] **FT-06: User can start an activity session.**
  - **Action:** Select an activity and choose **“Start”** or **“Begin session.”**
  - **Expected:** The selected timed session opens and begins with its first guidance step.

- [X] **FT-07: User can complete a timed session.**
  - **Action:** Follow the on-screen guidance until the session timer ends.
  - **Expected:** The session reaches a completed state and the application records the session as completed.

- [X] **FT-08: User can view completed-session history or progress over time.**
  - **Action:** Open the progress, history, or session tracking area after completing a session.
  - **Expected:** The completed session appears and the total completed-session count reflects it.

- [X] **FT-09: User can save an activity as a favorite.**
  - **Action:** Select the favorite control for an activity.
  - **Expected:** The activity is saved to the user’s favorites.

- [X] **FT-10: User can access the personal favorites list.**
  - **Action:** Open the **Favorites** or personal list area.
  - **Expected:** All activities previously saved by the signed-in user are displayed in the list.

- [X] **FT-11: User can remove an activity from favorites.**
  - **Action:** Select the active favorite control for a saved activity.
  - **Expected:** The activity is removed from the personal favorites list.

## Constraint

- [X] **CS-01: Personal data and session tracking require authentication.**
  - **Action:** Sign out, then attempt to open the dashboard’s favorites or progress area.
  - **Expected:** The application does not expose the signed-in user’s favorites or completion history and instead requests sign-in.

- [X] **CS-02: Only completed sessions increase the completion count.**
  - **Action:** Start a session and leave or stop it before the timer ends, then view session tracking.
  - **Expected:** The abandoned or incomplete session is not recorded as a completed session.

- [X] **CS-03: An activity cannot appear more than once in the favorites list.**
  - **Action:** Select the favorite control for the same activity multiple times without removing it.
  - **Expected:** The activity appears only once in the personal favorites list.

- [X] **CS-04: Clearing activity filters restores the unfiltered activity set.**
  - **Action:** Apply duration and goal filters, then select **“Clear filters”** or equivalent.
  - **Expected:** The dashboard displays activities without the previously applied duration or goal restrictions.

## Interaction

- [X] **IX-01: Session timer and progress indicator update during an active session.**
  - **Action:** Start a timed session and observe the timer and progress indicator while the session is running.
  - **Expected:** The timer advances toward completion and the progress indicator reflects the current session progress.

- [X] **IX-02: Step-by-step guidance advances during the session.**
  - **Action:** Follow the session controls through each guidance step.
  - **Expected:** The current instruction changes to the next step only when the appropriate step transition occurs, and the active step is clearly indicated.

- [X] **IX-03: Applying filters updates the dashboard without showing stale results.**
  - **Action:** Change the duration or goal filter several times.
  - **Expected:** The displayed activity cards update to match the current filter selection, and activities from the previous selection are removed.

- [X] **IX-04: Session completion provides clear completion feedback.**
  - **Action:** Allow a timed session to reach its end.
  - **Expected:** A clear completion state or confirmation is displayed, and the user is given an option to return to the dashboard or view progress.

## Content

- [X] **CT-01: Each activity identifies its type, duration, and goal.**
  - **Action:** Inspect the available meditation, breathing, and relaxation activity cards.
  - **Expected:** Each activity displays accurate, readable information identifying its activity type, duration, and applicable goal.

- [X] **CT-02: Session guidance is relevant to meditation, breathing, or relaxation.**
  - **Action:** Open at least one activity from each available activity type and review its step-by-step instructions.
  - **Expected:** The instructions are complete, understandable, and directly relevant to the selected activity and its stated goal.