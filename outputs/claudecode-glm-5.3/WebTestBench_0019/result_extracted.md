# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Open the registration page, fill in all required fields (username, email, password) with valid values, and click "Register".
  - Expected: The account is created and the user is logged in (or redirected to the login page and can log in with the new credentials).
  - Verified: Registered "QATestPilot" (qa.testpilot@example.com) → toast "Account created! Welcome to ThreadHive!", redirected to home with logged-in header (New Thread link + profile link).

- [X] FT-02: User can add a short bio and interests to their profile
  - Action: Log in, open the profile/settings page, enter a short bio (e.g., "Aspiring web developer") and at least one interest (e.g., "JavaScript"), and save.
  - Expected: The profile page displays the entered bio and interests exactly as saved.
  - Verified: Via "Edit Profile", saved bio "Aspiring web developer" and interests "JavaScript, Web Development" → toast "Profile updated!", profile displayed the bio verbatim and interest tags "JavaScript" / "Web Development".

- [X] FT-03: User can start a new discussion thread in a category
  - Action: Log in, click "New Thread", enter a title and body, select a category from the category dropdown, and submit.
  - Expected: The thread is created and visible in the selected category's thread list with the author's name shown.
  - Verified: Created thread in "Gaming" category → redirected to its detail page (correct title/body/category/author), then the Gaming category list showed my thread alongside thread-4 with author "QATestPilot" and "less than a minute ago" timestamp.

- [X] FT-04: User can reply to an existing thread
  - Action: Log in, open any default thread, click "Reply", enter a reply message, and submit.
  - Expected: The reply appears under the thread's discussion, attributed to the logged-in user.
  - Verified: On default thread-4 ("Best indie games of 2023..."), posted a reply → toast "Reply posted!", "Replies (2)" heading, my reply rendered with my username "QATestPilot" (link to my profile) and correct text; thread meta updated 67 → 68 replies.

- [ ] FT-05: User can upvote/like a post
  - Action: Log in, click the upvote/like button on any default post, and note the count, then reload the page.
  - Expected: The vote count increases by 1 and remains incremented after the page reload.
  - Bug Report:
    - Issue: Data Loss / Non-Persistent State (vote not persisted after reload)
    - Actual: Logged in as QATestPilot, clicking the upvote button on thread-4's original post raised the count 124 → 125 (button highlighted). After reloading the page (http://localhost:6019/thread/thread-4), the count reverted to 124, my upvote state was gone, and the session was destroyed (header shows Login/Register; vote buttons disabled again). Root cause: the app keeps ALL state (auth session, users, threads, replies, votes) in React memory only — localStorage, sessionStorage, and cookies are all empty, and a created thread/account returns "Thread not found" after reload. The +1 vote therefore does NOT remain incremented after the page reload.

