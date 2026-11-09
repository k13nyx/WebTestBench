# Test Result

Notes on the run:
- Full page reloads reset the app's state. The account and profile from FT-01 and FT-02 did not survive them, so the later tests ran in a single session.
- The app's labels differ from the checklist in places: the button is "Create Thread" (not "Post Thread"), and Interests is a comma-separated text box rather than a selector. I used the equivalent controls.
- Tool calls used: about 62 of 100.

## Functionality

- [ ] FT-01: Register a new account and log in
  - Action: Click "Register", enter a unique username, email, and password, submit, then log in with the same credentials.
  - Expected: Registration succeeds with a confirmation, and the header shows the new username after login.
  - Bug Report:
    - Issue: Account Not Persisted / Login Rejected After Reload
    - Actual: Registration showed "Account created! Welcome to ThreadHive!" and the header showed `qa_tester_01`. After a full page reload, logging in as `qa_tester_01@example.com` with the same password returned "Invalid credentials. Try: tech@example.com". The field values were confirmed as correct via DOM read.
- [ ] FT-02: Save bio and interests on the profile
  - Action: Open the profile, click "Edit Profile", enter a short bio and select one or more interests, click "Save".
  - Expected: The saved bio and interests appear on the profile page after a page reload.
  - Bug Report:
    - Issue: Profile Data Lost on Reload
    - Actual: Save showed "Profile updated!" and the bio and interests ("Programming", "Gaming") were displayed. After reloading `/profile/user-1794232897043`, the page showed "User not found" and the header showed logged-out (Login / Register).
- [X] FT-03: Create a discussion thread in a category
  - Action: Click "New Thread", select a category, enter a title and body, click "Post Thread".
  - Expected: The thread appears in the selected category's list with the correct title, category, and author name.
- [X] FT-04: Reply to a thread
  - Action: Open any existing thread, type text in the reply box, click "Post Reply".
  - Expected: The reply appears at the bottom of the thread with the author name and timestamp, and the reply count increases by 1.
- [X] FT-05: Upvote a helpful post
  - Action: Open a thread by another user, click the upvote (▲) button on the thread or a reply.
  - Expected: The vote count increases by 1 and the upvote button shows an active state.
- [X] FT-06: Search threads by keyword
  - Action: Type a word that appears in an existing thread title into the search bar, press Enter.
  - Expected: Results list threads whose title or body contains that keyword.
- [ ] FT-07: Filter threads by category
  - Action: Select one category from the "Category" filter dropdown.
  - Expected: Only threads belonging to the selected category are listed.
  - Bug Report:
    - Issue: Missing Element (Category Filter)
    - Actual: No "Category" filter dropdown exists on the home page, the search results view, or the `/category/tech` page. No select or combobox is present on those pages. The only category controls are sidebar links.
- [ ] FT-08: View trending/most active discussions
  - Action: Open the "Trending" (or "Most Active") section from the forum home.
  - Expected: A list of threads is shown, ordered from most to least active over the recent period, with the period label displayed.
  - Bug Report:
    - Issue: Missing Period Label / Ordering Not Verifiable
    - Actual: The Trending section shows no period label; the header reads only "Trending Discussions" and "Join the conversation with our community". The list order by reply count is 89, 67, 41, 45, 34, 38, 31, 23, 1, which is not monotonic (41 precedes 45).

## Constraint

- [ ] CS-01: Registration requires valid, complete fields
  - Action: Submit the registration form with username, email, or password left empty; then submit with email "userexample.com".
  - Expected: Submission is blocked, each empty or invalid field shows an error message, and no account is created.
  - Bug Report:
    - Issue: Missing Per-Field Validation Messages
    - Actual: Submitting the empty form showed one toast, "Please fill in all fields", with no per-field errors. With email "userexample.com" (username and password filled), the form stayed on /register, but no error message appeared at all (no toast and no field error).
- [ ] CS-02: Duplicate username or email is rejected
  - Action: Register using the username or email of an existing default user.
  - Expected: Registration is blocked with a "already taken" or "already registered" error, and no new account is created.
  - Bug Report:
    - Issue: Incorrect Error Message
    - Actual: Registering as `TechExplorer` / `tech@example.com` was blocked and no account was created, but the message read "Username or email already exists", not "already taken" or "already registered".
