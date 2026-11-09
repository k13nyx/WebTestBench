# Test Result

## Functionality

- [X] FT-01: User can register for a forum account
  - Action: Open **Register**, enter valid account details, and submit the form.
  - Expected: The account is created successfully and the user receives access to the forum.

- [X] FT-02: User can create and save a profile
  - Action: Open the profile settings, enter a short bio and one or more interests, then select **Save Profile**.
  - Expected: The profile saves successfully, and the saved bio and interests are visible on the user’s profile.

- [X] FT-03: User can browse discussion categories
  - Action: Open the forum category list and select an available category.
  - Expected: The selected category page opens and displays threads assigned to that category.

- [X] FT-04: User can start a discussion thread
  - Action: Select **New Thread**, choose a category, enter a title and message, and submit the thread.
  - Expected: The new thread is published in the selected category and appears in the thread list.

- [X] FT-05: User can reply to an existing discussion
  - Action: Open an existing thread, enter a reply, and select **Reply** or **Post Reply**.
  - Expected: The reply appears within the selected discussion with the reply author and posting time.

- [X] FT-06: User can upvote or like a helpful post
  - Action: Select the **Upvote** or **Like** control on an existing post.
  - Expected: The post’s displayed vote or like total increases by one and the user’s interaction is recorded.

- [X] FT-07: User can search for threads by keyword
  - Action: Enter a keyword into the forum search field and submit the search.
  - Expected: Search results display threads whose titles or discussion content match the keyword.

- [ ] FT-08: User can filter thread results by category
  - Action: Apply a category filter to the thread list or search results.
  - Expected: Every displayed result belongs to the selected category.
  - Bug Report:
    - Issue: Missing Category Filter Control
    - Actual: The application provides category navigation pages, but no category filter control is available on the thread list or search results to combine with or filter those results.

- [X] FT-09: User can view trending or most active discussions
  - Action: Open the **Trending** or **Most Active** discussions view.
  - Expected: A list of currently popular or highly active discussion threads is displayed.

- [ ] FT-10: User can view discussion activity for a recent period
  - Action: Select an available recent-period option in the trending or activity view.
  - Expected: The displayed list refreshes to show discussions active within the selected recent period.
  - Bug Report:
    - Issue: Missing Recent-Period Selector
    - Actual: The interface provides Trending, Recent, and Most Active views, but no selectable recent-period option was available within the trending or activity view.

## Constraint

- [ ] CS-01: Registration cannot be completed with invalid or missing required details
  - Action: Submit the registration form with required fields empty or with invalid account details.
  - Expected: Registration is blocked and each invalid or missing field is identified with a validation message.
  - Bug Report:
    - Issue: Incomplete Field-Level Validation
    - Actual: Submitting the empty registration form displayed only the generic message “Please fill in all fields”; individual missing fields were not identified with separate validation messages.

- [ ] CS-02: A thread cannot be published without a category, title, and message
  - Action: Open **New Thread** and attempt to submit while omitting each required value individually.
  - Expected: The thread is not published, and the missing value is identified.
  - Bug Report:
    - Issue: Generic Thread Validation
    - Actual: Submitting without required values displayed only the generic message “Please fill in all fields”; the specific missing category, title, or message was not identified.

- [ ] CS-03: An empty reply cannot be submitted
  - Action: Open an existing thread and select **Reply** or **Post Reply** without entering text.
  - Expected: No reply is created and the reply field displays a required-content validation message.
  - Bug Report:
    - Issue: Missing Required-Content Validation Message
    - Actual: The empty reply form kept the “Post Reply” button disabled and displayed no required-content validation message in the reply field.

- [X] CS-04: A user cannot add duplicate votes or likes to the same post
  - Action: Select the **Upvote** or **Like** control on one post repeatedly.
  - Expected: The post receives at most one active vote or like from that user; a second selection either has no additional effect or removes the existing vote or like.

- [ ] CS-05: Combining keyword search and category filtering excludes unrelated threads
  - Action: Search for a keyword and apply a category filter that excludes at least one matching thread.
  - Expected: Results contain only threads matching the keyword and belonging to the selected category.
  - Bug Report:
    - Issue: Combined Search and Category Filtering Unavailable
    - Actual: Keyword search worked, but no category filter control was available to combine with the search results.

## Interaction

- [X] IX-01: Profile editing provides clear save feedback
  - Action: Change the bio or interests and select **Save Profile**.
  - Expected: The interface shows a clear success state, and the saved values remain displayed after leaving and reopening the profile.

- [X] IX-02: The selected category is visibly reflected while browsing
  - Action: Select different forum categories in succession.
  - Expected: The active category is visibly indicated and the thread list updates to the selected category.

- [X] IX-03: Search provides a clear no-results state
  - Action: Search for a keyword that does not match any available thread.
  - Expected: The interface shows a clear no-results message and does not display unrelated threads.

- [X] IX-04: The vote or like control reflects the user’s current state
  - Action: Select the **Upvote** or **Like** control on a post, then select it again if toggling is supported.
  - Expected: The control’s selected/unselected appearance and displayed total accurately reflect the current vote or like state.

## Content

- [X] CT-01: Profile content accurately represents the user’s bio and interests
  - Action: Open a profile containing a saved bio and interests.
  - Expected: The profile displays the complete saved bio and every saved interest without substitution or unrelated content.

- [X] CT-02: Discussion threads display essential identifying content
  - Action: Open a thread from a category or search result.
  - Expected: The thread displays its title, category, author, posting time, and discussion body.

- [X] CT-03: Search results contain relevant thread information
  - Action: Search for a keyword that matches existing threads.
  - Expected: Each result shows enough relevant information, such as the matching title or excerpt, to identify why it matched.

- [ ] CT-04: Trending or active discussion entries show current activity context
  - Action: Open the trending or most active discussions view for a recent period.
  - Expected: Each entry identifies the discussion and displays an activity indicator or count plus information showing the applicable recent period.
  - Bug Report:
    - Issue: Missing Applicable Recent-Period Context
    - Actual: Trending and Most Active entries displayed activity counts and timestamps, but the interface did not provide a recent-period selection or clearly identify the applicable recent period.
