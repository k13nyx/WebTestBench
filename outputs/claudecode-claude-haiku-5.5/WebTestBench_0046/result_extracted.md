# Test Result

Test mapping: [Topic A] = Epistemology (nested under Philosophy, not top-level as the checklist specifies). [Subpage A1] = Gettier Problems. [Topic B] = Rationalism vs Empiricism for link tests, and Scientific Method for citation tests, because Epistemology cites Scientific Method and does not cite Rationalism. [Tag X] = knowledge. [Tag Y] was not usable (see CS-04).

## Functionality

- [X] FT-01: Opening a topic page shows its content, its tags, and its "Cites" and "Cited by" sections.
  - Action: In the sidebar hierarchy, click [Topic A], a top-level topic with at least one tag, one citation, and one citing page.
  - Expected: Page title, body content, tag list, "Cites" list, and "Cited by" list are all visible and match the default data.
- [X] FT-02: A nested subpage opens with its own content.
  - Action: Click the expand control on [Topic A] in the sidebar, then click its subpage [Subpage A1].
  - Expected: [Subpage A1] opens showing its own title and body content, not the parent's.
- [ ] FT-03: Breadcrumb shows the full ancestor path and each ancestor is clickable.
  - Action: On [Subpage A1], click the breadcrumb segment for [Topic A].
  - Expected: Breadcrumb reads [Topic A] > [Subpage A1] before the click; after it, [Topic A] opens.
  - Bug Report:
    - Issue: Missing Element (Breadcrumb)
    - Actual: On Gettier Problems, the DOM contains no breadcrumb or nav element and no "Epistemology > Gettier Problems" path. The ancestor segment cannot be clicked.
- [X] FT-04: Clicking an inline link in body text opens the linked page.
  - Action: On [Topic A], click the inline link to [Topic B] in the body text.
  - Expected: [Topic B] opens with its own title and content.
- [X] FT-05: The "Linked from" list shows pages that link to the current page, and each entry opens its page.
  - Action: Open [Topic B], then click the entry [Topic A] in its "Linked from" list.
  - Expected: "Linked from" lists [Topic A]; clicking it opens [Topic A].
- [X] FT-06: Clicking a tag on a page opens a list of all pages with that tag.
  - Action: On [Topic A], click the tag [Tag X].
  - Expected: Results list opens and contains [Topic A] and every other default page tagged [Tag X], and no others.
- [X] FT-07: Searching by a partial title returns matching pages.
  - Action: Type a distinctive partial title of [Topic B] into the search box and press Enter.
  - Expected: Results include [Topic B]; clicking its result opens [Topic B].
- [ ] FT-08: Searching by a phrase from a citation note returns the pages whose citation notes contain it.
  - Action: Type a distinctive phrase from the citation note on [Topic A]'s citation to [Topic B] into the search box and press Enter.
  - Expected: [Topic A] appears in the results, and the result indicates a match on citation note text.
  - Bug Report:
    - Issue: Missing Match Indicator
    - Actual: Searching "underlies scientific methodology" returns Epistemology (1 result), but the result shows only its title. No indication of a citation-note match appears anywhere in the result DOM.
- [ ] FT-09: Selecting a tag in the filter panel narrows results, and clearing it restores the full list.
  - Action: Open search with no query, select [Tag X] in the filter panel, then clear the filter.
  - Expected: With the filter, only pages tagged [Tag X] are listed; after clearing, the full default list returns.
  - Bug Report:
    - Issue: Incomplete Filter Reset
    - Actual: With knowledge selected, the list narrows correctly to 3 pages (Epistemology, Gettier Problems, The Knowledge Definition Debate). After "Clear filters", the search view shows only the tag panel and no page list.
- [ ] FT-10: Following a chain of links and citations, then using Back, returns through the pages in reverse order.
  - Action: From [Topic A], click link to [Topic B], then click a citation entry to [Topic C], then click Back twice.
  - Expected: Back returns to [Topic B], then to [Topic A], each with its content unchanged.
  - Bug Report:
    - Issue: Missing In-App History / Back Navigation
    - Actual: No in-app Back control exists. The app does not push history entries. Browser Back from Scientific Method (Topic C) left the app and showed about:blank, instead of returning to Rationalism vs Empiricism (Topic B).

