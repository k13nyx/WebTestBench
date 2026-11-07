# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Open the Register/Sign Up page, fill in username, email, and password with unique valid values, and submit.
  - Expected: Registration succeeds and the user is logged in — username/profile link appears in the header.

- [ ] FT-02: Registered user can log out and log back in
  - Action: Click Log Out, then log in again using the credentials from FT-01.
  - Expected: Login succeeds and the same user is signed in (no new account created).
  - Bug Report:
    - Issue: Incorrect Login Authentication / Account Not Persisted
    - Actual: Log Out works (header reverts to "Login / Register"). Logging back in with `qa_tester_01@example.com` / `TestPass123!` stays on `/login` and shows the error "Invalid credentials. Try: tech@example.com". The same form works for the demo account (`tech@example.com` / `password` → "Welcome back!"), so newly registered accounts are never added to the credential store used by login.

- [X] FT-03: User can add a short bio and interests to their profile
  - Action: Go to My Profile → Edit Profile, enter a short bio (e.g. "Loves hiking and Python") and at least one interest/tag, then Save.
  - Expected: Profile saves; the profile page displays the entered bio and interests.

- [X] FT-04: User can start a new discussion thread in a category
  - Action: Click New Thread / Create Thread, enter a title and body, select a category, and submit.
  - Expected: Thread is created and appears in the thread list and its selected category.

- [X] FT-05: User can reply to an existing thread
  - Action: Open any default thread and post a reply using the reply box.
  - Expected: Reply is added and appears under the thread's original post with the replier's name.

- [X] FT-06: User can upvote/like a helpful post
  - Action: While logged in, click the Like/Upvote control on another user's post.
  - Expected: The post's vote/like count increases by exactly 1.

- [X] FT-07: User can search threads by keyword
  - Action: Type a word present in a default thread title (e.g. a keyword from an existing thread) into the Search box and submit.
  - Expected: Results list appears and every returned thread contains that keyword in its title or body.

- [X] FT-08: User can filter threads by category
  - Action: Select a specific category from the category filter/dropdown on the threads page.
  - Expected: Only threads belonging to that category are listed; threads from other categories are absent.

- [ ] FT-09: Trending / most active discussions for a recent period are listed
  - Action: Open the Trending / Most Active section on the forum home page.
  - Expected: A non-empty list of threads is shown, ordered from highest activity to lowest, and is labeled with the recent period (e.g. "Today", "This Week", "Last 7 days").
  - Bug Report:
    - Issue: Missing Period Label on Trending List
    - Actual: The home page shows a non-empty list of 8 threads ordered descending by activity (156, 124, 92, 89, 78, 67, 56, 47 likes), but the heading is only "Trending Discussions" with subtitle "Join the conversation with our community". No period label such as "Today", "This Week" or "Last 7 days" appears anywhere on the page (a regex scan for `today|this week|last 7|past week|24 hours|this month|yesterday` returned zero matches).

## Constraint

- [ ] CS-01: Registration rejects duplicate or invalid email
  - Action: Register with an email already used by FT-01, and again with a malformed value (e.g. "notanemail").
  - Expected: Both attempts are rejected with a visible error message and no account is created.
  - Bug Report:
    - Issue: Missing Duplicate-Email Validation / No Visible Error for Invalid Email
    - Actual: Registering again with the already-used email `qa_tester_01@example.com` (username `qa_dup_user`) SUCCEEDED — the app showed "Account created! Welcome to ThreadHive!" and logged in as `qa_dup_user`, so a second account with a duplicate email was created. Registering with the malformed value `notanemail` did not create an account (still on `/register`), but no visible error message was rendered in the DOM (body contained only "Join the Hive / Create an account to start discussing / Username / Email / Password / Create Account").

- [X] CS-02: Registration rejects empty required fields
  - Action: Submit the registration form with username and password left blank.
  - Expected: Submission is blocked and required-field error messages are shown.

- [ ] CS-03: Logged-out visitor cannot create a thread or reply
  - Action: Log out, then attempt to open the New Thread page and to submit a reply on a thread.
  - Expected: Both actions are blocked — user is prompted to log in or the controls are unavailable; no thread/reply is created.
  - Bug Report:
    - Issue: Broken Auth Guard — Blank Page Instead of Login Prompt
    - Actual: The reply control is correctly blocked (on `/thread/thread-1` while logged out, the textarea is `disabled` with placeholder "Login to Reply"). However, opening `/new-thread` while logged out renders a completely blank page: `#root` contains only the notifications section (169 chars), page body innerText is empty, 0 inputs/textareas, and no "log in" prompt or redirect to `/login` (console shows "You should call navigate() in a React.useEffect, not when rendering the component"). No thread is created, but the app crashes to a white screen rather than prompting login.

- [X] CS-04: Thread creation requires a title and a category
  - Action: Submit the new thread form with an empty title, then with a title but no category selected.
  - Expected: Both submissions are rejected with validation errors; no empty or uncategorized thread is created.

- [X] CS-05: A single user can only count as one vote per post
  - Action: Click Like/Upvote on the same post 3 times in a row.
  - Expected: Count ends at +1 (or returns to unvoted if toggled off) — never increases past one per user.

## Interaction

- [X] IX-01: Like control shows an active/upvoted state after clicking
  - Action: Click Like/Upvote once on a post and observe the control after the update.
  - Expected: The control appears in a visually distinct active/upvoted state and the new count is shown immediately.

- [ ] IX-02: Trending list updates when the recent period is changed
  - Action: In the Trending section, switch the period selector (e.g. from "Today" to "This Week").
  - Expected: The listed threads and/or their order change to reflect the newly selected period.
  - Bug Report:
    - Issue: Missing Period Selector Control
    - Actual: There is no recent-period selector in the Trending section. The page contains 0 `<select>` elements and the only buttons are "Trending", "Recent", "Most Active" (sort modes) plus icon buttons — none of which represent a time period ("Today"/"This Week"/"Last 7 days"). Clicking "Most Active" only changes the heading to "Most Active Discussions" and re-sorts by reply count; no period-based filtering exists.

- [X] IX-03: Success feedback is shown after posting a thread or reply
  - Action: Create a thread, then post a reply, observing the screen each time.
  - Expected: A confirmation message or redirect to the new content appears for each successful post.

## Content

- [X] CT-01: Thread list entries show complete thread metadata
  - Action: View the main threads list and inspect any 3 entries.
  - Expected: Each entry displays title, author name, category name, and reply count/like count (and timestamp).

- [X] CT-02: Forum categories are meaningful topics with no placeholder text
  - Action: Open the category filter/list and read all available category names.
  - Expected: All categories are coherent community forum topics with no "Lorem ipsum", "Test", or "Category 1" style placeholders.

- [ ] CT-03: Profile page shows the correct bio and interests for that user
  - Action: View the profile of the user edited in FT-03 and of another default user.
  - Expected: Each profile shows its own username, bio, and interest tags — no blank, mismatched, or placeholder content.
  - Bug Report:
    - Issue: Registered Profile Not Persisted / "User not found"
    - Actual: The other default user is correct — `/profile/user-1` shows "TechExplorer", joined date, bio "Full-stack developer passionate about open source…" and tags "Programming / Open Source / AI/ML / DevOps". But the profile of the user edited in FT-03 (`/profile/user-1794077710259`, `qa_tester_01`) renders "User not found / Go Home" instead of the saved bio "Loves hiking and Python" and interests "Python, Hiking, Photography" — the registered user only exists in in-memory session state and is lost on any page load.
