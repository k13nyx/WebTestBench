# Test Checklist

## Functionality
- [ ] FT-01: User can input multiple contract texts
  - Action: Click "Add Contract" to create additional inputs, then paste different contract text into each contract text area.
  - Expected: Multiple contract text areas are available and each accepts and retains its pasted text.

- [ ] FT-02: User can give each contract a simple name
  - Action: Type a distinct name (e.g., "Vendor A") into each contract's name field.
  - Expected: Each name is captured and associated with its corresponding contract.

- [ ] FT-03: System auto-detects and groups clauses by type
  - Action: Provide contracts containing payment, confidentiality, and termination clauses, then trigger "Compare" / "Group Clauses".
  - Expected: Clauses are organized under separate groups by detected type (Payment Terms, Confidentiality, Termination).

- [ ] FT-04: Clause groups are shown side by side across contracts
  - Action: Open any clause group after processing.
  - Expected: Each contract's clause text appears in an adjacent column within the group.

- [ ] FT-05: User can filter the view by clause type
  - Action: Select a clause type (e.g., "Confidentiality") from the clause-type filter.
  - Expected: Only the selected clause group is displayed; all others are hidden.

- [ ] FT-06: Differences in wording between contracts are highlighted
  - Action: View a clause group containing differing text across contracts.
  - Expected: The differing wording between contracts is visually marked within the clause text.

- [ ] FT-07: User can switch between summarized and full-text view per clause group
  - Action: Click "Summary View" then "Full Text View" for a clause group.
  - Expected: The group toggles between a condensed summary and the complete clause text.

## Constraint
- [ ] CS-01: Empty contract text cannot be processed
  - Action: Leave one contract text area empty and click "Compare" / "Group Clauses".
  - Expected: Processing is blocked and a message indicates the contract text is required.

- [ ] CS-02: A name is required for each contract
  - Action: Leave a contract name field blank and attempt to process.
  - Expected: Processing is blocked and a message indicates the name is required.

- [ ] CS-03: Duplicate contract names are prevented
  - Action: Assign the same name to two different contracts and attempt to process.
  - Expected: System blocks submission or warns that contract names must be unique.

## Interaction
- [ ] IX-01: View toggle preserves data
  - Action: Switch a clause group to "Full Text View", then back to "Summary View".
  - Expected: The displayed content updates without losing any clause data or re-processing.

- [ ] IX-02: Filter updates the view immediately
  - Action: Change the clause-type filter selection.
  - Expected: The visible clause groups update instantly to reflect the selected type.

- [ ] IX-03: Grouping produces a visible result indicator
  - Action: Successfully run "Compare" / "Group Clauses" with valid input.
  - Expected: A results indicator appears (e.g., "3 clause groups found") confirming completion.

## Content
- [ ] CT-01: Clause group labels match detected types
  - Action: Review the headings of each clause group after processing.
  - Expected: Group labels accurately reflect detected clause types (e.g., Payment Terms, Confidentiality, Termination) and relate to the contracts' content.

- [ ] CT-02: Contract names appear correctly in the side-by-side view
  - Action: Open a clause group and inspect the column headers.
  - Expected: Each column header displays the exact name entered for that contract.

- [ ] CT-03: Page provides relevant instructional content
  - Action: Inspect the page before adding any contracts.
  - Expected: Placeholder/instruction text (e.g., "Paste contract text here" and "Name this contract") clearly explains how to use the page and aligns with the contract-comparison purpose.