# Test Checklist

## Functionality
- [ ] FT-01: New User Account Registration
  - Action: Navigate to the "/signup" page, fill in valid credentials in the username, email, and password fields, and click the "Sign Up" button.
  - Expected: Account is created, the user is automatically logged in, and the browser redirects to the dashboard with a session confirmation.
- [ ] FT-02: Publish Markdown Post with Custom and Intelligent Tags
  - Action: In the post editor, enter a title, technical Markdown body text (e.g., Python code snippets), enter "Technology" in the "Custom Tags" input, and click "Publish".
  - Expected: Post publishes to the author's profile page showing the custom tag "Technology" and auto-extracted intelligent tags (e.g., "Python").
- [ ] FT-03: Edit and Update Published Post
  - Action: Navigate to an existing post on the author's profile page, click "Edit Post", update the Markdown body content, and click "Save Changes".
  - Expected: The updated content is saved and immediately reflected on the published article view with the latest modification timestamp.
- [ ] FT-04: Post Reading and Comment Submission
  - Action: As a visitor, open a published article, type "Great write-up!" into the comment textarea under the article, and click "Post Comment".
  - Expected: The comment appears immediately in the comment list below the article with the author's name and timestamp.
- [ ] FT-05: Like and Save Post to Personal List
  - Action: Click the "Like" button and the "Save" button on an article page, then navigate to the "Saved Posts" tab on the user profile.
  - Expected: The like counter increments by 1, and the article is present in the user's "Saved Posts" list.
- [ ] FT-06: Dual-Dimension Tag Filtering and Combined Search
  - Action: On the explore page, select the custom tag "Technology", select the intelligent tag "Python", and click "Apply Filter".
  - Expected: The article list updates to show only articles tagged with both "Technology" and "Python".
- [ ] FT-07: Save and Apply Tag Groups for Quick Access
  - Action: Select multiple tags ("Technology" and "Python"), click "Save Tag Group", input name "Tech-Stack", click "Save", and then click the newly created "Tech-Stack" shortcut in the sidebar.
  - Expected: The tag group is saved to the sidebar, and clicking it automatically applies the combined filter to the article list.
- [ ] FT-08: Generate Tag Popularity Analysis Report
  - Action: In the author backend, navigate to the "Analytics" tab and click the "Generate Popularity Report" button.
  - Expected: The system generates and renders a tag popularity report showing page views, like counts, and comment counts broken down by tag.

## Constraint
- [ ] CS-01: Prevent Publishing Post with Missing Required Fields
  - Action: In the post editor, leave the title and content fields blank, and click the "Publish" button.
  - Expected: Submission is blocked, the post is not published, and validation messages "Title is required" and "Content cannot be empty" are displayed.
- [ ] CS-02: Prevent Blank Comment Submission
  - Action: Navigate to a post's comment box, leave the text area empty, and click the "Post Comment" button.
  - Expected: The comment is not submitted, and a validation message "Comment cannot be empty" appears below the textarea.
- [ ] CS-03: Prevent Duplicate Likes (Toggle Unlike)
  - Action: Click the "Like" button on a post that the logged-in user has already liked.
  - Expected: The like is removed, the like counter decrements by 1, and duplicate likes from the same user are prevented.
- [ ] CS-04: Prevent Duplicate Tag Group Name
  - Action: In the tag filter panel, attempt to save a new tag group using an existing group name and click "Save".
  - Expected: The save action is rejected, and an error message "Tag group name already exists" is displayed.

## Interaction
- [ ] IX-01: Markdown Real-time Preview Mode Toggle
  - Action: In the post editor, enter Markdown syntax (`# Header`, `**bold**`, ```` ```code``` ````) and click the "Preview" tab.
  - Expected: The view switches instantly to formatted HTML showing styled headers, bold text, and formatted code snippets.
- [ ] IX-02: Tag Chip Selection and Deselection Visual State
  - Action: Click a tag chip in the filter panel, then click the "×" icon on the selected tag chip.
  - Expected: The chip highlights with an active background color when clicked, and returns to its default unselected state when "×" is clicked.
- [ ] IX-03: Save Post Visual Feedback and Toast Notification
  - Action: Click the "Save" icon button on any article card.
  - Expected: The bookmark icon changes to a filled active state and a toast notification reading "Post saved to your personal list" is displayed.

## Content
- [ ] CT-01: Markdown Elements Rendering Integrity
  - Action: View a published post containing code blocks, tables, blockquotes, and hyperlinks.
  - Expected: All Markdown elements render properly with correct typographic styling: syntax-highlighted code blocks, formatted tables, styled blockquotes, and clickable hyperlinks.
- [ ] CT-02: Author Backend Tag Metrics Data Consistency
  - Action: Navigate to the author backend "Tag Overview" table and inspect the metric values for any listed tag.
  - Expected: The displayed page views, like counts, and comment counts for each tag match the sum of metrics of all published articles under that tag.