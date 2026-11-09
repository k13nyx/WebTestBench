# Test Checklist

## Functionality
- [ ] FT-01: User can add multiple contracts, each with a name and text.
  - Action: Enter a name and contract text into the input fields, click the add/submit button, repeat for a second contract.
  - Expected: Both contracts appear in the comparison area, each labeled with its entered name.
- [ ] FT-02: Clauses are auto-detected and grouped by clause type.
  - Action: View the clause groups generated for the default contracts present on the page.
  - Expected: Clauses are grouped under type headings such as "Payment Terms", "Confidentiality", "Termination", each clause placed under the type it belongs to.
- [ ] FT-03: Clauses of the same type are shown side by side across contracts.
  - Action: Open any clause group for the default contracts.
  - Expected: The corresponding clause text of each contract is displayed in adjacent columns/panels, one per contract, aligned within the group.
- [ ] FT-04: User can filter the view by clause type.
  - Action: Select "Payment Terms" in the clause-type filter control.
  - Expected: Only the "Payment Terms" clause group is displayed; all other clause groups are hidden.
- [ ] FT-05: Differences in wording between contracts are highlighted.
  - Action: Open a clause group whose wording differs across contracts.
  - Expected: The words/phrases that differ between the contracts' clause texts are visually highlighted.
- [ ] FT-06: User can switch a clause group to the summarized comparison view.
  - Action: Switch one clause group to the summarized comparison view via its view control.
  - Expected: The group displays a concise summary comparing the contracts' clauses instead of the full clause text.
- [ ] FT-07: User can switch a clause group to the full-text view.
  - Action: Switch the same clause group to the full-text view via its view control.
  - Expected: The group displays the complete clause text for each contract.

## Constraint
- [ ] CS-01: A contract cannot be added with an empty name or empty text.
  - Action: Click the add/submit button with the name field empty, then again with the text field empty.
  - Expected: The contract is not added in either case; a validation error message indicates the required field is missing.
- [ ] CS-02: Each clause is assigned to exactly one clause-type group.
  - Action: Inspect all clause groups rendered for the default contracts.
  - Expected: No clause text appears in more than one clause-type group.
- [ ] CS-03: Identical wording produces no difference highlighting.
  - Action: Open a clause group where two contracts contain identical wording.
  - Expected: No highlight is shown over the identical wording.
- [ ] CS-04: A clause type missing from one contract is not filled with other contracts' text.
  - Action: Open a clause group where one contract contains no clause of that type.
  - Expected: That contract's column shows an explicit "no clause found"/empty indicator; no text from another clause type or another contract appears there.

## Interaction
- [ ] IX-01: Adding a contract updates the comparison view immediately.
  - Action: Add a contract and observe the comparison area without reloading the page.
  - Expected: The comparison view updates immediately to include the new contract, with no full page reload or manual refresh required.
- [ ] IX-02: View toggle responds in place and indicates the active view.
  - Action: Click the Summarized / Full Text toggle on a clause group.
  - Expected: The group's content changes in place without a page reload, and the currently active view option is visually indicated on the control.
- [ ] IX-03: Clause-type filter responds immediately and indicates the selection.
  - Action: Select a clause type in the filter, then change or clear the selection.
  - Expected: The view updates immediately without a page reload, and the selected filter option shows a selected/active state.

## Content
- [ ] CT-01: Clause group headings correctly name the clause type.
  - Action: Read the headings of all clause groups for the default contracts.
  - Expected: Each heading displays a clause type name (e.g., "Payment Terms", "Confidentiality", "Termination") that matches the clauses shown under it.
- [ ] CT-02: Contract columns display the user-assigned contract names.
  - Action: Read the labels of each contract column/panel in a clause group.
  - Expected: Each column shows the name given to that contract, not a generic placeholder like "Contract 1" for a named contract.
- [ ] CT-03: Full-text view shows the clause wording exactly as in the source contract.
  - Action: Compare the full-text clause text displayed with the corresponding text in the original contract input.
  - Expected: Displayed text matches the source wording exactly — complete, unaltered, and not truncated.
- [ ] CT-04: Summarized view content is relevant to its clause group only.
  - Action: Read the summary shown for one clause group in summarized view.
  - Expected: The summary reflects only that group's clause wording across the contracts, with no text from unrelated clause types.