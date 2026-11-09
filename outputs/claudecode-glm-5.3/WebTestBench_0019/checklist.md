# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, fill in all required fields (username, email, password) with valid values, and click "Register".
  - Expected: The account is created and the user is logged in (or redirected to the login page and can log in with the new credentials).

- [ ] FT-02: User can add a short bio and interests to their profile
  - Action: Log in, open the profile/settings page, enter a short bio (e.g., "Aspiring web developer") and at least one interest (e.g., "JavaScript"), and save.
  - Expected: The profile page displays the entered bio and interests exactly as saved.

- [ ] FT-03: User can start a new discussion thread in a category
  - Action: Log in, click "New Thread", enter a title and body, select a category from the category dropdown, and submit.
  - Expected: The thread is created and visible in the selected category's thread list with the author's name shown.

- [ ] FT-04: User can reply to an existing thread
  - Action: Log in, open any default thread, click "Reply", enter a reply message, and submit.
  - Expected: The reply appears under the thread's discussion, attributed to the logged-in user.

- [ ] FT-05: User can upvote/like a post
  - Action: Log in, click the upvote/like button on any default post, and note the count, then reload the page.
  - Expected: The vote count increases by 1 and remains incremented after the page reload.

- [ ] FT-06: User can search threads by keyword
  - Action: Type a keyword that appears in a default thread's title (or body) into the search box and submit the search.
  - Expected: Threads containing the keyword are listed; threads not containing the keyword are not shown.

- [ ] FT-07: User can filter threads by category
  - Action: Go to the thread list, select a specific category from the category filter (dropdown or category link).
  - Expected: Only threads belonging to the selected category are displayed.

- [ ] FT-08: Trending/most active discussions are listed for a recent period
  - Action: Open the "Trending" (or "Most Active") section and compare its entries against threads with the most recent replies/upvotes.
  - Expected: The list shows the most active discussions ranked by recent activity (replies/votes within the recent period), not simply all threads or oldest threads.

## Constraint
- [ ] CS-01: Registration cannot be completed with invalid input
  - Action: Open the registration page and submit with an empty required field (and/or mismatched password confirmation).
  - Expected: Submission is blocked with a clear validation error per invalid field; no account is created.

- [ ] CS-02: Duplicate account registration is rejected
  - Action: Attempt to register with a username or email already used by an existing (default) account.
  - Expected: Registration is rejected with an error message indicating the username/email is already taken; no second account is created.

- [ ] CS-03: Guests cannot post, reply, or upvote
  - Action: While logged out, attempt to create a thread, reply to a thread, and upvote a post.
  - Expected: Each action is blocked and the user is prompted to log in or register; no content or vote is created.

- [ ] CS-04: Empty thread or reply cannot be submitted
  - Action: While logged in, open the reply form (or new thread form) and submit without entering any text.
  - Expected: Submission is blocked with a validation message; no empty post appears in the thread.

- [ ] CS-05: A user cannot inflate a post's score with repeated upvotes
  - Action: While logged in, click the upvote button on the same post multiple times.
  - Expected: The post's count increases by at most 1 from that user (e.g., the click toggles the vote off, or is ignored with the button shown as already upvoted); the count never accumulates per extra click.

## Interaction
- [ ] IX-01: Registration success is confirmed to the user
  - Action: Complete a valid registration (see FT-01).
  - Expected: A success message/toast or confirmation page is displayed, or the user is visibly redirected into the logged-in state.

- [ ] IX-02: Upvote button reflects its state visually
  - Action: While logged in, click the upvote button on a default post and observe the button.
  - Expected: The button immediately changes to an active/highlighted state and the count updates in place without a full page reload.

- [ ] IX-03: Clicking a thread in a list opens its detail view
  - Action: On the thread list (or search/filter results), click a thread's title.
  - Expected: The thread detail page opens, showing the original post and its replies.

- [ ] IX-04: Search and filter controls respond immediately
  - Action: Enter a keyword in the search box and submit; then change the category filter selection.
  - Expected: The thread list updates to reflect the new search term or category without requiring a page re-navigation.

## Content
- [ ] CT-01: Thread lists display complete and accurate metadata
  - Action: Inspect the default threads in the main list and in any category view.
  - Expected: Each thread shows its title, author, category, reply count, vote/like count, and creation/last-activity time, and these values match the actual thread data.

- [ ] CT-02: Default thread content matches its category
  - Action: Open several default threads across at least two different categories and read their titles/bodies.
  - Expected: Every thread's subject matter is relevant to the category it is filed under (no miscategorized or off-topic content).

- [ ] CT-03: Profile content is accurate and correctly attributed
  - Action: Open your own profile page and at least one default user's profile.
  - Expected: The bio and interests shown match what was saved for your profile, and other profiles display their own (not swapped or empty-by-default beyond a blank bio) data.

- [ ] CT-04: Trending list activity numbers match actual thread data
  - Action: Compare the reply/vote counts displayed next to each entry in the Trending/Most Active list against the counts shown on those threads' detail pages.
  - Expected: The metrics displayed in the trending list are identical to the actual counts on each thread.