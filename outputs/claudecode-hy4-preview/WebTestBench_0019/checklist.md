# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the Register/Sign Up page, fill in username, email, and password with unique valid values, and submit.
  - Expected: Registration succeeds and the user is logged in — username/profile link appears in the header.

- [ ] FT-02: Registered user can log out and log back in
  - Action: Click Log Out, then log in again using the credentials from FT-01.
  - Expected: Login succeeds and the same user is signed in (no new account created).

- [ ] FT-03: User can add a short bio and interests to their profile
  - Action: Go to My Profile → Edit Profile, enter a short bio (e.g. "Loves hiking and Python") and at least one interest/tag, then Save.
  - Expected: Profile saves; the profile page displays the entered bio and interests.

- [ ] FT-04: User can start a new discussion thread in a category
  - Action: Click New Thread / Create Thread, enter a title and body, select a category, and submit.
  - Expected: Thread is created and appears in the thread list and its selected category.

- [ ] FT-05: User can reply to an existing thread
  - Action: Open any default thread and post a reply using the reply box.
  - Expected: Reply is added and appears under the thread's original post with the replier's name.

- [ ] FT-06: User can upvote/like a helpful post
  - Action: While logged in, click the Like/Upvote control on another user's post.
  - Expected: The post's vote/like count increases by exactly 1.

- [ ] FT-07: User can search threads by keyword
  - Action: Type a word present in a default thread title (e.g. a keyword from an existing thread) into the Search box and submit.
  - Expected: Results list appears and every returned thread contains that keyword in its title or body.

- [ ] FT-08: User can filter threads by category
  - Action: Select a specific category from the category filter/dropdown on the threads page.
  - Expected: Only threads belonging to that category are listed; threads from other categories are absent.

- [ ] FT-09: Trending / most active discussions for a recent period are listed
  - Action: Open the Trending / Most Active section on the forum home page.
  - Expected: A non-empty list of threads is shown, ordered from highest activity to lowest, and is labeled with the recent period (e.g. "Today", "This Week", "Last 7 days").

## Constraint
- [ ] CS-01: Registration rejects duplicate or invalid email
  - Action: Register with an email already used by FT-01, and again with a malformed value (e.g. "notanemail").
  - Expected: Both attempts are rejected with a visible error message and no account is created.

- [ ] CS-02: Registration rejects empty required fields
  - Action: Submit the registration form with username and password left blank.
  - Expected: Submission is blocked and required-field error messages are shown.

- [ ] CS-03: Logged-out visitor cannot create a thread or reply
  - Action: Log out, then attempt to open the New Thread page and to submit a reply on a thread.
  - Expected: Both actions are blocked — user is prompted to log in or the controls are unavailable; no thread/reply is created.

- [ ] CS-04: Thread creation requires a title and a category
  - Action: Submit the new thread form with an empty title, then with a title but no category selected.
  - Expected: Both submissions are rejected with validation errors; no empty or uncategorized thread is created.

- [ ] CS-05: A single user can only count as one vote per post
  - Action: Click Like/Upvote on the same post 3 times in a row.
  - Expected: Count ends at +1 (or returns to unvoted if toggled off) — never increases past one per user.

## Interaction
- [ ] IX-01: Like control shows an active/upvoted state after clicking
  - Action: Click Like/Upvote once on a post and observe the control after the update.
  - Expected: The control appears in a visually distinct active/upvoted state and the new count is shown immediately.

- [ ] IX-02: Trending list updates when the recent period is changed
  - Action: In the Trending section, switch the period selector (e.g. from "Today" to "This Week").
  - Expected: The listed threads and/or their order change to reflect the newly selected period.

- [ ] IX-03: Success feedback is shown after posting a thread or reply
  - Action: Create a thread, then post a reply, observing the screen each time.
  - Expected: A confirmation message or redirect to the new content appears for each successful post.

## Content
- [ ] CT-01: Thread list entries show complete thread metadata
  - Action: View the main threads list and inspect any 3 entries.
  - Expected: Each entry displays title, author name, category name, and reply count/like count (and timestamp).

- [ ] CT-02: Forum categories are meaningful topics with no placeholder text
  - Action: Open the category filter/list and read all available category names.
  - Expected: All categories are coherent community forum topics with no "Lorem ipsum", "Test", or "Category 1" style placeholders.

- [ ] CT-03: Profile page shows the correct bio and interests for that user
  - Action: View the profile of the user edited in FT-03 and of another default user.
  - Expected: Each profile shows its own username, bio, and interest tags — no blank, mismatched, or placeholder content.