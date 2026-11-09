# Test Checklist

## Functionality
- [ ] FT-01: User can add a contract by entering its text and a simple name
  - Action: Enter contract text into the contract input field, enter a name (e.g., "Contract A") into the name field, and click the "Add Contract" button
  - Expected: "Contract A" appears in the list of loaded contracts, with its text stored and displayed when selected

- [ ] FT-02: User can add multiple contracts for comparison
  - Action: Repeat FT-01 for a second contract (e.g., "Contract B") and a third (e.g., "Contract C")
  - Expected: All contracts ("Contract A", "Contract B", "Contract C") are listed and simultaneously available for comparison

- [ ] FT-03: Clauses are auto-detected and grouped by type
  - Action: Load contracts containing payment terms, confidentiality, and termination clauses, then view the comparison area
  - Expected: Clause groups are displayed for each detected type (e.g., "Payment Terms", "Confidentiality", "Termination"), each containing the corresponding clause text from the contracts

- [ ] FT-04: Clauses are shown side by side across contracts
  - Action: Open a clause group (e.g., "Payment Terms")
  - Expected: The clause text from each contract is displayed side by side, in columns or panels labeled with each contract's name

- [ ] FT-05: User can filter the view by clause type
  - Action: Select a clause type filter (e.g., "Confidentiality") from the filter control
  - Expected: Only the "Confidentiality" group is shown; other clause types (e.g., "Payment Terms", "Termination") are hidden

- [ ] FT-06: Filtering by "All" restores the full view
  - Action: Select the "All" (or equivalent) option in the clause type filter
  - Expected: All clause type groups are displayed again

- [ ] FT-07: User can switch between summarized comparison view and full-text view
  - Action: Toggle from the summarized view to the full-text view for a clause group (e.g., "Termination")
  - Expected: The view switches to show the complete clause text from each contract; toggling back shows the summarized view again

- [ ] FT-08: Summarized view shows a condensed comparison of each clause group
  - Action: View the summarized comparison for a clause group (e.g., "Payment Terms")
  - Expected: A condensed summary of each contract's clause is shown (clearly shorter than the full text), aligned side by side per contract

- [ ] FT-09: Differences in wording between contracts are highlighted
  - Action: View a clause group where two contracts use different wording (e.g., different payment percentages or notice periods)
  - Expected: The differing words/phrases are visually highlighted (e.g., different background or text color) so the differences are immediately identifiable

- [ ] FT-10: Identical wording is not highlighted as a difference
  - Action: View a clause group where two contracts use identical wording
  - Expected: No difference highlighting appears on the shared, identical text

- [ ] FT-11: User can remove a contract
  - Action: Click the remove/delete control next to a contract (e.g., "Contract B")
  - Expected: "Contract B" is removed from the contract list and its column disappears from the comparison view; remaining contracts continue to compare correctly

## Constraint
- [ ] CS-01: Contract cannot be added with an empty name
  - Action: Enter contract text but leave the name field empty, then click "Add Contract"
  - Expected: The contract is not added; an error message (e.g., "Please enter a contract name") is shown

- [ ] CS-02: Contract cannot be added with empty text
  - Action: Enter a name but leave the contract text field empty, then click "Add Contract"
  - Expected: The contract is not added; an error message (e.g., "Please enter contract text") is shown

- [ ] CS-03: Duplicate contract names are not allowed
  - Action: Add a contract named "Contract A", then attempt to add another contract with the same name "Contract A"
  - Expected: The duplicate is rejected with an error message (e.g., "A contract with this name already exists")

- [ ] CS-04: Comparison view is not shown until at least two contracts exist
  - Action: Load only one contract and observe the comparison area
  - Expected: No clause comparison/grouping is shown; a message (e.g., "Add at least two contracts to compare") is displayed instead

- [ ] CS-05: Non-contract text does not produce clause groups
  - Action: Add a contract whose text contains no recognizable clauses (e.g., "Hello world")
  - Expected: No clause group is created for it; the group area shows an empty/no-clauses state instead of miscategorized content

## Interaction
- [ ] IX-01: Switching view mode updates immediately without page reload
  - Action: Click the summarized/full-text toggle
  - Expected: The view updates instantly in place, with no full page reload or loss of selected filter state

- [ ] IX-02: Clause group can be expanded/collapsed
  - Action: Click on a clause group header (e.g., "Confidentiality")
  - Expected: The group expands to show the side-by-side clauses; clicking again collapses it

- [ ] IX-03: Selecting a contract highlights or focuses its column
  - Action: Click on a contract name in the contract list
  - Expected: The selected contract's clause column is visually emphasized or scrolled into view in the comparison area

- [ ] IX-04: Visual feedback during clause analysis
  - Action: Click the "Add Contract" / "Analyze" button and observe the interface
  - Expected: A loading indicator or progress state (e.g., spinner, "Analyzing...") is shown while clause detection runs, and the result appears once complete

## Content
- [ ] CT-01: Contract names are displayed correctly in the comparison view
  - Action: Add "Contract A" and "Contract B", then view any clause group
  - Expected: The column/panel headers show exactly "Contract A" and "Contract B" matching the names entered

- [ ] CT-02: Displayed clause text matches the entered contract text
  - Action: Add a contract with a distinctive clause (e.g., "The payment shall be made within 30 days of invoice") and view its clause group
  - Expected: The displayed clause text matches the entered wording exactly (no truncation or alteration in full-text view)

- [ ] CT-03: Clause type labels are relevant and correctly named
  - Action: View the clause group headers for contracts containing payment, confidentiality, and termination clauses
  - Expected: Headers use relevant type labels (e.g., "Payment Terms", "Confidentiality", "Termination") that match the clause content under them — not mislabeled (e.g., a payment clause not shown under "Termination")

- [ ] CT-04: Default data is present for testing on first load
  - Action: Open the page without adding anything
  - Expected: The page loads with usable default data or ready input controls (e.g., pre-loaded sample contracts or empty input fields with clear placeholders), and no error states are shown