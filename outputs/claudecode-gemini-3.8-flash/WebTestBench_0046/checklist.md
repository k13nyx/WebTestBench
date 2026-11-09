# Test Checklist

## Functionality
- [ ] FT-01: Create a top-level topic page
  - Action: Click the "New Page" button, enter a title and content in the editor, and click "Save".
  - Expected: The new topic page is created and displayed in the main content area and page list.
- [ ] FT-02: Create a nested subpage under an existing page
  - Action: Open an existing topic page, click "Add Subpage", enter a title and content, and click "Save".
  - Expected: The subpage is created and appears nested under the parent topic in the hierarchical navigation.
- [ ] FT-03: Create a bidirectional link between pages
  - Action: In the page editor, insert a bidirectional link referencing an existing target page and save.
  - Expected: The link appears in the current page, and the current page automatically appears in the target page's incoming links list.
- [ ] FT-04: Add a citation relationship with a citation note
  - Action: Click "Add Citation", select an existing target page, type a citation note, and click "Save Citation".
  - Expected: The citation is saved and appears under the page's "Cites" section with the specified note.
- [ ] FT-05: Navigate using bidirectional links and citations
  - Action: Click on a linked page title in the "Cites" or "Cited By" list of the active page.
  - Expected: The application navigates to and displays the selected referenced page.
- [ ] FT-06: Search pages by title
  - Action: Enter an existing page title into the search input and press Enter.
  - Expected: The search results list displays only the pages whose titles match the search query.
- [ ] FT-07: Filter pages by tag
  - Action: Click on a tag name in the tag list or filter sidebar.
  - Expected: The displayed page list updates to show only pages assigned to the selected tag.
- [ ] FT-08: Filter or search by citation notes
  - Action: Enter a keyword from an existing citation note into the citation search/filter field.
  - Expected: The results list displays pages that contain or are cited with the matching citation note.

## Constraint
- [ ] CS-01: Prevent page creation with an empty title
  - Action: Click "New Page", leave the title field blank, and click "Save".
  - Expected: The page is not saved, and a validation error "Title cannot be empty" is displayed.
- [ ] CS-02: Prevent self-referencing citation
  - Action: Open the "Add Citation" modal on a page and attempt to select the currently opened page as the citation target.
  - Expected: The current page is disabled or excluded from the target selection list.
- [ ] CS-03: Prevent circular parent-child nesting
  - Action: Edit a parent page's hierarchy settings and select one of its own descendant subpages as its new parent.
  - Expected: The action is blocked, and an error message indicating invalid hierarchy or circular dependency is shown.
- [ ] CS-04: Empty state for non-matching search or filter queries
  - Action: Type a non-existent keyword into the search bar.
  - Expected: The results panel displays a "No matching pages found" message and lists zero page items.

## Interaction
- [ ] IX-01: Expand and collapse hierarchical navigation nodes
  - Action: Click the chevron toggle next to a parent topic in the hierarchical sidebar.
  - Expected: The nested subpage list toggles between expanded (visible) and collapsed (hidden) states.
- [ ] IX-02: Citation hover preview
  - Action: Hover the mouse cursor over a citation link within a page.
  - Expected: A popover card appears displaying a snippet of the cited page's content and its citation note.
- [ ] IX-03: Immediate update of citation backlink panel
  - Action: Add a citation to a target page and immediately navigate to that target page.
  - Expected: The target page's "Cited By" section reflects the newly added backlink without requiring a page refresh.

## Content
- [ ] CT-01: Page view structure and metadata display
  - Action: Open an existing page that contains tags and citations.
  - Expected: The view displays the page title, main content, assigned tags, a "Cites" section, and a "Cited By" section.
- [ ] CT-02: Citation details completeness
  - Action: View the "Cites" list on a page with existing citations.
  - Expected: Each citation item displays the referenced page title and its corresponding citation note text.
- [ ] CT-03: Visual indentation in hierarchical navigation
  - Action: Inspect the sidebar navigation containing parent topics and nested subpages.
  - Expected: Subpages are visually indented beneath their respective parent topics to reflect the hierarchy.