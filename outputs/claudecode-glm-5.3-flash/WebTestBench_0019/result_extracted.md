# Test Result

## Functionality
- [X] FT-01: User can register a new account
  - Action: Open the registration page, enter a valid username/email and password, submit the form.
  - Expected: Registration succeeds, account is created, and the user is logged in or redirected to the forum.
- [ ] FT-02: Registered user can log in and log out
  - Action: Log in with the credentials created in FT-01, then log out.
  - Expected: Login succeeds and shows the user as logged in; logout returns the app to a logged-out state.
  - Bug Report:
    - Issue: Login rejects freshly registered accounts (invalid credentials)
    - Actual: After registering `testuser_qa1` / `qa_tester1@example.com` / `S3curePass!` (registration succeeded and auto-logged the user in), clicking the logout button correctly returns the header to "Login / Register", but subsequent login attempts with those exact credentials are rejected with the error toast "Invalid credentials. Try: tech@example.com". Retried with verified field values twice — still rejected. Only hard-coded demo accounts (e.g., `tech@example.com` / `password123`) can log in; accounts created via the registration form cannot ever log in again once logged out.
- [X] FT-03: User can create a profile with bio and interests
  - Action: Go to the profile page, enter a short bio and add one or more interests (e.g., "photography"), and save.
  - Expected: The profile saves and subsequently displays the entered bio and interests.
- [X] FT-04: User can start a new discussion thread in a category
  - Action: Click the new thread / create post button, select a category (e.g., "General"), enter a title and body, and submit.
  - Expected: The thread is created, appears in the selected category's thread list with its title and author.
- [X] FT-05: User can reply to an existing thread
  - Action: Open a thread, type a reply in the reply box, and submit.
  - Expected: The reply appears in the thread under the original post, showing author and content.
- [X] FT-06: User can upvote/like a post
  - Action: Click the upvote/like button on a post or reply.
  - Expected: The vote count increases by one and the control shows as activated (e.g., highlighted).
- [X] FT-07: Search returns threads matching a keyword
  - Action: Enter a keyword from an existing thread's title or body (e.g., a known topic word) in the search box and submit.
  - Expected: The results list contains threads containing that keyword; unrelated threads are excluded.
- [X] FT-08: Filter thread list by category
  - Action: Select a specific category from the category filter/navigation (e.g., "Tech").
  - Expected: Only threads belonging to that category are listed; selecting "All" restores the full list.
- [X] FT-09: Trending / most active discussions list is shown
  - Action: View the trending/most-active section of the home page.
  - Expected: A list of discussions over a recent period is displayed with activity indicators (reply or vote counts), ordered by activity level.

## Constraint
- [X] CS-01: Registration rejects empty or invalid required fields
  - Action: Submit the registration form with empty fields, or an invalid email / too-short password.
  - Expected: The form is not submitted and a validation error message is shown for the invalid field.
- [X] CS-02: New thread cannot be created without required fields
  - Action: Attempt to submit a new thread with an empty title or body.
  - Expected: Submission is blocked and a validation error is displayed.
- [X] CS-03: Forum actions require being logged in
  - Action: While logged out, attempt to create a thread, reply, or like a post.
  - Expected: The action is not performed; the user is prompted to log in / register.
- [X] CS-04: A user cannot upvote/like the same post multiple times
  - Action: Click the like/upvote button on the same post a second time.
  - Expected: The count does not double-increase; the toggle removes the vote or further clicks are ignored.
- [X] CS-05: Search with no matching keyword shows a no-results state
  - Action: Search for a nonsense keyword that matches no threads (e.g., "zzzzxq").
  - Expected: A "no results" message or empty state is shown; no unrelated threads are displayed.

## Interaction
- [X] IX-01: Successful thread creation gives visible confirmation
  - Action: Create a valid new thread.
  - Expected: A success message/toast appears and/or the user is taken to the newly created thread view.
- [X] IX-02: Clicking a thread in the list opens its detail view
  - Action: Click a thread title in the thread list or trending list.
  - Expected: The thread detail page opens showing the original post, category, and all replies.

## Content
- [X] CT-01: Forum displays multiple discussion categories
  - Action: View the category list/filter on the home page.
  - Expected: At least two distinct categories are shown with meaningful names (e.g., General, Tech), and threads are labeled with their category.
- [X] CT-02: Default forum data is present and relevant
  - Action: Load the home page without adding any data.
  - Expected: Pre-existing threads, posts, and/or users are displayed with readable titles, content, authors, and vote/reply counts (no blank or placeholder-only listings).