- [ ] CS-03: New thread requires title, body, and category
  - Action: Open "New Thread" and click "Post Thread" with the title, body, or category left empty.
  - Expected: Posting is blocked with an error message for each missing field, and no thread is created.
  - Bug Report:
    - Issue: Missing Per-Field Error Messages
    - Actual: With all three fields empty, clicking "Create Thread" showed one toast, "Please fill in all fields". No message identified the missing title, body, or category. Posting was blocked and no thread was created. (Each field was not tested individually.)
- [X] CS-04: Empty replies are not allowed
  - Action: Open a thread, leave the reply box empty (or only spaces), click "Post Reply".
  - Expected: Posting is blocked and no reply is added to the thread.
- [X] CS-05: One vote per user per post
  - Action: Upvote the same post twice.
  - Expected: The vote count changes by at most 1 across both clicks; the second click does not increase the count again.
- [ ] CS-06: Guests cannot post, reply, or vote
  - Action: Log out, then click "New Thread", "Post Reply", and the upvote button.
  - Expected: Each action is blocked and the user is redirected to the login page or shown a login prompt; no content or vote is recorded.
  - Bug Report:
    - Issue: Blank Page for Guest on New Thread
    - Actual: As a logged-out guest, the "New Thread" link is absent, so I navigated directly to `/new-thread`. The page rendered empty: no form, no redirect to login, and no login prompt. On `/thread/thread-6`, the guest reply box was disabled with "Login to Reply", Post Reply was disabled, and the upvote buttons were disabled. Those reply and vote parts are blocked correctly.

## Interaction

- [X] IX-01: Success message after creating a thread
  - Action: Create a valid thread using "Post Thread".
  - Expected: A success toast or message reading "Thread created" appears, and the user is taken to the new thread or the category list.
- [X] IX-02: Upvote updates instantly without reload
  - Action: Click the upvote button on a post and observe the button and counter without refreshing.
  - Expected: The button changes to its active (highlighted) state and the counter updates immediately.
- [ ] IX-03: Empty search result message
  - Action: Search for "zzqxnomatch" in the search bar and press Enter.
  - Expected: The results area shows the message "No results found" and no threads are listed.
  - Bug Report:
    - Issue: Incorrect Empty-State Message
    - Actual: The results area shows "No threads found." and "Try adjusting your search terms." No threads are listed. The message does not match the expected "No results found".

## Content

- [ ] CT-01: Search results match the keyword
  - Action: Search for a keyword from FT-06 and review every result listed.
  - Expected: Every result contains the keyword in its title or body, and no unrelated threads appear.
- [ ] CT-02: Trending list shows only recent activity
  - Action: Open the Trending section and compare each thread's last-activity date with the period label shown.
  - Expected: Every listed thread has activity within the displayed period, and the activity dates are consistent with the sort order.
  - Bug Report:
    - Issue: Stale Activity Data / No Period Label
    - Actual: Eight of nine Trending threads are dated "almost 3 years ago" (current date 2026-11-09). Only the newly created QA thread is recent. No period label is displayed, so the recent window cannot be confirmed.
- [ ] CT-03: Author profile data is consistent across the forum
  - Action: Open the profile saved in FT-02, then click the author name on a thread or reply that user posted.
  - Expected: The author profile shows the same username, bio, and interests as those saved in FT-02.
  - Bug Report:
    - Issue: Blocked by FT-02 Failure
    - Actual: The profile saved in FT-02 does not persist; `/profile/user-1794232897043` returns "User not found" after reload. There is no saved profile to compare against, so the author-name check was not performed.

Correction to the earlier checklist results: I marked CT-01 above as `[ ]`, but its result is a pass. Both returned search results contain "keyboard" in the title and body, and no unrelated threads appear. The corrected status is:

- [X] CT-01: Search results match the keyword
  - Action: Search for a keyword from FT-06 and review every result listed.
  - Expected: Every result contains the keyword in its title or body, and no unrelated threads appear.
