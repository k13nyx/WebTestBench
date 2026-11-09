# Test Result

## Functionality
- [X] FT-01: Register a new user account with valid credentials.
  - Action: Open the registration form, fill in a unique username, email, and password, then click "Register"/"Sign Up".
  - Expected: The account is created and the user is signed in (or redirected to login with a confirmation).

- [ ] FT-02: Log in with a registered account.
  - Action: Enter the registered username/email and password, then click "Log In".
  - Expected: The user is authenticated and the header shows the logged-in username or profile link.
  - Bug Report:
    - Issue: Incorrect Form Submission / Authentication Failure — credentials of a freshly registered account are rejected at login.
    - Actual: After registering "login_tester" (login_tester@test.com / LoginPass123!) in the same session (toast: "Account created! Welcome to ThreadHive!"), logging out, and submitting those exact credentials on the login form (Email + Password, "Sign In" button), the app responds with the toast "Invalid credentials. Try: tech@example.com" and keeps the user on /login. The header does not show the logged-in username or profile link. The same failure occurred for the earlier-registered qa_tester@example.com / TestPass123!. Only the seeded demo accounts (tech@example.com, gamer@example.com) appear acceptable to the login.

- [X] FT-03: Save a profile with a short bio and interests.
  - Action: Open "Edit Profile", enter a short bio and one or more interests, then click "Save".
  - Expected: The changes are saved and shown on the profile page.

- [X] FT-04: Start a new discussion thread in a category.
  - Action: Click "New Thread", enter a title and body, select one of the existing categories, then submit.
  - Expected: The thread is created and appears in the thread list of the selected category.

- [X] FT-05: Reply to an existing thread.
  - Action: Open an existing default thread, type a reply, then click "Post Reply".
  - Expected: The reply appears in the thread's reply list with its author and content.

- [X] FT-06: Upvote or like a post.
  - Action: Click the upvote/like button on an existing post.
  - Expected: The post's vote/like count increases by 1 and no error occurs.

- [X] FT-07: Search threads by keyword.
  - Action: Type a keyword that appears in a default thread's title into the search field and submit.
  - Expected: A results list containing the matching thread(s) is displayed.

- [X] FT-08: Filter threads by category.
  - Action: Select one existing category from the category filter control.
  - Expected: The thread list updates to show only threads belonging to that category.

- [X] FT-09: View trending/most active discussions.
  - Action: Open the "Trending"/"Most Active" section.
  - Expected: A non-empty list of discussions from a recent period is shown, ordered by most activity.

## Constraint
- [ ] CS-01: Duplicate registration is rejected.
  - Action: Attempt to register with a username or email already used by an existing account.
  - Expected: Registration is blocked with a validation message and no duplicate account is created.
  - Bug Report:
    - Issue: Missing Duplicate-Account Validation / Incorrect Form Submission.
    - Actual: Registering with the already-used username "qa_user_ft01" and already-used email "qa_tester@example.com" succeeds with the toast "Account created! Welcome to ThreadHive!" and redirects to the home page. Within a single session, re-registering the same username "dup_user" with a different email also succeeds ("Account created!"), as does re-using the same email "dup_email@test.com" with a different username. No validation message is shown and duplicate accounts are created every time.

- [X] CS-02: Registration cannot be submitted with empty required fields.
  - Action: Submit the registration form with an empty username, then empty email, then empty password.
  - Expected: Each submission is blocked with a validation message; no account is created.

- [ ] CS-03: Thread cannot be created with missing title, body, or category.
  - Action: Submit the new-thread form with an empty title, then with an empty body, then with no category selected.
  - Expected: Each submission is blocked with a validation message; no thread is created.
  - Bug Report:
    - Issue: Missing Category Validation on Thread Creation.
    - Actual: Empty title and empty body are correctly blocked with the toast "Please fill in all fields", but submitting the new-thread form with title and content while no category is selected (dropdown left on "Select a category") creates the thread anyway without any validation message — the thread "CS-03 no category test" was created and filed under "General Discussion" (auto-assigned default category). No thread should be created in this case.

- [ ] CS-04: Reply cannot be submitted empty.
  - Action: Click "Post Reply" in a thread without typing any reply text.
  - Expected: Submission is blocked with a validation message; no empty reply is added.
  - Bug Report:
    - Issue: Missing Validation Message on Empty Reply.
    - Actual: Empty-reply submission is blocked, but silently: while the reply textarea is empty the "Post Reply" button is disabled (a forced click triggers no action), no reply is added and the reply count stays "Replies (3)", yet no validation message is displayed anywhere (no toast, no inline error). The expected "blocked with a validation message" feedback is missing.

- [X] CS-05: Logged-out users cannot post or vote.
  - Action: While logged out, attempt to start a thread, post a reply, and upvote a post.
  - Expected: Each action is blocked (user is prompted to log in); no thread, reply, or vote is created.

## Interaction
- [X] IX-01: Success confirmation appears after creating a thread.
  - Action: Successfully create a thread (per FT-04) and observe the page immediately after submission.
  - Expected: A success toast/confirmation message (e.g., "Thread created") is displayed.

- [X] IX-02: Upvote provides immediate visual feedback.
  - Action: Click the upvote/like button on a post and observe the button and its counter.
  - Expected: The counter increments by 1 and the button switches to an active/selected state immediately.

- [X] IX-03: Hovering over interactive elements shows a visual state change.
  - Action: Hover over a thread title/row and a primary button (e.g., "New Thread") without clicking.
  - Expected: Each element displays a visible hover effect (highlight, color change, or underline).

## Content
- [X] CT-01: Thread lists show complete thread metadata.
  - Action: View the main thread list and one category's thread list.
  - Expected: Each thread entry shows title, author name, category, and activity info (reply count and/or vote count) matching the actual data.

- [X] CT-02: Profile displays the saved bio and interests.
  - Action: Open the profile page of the account whose bio and interests were saved in FT-03.
  - Expected: The bio and interests are displayed exactly as entered.

- [X] CT-03: Trending entries show relevant activity data.
  - Action: View the "Trending"/"Most Active" list.
  - Expected: Each entry shows the thread title and activity information (e.g., reply count, last activity date), and the listed threads are the most recently active default threads.
