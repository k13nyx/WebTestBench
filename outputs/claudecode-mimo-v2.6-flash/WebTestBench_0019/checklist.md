# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, enter a username, email, and password, then submit the form.
  - Expected: The account is created and the user is signed in (or directed to sign in), with the new account usable for forum actions.

- [ ] FT-02: User can create a profile with bio and interests
  - Action: Navigate to the profile editing page, enter a short bio and one or more interests, then save.
  - Expected: The profile is saved and displays the entered bio and interests.

- [ ] FT-03: User can start a new discussion thread in a category
  - Action: Select a category, click the button to create a new thread, enter a title and body, then submit.
  - Expected: The new thread is created, appears in the chosen category's thread list, and opens with the posted content.

- [ ] FT-04: User can reply to an existing thread
  - Action: Open any default thread, enter a reply in the reply box, and submit it.
  - Expected: The reply appears in the thread's reply list with the user's name and the entered text.

- [ ] FT-05: User can upvote/like a post
  - Action: Click the upvote/like control on a post or reply.
  - Expected: The upvote/like count increases by 1 and the control shows an active/selected state.

- [ ] FT-06: User can search threads by keyword
  - Action: Enter a keyword that appears in an existing default thread title or body into the search field and submit.
  - Expected: A results list is shown containing threads matching the keyword, including the expected default thread.

- [ ] FT-07: User can filter threads by category
  - Action: Select a specific category from the category filter/list.
  - Expected: Only threads belonging to that category are displayed.

- [ ] FT-08: User can view a trending/most-active discussions list
  - Action: Navigate to the trending or most active discussions view.
  - Expected: A ranked list of threads is displayed, ordered by recent activity or popularity over a recent time period.

## Constraint
- [ ] CS-01: Registration cannot be submitted with empty required fields
  - Action: On the registration form, leave one or more required fields (e.g., username, email, password) empty and submit.
  - Expected: The form is rejected with a validation error; no account is created.

- [ ] CS-02: Duplicate username/email cannot be registered
  - Action: Attempt to register using credentials that already exist in the application's default data.
  - Expected: Registration is rejected with a clear error indicating the username or email is already taken.

- [ ] CS-03: Thread cannot be created without a title and body
  - Action: Open the new-thread form, leave the title or body empty, and submit.
  - Expected: Submission is blocked with a validation error; no thread is created.

- [ ] CS-04: Reply cannot be submitted while the reply box is empty
  - Action: On a thread page, submit the reply control with an empty reply box.
  - Expected: No reply is posted and a validation error is shown.

- [ ] CS-05: A user cannot upvote the same post twice
  - Action: Click the upvote/like control on the same post once, then click it again.
  - Expected: The count increases only once; the second action either is rejected or toggles off, never double-counting.

- [ ] CS-06: Guest users cannot post or vote
  - Action: While signed out, attempt to create a thread, reply, or upvote a post.
  - Expected: The action is blocked and the user is prompted to register or sign in; no content or vote is recorded.

## Interaction
- [ ] IX-01: Voting provides immediate visual feedback
  - Action: Click the upvote/like control on a post.
  - Expected: The count and active state update instantly without a full page reload, and clicking again reverts the state.

- [ ] IX-02: Search and category filter respond immediately to user input
  - Action: Type a keyword into search and submit, then change the category filter.
  - Expected: The thread list updates to reflect the search term and selected category, showing a clear empty state when nothing matches.

- [ ] IX-03: Successful actions confirm completion
  - Action: Complete each of: registering, saving a profile, creating a thread, and posting a reply.
  - Expected: Each action shows a visible success confirmation (e.g., message/toast) and the new content appears on screen.

## Content
- [ ] CT-01: Profiles display the entered bio and interests accurately
  - Action: Open a profile page after saving a bio and interests.
  - Expected: The displayed bio and interest tags match exactly what was entered.

- [ ] CT-02: Thread and reply content is displayed faithfully
  - Action: Create a thread with a known title/body, then reply with known text, and view the thread.
  - Expected: The title, body, and reply text are shown verbatim, along with the correct author name and category label.

- [ ] CT-03: Trending list shows relevant, correctly labeled thread data
  - Action: Open the trending/most active discussions view.
  - Expected: Each entry shows a relevant thread title with its category and an activity indicator (e.g., reply count or last-activity time), with no placeholder or unrelated content.