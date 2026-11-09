# Test Result

## Functionality
- [X] FT-01: User Registration and Profile Redirection
  - Action: Fill in the signup form with valid name, email, and password (at least 8 chars with letters and numbers) and submit.
  - Expected: Registration succeeds, user session is created, and user is redirected to the home dashboard.
- [ ] FT-02: Publish Article to Personal Profile
  - Action: Write and publish a new post titled "Python Data Science" with tags "Technology" and content containing Python code blocks, then navigate to the profile page.
  - Expected: The post appears on the author's profile page with the custom tag "Technology" and the extracted intelligent tag "Python".
  - Bug Report:
    - Issue: Missing Intelligent Tag on Post Card
    - Actual: The post appears on the author's profile page, but only the custom tag "Technology" is rendered. The extracted intelligent tag "Python" (stored in `post.autoTags`) is omitted because `PostCard.tsx` exclusively maps `post.tags` and does not render `post.autoTags`.
- [X] FT-03: Edit and Update Existing Article
  - Action: Open an existing published article, click "Edit", modify the content by adding a new paragraph, and click "Save".
  - Expected: The updated content is saved and immediately reflected on the article detail page with an updated timestamp.
- [X] FT-04: Comment on an Article
  - Action: Navigate to an article detail page, type a comment "Great insights!" in the comment input area, and click "Post Comment".
  - Expected: The comment is submitted successfully and immediately displayed in the comment list with author name and timestamp.
- [X] FT-05: Like and Save Post to Personal List
  - Action: On an article detail page, click the "Like" button and the "Save" (bookmark) button, then navigate to the "/saved" page.
  - Expected: The like counter increments by 1, and the saved article appears in the user's personal saved list.
- [X] FT-06: Dual-Dimension Tag Filtering and Combined Search
  - Action: On the explore page, select the custom tag "Technology", select the intelligent tag "Python", and click "Apply Filter".
  - Expected: The article list updates to show only articles tagged with both "Technology" and "Python".
- [X] FT-07: Save and Apply Tag Groups for Quick Access
  - Action: Select the custom tag "Technology" and intelligent tag "Python", click "Save Tag Group", name it "Tech-Stack", save it, and then click the "Tech-Stack" tag group shortcut.
  - Expected: The "Tech-Stack" group is saved and selecting it immediately applies the filter for both "Technology" and "Python".
- [X] FT-08: Generate Tag Popularity Analysis Report
  - Action: In the author backend, navigate to the "Analytics" tab and click "Generate Popularity Report".
  - Expected: A report is generated showing total page views, like counts, and comment counts broken down by tag, along with a tag popularity ranking.

## Constraint
- [ ] CS-01: Prevent Empty Post Submission
  - Action: On the post creation page, leave both title and content empty and click "Publish".
  - Expected: Submission is blocked, and validation messages "Title is required" and "Content cannot be empty" are displayed.
  - Bug Report:
    - Issue: Incorrect Validation Feedback and Sequential Blocking
    - Actual: Submission is blocked, but validation messages "Title is required" and "Content cannot be empty" are not displayed. The application displays toasts titled "Title required" and "Content required", and evaluates fields sequentially—halting immediately after title validation fails without evaluating or displaying content validation at the same time.
- [ ] CS-02: Prevent Blank Comment Submission
  - Action: In the comment section of an article, leave the comment input empty (or only whitespace) and attempt to click "Post Comment".
  - Expected: Submission is blocked, and an inline error message "Comment cannot be empty" is displayed below the input area.
  - Bug Report:
    - Issue: Missing Inline Validation Message and Disabled Button Control
    - Actual: Submission is blocked because the "Post Comment" button has the HTML `disabled` attribute (`disabled={!newComment.trim()}`) when the input is empty or whitespace, preventing click interaction. No inline error message "Comment cannot be empty" is displayed below the input area.
- [X] CS-03: Prevent Duplicate Liking on Same Article
  - Action: Click the "Like" button on an article that the user has already liked.
  - Expected: The like count decrements by 1 (toggle unlike) and does not allow multiple active likes from the same user session.
- [ ] CS-04: Prevent Duplicate Tag Group Name
  - Action: Attempt to save another tag group with the name "Tech-Stack".
  - Expected: The system rejects the creation and displays an error message "Tag group name already exists".
  - Bug Report:
    - Issue: Duplicate Tag Group Creation Allowed
    - Actual: The system does not reject the creation of a duplicate tag group; attempting to save another tag group with the name "Tech-Stack" saves a second group with the identical name into `localStorage` (`blog_saved_tag_groups`), and no error message "Tag group name already exists" is displayed.

## Interaction
- [X] IX-01: Real-time Markdown Preview Rendering
  - Action: In the post editor, enter Markdown syntax (# Heading, **bold**, `code`) and toggle between "Write" and "Preview" tabs.
  - Expected: The preview tab immediately renders formatted HTML headings, bold text, and code blocks matching the input Markdown.
- [X] IX-02: Tag Chip Selection and Deselection Visual State
  - Action: Click a tag chip in the filter panel, then click the "×" icon on the selected tag chip.
  - Expected: The chip highlights with an active background color when clicked, and returns to its default unselected state when "×" is clicked.
- [ ] IX-03: Visual Feedback on Liking and Saving Posts
  - Action: Click the "Like" (heart) icon and "Save" (bookmark) icon on a post card.
  - Expected: The heart icon toggles to a filled active state with counter increment, and the bookmark icon toggles to a filled active state with a toast notification "Post saved to your personal list".
  - Bug Report:
    - Issue: Incomplete Visual State Feedback and Missing Notification Toast
    - Actual: Clicking the bookmark/save icon toggles from `BookmarkPlus` to `BookmarkCheck` without a filled active state styling (`fill-current` or filled background), and no toast notification "Post saved to your personal list" is triggered upon saving.

## Content
- [X] CT-01: Markdown Typography and Styling Verification
  - Action: View a published article containing code blocks, tables, blockquotes, and hyperlinks.
  - Expected: Code blocks display with syntax highlighting and background styling, tables show clear borders and header row distinctions, blockquotes display a left accent border, and hyperlinks are underlined with accent color.
- [X] CT-02: Author Backend Tag Metrics Data Consistency
  - Action: Compare the tag metrics (views, likes, comments) shown in the popularity report against the sum of the corresponding metrics of published articles under that tag.
  - Expected: The tag metrics in the report exactly match the aggregated sums of views, likes, and comments from all published articles tagged with that tag.
