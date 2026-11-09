All tests are complete. Here is the full checklist with results:

# Test Result

## Functionality
- [X] FT-01: User can add a contract by entering its text and a simple name
  - Action: Enter contract text into the contract input field, enter a name (e.g., "Contract A") into the name field, and click the "Add Contract" button
  - Expected: "Contract A" appears in the list of loaded contracts, with its text stored and displayed when selected
- [X] FT-02: User can add multiple contracts for comparison
  - Action: Repeat FT-01 for a second contract (e.g., "Contract B") and a third (e.g., "Contract C")
  - Expected: All contracts ("Contract A", "Contract B", "Contract C") are listed and simultaneously available for comparison
- [X] FT-03: Clauses are auto-detected and grouped by type
  - Action: Load contracts containing payment terms, confidentiality, and termination clauses, then view the comparison area
  - Expected: Clause groups are displayed for each detected type (e.g., "Payment Terms", "Confidentiality", "Termination"), each containing the corresponding clause text from the contracts
- [X] FT-04: Clauses are shown side by side across contracts
  - Action: Open a clause group (e.g., "Payment Terms")
  - Expected: The clause text from each contract is displayed side by side, in columns or panels labeled with each contract's name
- [X] FT-05: User can filter the view by clause type
  - Action: Select a clause type filter (e.g., "Confidentiality") from the filter control
  - Expected: Only the "Confidentiality" group is shown; other clause types (e.g., "Payment Terms", "Termination") are hidden
- [X] FT-06: Filtering by "All" restores the full view
  - Action: Select the "All" (or equivalent) option in the clause type filter
  - Expected: All clause type groups are displayed again
- [ ] FT-07: User can switch between summarized comparison view and full-text view
  - Action: Toggle from the summarized view to the full-text view for a clause group (e.g., "Termination")
  - Expected: The view switches to show the complete clause text from each contract; toggling back shows the summarized view again
  - Bug Report:
    - Issue: Non-functional View Toggle — no distinct summarized view exists
    - Actual: The "Full text" switch toggles its state instantly, but the displayed clause content is byte-for-byte identical in both modes (main area innerText length identical, e.g., 1811 chars in both). Even a 2833-character clause renders fully expanded in "summarized" mode (p.clientHeight == p.scrollHeight == 1706px, max-height: none). In summarized mode a per-card "Show full text" button appears, but clicking it only swaps the button label to "Show less" with no visible change to the text, so the user can never see a condensed/summarized representation.
- [ ] FT-08: Summarized view shows a condensed comparison of each clause group
  - Action: View the summarized comparison for a clause group (e.g., "Payment Terms")
  - Expected: A condensed summary of each contract's clause is shown (clearly shorter than the full text), aligned side by side per contract
  - Bug Report:
    - Issue: Missing Condensed Summary — full text shown in "summarized" mode
    - Actual: No condensed/summarized text is generated. In summarized mode the complete clause text is rendered for every contract (verified with a 612-char and a 2833-char clause: DOM text length identical in both modes, no truncation, no max-height/line-clamp CSS applied). The only difference is an inert "Show full text"/"Show less" button whose toggling produces no visual change.
- [X] FT-09: Differences in wording between contracts are highlighted
  - Action: View a clause group where two contracts use different wording (e.g., different payment percentages or notice periods)
  - Expected: The differing words/phrases are visually highlighted (e.g., different background or text color) so the differences are immediately identifiable
- [X] FT-10: Identical wording is not highlighted as a difference
  - Action: View a clause group where two contracts use identical wording
  - Expected: No difference highlighting appears on the shared, identical text
- [X] FT-11: User can remove a contract
  - Action: Click the remove/delete control next to a contract (e.g., "Contract B")
  - Expected: "Contract B" is removed from the contract list and its column disappears from the comparison view; remaining contracts continue to compare correctly

## Constraint
- [ ] CS-01: Contract cannot be added with an empty name
  - Action: Enter contract text but leave the name field empty, then click "Add Contract"
  - Expected: The contract is not added; an error message (e.g., "Please enter a contract name") is shown
  - Bug Report:
    - Issue: Missing Validation Feedback (no error message)
    - Actual: The contract is correctly not added, but only because the "Add Contract" button stays disabled (opacity 0.5) when the name field is empty. No error message (e.g., "Please enter a contract name") is displayed anywhere; pressing Enter also produces no validation message.
- [ ] CS-02: Contract cannot be added with empty text
  - Action: Enter a name but leave the contract text field empty, then click "Add Contract"
  - Expected: The contract is not added; an error message (e.g., "Please enter contract text") is shown
  - Bug Report:
    - Issue: Missing Validation Feedback (no error message)
    - Actual: The contract is correctly not added (button remains disabled with empty text), but no error message such as "Please enter contract text" is shown; the empty state simply persists silently.
