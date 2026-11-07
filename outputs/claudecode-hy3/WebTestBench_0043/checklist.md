# Test Checklist

## Functionality
- [ ] FT-01: User can sign up for a new account
  - Action: Open the sign-up page, fill required fields (username/email/password), click "Sign Up"
  - Expected: Account is created and the user is logged in / redirected to their home

- [ ] FT-02: User can write a post using the Markdown editor
  - Action: Open "New Post", type Markdown content (headings, lists, code), click "Save Draft"
  - Expected: A draft post is created containing the entered content

- [ ] FT-03: User can publish a post to their profile page
  - Action: Open a draft, click "Publish"
  - Expected: The post appears on the author's profile page

- [ ] FT-04: User can edit an existing published post
  - Action: Open a published post, click "Edit", change content, click "Save"
  - Expected: The post content is updated and the change is visible in reading view

- [ ] FT-05: A visitor can open and read any post
  - Action: Click a post title from the listing or profile page
  - Expected: The post opens in a full reading view showing its content

- [ ] FT-06: A visitor can leave a comment under a post
  - Action: Scroll to comments, enter text in the comment box, click "Comment"
  - Expected: The new comment appears in the comment list under the post

- [ ] FT-07: A user can like a post
  - Action: Click the "Like" button on a post
  - Expected: The like count increments by 1 and the button shows a liked state

- [ ] FT-08: A user can save a post to a personal list
  - Action: Click the "Save" / "Save to List" button on a post
  - Expected: The post is added to the user's personal saved list and is retrievable there

- [ ] FT-09: Author can add custom tags when publishing
  - Action: On publish, enter custom tags (e.g., "Technology", "Life", "Reading Notes")
  - Expected: The custom tags are attached to and displayed on the post

- [ ] FT-10: System auto-generates intelligent tags from content
  - Action: Publish a code-related post containing terms like "Python"
  - Expected: Intelligent tags (e.g., "Python", "Frontend Development") are automatically extracted and shown on the post

- [ ] FT-11: Visitor can filter posts by combined custom + intelligent tags
  - Action: Select a custom tag (e.g., "Technology") and an intelligent tag (e.g., "Python"), click "Apply Filter"
  - Expected: Only posts matching both selected tags are displayed

- [ ] FT-12: User can save frequently-used tag groups for quick access
  - Action: Build a tag filter combination, click "Save Tag Group", name it
  - Expected: The tag group is saved and selectable later from a saved-groups list

- [ ] FT-13: Author can view per-tag stats (views, likes, comments)
  - Action: Open the personal backend, navigate to the tag statistics view
  - Expected: Each tag shows its page views, like counts, and comment counts

- [ ] FT-14: Author can generate a tag popularity analysis report
  - Action: In the backend, click "Generate Report" for tag popularity
  - Expected: A popularity analysis report is produced summarizing tag metrics

## Constraint
- [ ] CS-01: Publishing is blocked when required fields are empty
  - Action: Click "Publish" with an empty title or empty content
  - Expected: Publish is prevented and a validation message identifies the missing field

- [ ] CS-02: No-match tag filter shows an empty state (not an error)
  - Action: Select a tag combination that matches no posts, click "Apply Filter"
  - Expected: An empty-state message is shown and the app does not crash

## Interaction
- [ ] IX-01: Markdown renders as formatted content in reading view
  - Action: Open a post written with Markdown (headings, lists, code blocks)
  - Expected: Content displays with proper visual formatting (styled headings, lists, code)

- [ ] IX-02: Success toast appears after publishing a post
  - Action: Click "Publish" on a valid post
  - Expected: A success notification/toast is displayed confirming publication

- [ ] IX-03: Tag filtering updates the post list dynamically
  - Action: Apply or change a tag filter
  - Expected: The post list updates immediately to reflect the selection

## Content
- [ ] CT-01: An author's profile page shows only that author's posts
  - Action: Open a specific author's profile page
  - Expected: The page lists only posts published by that author, with relevant titles/tags