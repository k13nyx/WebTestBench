All checklist items are now verified. FT-03's category-listing requirement is confirmed ("Verification thread for category listing" appears under /category/tech). Compiling final results:

# Test Result

## Functionality
- [X] FT-01: User can register a new account
  - Action: Open the registration page, enter a username, email, and password, then submit the form.
  - Expected: The account is created and the user is signed in (or directed to sign in), with the new account usable for forum actions.
  - Actual: Submitted qa_tester_2026 / qa_tester_2026@mail.com; toast "Account created! Welcome to ThreadHive!", redirected to home signed in; header showed "New Thread" + username; account then used successfully for profile edit, thread creation, replying, and upvoting.

- [X] FT-02: User can create a profile with bio and interests
  - Action: Navigate to the profile editing page, enter a short bio and one or more interests, then save.
  - Expected: The profile is saved and displays the entered bio and interests.
  - Actual: Edit Profile → entered bio and "Testing, Coffee, Hiking" → Save → toast "Profile updated!"; profile immediately displayed the bio paragraph and three interest tags.

- [X] FT-03: User can start a new discussion thread in a category
  - Action: Select a category, click the button to create a new thread, enter a title and body, then submit.
  - Expected: The new thread is created, appears in the chosen category's thread list, and opens with the posted content.
  - Actual: Created "Automated QA checklist walkthrough" in Technology; toast "Thread created successfully!"; opened at /thread/thread-1794167978511 with full content. Re-verified: "Verification thread for category listing" appears in the Technology category list (/category/tech).

- [X] FT-04: User can reply to an existing thread
  - Action: Open any default thread, enter a reply in the reply box, and submit it.
  - Expected: The reply appears in the thread's reply list with the user's name and the entered text.
  - Actual: Posted reply on the new thread; toast "Reply posted!"; "Replies (1)" showed author "qa_tester_2026" with the exact reply text.

- [X] FT-05: User can upvote/like a post
  - Action: Click the upvote/like control on a post or reply.
  - Expected: The upvote/like count increases by 1 and the control shows an active/selected state.
  - Actual: On thread-1 the vote count went 47 → 48 and the button gained the selected classes `bg-primary/10 text-primary` (also verified 0 → 1 on a reply).

- [X] FT-06: User can search threads by keyword
  - Action: Enter a keyword that appears in an existing default thread title or body into the search field and submit.
  - Expected: A results list is shown containing threads matching the keyword, including the expected default thread.
  - Actual: Searched "keyboard" → subheading `Showing results for "keyboard"` with exactly the expected default thread "Building a mechanical keyboard from scratch" (Technology).

- [X] FT-07: User can filter threads by category
  - Action: Select a specific category from the category filter/list.
  - Expected: Only threads belonging to that category are displayed.
  - Actual: Clicked sidebar "Gaming (312)" → only the Gaming thread ("Best indie games of 2023...") listed; earlier /category/news showed only the News thread.

- [X] FT-08: User can view a trending/most-active discussions list
  - Action: Navigate to the trending or most active discussions view.
  - Expected: A ranked list of threads is displayed, ordered by recent activity or popularity over a recent time period.
  - Actual: Home defaults to "Trending Discussions" (votes 156→47 descending); clicking "Most Active" switched to "Most Active Discussions" ranked by replies descending (89, 67, 45, 41, 38, 34, 31, 23).

## Constraint
- [X] CS-01: Registration cannot be submitted with empty required fields
  - Action: On the registration form, leave one or more required fields (e.g., username, email, password) empty and submit.
  - Expected: The form is rejected with a validation error; no account is created.
  - Actual: Clicked "Create Account" with all fields empty → toast "Please fill in all fields"; stayed on /register, no account created.

- [X] CS-02: Duplicate username/email cannot be registered
  - Action: Attempt to register using credentials that already exist in the application's default data.
  - Expected: Registration is rejected with a clear error indicating the username or email is already taken.
  - Actual: Registered with existing username "TechExplorer" → toast "Username or email already exists"; registration rejected, remained on /register.

- [X] CS-03: Thread cannot be created without a title and body
  - Action: Open the new-thread form, leave the title or body empty, and submit.
  - Expected: Submission is blocked with a validation error; no thread is created.
  - Actual: Clicked "Create Thread" with empty category/title/content → toast "Please fill in all fields"; stayed on /new-thread, no thread created.