- [ ] CS-03: Duplicate contract names are not allowed
  - Action: Add a contract named "Contract A", then attempt to add another contract with the same name "Contract A"
  - Expected: The duplicate is rejected with an error message (e.g., "A contract with this name already exists")
  - Bug Report:
    - Issue: Incorrect Form Submission — duplicate name accepted
    - Actual: Adding a second contract named "Contract A" succeeded with no error: the list showed "Added Contracts (2)" containing two entries both named "Contract A". No duplicate-name rejection or error message appeared.
- [ ] CS-04: Comparison view is not shown until at least two contracts exist
  - Action: Load only one contract and observe the comparison area
  - Expected: No clause comparison/grouping is shown; a message (e.g., "Add at least two contracts to compare") is displayed instead
  - Bug Report:
    - Issue: Premature Comparison Display
    - Actual: After adding only one contract ("Contract A"), the full clause-group comparison view (Payment Terms / Confidentiality / Termination groups with the contract's clause text) was already displayed; no "Add at least two contracts to compare" message was shown.
- [X] CS-05: Non-contract text does not produce clause groups
  - Action: Add a contract whose text contains no recognizable clauses (e.g., "Hello world")
  - Expected: No clause group is created for it; the group area shows an empty/no-clauses state instead of miscategorized content

## Interaction
- [X] IX-01: Switching view mode updates immediately without page reload
  - Action: Click the summarized/full-text toggle
  - Expected: The view updates instantly in place, with no full page reload or loss of selected filter state
- [ ] IX-02: Clause group can be expanded/collapsed
  - Action: Click on a clause group header (e.g., "Confidentiality")
  - Expected: The group expands to show the side-by-side clauses; clicking again collapses it
  - Bug Report:
    - Issue: Unresponsive Element — group headers are not interactive
    - Actual: The group headers ("Confidentiality" / "N clauses") are plain divs with `cursor: auto` (no button role, no chevron, no click affordance). Clicking the header twice produced no collapse or expansion — the group's clause cards remained visible after both clicks. No expand/collapse control exists anywhere for clause groups.
- [ ] IX-03: Selecting a contract highlights or focuses its column
  - Action: Click on a contract name in the contract list
  - Expected: The selected contract's clause column is visually emphasized or scrolled into view in the comparison area
  - Bug Report:
    - Issue: Unresponsive Element — contract selection has no effect
    - Actual: Clicking "Contract B" in the "Added Contracts" list produced no change: the list item has `cursor: auto`, no column classes/styles changed after the click, no emphasis (ring/border/active) styles appeared, and no scrolling into view occurred. The contract names in the list are not clickable.
- [ ] IX-04: Visual feedback during clause analysis
  - Action: Click the "Add Contract" / "Analyze" button and observe the interface
  - Expected: A loading indicator or progress state (e.g., spinner, "Analyzing...") is shown while clause detection runs, and the result appears once complete
  - Bug Report:
    - Issue: Missing Loading Indicator
    - Actual: On click, the form fields are cleared instantly and the button merely returns to the same disabled/dimmed state (opacity 0.5) it already has for an empty form — indistinguishable from idle. No spinner, no "Analyzing..." text, no aria-busy attribute, and no animate-spin/animate-pulse elements were detected at any sample point during processing. The result simply appears without any progress feedback.

## Content
- [X] CT-01: Contract names are displayed correctly in the comparison view
  - Action: Add "Contract A" and "Contract B", then view any clause group
  - Expected: The column/panel headers show exactly "Contract A" and "Contract B" matching the names entered
- [X] CT-02: Displayed clause text matches the entered contract text
  - Action: Add a contract with a distinctive clause (e.g., "The payment shall be made within 30 days of invoice") and view its clause group
  - Expected: The displayed clause text matches the entered wording exactly (no truncation or alteration in full-text view)
- [X] CT-03: Clause type labels are relevant and correctly named
  - Action: View the clause group headers for contracts containing payment, confidentiality, and termination clauses
  - Expected: Headers use relevant type labels (e.g., "Payment Terms", "Confidentiality", "Termination") that match the clause content under them — not mislabeled (e.g., a payment clause not shown under "Termination")
- [X] CT-04: Default data is present for testing on first load
  - Action: Open the page without adding anything
  - Expected: The page loads with usable default data or ready input controls (e.g., pre-loaded sample contracts or empty input fields with clear placeholders), and no error states are shown

**Summary:** 13 of 21 tests passed. Core clause detection, grouping, side-by-side comparison, word-level difference highlighting (amber background/orange text on differing values like "30"/"45" and "5%"/"10%"), filtering, and contract removal all work correctly. The main defects are: the summarized/full-text views are visually identical (no condensed summary is ever produced), no expand/collapse on group headers, no contract-selection feedback, no loading indicator during analysis, silent validation (no error messages for empty/duplicate inputs), duplicates accepted, and the comparison view appearing with only one contract.