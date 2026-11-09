# Test Result

## Functionality

- [ ] FT-01: Create a top-level topic page with content.
  - Action: Select **New Page**, enter a title and content, and save it.
  - Expected: The new topic page appears in the knowledge base with the entered title and content.
  - Bug Report:
    - Issue: Unresponsive New Page control
    - Actual: The New Page plus button is visible, but clicking it does not open a page editor or provide title/content fields.

- [ ] FT-02: Create a nested subpage under an existing topic page.
  - Action: Open an existing topic page, choose **New Subpage**, enter a title and content, and save it.
  - Expected: The subpage is displayed beneath its parent topic in the page hierarchy.
  - Bug Report:
    - Issue: Missing subpage creation control
    - Actual: No New Subpage control or editor is available when opening an existing topic page.

- [ ] FT-03: Create a bidirectional link between two pages.
  - Action: From one existing page, add a link to a second existing page and save the change.
  - Expected: The link is visible on the source page, and the linked page identifies the source page as a backlink.
  - Bug Report:
    - Issue: Missing link-editing control
    - Actual: Existing page links and backlink sections are displayed, but no control is available to add a new link or save the relationship.

- [ ] FT-04: Add tags to a page.
  - Action: Open an existing page, add one or more tags, and save the page.
  - Expected: The selected tags are displayed on the page and can be used for filtering.
  - Bug Report:
    - Issue: Missing tag-editing control
    - Actual: Existing tags are displayed and can be filtered, but no page editor or control is available to add tags.

- [ ] FT-05: Create a citation relationship with a citation note.
  - Action: Open an existing page, cite another existing page, enter a citation note, and save the relationship.
  - Expected: The citation and its note are associated with the page and available when viewing citation details.
  - Bug Report:
    - Issue: Missing citation-editing control
    - Actual: Existing citation relationships and notes are displayed, but no control is available to create or save a citation relationship.

- [X] FT-06: Display a page’s complete knowledge context.
  - Action: Open a page that has content, tags, outgoing citations, and incoming citations.
  - Expected: The page view displays its content, tags, pages it cites, and pages that cite it.

- [X] FT-07: Browse pages through hierarchical navigation.
  - Action: Expand a parent page in the navigation tree and select one of its nested subpages.
  - Expected: The child page opens, and its position under the parent remains visible in the hierarchy.

- [X] FT-08: Follow a chain of page links.
  - Action: Open a page link, then select a link on the destination page.
  - Expected: Each selected link opens the corresponding related page without losing the ability to navigate back.

- [X] FT-09: Follow a chain of citation relationships.
  - Action: Open a page’s citation list, select a cited page, and then select one of that page’s cited or citing pages.
  - Expected: Each selected citation opens the correct related page and preserves the citation relationship context.

## Constraint

- [ ] CS-01: Prevent a page from being saved without a title.
  - Action: Open the page editor, leave the title empty, and attempt to save.
  - Expected: The page is not saved, and a required-title validation message is displayed.
  - Bug Report:
    - Issue: Page editor unavailable
    - Actual: No page editor or save control opens from the New Page button, so the required-title validation cannot be triggered or observed.

- [ ] CS-02: Prevent contradictory or duplicate citation relationships.
  - Action: Attempt to add the same page as a citation more than once from the same source page.
  - Expected: The duplicate citation is rejected or consolidated so only one citation relationship remains.
  - Bug Report:
    - Issue: Citation relationship editor unavailable
    - Actual: No control is available to add or duplicate a citation relationship, so duplicate handling cannot be verified.

- [ ] CS-03: Preserve bidirectional link consistency.
  - Action: Create a link from Page A to Page B, then remove the link from Page A.
  - Expected: The link is removed from Page A and the corresponding backlink is also removed from Page B.
  - Bug Report:
    - Issue: Link management controls unavailable
    - Actual: Existing links and backlinks are read-only in the visible interface; no controls are available to create or remove a link.

- [ ] CS-04: Keep nested pages associated with their selected parent.
  - Action: Move or edit a subpage using the available hierarchy controls and save the change.
  - Expected: The subpage appears under exactly the selected parent and is not shown as an unrelated top-level page.
  - Bug Report:
    - Issue: Hierarchy editing controls unavailable
    - Actual: The hierarchy can be expanded and selected, but no move, edit, or save control is available for changing a subpage’s parent.

## Interaction

- [ ] IX-01: Confirm successful page and relationship saves.
  - Action: Save a page after adding content, tags, a link, or a citation.
  - Expected: The interface provides a visible save confirmation and displays the updated information without requiring a manual refresh.
  - Bug Report:
    - Issue: Missing save workflow
    - Actual: No page or relationship editor opens, so no save action or save confirmation is provided.

- [X] IX-02: Update navigation state when opening related pages.
  - Action: Select a page from the hierarchy, a page link, or a citation link.
  - Expected: The selected page becomes the active page, and the navigation state clearly indicates the current location.

- [X] IX-03: Apply and clear knowledge-base filters.
  - Action: Apply a tag filter, then clear the filter.
  - Expected: Only pages matching the selected tag are shown while active; clearing it restores the unfiltered page list.

- [X] IX-04: Search by title, tag, and citation note.
  - Action: Enter a known title term, a known tag, and a known citation-note term in the search control.
  - Expected: Each search returns the pages matching that field, and clearing the search restores the full available list.

## Content

- [X] CT-01: Display accurate page metadata and relationship labels.
  - Action: Compare an opened page with its saved data and related pages.
  - Expected: The displayed title, content, tags, cited pages, citing pages, hierarchy labels, and citation notes exactly match the stored relationships and text.
