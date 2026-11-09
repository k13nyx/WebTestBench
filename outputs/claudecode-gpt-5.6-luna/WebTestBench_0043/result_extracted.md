# Test Result

## Functionality

- [X] FT-01: User can create an account and access their personal profile and author backend.
  - Action: Select **Sign Up**, complete all required fields with valid data, and submit.
  - Expected: The account is created successfully, the user is signed in, and profile/backend access is available.

- [X] FT-02: Author can write and save a post using Markdown.
  - Action: Open the post editor, enter a title and Markdown content, then select **Save**.
  - Expected: The post is saved and its Markdown formatting is preserved in the editor or preview.

- [X] FT-03: Author can edit an existing post and publish it.
  - Action: Open a saved post, change its title or content, save the change, and select **Publish**.
  - Expected: The updated content is published and available from the author’s profile page.

- [X] FT-04: Published posts appear on the author’s profile page.
  - Action: Open the author profile after publishing a post.
  - Expected: The published post is listed with its title and can be opened.

- [X] FT-05: Visitor can open and read a published post.
  - Action: Open a published post from the author profile or article listing.
  - Expected: The post page displays the title, author, published content, and Markdown rendered as readable formatting.

- [X] FT-06: Visitor can submit a comment under a post.
  - Action: Open a published post, enter valid comment text, and select **Comment** or **Submit**.
  - Expected: The comment appears under the post with the submitted text.

- [X] FT-07: User can like and unlike a post.
  - Action: Select the post’s **Like** control, then select it again.
  - Expected: The first selection increases or displays the user’s like state; the second removes that user’s like state.

- [X] FT-08: User can save a post to a personal list and access it later.
  - Action: Select **Save** on a post, then open the user’s saved-post list.
  - Expected: The post appears in the personal list and can be opened from there.

- [X] FT-09: Author can publish a post with custom tags.
  - Action: In the post editor, add `Technology`, `Life`, and `Reading Notes` as custom tags and publish the post.
  - Expected: All three custom tags are associated with the published post and displayed wherever post tags are shown.

- [ ] FT-10: System generates intelligent tags from published article content.
  - Action: Publish or inspect a code-related article containing Python and frontend-development content.
  - Expected: Intelligent tags are generated and include relevant keywords such as `Python` and `Frontend Development`.
  - Bug Report:
    - Issue: Incomplete intelligent tag extraction
    - Actual: The editor generated intelligent tags including `Python`, `React`, `Tutorial`, and `Reading Notes`, but did not generate the expected `Frontend Development` tag.

- [X] FT-11: Author backend displays article metrics grouped by tag.
  - Action: Open the author backend’s tag analytics area and select a custom or intelligent tag.
  - Expected: Articles under that tag display page views, like counts, and comment counts.

- [ ] FT-12: Author can generate a tag popularity analysis report.
  - Action: Open tag analytics and select **Generate Report**.
  - Expected: A report is produced showing tag popularity based on the available article activity metrics.
  - Bug Report:
    - Issue: Missing Generate Report control
    - Actual: The Analytics tab displays a Tag Popularity Report automatically, but no **Generate Report** control is available to perform the requested action.

## Constraint

- [X] CS-01: Required account, post, and comment fields cannot be submitted empty.
  - Action: Submit each relevant form with one or more required fields blank.
  - Expected: Submission is blocked and a clear required-field validation message is shown.

- [X] CS-02: Only the post author can edit or publish their own draft or post.
  - Action: While signed in as a different user, open another author’s post and check available actions.
  - Expected: Edit and author-only publishing controls are unavailable or access is denied.

- [X] CS-03: A user cannot create duplicate likes or duplicate saved-list entries for the same post.
  - Action: Select **Like** or **Save** repeatedly for the same post.
  - Expected: The like count increases at most once for that user, and the saved list contains at most one entry for that post.

- [ ] CS-04: Tag filtering supports both dimensions and combined conditions.
  - Action: Select custom tag `Technology` and intelligent tag `Python`, then apply the filter.
  - Expected: Results contain only articles matching both selected tags; clearing either selection updates the results accordingly.
  - Bug Report:
    - Issue: Incorrect combined tag-filter results
    - Actual: After selecting `Technology` and `Python`, the page displayed the matching post in the upper listing while the `Filtered Stories (1)` section simultaneously stated `No posts match the selected tags.`

## Interaction

- [X] IX-01: Post actions provide immediate state feedback.
  - Action: Like and save a post, then observe the controls and counts.
  - Expected: The controls visibly change to the active state and the corresponding count or saved status updates without requiring a page refresh.

- [X] IX-02: Frequently used tag groups can be saved and reused.
  - Action: Apply a multi-tag filter, select **Save Tag Group**, name it, then open the saved tag-group list and select it.
  - Expected: The tag group is saved and reapplying it restores the same custom-tag and intelligent-tag filters.

## Content

- [ ] CT-01: Article listings and tag results display relevant, accurate post information.
  - Action: Compare a post’s title, author, custom tags, intelligent tags, and displayed metrics between its detail page and filtered/listing views.
  - Expected: The information is relevant to the selected article and matches across all views.
  - Bug Report:
    - Issue: Inconsistent tag information across views
    - Actual: The post detail page displayed custom tags `Technology`, `Life`, and `Reading Notes`, while the profile and listing views displayed only `Technology` and `Life`. Intelligent tags were also visible in the editor but were not displayed in the profile or listing views.

- [X] CT-02: Tag popularity reports contain identifiable tag and metric data.
  - Action: Open a generated tag popularity report.
  - Expected: Each reported tag is clearly named and includes its associated popularity or activity values, including page views, likes, and comments where applicable.
