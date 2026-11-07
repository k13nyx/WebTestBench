# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, fill a valid email, username, and password, then click "Sign Up".
  - Expected: Account is created, the user is logged in and redirected to the home/profile page.

- [ ] FT-02: User can create a profile with a short bio and interests
  - Action: Go to profile settings, enter a short bio and select interests, then click "Save".
  - Expected: Profile is saved and the bio and interests are displayed on the profile page.

- [ ] FT-03: User can start a discussion thread in a category
  - Action: Select a category, enter a thread title and content, then click "Create Thread" (or "Post").
  - Expected: The new thread appears in that category's thread list.

- [ ] FT-04: User can reply to a discussion thread
  - Action: Open a thread, enter reply text, then click "Reply".
  - Expected: The reply appears in the thread's reply list.

- [ ] FT-05: User can upvote/like a helpful post
  - Action: Click the "Like"/"Upvote" button on a post.
  - Expected: The post's like count increases by 1.

- [ ] FT-06: User can search threads by keyword
  - Action: Enter a keyword into the search box and submit the search.
  - Expected: Results show only threads whose content or title contains the keyword.

- [ ] FT-07: User can filter threads by category
  - Action: Select a category from the category filter and apply it.
  - Expected: Only threads belonging to the selected category are shown.

- [ ] FT-08: User can view a list of trending/most active discussions
  - Action: Open the "Trending" (or "Most Active") section.
  - Expected: A list of discussions ranked by activity is displayed.

## Constraint
- [ ] CS-01: Registration rejects invalid or empty credentials
  - Action: Submit registration with an empty or malformed email and/or a weak/empty password.
  - Expected: An error message is shown and no account is created.

- [ ] CS-02: Thread creation requires a category and required fields
  - Action: Submit the thread form with an empty title or no category selected.
  - Expected: A validation error is shown and the thread is not created.

- [ ] CS-03: A post cannot be liked more than once by the same user
  - Action: Click "Like" on the same post a second time.
  - Expected: The like count does not increment again (it stays unchanged or toggles off).

- [ ] CS-04: Profile bio respects the maximum length limit
  - Action: Enter a bio longer than the allowed maximum and attempt to save.
  - Expected: The over-limit bio cannot be saved (input truncated or error shown).

- [ ] CS-05: Trending list contains only discussions from a recent period
  - Action: Inspect the timestamps/activity window of items in the trending list.
  - Expected: Every listed thread falls within the defined recent period.

## Interaction
- [ ] IX-01: Success notification appears after creating a thread
  - Action: Successfully create a discussion thread.
  - Expected: A success toast/notification is displayed confirming creation.

- [ ] IX-02: Like button reflects an active "liked" state
  - Action: Click "Like" on a post.
  - Expected: The button changes to a "Liked" visual state (e.g., color/icon change).

- [ ] IX-03: Search results filter live as the keyword is typed
  - Action: Type a keyword into the search field.
  - Expected: The thread list updates in real time to matching results without a full page reload.

- [ ] IX-04: Category filter updates the thread list immediately
  - Action: Click a category filter option.
  - Expected: The visible thread list updates instantly to that category without a page reload.

## Content
- [ ] CT-01: Thread list shows relevant metadata for each thread
  - Action: Open any thread list (home, category, or search results).
  - Expected: Each thread displays title, author, category, reply count, and like count.

- [ ] CT-02: Profile interests are rendered as distinct, relevant tags
  - Action: View a profile that has interests set.
  - Expected: Interests are displayed as tags/chips that are clearly relevant to the forum theme.

- [ ] CT-03: Trending list shows accurate, labeled activity metrics
  - Action: Open the trending list.
  - Expected: Each item shows its activity metric (e.g., replies/likes) and a label indicating the recent period.