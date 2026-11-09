# Test Checklist

## Functionality
- [ ] FT-01: New visitor can register an account
  - Action: Open the registration page, submit a valid username, email, and password.
  - Expected: Account is created and the user is signed in (or redirected to login and can log in).
- [ ] FT-02: Existing user can log in
  - Action: Log out, then log in using a default account's email and password.
  - Expected: User is signed in and reaches the forum home page.
- [ ] FT-03: User can set a profile with a short bio and interests
  - Action: Open profile settings, enter a short bio text and one or more interests, then save.
  - Expected: Changes are saved and the profile page shows the bio and interests.
- [ ] FT-04: User can start a new discussion thread in a category
  - Action: Create a thread with a title, body text, and a selected category (e.g., "General").
  - Expected: Thread is created and appears in that category's thread list.
- [ ] FT-05: User can reply to an existing thread
  - Action: Open a default thread, submit a reply with text.
  - Expected: Reply appears in the thread with the replying user's name.
- [ ] FT-06: User can upvote/like a post
  - Action: Click the upvote/like control on a default thread (and on a reply).
  - Expected: The vote is recorded and the displayed count for that post increases by 1.
- [ ] FT-07: User can search threads by keyword
  - Action: Enter a keyword that appears in a known default thread's title/body and run the search.
  - Expected: The matching thread is listed in the search results.
- [ ] FT-08: Thread list can be filtered by category
  - Action: From the main thread list, apply a filter for one specific category.
  - Expected: Only threads belonging to that category remain listed.

## Constraint
- [ ] CS-01: Required fields cannot be empty when creating a thread or reply
  - Action: Submit the new-thread form with an empty title (or body), then the reply form with empty text.
  - Expected: A validation error is shown and nothing is saved/displayed.
- [ ] CS-02: Unauthenticated visitors cannot post, reply, or vote
  - Action: As a logged-out visitor, attempt to create a thread, reply, or upvote.
  - Expected: The action is blocked and the user is prompted to register/log in.
- [ ] CS-03: A user cannot count multiple votes on the same post
  - Action: Upvote the same thread/reply repeatedly as the same user.
  - Expected: The count increases at most once for that user (repeat clicks toggle or are rejected).
- [ ] CS-04: Duplicate email cannot be registered
  - Action: Attempt to register using an email that already belongs to a default account.
  - Expected: Registration fails with a clear "already in use / taken" error.

## Interaction
- [ ] IX-01: Upvote control gives immediate visual feedback
  - Action: Click an upvote/like button on a post.
  - Expected: The count and button state (active/selected) update without a full page reload; clicking again reverses it.
- [ ] IX-02: Success feedback after write actions
  - Action: Create a thread, post a reply, and save profile changes.
  - Expected: Each action shows a success message/toast or otherwise confirms completion.
- [ ] IX-03: Thread detail view opens from the list
  - Action: Click a thread's title/link in the thread list.
  - Expected: The thread opens showing its full body, its replies, and a reply form.

## Content
- [ ] CT-01: Categories are present and labeled
  - Action: View the home/category list and open any thread.
  - Expected: Multiple forum categories exist and each thread displays its category name consistently.
- [ ] CT-02: Trending / most active discussions are shown
  - Action: Open the trending (or "most active") section on the forum home.
  - Expected: A list of threads is shown, ranked by recent activity (replies/votes over a recent period).
- [ ] CT-03: Profile information is displayed on user profiles
  - Action: Visit the profile page of the default user set up in FT-03.
  - Expected: The short bio and interests are shown, non-empty and correctly matching what was saved.
- [ ] CT-04: Search with no matches shows an empty-state message
  - Action: Search using a nonsense keyword not present in any default thread.
  - Expected: A clear "no results" message appears; the page does not show errors or a blank/broken list.