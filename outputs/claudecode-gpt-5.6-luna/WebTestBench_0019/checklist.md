# Test Checklist

## Functionality

- [ ] **FT-01: User can register for a forum account**
  - **Action:** Open **Register**, enter valid account details, and submit the form.
  - **Expected:** The account is created successfully and the user receives access to the forum.

- [ ] **FT-02: User can create and save a profile**
  - **Action:** Open the profile settings, enter a short bio and one or more interests, then select **Save Profile**.
  - **Expected:** The profile saves successfully, and the saved bio and interests are visible on the user’s profile.

- [ ] **FT-03: User can browse discussion categories**
  - **Action:** Open the forum category list and select an available category.
  - **Expected:** The selected category page opens and displays threads assigned to that category.

- [ ] **FT-04: User can start a discussion thread**
  - **Action:** Select **New Thread**, choose a category, enter a title and message, and submit the thread.
  - **Expected:** The new thread is published in the selected category and appears in the thread list.

- [ ] **FT-05: User can reply to an existing discussion**
  - **Action:** Open an existing thread, enter a reply, and select **Reply** or **Post Reply**.
  - **Expected:** The reply appears within the selected discussion with the reply author and posting time.

- [ ] **FT-06: User can upvote or like a helpful post**
  - **Action:** Select the **Upvote** or **Like** control on an existing post.
  - **Expected:** The post’s displayed vote or like total increases by one and the user’s interaction is recorded.

- [ ] **FT-07: User can search for threads by keyword**
  - **Action:** Enter a keyword into the forum search field and submit the search.
  - **Expected:** Search results display threads whose titles or discussion content match the keyword.

- [ ] **FT-08: User can filter thread results by category**
  - **Action:** Apply a category filter to the thread list or search results.
  - **Expected:** Every displayed result belongs to the selected category.

- [ ] **FT-09: User can view trending or most active discussions**
  - **Action:** Open the **Trending** or **Most Active** discussions view.
  - **Expected:** A list of currently popular or highly active discussion threads is displayed.

- [ ] **FT-10: User can view discussion activity for a recent period**
  - **Action:** Select an available recent-period option in the trending or activity view.
  - **Expected:** The displayed list refreshes to show discussions active within the selected recent period.

## Constraint

- [ ] **CS-01: Registration cannot be completed with invalid or missing required details**
  - **Action:** Submit the registration form with required fields empty or with invalid account details.
  - **Expected:** Registration is blocked and each invalid or missing field is identified with a validation message.

- [ ] **CS-02: A thread cannot be published without a category, title, and message**
  - **Action:** Open **New Thread** and attempt to submit while omitting each required value individually.
  - **Expected:** The thread is not published, and the missing value is identified.

- [ ] **CS-03: An empty reply cannot be submitted**
  - **Action:** Open an existing thread and select **Reply** or **Post Reply** without entering text.
  - **Expected:** No reply is created and the reply field displays a required-content validation message.

- [ ] **CS-04: A user cannot add duplicate votes or likes to the same post**
  - **Action:** Select the **Upvote** or **Like** control on one post repeatedly.
  - **Expected:** The post receives at most one active vote or like from that user; a second selection either has no additional effect or removes the existing vote or like.

- [ ] **CS-05: Combining keyword search and category filtering excludes unrelated threads**
  - **Action:** Search for a keyword and apply a category filter that excludes at least one matching thread.
  - **Expected:** Results contain only threads matching the keyword and belonging to the selected category.

## Interaction

- [ ] **IX-01: Profile editing provides clear save feedback**
  - **Action:** Change the bio or interests and select **Save Profile**.
  - **Expected:** The interface shows a clear success state, and the saved values remain displayed after leaving and reopening the profile.

- [ ] **IX-02: The selected category is visibly reflected while browsing**
  - **Action:** Select different forum categories in succession.
  - **Expected:** The active category is visibly indicated and the thread list updates to the selected category.

- [ ] **IX-03: Search provides a clear no-results state**
  - **Action:** Search for a keyword that does not match any available thread.
  - **Expected:** The interface shows a clear no-results message and does not display unrelated threads.

- [ ] **IX-04: The vote or like control reflects the user’s current state**
  - **Action:** Select the **Upvote** or **Like** control on a post, then select it again if toggling is supported.
  - **Expected:** The control’s selected/unselected appearance and displayed total accurately reflect the current vote or like state.

## Content

- [ ] **CT-01: Profile content accurately represents the user’s bio and interests**
  - **Action:** Open a profile containing a saved bio and interests.
  - **Expected:** The profile displays the complete saved bio and every saved interest without substitution or unrelated content.

- [ ] **CT-02: Discussion threads display essential identifying content**
  - **Action:** Open a thread from a category or search result.
  - **Expected:** The thread displays its title, category, author, posting time, and discussion body.

- [ ] **CT-03: Search results contain relevant thread information**
  - **Action:** Search for a keyword that matches existing threads.
  - **Expected:** Each result shows enough relevant information, such as the matching title or excerpt, to identify why it matched.

- [ ] **CT-04: Trending or active discussion entries show current activity context**
  - **Action:** Open the trending or most active discussions view for a recent period.
  - **Expected:** Each entry identifies the discussion and displays an activity indicator or count plus information showing the applicable recent period.