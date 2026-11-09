All checklist items have now been executed. Here are the complete results.

# Test Result

## Functionality
- [X] FT-01: New visitor can register an account
  - Action: Opened /register, submitted username "qa_alice_118", email qa.alice.118@example.com, and a valid password via "Create Account".
  - Expected: Account is created and the user is signed in (or redirected to login and can log in).
  - Verified: Redirected to forum home, success toast "Account created! Welcome to ThreadHive!", header shows "New Thread" link and the new username → signed in. (Note: the new account is not persisted beyond a page reload — see CT-03 bug report.)

- [X] FT-02: Existing user can log in
  - Action: Logged out via the header logout button, then signed in with the default demo account tech@example.com / password (login page advertises "Demo accounts: tech@example.com, gamer@example.com").
  - Expected: User is signed in and reaches the forum home page.
  - Verified: Landed on http://localhost:6019/ with toast "Welcome back!" and TechExplorer shown in the header.

- [X] FT-03: User can set a profile with a short bio and interests
  - Action: Opened /profile/user-1 → "Edit Profile" → entered bio "QA engineer who loves mechanical keyboards and open-source tooling. Testing ThreadHive on 2026-11-08." and interests "Keyboards, Testing, Coffee, Rust" → Save.
  - Expected: Changes are saved and the profile page shows the bio and interests.
  - Verified: Toast "Profile updated!"; profile view immediately shows the new bio paragraph and four interest chips (Keyboards / Testing / Coffee / Rust). (Durability of the save is covered under CT-03's bug.)

- [X] FT-04: User can start a new discussion thread in a category
  - Action: From /new-thread, selected category "General Discussion", entered title "QA Test Thread: mechanical keyboard switches" and a body, clicked "Create Thread".
  - Expected: Thread is created and appears in that category's thread list.
  - Verified: Redirected to /thread/thread-1794110840100 showing full title/body with "General Discussion" category chip; the thread then appeared on /category/general alongside the seeded "Share your favorite productivity tips!" thread.

- [X] FT-05: User can reply to an existing thread
  - Action: Opened default thread-1 ("What programming language should I learn in 2024?"), submitted reply text "QA automation reply: JavaScript is a solid first choice…".
  - Expected: Reply appears in the thread with the replying user's name.
  - Verified: Toast "Reply posted!", section changed to "Replies (3)", the new reply is displayed attributed to "TechExplorer" (less than a minute ago).

- [X] FT-06: User can upvote/like a post
  - Action: Clicked the upvote arrow on default thread-1 (count 47) and on a reply with 0 votes (my own reply); verified reply GameMaster42's vote button too.
  - Expected: The vote is recorded and the displayed count for that post increases by 1.
  - Verified: Thread 47 → 48; reply 0 → 1, both with the button entering the active state (text-primary + filled icon). Reply vote counts toggle correctly (seed-voted reply 15 → 14 → 15, matching its pre-pressed state).

- [X] FT-07: User can search threads by keyword
  - Action: Typed "keyboard" in the header search box and pressed Enter from the home list.
  - Expected: The matching thread is listed in the search results.
  - Verified: List filtered to "Showing results for \"keyboard\"" with matching threads "Building a mechanical keyboard from scratch" and "QA Test Thread: mechanical keyboard switches"; non-matching threads removed.

- [X] FT-08: Thread list can be filtered by category
  - Action: From the home thread list, opened the "General Discussion (156)" category link (/category/general).
  - Expected: Only threads belonging to that category remain listed.
  - Verified: Page heading "General Discussion"; every listed article's category chip is "General Discussion" (2 threads shown, no threads from other categories).

## Constraint
- [X] CS-01: Required fields cannot be empty when creating a thread or reply
  - Action: Submitted the new-thread form with empty title/content/category; then attempted to submit the reply form with empty text (and whitespace-only text).
  - Expected: A validation error is shown and nothing is saved/displayed.
  - Verified: Empty thread form → error toast "Please fill in all fields", stayed on /new-thread, nothing created. Empty/whitespace reply → "Post Reply" button stays disabled so submission is impossible; reply count unchanged ("Replies (0)"), nothing displayed. (Note: the reply guard is a disabled button rather than an error toast — submission is fully blocked either way.)

- [ ] CS-02: Unauthenticated visitors cannot post, reply, or vote
  - Action: As a logged-out visitor: checked upvote buttons on home/thread replies, opened /thread/thread-1 to try to reply, and navigated directly to /new-thread.
  - Expected: The action is blocked and the user is prompted to register/log in.
  - Bug Report:
    - Issue: Unauthenticated thread-creation route renders a blank page with no login prompt; upvote controls silently disabled.
    - Actual: (1) Visiting /new-thread while logged out renders a completely empty page (body innerText = "", 256 chars HTML) — the post action is blocked but the user is never prompted to register/log in. (2) Thread and reply upvote buttons are merely disabled with no explanatory message or login link. The reply section is handled correctly ("Login to Reply" heading + disabled textbox "You need to be logged in to reply"), so the requirement holds only for replies, not for voting or thread creation.

- [X] CS-03: A user cannot count multiple votes on the same post
  - Action: Clicked the same thread-1 upvote button three times in a row (47 → 48 → 47 → 48), and toggled a reply vote repeatedly (15 → 14 → 15).
  - Expected: The count increases at most once for that user (repeat clicks toggle or are rejected).
  - Verified: Repeated clicks toggle the vote on/off; the net count for this user never exceeded the baseline + 1.

- [X] CS-04: Duplicate email cannot be registered
  - Action: Logged out, went to /register, submitted username "dupe_checker" with the existing default account email tech@example.com and a password.
  - Expected: Registration fails with a clear "already in use / taken" error.
  - Verified: Error toast "Username or email already exists"; stayed on the registration page; no account created (tech@example.com login continued to work with the original credentials).

## Interaction
- [X] IX-01: Upvote control gives immediate visual feedback
  - Action: Clicked the thread-1 upvote button, with a JS marker (window.__qa_marker) set beforehand to detect reloads; captured count, button class/icon state, then clicked again.
  - Expected: The count and button state (active/selected) update without a full page reload; clicking again reverses it.
  - Verified: Count updated 47→48→47→48 within ~350 ms per click; marker survived → no page reload occurred; active state visible (button gains "bg-primary/10 text-primary", arrow icon gains "fill-current") and reverses on the next click. (No aria-pressed attribute is exposed — state is conveyed only by styling.)

- [X] IX-02: Success feedback after write actions
  - Action: Observed feedback for creating a thread, posting a reply, and saving profile changes.
  - Expected: Each action shows a success message/toast or otherwise confirms completion.
  - Verified: Profile save → toast "Profile updated!"; reply → toast "Reply posted!"; thread creation → redirect to the new thread's URL (/thread/thread-1794110840100) displaying the created content, which confirms completion (no toast observed for thread creation itself, but the requirement allows "or otherwise confirms").

- [X] IX-03: Thread detail view opens from the list
  - Action: Clicked "What programming language should I learn in 2024?" from the home trending list.
  - Expected: The thread opens showing its full body, its replies, and a reply form.
  - Verified: Navigated to /thread/thread-1 showing the full untruncated body, "Replies" section with individual replies (authors, timestamps, vote buttons), and the "Add a Reply" textbox + "Post Reply" button.

## Content
- [X] CT-01: Categories are present and labeled
  - Action: Viewed the home sidebar category list and opened threads (thread-1 detail, new QA thread) to compare category labels.
  - Expected: Multiple forum categories exist and each thread displays its category name consistently.
  - Verified: Six labeled categories with counts (General Discussion 156, Technology 243, Creative Corner 89, Lifestyle 167, Gaming 312, News & Current Events 78); every thread card and the thread detail page display a matching category chip that links to the correct /category/* route (e.g., thread-1 → "Technology" → /category/tech; QA thread → "General Discussion" → /category/general).

- [X] CT-02: Trending / most active discussions are shown
  - Action: Opened the forum home (defaults to "Trending Discussions") and clicked the "Most Active" browse button.
  - Expected: A list of threads is shown, ranked by recent activity (replies/votes over a recent period).
  - Verified: "Trending Discussions" lists 8 threads strictly ranked by votes (156 ≥ 124 ≥ 92 ≥ 89 ≥ 78 ≥ 67 ≥ 56 ≥ 47); "Most Active Discussions" re-ranks the same threads strictly by reply count (89, 67, 45, 41, 38, 34, 31, 23 replies). (Minor note: all seeded timestamps read "almost 3 years ago", so the "recent period" window could not be differentiated empirically — ranking is by votes/replies as specified.)

- [ ] CT-03: Profile information is displayed on user profiles
  - Action: After saving new bio/interests in FT-03 (as TechExplorer), visited the profile page /profile/user-1 with a full page load.
  - Expected: The short bio and interests are shown, non-empty and correctly matching what was saved.
  - Bug Report:
    - Issue: Data persistence failure — saved profile (and all user-generated content) is stored in memory only and lost on any page load.
    - Actual: The freshly visited profile shows the seeded values "Full-stack developer passionate about open source…" and interests Programming/Open Source/AI/ML/DevOps — NOT the saved bio "QA engineer who loves mechanical keyboards…" or interests Keyboards/Testing/Coffee/Rust. The same root cause reverts everything else after a reload: the thread-1 vote count went back to 47, the reply list back to 2 (seed), the new QA thread disappeared from /category/general, the login session was lost (header shows Login/Register), and the FT-01 account qa_alice_118 can no longer sign in ("Invalid credentials").

- [X] CT-04: Search with no matches shows an empty-state message
  - Action: Entered nonsense keyword "zzqxvqwo nonsense keyword" in the header search and pressed Enter.
  - Expected: A clear "no results" message appears; the page does not show errors or a blank/broken list.
  - Verified: Results area shows "Showing results for \"zzqxvqwo nonsense keyword\"", "No threads found." and "Try adjusting your search terms." — zero thread articles, no error text, layout intact.

---
**Summary: 15 PASS / 4 FAIL (of 19).** Key defects: (1) CS-02 — logged-out visitors hitting /new-thread see a blank page with no login prompt (upvote buttons also disabled with no message); (2) CT-03 — no persistence layer: after any page reload, registered accounts, sessions, profile edits, created threads, replies, and votes are all reverted/lost.