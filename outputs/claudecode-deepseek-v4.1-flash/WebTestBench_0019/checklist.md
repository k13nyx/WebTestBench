# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, enter a valid username, email, and password, and submit the form.
  - Expected: Account is created and the user is logged in or redirected to the login page with a confirmation.
- [ ] FT-02: User can log in with registered credentials
  - Action: Enter the credentials of a registered account on the login page and submit.
  - Expected: User is logged in and their username/avatar appears in the header.
- [ ] FT-03: User can create a profile with bio and interests
  - Action: Go to profile settings, enter a short bio and one or more interests, and save.
  - Expected: Bio and interests are saved and displayed on the user's profile page.
- [ ] FT-04: User can start a new discussion thread in a category
  - Action: Click "New Thread", enter a title and body, select a category, and submit.
  - Expected: The thread is created and appears in the selected category's thread list.
- [ ] FT-05: User can reply to an existing thread
  - Action: Open any default thread, enter reply text in the reply box, and submit.
  - Expected: The reply is posted and appears at the end of the thread's reply list.
- [ ] FT-06: User can upvote/like a helpful post or thread
  - Action: Click the upvote/like button on a default thread or reply.
  - Expected: The vote is recorded and the vote count increases by one.
- [ ] FT-07: User can search threads by keyword
  - Action: Enter a keyword that matches a default thread title into the search field and submit.
  - Expected: A results list shows threads matching the keyword.
- [ ] FT-08: User can filter threads by category
  - Action: Select a category from the category filter/sidebar.
  - Expected: Only threads belonging to the selected category are listed.
- [ ] FT-09: User can view trending or most active discussions over a recent period
  - Action: Open the trending/most active section (e.g., "Trending this week").
  - Expected: A list of threads ranked by recent activity is displayed for the stated recent period.

## Constraint
- [ ] CS-01: Registration is rejected when the email/username already exists
  - Action: Register using an email or username already tied to a default account.
  - Expected: Submission is blocked and an error such as "Email already in use" is shown.
- [ ] CS-02: Registration/submission is rejected when required fields are empty
  - Action: Submit the registration form with required fields (username, email, password) left blank.
  - Expected: Submission is blocked and validation errors identify the empty required fields.
- [ ] CS-03: Logged-out users cannot start threads or reply
  - Action: While logged out, attempt to start a thread or submit a reply.
  - Expected: Action is blocked and the user is prompted to log in.
- [ ] CS-04: Thread or reply with empty content cannot be submitted
  - Action: Attempt to submit a new thread or reply with an empty title/body.
  - Expected: Submission is blocked with a message that content is required.
- [ ] CS-05: A user cannot upvote the same post more than once
  - Action: Upvote a post, then click the upvote button on the same post again.
  - Expected: The vote toggles/removes rather than incrementing the count above one per user.

## Interaction
- [ ] IX-01: Vote count updates immediately after upvoting
  - Action: Click the upvote/like button on a post and observe the count.
  - Expected: The displayed vote count updates without a full page reload.
- [ ] IX-02: Success feedback is shown after key actions
  - Action: Complete registration, thread creation, and reply submission.
  - Expected: A success toast/message confirms each successful action.
- [ ] IX-03: Active category filter is visually indicated
  - Action: Select a category in the filter.
  - Expected: The selected category is highlighted/marked as active, and updates when another is chosen.

## Content
- [ ] CT-01: Profile page displays the user's bio and interests
  - Action: Open a profile that has a bio and interests set.
  - Expected: The short bio and the list of interests are shown on the profile.
- [ ] CT-02: Thread list items show required metadata
  - Action: View any category's thread list or search results.
  - Expected: Each thread shows its title, author, category, vote count, reply count, and posting time.
- [ ] CT-03: Trending list shows activity metric and stated time period
  - Action: View the trending/most active list.
  - Expected: The list displays the recent period (e.g., "this week") and an activity indicator (votes/replies) consistent with the ranking.