- [X] FT-06: User can search threads by keyword
  - Action: Type a keyword that appears in a default thread's title (or body) into the search box and submit the search.
  - Expected: Threads containing the keyword are listed; threads not containing the keyword are not shown.
  - Verified: Searching "keyboard" (in thread-7's title) → "Showing results for 'keyboard'" and only thread-7 ("Building a mechanical keyboard from scratch") listed; all 7 other threads excluded.

- [X] FT-07: User can filter threads by category
  - Action: Go to the thread list, select a specific category from the category filter (dropdown or category link).
  - Expected: Only threads belonging to the selected category are displayed.
  - Verified: /category/tech showed only Technology threads (thread-7, thread-1); /category/gaming showed only Gaming threads (thread-4, and my newly created gaming thread while it existed).

- [X] FT-08: Trending/most active discussions are listed for a recent period
  - Action: Open the "Trending" (or "Most Active") section and compare its entries against threads with the most recent replies/upvotes.
  - Expected: The list shows the most active discussions ranked by recent activity (replies/votes within the recent period), not simply all threads or oldest threads.
  - Verified: Home "Trending Discussions" ranks by votes desc (156, 124, 92, 89, 78, 67, 56, 47); clicking "Most Active" re-sorts to "Most Active Discussions" by reply count desc (89, 67, 45, 41, 38, 34, 31, 23) — a genuine activity ranking, not an arbitrary/oldest-first list.

## Constraint

- [X] CS-01: Registration cannot be completed with invalid input
  - Action: Open the registration page and submit with an empty required field (and/or mismatched password confirmation).
  - Expected: Submission is blocked with a clear validation error per invalid field; no account is created.
  - Verified: Submitting the registration form with all fields empty → blocked with toast "Please fill in all fields"; remained on /register, no account created. (Note: one combined validation message identifies the missing required fields; there is no confirm-password field on this form.)

- [X] CS-02: Duplicate account registration is rejected
  - Action: Attempt to register with a username or email already used by an existing (default) account.
  - Expected: Registration is rejected with an error message indicating the username/email is already taken; no second account is created.
  - Verified: Registered with existing default username "TechExplorer" (fresh email) → rejected with toast "Username or email already exists"; stayed on /register, no account created.

- [X] CS-03: Guests cannot post, reply, or upvote
  - Action: While logged out, attempt to create a thread, reply to a thread, and upvote a post.
  - Expected: Each action is blocked and the user is prompted to log in or register; no content or vote is created.
  - Verified (logged out): Reply form shows "Login to Reply" heading with disabled textarea ("You need to be logged in to reply") and disabled "Post Reply" button; all upvote buttons render with `disabled` attribute (unclickable, no vote created); "New Thread" entry point is not rendered at all for guests (only Login/Register in nav), so thread creation is inaccessible.

- [X] CS-04: Empty thread or reply cannot be submitted
  - Action: While logged in, open the reply form (or new thread form) and submit without entering any text.
  - Expected: Submission is blocked with a validation message; no empty post appears in the thread.
  - Verified: New-thread form submitted empty → blocked with toast "Please fill in all fields", no thread created. Reply form: "Post Reply" button is `disabled` while the textarea is empty (observed before typing and again after a successful reply), so an empty reply cannot be submitted.

- [X] CS-05: A user cannot inflate a post's score with repeated upvotes
  - Action: While logged in, click the upvote button on the same post multiple times.
  - Expected: The post's count increases by at most 1 from that user (e.g., the click toggles the vote off, or is ignored with the button shown as already upvoted); the count never accumulates per extra click.
  - Verified: Clicked thread-4 OP upvote 3×: 124 → 125 (voted) → 124 (toggled off) → 125 (toggled on). Count never accumulated beyond +1 for the logged-in user.

## Interaction

- [X] IX-01: Registration success is confirmed to the user
  - Action: Complete a valid registration (see FT-01).
  - Expected: A success message/toast or confirmation page is displayed, or the user is visibly redirected into the logged-in state.
  - Verified: Toast "Account created! Welcome to ThreadHive!" displayed and header switched to logged-in state (New Thread link, profile avatar, logout button) with redirect to home.

- [X] IX-02: Upvote button reflects its state visually
  - Action: While logged in, click the upvote button on a default post and observe the button.
  - Expected: The button immediately changes to an active/highlighted state and the count updates in place without a full page reload.
  - Verified: After click, count updated 124 → 125 in place (same URL, no reload) and the button adopted active/highlighted styling (`bg-primary/10 text-primary` classes vs. the default inactive vote buttons).

- [X] IX-03: Clicking a thread in a list opens its detail view
  - Action: On the thread list (or search/filter results), click a thread's title.
  - Expected: The thread detail page opens, showing the original post and its replies.
  - Verified: Clicked thread titles from home list, category list, and Most Active list (thread-1, thread-4, thread-6) — each navigated to /thread/:id detail pages showing the full original post plus its replies.

- [X] IX-04: Search and filter controls respond immediately
  - Action: Enter a keyword in the search box and submit; then change the category filter selection.
  - Expected: The thread list updates to reflect the new search term or category without requiring a page re-navigation.
  - Verified: Pressing Enter on "keyboard" updated the list instantly in place (URL stayed "/", header changed to "Showing results for 'keyboard'"); clicking the Gaming category link then swapped the list to gaming threads via client-side routing — no page re-navigation.

## Content

- [X] CT-01: Thread lists display complete and accurate metadata
  - Action: Inspect the default threads in the main list and in any category view.
  - Expected: Each thread shows its title, author, category, reply count, vote/like count, and creation/last-activity time, and these values match the actual thread data.
  - Verified: Every list item (home, category, search, most-active views) renders title, author (linked), category (linked), vote count next to the vote button, "N replies", "N views", and a relative timestamp. Cross-checked list values against detail pages: thread-1 (47 votes/23 replies), thread-4 (124/67), thread-6 (156/89), thread-7 (92/41) — all identical.

- [X] CT-02: Default thread content matches its category
  - Action: Open several default threads across at least two different categories and read their titles/bodies.
  - Expected: Every thread's subject matter is relevant to the category it is filed under (no miscategorized or off-topic content).
  - Verified: thread-1 (Technology: which programming language to learn), thread-7 (Technology: mechanical keyboard build), thread-4 (Gaming: best indie games of 2023), thread-6 (News & Current Events: future of remote work debate), thread-3/thread-8 (Creative Corner: digital vs traditional art / creative block), thread-5 (Lifestyle: meal prep), thread-2 (General Discussion: productivity tips) — all on-topic for their categories.

- [X] CT-03: Profile content is accurate and correctly attributed
  - Action: Open your own profile page and at least one default user's profile.
  - Expected: The bio and interests shown match what was saved for your profile, and other profiles display their own (not swapped or empty-by-default beyond a blank bio) data.
  - Verified: My profile showed exactly my saved bio "Aspiring web developer" and interests JavaScript / Web Development. GameMaster42's profile (/profile/user-3) shows their own data: bio "Competitive gamer and game reviewer. Always looking for the next great adventure.", interests RPGs / Strategy Games / Esports / Game Design, 3,156 reputation, "Threads by GameMaster42 (1)" — nothing swapped, and Edit Profile is only offered on my own profile.

- [X] CT-04: Trending list activity numbers match actual thread data
  - Action: Compare the reply/vote counts displayed next to each entry in the Trending/Most Active list against the counts shown on those threads' detail pages.
  - Expected: The metrics displayed in the trending list are identical to the actual counts on each thread.
  - Verified: thread-6 — list shows vote count "156" and "89 replies"; detail page shows vote count 156 on the OP and "89 replies" meta. thread-4 — list shows "124" and "67 replies"; detail page shows 124 and 67 replies. Identical metrics in both directions.
