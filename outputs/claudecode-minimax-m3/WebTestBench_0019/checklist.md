# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Navigate to the registration page, fill in valid credentials, and submit the form.
  - Expected: A new user account is successfully created and the user is logged in or redirected to their profile.
- [ ] FT-02: User can create a profile with bio and interests
  - Action: Log in, go to the profile/settings page, enter a short bio and select or type interests, then save.
  - Expected: The bio text and selected interests are saved and visible on the user's profile page.
- [ ] FT-03: User can start a new discussion thread in a category
  - Action: Navigate to a category, click "New Thread", enter a title and body, and submit.
  - Expected: The new thread appears in the selected category's thread list and is openable.
- [ ] FT-04: User can reply to an existing thread
  - Action: Open an existing thread, type a reply in the reply box, and submit.
  - Expected: The reply is added to the thread and appears under the original post.
- [ ] FT-05: User can upvote/like a helpful post
  - Action: Open a thread or reply and click the upvote/like button.
  - Expected: The upvote/like is registered on that post and the like count increases by one.
- [ ] FT-06: User can search for threads by keyword
  - Action: Enter a keyword that appears in an existing thread's title or body into the search box and submit.
  - Expected: A results list shows the threads matching that keyword.
- [ ] FT-07: User can filter threads by category
  - Action: Select a specific category from the category filter/dropdown.
  - Expected: Only threads belonging to the selected category are displayed.
- [ ] FT-08: User can view trending/most active discussions over a recent period
  - Action: Navigate to the "Trending" or "Most Active" section.
  - Expected: A list of threads ranked by recent activity (e.g., recent replies, upvotes) is displayed.

## Constraint
- [ ] CS-01: Registration form rejects submission with missing required fields
  - Action: Open the registration form, leave one or more required fields (e.g., username, email, password) empty, and submit.
  - Expected: The form is not submitted and a validation error is shown for the missing field(s).
- [ ] CS-02: Thread creation requires a category to be selected
  - Action: Open the "New Thread" form and submit it without selecting a category.
  - Expected: The thread is not created and a validation error prompts the user to pick a category.
- [ ] CS-03: User cannot upvote/like the same post more than once
  - Action: Click the upvote/like button on a post, then click it again.
  - Expected: The like count does not increase past one per user; clicking again either un-likes or is a no-op.
- [ ] CS-04: Empty reply cannot be submitted to a thread
  - Action: Open a thread, leave the reply box empty, and submit.
  - Expected: The reply is not posted and a validation error is shown.

## Interaction
- [ ] IX-01: Upvote/like button provides visual feedback when toggled
  - Action: Click the upvote/like button on a post.
  - Expected: The button's visual state changes (e.g., filled icon, highlight color) to indicate it is active.
- [ ] IX-02: Like count updates immediately after upvoting
  - Action: Note the current like count on a post, click the upvote/like button.
  - Expected: The displayed like count increments by one without requiring a page refresh.
- [ ] IX-03: Search results update when a keyword is entered
  - Action: Type a keyword into the search box.
  - Expected: Matching threads appear in the results list as the search is performed.
- [ ] IX-04: Trending list reflects activity from a recent time period only
  - Action: View the trending/most active list and check the timestamps or ordering of listed threads.
  - Expected: All displayed threads show recent activity (e.g., within the past days/weeks), not stale threads.

## Content
- [ ] CT-01: Thread titles and body content are displayed accurately
  - Action: Open any existing thread from the default data.
  - Expected: The title and body content shown match what was originally posted (no truncation, missing text, or wrong data).
- [ ] CT-02: Category labels are visible on threads and in the filter
  - Action: View the category filter list and open a thread from a category.
  - Expected: Category names are clearly displayed in the filter dropdown and on each thread.
- [ ] CT-03: User profile shows bio and interests
  - Action: Open the profile of a registered user.
  - Expected: The user's bio and interests are visible on the profile page.