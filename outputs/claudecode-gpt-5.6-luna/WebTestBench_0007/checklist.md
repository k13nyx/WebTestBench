# Test Checklist

## Functionality
- [ ] **FT-01: Resident can sign up for an account**
  - **Action:** Open the “Sign Up” form, enter valid resident details, and select “Sign Up.”
  - **Expected:** The account is created successfully and the user is signed in or shown a successful registration confirmation.

- [ ] **FT-02: Resident can create a categorized safety post**
  - **Action:** Open the post form, enter a short safety-related message, select “Safety Alert,” and select “Post” or “Submit.”
  - **Expected:** The post is published and appears in the recent alerts feed with the “Safety Alert” category.

- [ ] **FT-03: Resident can create a lost-and-found post**
  - **Action:** Submit a short post describing a lost or found item and select “Lost and Found.”
  - **Expected:** The post is published with the “Lost and Found” category displayed.

- [ ] **FT-04: Resident can create a community event post**
  - **Action:** Submit a short post describing a neighborhood event and select “Community Event.”
  - **Expected:** The post is published with the “Community Event” category displayed.

- [ ] **FT-05: User can browse recent alerts**
  - **Action:** Open the main feed after signing in.
  - **Expected:** Existing alerts are displayed as posts, with each post showing its message, category, author or resident attribution, and posting information.

- [ ] **FT-06: User can comment on a post**
  - **Action:** Open a default feed post, enter an update in its comment field, and select “Comment” or “Submit.”
  - **Expected:** The comment is added to that post and is visibly associated with the correct post.

- [ ] **FT-07: User can mark an important alert as resolved**
  - **Action:** Open an alert that is not resolved and select “Mark as Resolved” or the equivalent control.
  - **Expected:** The alert is marked as resolved and its resolved status is visible in the feed or post details.

- [ ] **FT-08: User can mark an alert as no longer relevant**
  - **Action:** Open an active alert and select “No Longer Relevant” or the equivalent control.
  - **Expected:** The alert is marked as no longer relevant and its updated status is visible.

- [ ] **FT-09: User can filter the feed by category**
  - **Action:** Select each available category filter, including “Safety Alert,” “Lost and Found,” and “Community Event.”
  - **Expected:** The feed displays only posts matching the selected category.

- [ ] **FT-10: User can search alerts by keyword**
  - **Action:** Enter a keyword that appears in a default post and submit or activate the search.
  - **Expected:** The feed displays posts containing or matching that keyword.

## Constraint
- [ ] **CS-01: Required sign-up fields prevent incomplete registration**
  - **Action:** Leave one or more required sign-up fields empty and select “Sign Up.”
  - **Expected:** Registration is blocked and each missing required field displays a clear validation message.

- [ ] **CS-02: Posts cannot be submitted without required content**
  - **Action:** Open the post form, leave the message empty, and select “Post” or “Submit.”
  - **Expected:** The post is not created and the form identifies that post content is required.

- [ ] **CS-03: Posts cannot be submitted without a category**
  - **Action:** Enter valid post content, leave the category unselected, and select “Post” or “Submit.”
  - **Expected:** The post is not created and the form indicates that a category must be selected.

- [ ] **CS-04: Empty comments cannot be submitted**
  - **Action:** Leave a post’s comment field empty or enter only whitespace, then select “Comment” or “Submit.”
  - **Expected:** No comment is created and the interface identifies that comment text is required.

- [ ] **CS-05: Feed filters do not show posts from other categories**
  - **Action:** Select one category filter and compare all displayed post category labels with the selected category.
  - **Expected:** Every displayed post belongs to the selected category; posts from other categories are excluded.

## Interaction
- [ ] **IX-01: Category filter updates the feed state**
  - **Action:** Change the category filter from one category to another and observe the feed.
  - **Expected:** The selected category is visibly indicated and the feed updates to the new category without retaining results from the previous selection.

- [ ] **IX-02: Search provides a clear no-results state**
  - **Action:** Search for a unique keyword that does not appear in any default post.
  - **Expected:** The feed shows a clear “no results” message or equivalent empty state instead of unrelated posts.

- [ ] **IX-03: Post status control updates after resolution**
  - **Action:** Mark an active alert as resolved, then return to or refresh the feed.
  - **Expected:** The alert continues to display its resolved state, and the available status control reflects that it is no longer active.

- [ ] **IX-04: Successful submissions provide user feedback**
  - **Action:** Successfully submit a post or comment.
  - **Expected:** The interface provides visible confirmation of success and clears or closes the completed input form.

## Content
- [ ] **CT-01: Category labels use the required neighborhood-watch terminology**
  - **Action:** Review category selectors and category labels on feed posts.
  - **Expected:** The interface supports and displays “Safety Alert,” “Lost and Found,” and “Community Event” as distinct categories.

- [ ] **CT-02: Feed content is relevant to neighborhood safety and community activity**
  - **Action:** Review the default feed posts, their categories, and their visible comments.
  - **Expected:** Displayed content concerns local safety concerns, lost-and-found items, or community events; unrelated placeholder content is not shown.