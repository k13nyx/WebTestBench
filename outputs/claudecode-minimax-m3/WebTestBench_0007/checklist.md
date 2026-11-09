# Test Checklist

## Functionality
- [ ] FT-01: New resident can create an account via the sign-up form
  - Action: Navigate to sign-up page, fill in name/email/password, click "Sign Up"
  - Expected: Account is created and user is logged in or redirected to the main feed

- [ ] FT-02: Logged-in user can create a new post with a category
  - Action: Click "Create Post", enter title and body, select a category (e.g., "Safety Alert"), submit
  - Expected: Post is saved and appears in the feed with the chosen category label

- [ ] FT-03: User can view the feed of recent posts
  - Action: Navigate to the main feed page
  - Expected: A list of existing posts is displayed, each showing title, author, category, and timestamp

- [ ] FT-04: User can filter the feed by a specific category
  - Action: Select a category filter (e.g., "Community Event") from the filter control
  - Expected: Feed shows only posts belonging to the selected category

- [ ] FT-05: User can search the feed by keyword
  - Action: Enter a keyword (matching an existing post's title or body) into the search box
  - Expected: Feed displays only posts containing the keyword in their title or content

- [ ] FT-06: User can add a comment to an existing post
  - Action: Open a post, type text into the comment field, click "Post Comment"
  - Expected: The new comment is appended to the post's comment list with author and timestamp

- [ ] FT-07: User can mark a post as resolved / no longer relevant
  - Action: Click the "Mark as Resolved" (or equivalent) button on a post
  - Expected: Post's status changes to "Resolved" and the status indicator is visible in the feed

## Constraint
- [ ] CS-01: Sign-up form rejects submission with empty required fields
  - Action: Leave one or more required fields blank on the sign-up form and click "Sign Up"
  - Expected: Submission is blocked and an error message indicates the missing field(s)

- [ ] CS-02: Creating a post requires a category to be selected
  - Action: Fill in title and body but leave category unselected, then submit
  - Expected: Submission is blocked and an error message indicates a category must be chosen

- [ ] CS-03: Creating a post with empty title or body is blocked
  - Action: Leave the title or body blank and click "Submit"
  - Expected: Submission is blocked and an error message indicates content is required

- [ ] CS-04: Submitting a comment with empty text is blocked
  - Action: Leave the comment input empty and click "Post Comment"
  - Expected: Submission is blocked and an error message indicates a comment is required

- [ ] CS-05: Search with no matching keyword shows an empty-state message
  - Action: Enter a keyword that does not match any existing post
  - Expected: Feed displays a "no results" / empty-state message instead of all posts

## Interaction
- [ ] IX-01: A confirmation/success message appears after sign-up
  - Action: Successfully complete the sign-up form
  - Expected: A success message or toast appears confirming account creation

- [ ] IX-02: A newly created post immediately appears in the feed without manual refresh
  - Action: Submit a new post and observe the feed
  - Expected: The new post appears at the top (or correct position) of the feed automatically

- [ ] IX-03: A newly posted comment appears under its parent post without page reload
  - Action: Submit a comment on a post
  - Expected: The comment is displayed under the post immediately after submission

- [ ] IX-04: Resolved posts remain visible but display a clear "Resolved" status indicator
  - Action: Mark a post as resolved and view the feed
  - Expected: The post is still listed but visually marked (e.g., badge/strikethrough) as Resolved

## Content
- [ ] CT-01: The category list includes "Safety Alert", "Lost and Found", and "Community Event"
  - Action: Open the "Create Post" form's category dropdown
  - Expected: All three categories are present and labeled exactly as specified

- [ ] CT-02: Default seed posts in the feed relate to neighborhood safety / community topics
  - Action: View the feed before creating any new posts
  - Expected: Pre-existing posts cover neighborhood-watch themes (safety, lost & found, community events)

- [ ] CT-03: All feed content is displayed in a readable language without untranslated/placeholder text
  - Action: Browse the feed, post details, and comment sections
  - Expected: No "Lorem ipsum" or developer placeholder strings appear; all labels and messages are real text