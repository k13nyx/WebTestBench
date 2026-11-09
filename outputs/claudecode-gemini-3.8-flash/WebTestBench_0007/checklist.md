# Test Checklist

## Functionality
- [ ] FT-01: Resident account registration
  - Action: Enter valid details into "Full Name", "Email", and "Password" fields in the sign-up form, then click the "Sign Up" button.
  - Expected: The account is successfully created and the user is redirected to the neighborhood watch dashboard.
- [ ] FT-02: Create and publish a categorized alert post
  - Action: Enter a title and description, select "Safety Alert" from the category dropdown, and click the "Publish Alert" button.
  - Expected: The post is created and appears at the top of the alerts feed showing the title, description, and "Safety Alert" category tag.
- [ ] FT-03: Filter alerts feed by category
  - Action: Click the "Lost and Found" filter tab above the alerts feed.
  - Expected: The feed refreshes to display only posts assigned to the "Lost and Found" category.
- [ ] FT-04: Search alerts feed by keyword
  - Action: Type a specific keyword from an existing post into the "Search alerts..." bar and press Enter.
  - Expected: The feed displays only posts that contain the keyword in their title or description.
- [ ] FT-05: Add a comment to an alert post
  - Action: Type a message into the "Add a comment..." field under an existing post and click the "Post Comment" button.
  - Expected: The comment is immediately published and displayed beneath the post with the author's name and comment text.
- [ ] FT-06: Mark an active alert as resolved
  - Action: Click the "Mark as Resolved" button on an active alert post in the feed.
  - Expected: The post status changes from "Active" to "Resolved".

## Constraint
- [ ] CS-01: Prevent registration with empty required fields
  - Action: Leave the "Email" and "Password" fields blank in the sign-up form and click the "Sign Up" button.
  - Expected: The form is blocked from submitting and an error message "Please fill in all required fields" is displayed.
- [ ] CS-02: Prevent publishing a post with missing content
  - Action: Select a category but leave the title and description fields empty, then click "Publish Alert".
  - Expected: The post is not submitted and a validation error "Title and description cannot be empty" is displayed.
- [ ] CS-03: Prevent submitting an empty comment
  - Action: Click the "Post Comment" button on an alert post while the comment text box is empty.
  - Expected: The comment is not submitted and the "Post Comment" button remains disabled or displays a "Comment cannot be blank" message.
- [ ] CS-04: Search query yielding zero matches
  - Action: Enter an unmatching string (e.g., "nonexistentkeyword999") into the search bar and press Enter.
  - Expected: The feed displays zero post cards and shows a "No alerts found matching your search" message.
- [ ] CS-05: Prevent re-resolving an already resolved post
  - Action: Locate a post that is already in "Resolved" status and attempt to click "Mark as Resolved".
  - Expected: The "Mark as Resolved" button is hidden or disabled, preventing duplicate resolution actions.

## Interaction
- [ ] IX-01: Visual feedback for active category filter
  - Action: Click the "Community Event" category filter button.
  - Expected: The "Community Event" button displays a highlighted active visual state (e.g., contrasting background color) while all other category buttons appear inactive.
- [ ] IX-02: Success feedback upon post creation
  - Action: Fill out the post creation form with valid data and click "Publish Alert".
  - Expected: A confirmation toast notification reading "Alert posted successfully" appears and the form fields reset to blank.
- [ ] IX-03: Dynamic status badge update on resolution
  - Action: Click the "Mark as Resolved" button on an active post card.
  - Expected: The status badge immediately updates its text to "Resolved" and shifts its visual style (e.g., changes badge color to green).
- [ ] IX-04: Toggle comment section visibility
  - Action: Click the "Comments" button on an alert post that has existing comments.
  - Expected: The comment list expands smoothly into view; clicking the button a second time collapses the comment list.

## Content
- [ ] CT-01: Alert post card information structure
  - Action: Inspect any default post displayed in the alerts feed.
  - Expected: Each card clearly displays the author's name, timestamp, category badge ("Safety Alert", "Lost and Found", or "Community Event"), title, description, and status indicator.
- [ ] CT-02: Category taxonomy options
  - Action: Open the category selection dropdown in the post creation form.
  - Expected: The available options strictly include community-relevant categories: "Safety Alert", "Lost and Found", and "Community Event".