## Constraint

- [X] CS-01: A page never lists itself in its own "Linked from", "Cites", or "Cited by" sections.
  - Action: Open [Topic A] and review all three sections.
  - Expected: The title [Topic A] does not appear in any of the three sections.
- [X] CS-02: Links are symmetric: if A links to B, B shows A in "Linked from".
  - Action: On [Topic A], note the link to [Topic B]. Open [Topic B] and check "Linked from".
  - Expected: [Topic A] appears in [Topic B]'s "Linked from" list.
- [X] CS-03: Citations are symmetric: if A cites B, B shows A in "Cited by" and A shows B in "Cites".
  - Action: On [Topic A], find its citation to [Topic B]. Open [Topic B] and check "Cited by". Return to [Topic A] and check "Cites".
  - Expected: [Topic A] appears in [Topic B]'s "Cited by", and [Topic B] appears in [Topic A]'s "Cites".
- [ ] CS-04: Multiple selected tags combine with AND logic.
  - Action: In the filter panel, select [Tag X] and then [Tag Y], where at least one default page has both and at least one has only one.
  - Expected: Results include only pages that have both [Tag X] and [Tag Y].
  - Bug Report:
    - Issue: Multi-Tag Filter Not Possible
    - Actual: After selecting knowledge, the tag panel is replaced by the results list and no control adds a second tag. Clicking the sidebar and search box did not expose any tag control. [Tag Y] could not be selected, so AND logic could not be tested.
- [X] CS-05: A search with no matching pages shows a no-results message and no page entries.
  - Action: Type "zzqxnomatch" into the search box and press Enter.
  - Expected: A no-results message is shown, and the results list contains no pages.

## Interaction

- [X] IX-01: Search results update as the user types, without pressing Enter.
  - Action: Click the search box and type "[first 3 letters of Topic B's title]" one character at a time, without pressing Enter.
  - Expected: Results narrow with each keystroke, and [Topic B] appears once at least 3 characters are entered.
- [X] IX-02: Clicking a topic's expand control shows or hides its subpages, and the control changes state.
  - Action: Click the expand control on [Topic A] to open it, then click it again.
  - Expected: First click shows [Subpage A1] and the control shows expanded state; second click hides [Subpage A1] and the control shows collapsed state.
- [ ] IX-03: Each active tag filter appears as a removable chip, and removing the chip removes the filter.
  - Action: In search, select [Tag X], then click the remove control on its chip.
  - Expected: A chip labeled [Tag X] appears after selection; after removal, the chip disappears and the results return to the unfiltered list.
  - Bug Report:
    - Issue: Missing Filter Chip
    - Actual: After selecting knowledge, the results header shows only "3 results" and "Clear filters". No element labeled "knowledge" exists in the DOM, so no removable chip appears.

## Content

- [ ] CT-01: The citation note shown beside each "Cites" and "Cited by" entry matches the stored note exactly, without truncation.
  - Action: On [Topic A], compare each citation entry's note with the note stored for that citation in the default data.
  - Expected: Every displayed note matches the stored text word for word.
  - Bug Report:
    - Issue: Unverifiable (Stored Note Not Exposed in DOM)
    - Actual: The notes on Epistemology match their mirrored entries on Scientific Method, Gettier Problems, and Rationalism vs Empiricism, and none is truncated. The stored default-data text is not exposed in the DOM, so an exact match to the stored text could not be verified.
- [X] CT-02: Opened pages show no placeholder or error text.
  - Action: Open [Topic A], [Subpage A1], and [Topic B] in turn and read the title, body, tags, and citation sections.
  - Expected: No text such as "undefined", "null", "Lorem ipsum", "TODO", or "[object Object]" appears on any of the pages.
