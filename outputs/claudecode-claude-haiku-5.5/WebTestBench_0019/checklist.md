# Test Checklist

## Functionality
- [ ] FT-01: Register a new account and log in
  - Action: Click "Register", enter a unique username, email, and password, submit, then log in with the same credentials.
  - Expected: Registration succeeds with a confirmation, and the header shows the new username after login.
- [ ] FT-02: Save bio and interests on the profile
  - Action: Open the profile, click "Edit Profile", enter a short bio and select one or more interests, click "Save".
  - Expected: The saved bio and interests appear on the profile page after a page reload.
- [ ] FT-03: Create a discussion thread in a category
  - Action: Click "New Thread", select a category, enter a title and body, click "Post Thread".
  - Expected: The thread appears in the selected category's list with the correct title, category, and author name.
- [ ] FT-04: Reply to a thread
  - Action: Open any existing thread, type text in the reply box, click "Post Reply".
  - Expected: The reply appears at the bottom of the thread with the author name and timestamp, and the reply count increases by 1.
- [ ] FT-05: Upvote a helpful post
  - Action: Open a thread by another user, click the upvote (▲) button on the thread or a reply.
  - Expected: The vote count increases by 1 and the upvote button shows an active state.
- [ ] FT-06: Search threads by keyword
  - Action: Type a word that appears in an existing thread title into the search bar, press Enter.
  - Expected: Results list threads whose title or body contains that keyword.
- [ ] FT-07: Filter threads by category
  - Action: Select one category from the "Category" filter dropdown.
  - Expected: Only threads belonging to the selected category are listed.
- [ ] FT-08: View trending/most active discussions
  - Action: Open the "Trending" (or "Most Active") section from the forum home.
  - Expected: A list of threads is shown, ordered from most to least active over the recent period, with the period label displayed.

## Constraint
- [ ] CS-01: Registration requires valid, complete fields
  - Action: Submit the registration form with username, email, or password left empty; then submit with email "userexample.com".
  - Expected: Submission is blocked, each empty or invalid field shows an error message, and no account is created.
- [ ] CS-02: Duplicate username or email is rejected
  - Action: Register using the username or email of an existing default user.
  - Expected: Registration is blocked with a "already taken" or "already registered" error, and no new account is created.
- [ ] CS-03: New thread requires title, body, and category
  - Action: Open "New Thread" and click "Post Thread" with the title, body, or category left empty.
  - Expected: Posting is blocked with an error message for each missing field, and no thread is created.
- [ ] CS-04: Empty replies are not allowed
  - Action: Open a thread, leave the reply box empty (or only spaces), click "Post Reply".
  - Expected: Posting is blocked and no reply is added to the thread.
- [ ] CS-05: One vote per user per post
  - Action: Upvote the same post twice.
  - Expected: The vote count changes by at most 1 across both clicks; the second click does not increase the count again.
- [ ] CS-06: Guests cannot post, reply, or vote
  - Action: Log out, then click "New Thread", "Post Reply", and the upvote button.
  - Expected: Each action is blocked and the user is redirected to the login page or shown a login prompt; no content or vote is recorded.

## Interaction
- [ ] IX-01: Success message after creating a thread
  - Action: Create a valid thread using "Post Thread".
  - Expected: A success toast or message reading "Thread created" appears, and the user is taken to the new thread or the category list.
- [ ] IX-02: Upvote updates instantly without reload
  - Action: Click the upvote button on a post and observe the button and counter without refreshing.
  - Expected: The button changes to its active (highlighted) state and the counter updates immediately.
- [ ] IX-03: Empty search result message
  - Action: Search for "zzqxnomatch" in the search bar and press Enter.
  - Expected: The results area shows the message "No results found" and no threads are listed.

## Content
- [ ] CT-01: Search results match the keyword
  - Action: Search for a keyword from FT-06 and review every result listed.
  - Expected: Every result contains the keyword in its title or body, and no unrelated threads appear.
- [ ] CT-02: Trending list shows only recent activity
  - Action: Open the Trending section and compare each thread's last-activity date with the period label shown.
  - Expected: Every listed thread has activity within the displayed period, and the activity dates are consistent with the sort order.
- [ ] CT-03: Author profile data is consistent across the forum
  - Action: Open the profile saved in FT-02, then click the author name on a thread or reply that user posted.
  - Expected: The author profile shows the same username, bio, and interests as those saved in FT-02.