- [ ] CS-04: Reply cannot be submitted while the reply box is empty
  - Action: On a thread page, submit the reply control with an empty reply box.
  - Expected: No reply is posted and a validation error is shown.
  - Actual: With an empty reply box (and with whitespace-only input), the "Post Reply" button is silently disabled so it cannot be clicked, and no validation error message is ever displayed.
  - Bug Report:
    - Issue: Missing validation error feedback for empty reply submission
    - Actual: Submission is prevented only via a disabled "Post Reply" button (remains disabled even for whitespace-only input); unlike the register/new-thread forms which show an explicit error toast ("Please fill in all fields"), no validation error is shown to the user explaining why the reply cannot be posted.

- [X] CS-05: A user cannot upvote the same post twice
  - Action: Click the upvote/like control on the same post once, then click it again.
  - Expected: The count increases only once; the second action either is rejected or toggles off, never double-counting.
  - Actual: Count 47 → 48 on first click, then toggled back to 47 (selected classes removed) on second click; never reached 49; same 0 → 1 → 0 behavior on a reply.

- [X] CS-06: Guest users cannot post or vote
  - Action: While signed out, attempt to create a thread, reply, or upvote a post.
  - Expected: The action is blocked and the user is prompted to register or sign in; no content or vote is recorded.
  - Actual: Signed out, all vote buttons rendered `disabled` (count unchanged); reply box disabled with heading "Login to Reply" and placeholder "You need to be logged in to reply", "Post Reply" disabled; no "New Thread" entry point exists for guests (/new → 404). No content or votes recorded; login prompt shown ("Login to Reply", header Login/Register).

## Interaction
- [X] IX-01: Voting provides immediate visual feedback
  - Action: Click the upvote/like control on a post.
  - Expected: The count and active state update instantly without a full page reload, and clicking again reverts the state.
  - Actual: Partial DOM update only (no reload): count 47 → 48 with `bg-primary/10 text-primary` added instantly; second click reverted count to 47 and removed the selected classes.

- [X] IX-02: Search and category filter respond immediately to user input
  - Action: Type a keyword into search and submit, then change the category filter.
  - Expected: The thread list updates to reflect the search term and selected category, showing a clear empty state when nothing matches.
  - Actual: "keyboard" → list updated to matching thread with `Showing results for "keyboard"`; "zzzquantumunicycle999" → empty state "No threads found. / Try adjusting your search terms."; clicking Gaming category immediately showed only Gaming threads.

- [X] IX-03: Successful actions confirm completion
  - Action: Complete each of: registering, saving a profile, creating a thread, and posting a reply.
  - Expected: Each action shows a visible success confirmation (e.g., message/toast) and the new content appears on screen.
  - Actual: Four toasts observed — "Account created! Welcome to ThreadHive!", "Profile updated!", "Thread created successfully!", "Reply posted!" — each followed by the new content appearing (signed-in header, saved bio/tags, opened thread, reply in list).

## Content
- [X] CT-01: Profiles display the entered bio and interests accurately
  - Action: Open a profile page after saving a bio and interests.
  - Expected: The displayed bio and interest tags match exactly what was entered.
  - Actual: Bio shown verbatim: "QA engineer who loves testing web apps and drinking coffee."; interest tags exactly "Testing", "Coffee", "Hiking".

- [X] CT-02: Thread and reply content is displayed faithfully
  - Action: Create a thread with a known title/body, then reply with known text, and view the thread.
  - Expected: The title, body, and reply text are shown verbatim, along with the correct author name and category label.
  - Actual: Title "Automated QA checklist walkthrough", body and reply "Automated test reply: thanks for sharing this discussion, it was very helpful!" displayed verbatim; author "qa_tester_2026" and category label "Technology" correct.

- [X] CT-03: Trending list shows relevant, correctly labeled thread data
  - Action: Open the trending/most active discussions view.
  - Expected: Each entry shows a relevant thread title with its category and an activity indicator (e.g., reply count or last-activity time), with no placeholder or unrelated content.
  - Actual: "Most Active Discussions" entries each had a real thread title, category label (e.g., "News & Current Events", "Gaming"), reply count ("89 replies"), views, and timestamp; no placeholder or unrelated content found.

**Summary: 20/21 PASS, 1 FAIL (CS-04 — empty reply is blocked by a disabled button but no validation error message is shown).**