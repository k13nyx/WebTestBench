I have completed testing all checklist items. Let me compile the final results.

# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Open the registration page, fill a valid email, username, and password, then click "Sign Up".
  - Expected: Account is created, the user is logged in and redirected to the home/profile page.
  - Note: Submit button is labeled "Create Account" (not "Sign Up"); registration succeeded, "Account created! Welcome to ThreadHive!" notification shown, redirected to home, and nav showed "New Thread" + the new user (logged in).

- [X] FT-02: User can create a profile with a short bio and interests
  - Action: Go to profile settings, enter a short bio and select interests, then click "Save".
  - Expected: Profile is saved and the bio and interests are displayed on the profile page.

- [X] FT-03: User can start a discussion thread in a category
  - Action: Select a category, enter a thread title and content, then click "Create Thread" (or "Post").
  - Expected: The new thread appears in that category's thread list.

- [X] FT-04: User can reply to a discussion thread
  - Action: Open a thread, enter reply text, then click "Reply".
  - Expected: The reply appears in the thread's reply list.

- [X] FT-05: User can upvote/like a helpful post
  - Action: Click the "Like"/"Upvote" button on a post.
  - Expected: The post's like count increases by 1.

- [X] FT-06: User can search threads by keyword
  - Action: Enter a keyword into the search box and submit the search.
  - Expected: Results show only threads whose content or title contains the keyword.

- [X] FT-07: User can filter threads by category
  - Action: Select a category from the category filter and apply it.
  - Expected: Only threads belonging to the selected category are shown.

- [X] FT-08: User can view a list of trending/most active discussions
  - Action: Open the "Trending" (or "Most Active") section.
  - Expected: A list of discussions ranked by activity is displayed.

## Constraint

- [ ] CS-01: Registration rejects invalid or empty credentials
  - Action: Submit registration with an empty or malformed email and/or a weak/empty password.
  - Expected: An error message is shown and no account is created.
  - Bug Report:
    - Issue: Incomplete input validation / missing error feedback for invalid-but-non-empty input
    - Actual: Empty submission correctly shows "Please fill in all fields" and creates no account. However, submitting a malformed email ("notanemail") with a weak password ("123") produces NO error message — the form simply stays on /register with no account created and no validation feedback. Invalid (non-empty) credentials are silently ignored rather than rejected with an error.

- [X] CS-02: Thread creation requires a category and required fields
  - Action: Submit the thread form with an empty title or no category selected.
  - Expected: A validation error is shown and the thread is not created.

- [X] CS-03: A post cannot be liked more than once by the same user
  - Action: Click "Like" on the same post a second time.
  - Expected: The like count does not increment again (it stays unchanged or toggles off).

- [ ] CS-04: Profile bio respects the maximum length limit
  - Action: Enter a bio longer than the allowed maximum and attempt to save.
  - Expected: The over-limit bio cannot be saved (input truncated or error shown).
  - Bug Report:
    - Issue: No maximum-length enforcement on profile bio
    - Actual: A 2000-character bio was accepted and saved ("Profile updated!") and displayed in full. There is no maxlength attribute and no client/server validation limiting bio length — the over-limit bio can be saved.

- [ ] CS-05: Trending list contains only discussions from a recent period
  - Action: Inspect the timestamps/activity window of items in the trending list.
  - Expected: Every listed thread falls within the defined recent period.
  - Bug Report:
    - Issue: Trending list includes non-recent discussions
    - Actual: Every trending item carries a timestamp of "almost 3 years ago"; none fall within any recent activity window, so the trending list is not restricted to a recent period.

## Interaction

- [X] IX-01: Success notification appears after creating a thread
  - Action: Successfully create a discussion thread.
  - Expected: A success toast/notification is displayed confirming creation.

- [X] IX-02: Like button reflects an active "liked" state
  - Action: Click "Like" on a post.
  - Expected: The button changes to a "Liked" visual state (e.g., color/icon change).

- [ ] IX-03: Search results filter live as the keyword is typed
  - Action: Type a keyword into the search field.
  - Expected: The thread list updates in real time to matching results without a full page reload.
  - Bug Report:
    - Issue: Search does not filter live on input
    - Actual: Typing "keyboard" into the search box left the full thread list unchanged. The list only filtered after pressing Enter/submit — the heading changed to "Showing results for 'keyboard'" and the list reduced to the single matching thread. No real-time filtering occurs as the keyword is typed.

- [X] IX-04: Category filter updates the thread list immediately
  - Action: Click a category filter option.
  - Expected: The visible thread list updates instantly to that category without a page reload.

## Content

- [X] CT-01: Thread list shows relevant metadata for each thread
  - Action: Open any thread list (home, category, or search results).
  - Expected: Each thread displays title, author, category, reply count, and like count.

- [X] CT-02: Profile interests are rendered as distinct, relevant tags
  - Action: View a profile that has interests set.
  - Expected: Interests are displayed as tags/chips that are clearly relevant to the forum theme.

- [ ] CT-03: Trending list shows accurate, labeled activity metrics
  - Action: Open the trending list.
  - Expected: Each item shows its activity metric (e.g., replies/likes) and a label indicating the recent period.
  - Bug Report:
    - Issue: Missing "recent period" label on trending items
    - Actual: Trending items display activity metrics (replies, views, and like counts), but there is no per-item (or list-level) label indicating the recent period (e.g., "this week" / "past 7 days"). Item timestamps read "almost 3 years ago," which contradicts any recent-period framing.

---

## Summary
- **Passed (15):** FT-01, FT-02, FT-03, FT-04, FT-05, FT-06, FT-07, FT-08, CS-02, CS-03, IX-01, IX-02, IX-04, CT-01, CT-02
- **Failed (5):** CS-01, CS-04, CS-05, IX-03, CT-03

### Key observations
- The app stores auth/registered users **in memory only** — a hard page reload (full navigation) logs the user out and discards newly created accounts/threads. All authenticated tests were therefore performed via in-app (client-side) navigation to preserve the session.
- Working well: registration (empty validation), thread creation with full validation, replies, likes with toggle, category filtering, search-by-submit, trending ranking, profile bio/interests, and the liked visual state.
- Notable defects: no bio length cap (CS-04); trending list not restricted to a recent period and lacking a period label (CS-05, CT-03); search lacks live (on-type) filtering — only filters on submit (IX-03); and invalid-but-non-empty registration input (malformed email / weak password) is silently dropped with no error message (CS-01).