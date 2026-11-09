# Test Checklist

## Functionality
- [ ] FT-01: User registration with valid details
  - Action: Fill in username, email, and password on the Registration page and click "Register".
  - Expected: Account is created successfully and the user is redirected to the logged-in forum view.
- [ ] FT-02: Profile creation and update with bio and interests
  - Action: Enter text into the "Bio" field, add items to "Interests", and click "Save Profile".
  - Expected: Bio and interests are saved and accurately displayed on the user's public profile page.
- [ ] FT-03: Create a new discussion thread in a category
  - Action: Click "New Thread", select a category, enter a thread title and body content, and click "Publish".
  - Expected: Thread is published and visible within the selected category listing.
- [ ] FT-04: Post a reply to an existing discussion thread
  - Action: Open an existing thread, enter text in the reply box, and click "Post Reply".
  - Expected: The new reply appears in the thread below the existing posts.
- [ ] FT-05: Upvote or like a post
  - Action: Click the "Upvote" or "Like" button on a thread or reply.
  - Expected: The upvote/like count increments by 1.
- [ ] FT-06: Search discussion threads by keyword
  - Action: Enter a matching keyword into the search bar and press Enter or click "Search".
  - Expected: Display a list of threads whose title or content contains the searched keyword.
- [ ] FT-07: Filter discussion threads by category
  - Action: Select a specific category from the category filter list.
  - Expected: Only threads belonging to the selected category are displayed in the feed.
- [ ] FT-08: View trending or most active discussions
  - Action: Click the "Trending" or "Most Active" tab in the discussions section.
  - Expected: Threads are sorted and displayed based on highest activity (replies/upvotes) over the recent period.

## Constraint
- [ ] CS-01: Prevent registration with empty required fields
  - Action: Leave mandatory fields (e.g., email or password) blank and click "Register".
  - Expected: Submission is blocked and inline validation messages indicate the required missing fields.
- [ ] CS-02: Enforce mandatory fields when creating a thread
  - Action: Attempt to submit the "New Thread" form without entering a title or selecting a category.
  - Expected: Submission is blocked and validation errors prompt the user to complete required fields.
- [ ] CS-03: Prevent submission of empty replies
  - Action: Click "Post Reply" without entering any text into the reply field.
  - Expected: The reply button remains disabled or an error prevents an empty post from being added.
- [ ] CS-04: Restrict duplicate upvotes/likes per user
  - Action: Click the "Upvote" button again on a post that the user has already upvoted.
  - Expected: The vote toggles off (count decrements by 1) or remains at 1 without allowing multiple positive votes from the same account.

## Interaction
- [ ] IX-01: Visual state feedback on upvote/like button
  - Action: Click the "Upvote" or "Like" button on an unvoted post.
  - Expected: The button highlights or changes color/icon fill to visually indicate the active voted state.
- [ ] IX-02: Active category filter badge and dismiss interaction
  - Action: Select a category filter from the menu.
  - Expected: An active filter tag or pill appears above the thread list with a remove/clear button.

## Content
- [ ] CT-01: Profile details display integrity
  - Action: Navigate to a user's profile that has an existing bio and interests.
  - Expected: The bio text and all interest tags render accurately with proper formatting and no truncation.
- [ ] CT-02: Thread card metadata display
  - Action: View any thread card in the main forum feed.
  - Expected: Card displays thread title, author name, category badge, timestamp, reply count, and upvote count.
- [ ] CT-03: Zero-results feedback for keyword search
  - Action: Search for a non-existent keyword string (e.g., "unmatchedquery123xyz").
  - Expected: A clear "No threads found" message is displayed in place of the thread list.