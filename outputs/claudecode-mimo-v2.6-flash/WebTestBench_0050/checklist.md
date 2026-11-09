# Test Checklist

## Functionality
- [ ] FT-01: Add a contract with text and a name, and confirm it is accepted and listed.
  - Action: Enter a contract name (e.g., "Vendor A") and paste contract text into the input area, then submit/add it.
  - Expected: The contract is added to the workspace and shown under the name "Vendor A".
- [ ] FT-02: Add several contracts and confirm each appears as a separate entry.
  - Action: Add at least three contracts with distinct names (e.g., "Vendor A", "Vendor B", "Vendor C") and distinct texts.
  - Expected: Three separate contracts are listed, each with its own name, ready for comparison.
- [ ] FT-03: Confirm clauses are auto-detected and grouped by type.
  - Action: View the comparison area after adding contracts that contain payment, confidentiality, and termination wording.
  - Expected: Clause groups are created for at least "Payment Terms", "Confidentiality", and "Termination", each containing the clauses detected from the contract texts without manual classification.
- [ ] FT-04: Confirm contracts are displayed side by side within each clause group.
  - Action: Open a clause group (e.g., Payment Terms) with three contracts added.
  - Expected: The clauses from all contracts are shown in adjacent columns/panels under that group, aligned so the same clause type can be compared horizontally.
- [ ] FT-05: Filter the view by a single clause type.
  - Action: Select "Confidentiality" in the clause-type filter control.
  - Expected: Only the Confidentiality group remains visible; all other clause groups are hidden.
- [ ] FT-06: Reset the filter to show all clause types.
  - Action: Clear the filter or select the "All" option after filtering.
  - Expected: All previously detected clause groups become visible again with their content unchanged.

## Constraint
- [ ] CS-01: Prevent analyzing a contract that has no name.
  - Action: Leave the contract-name field empty, enter contract text, and submit.
  - Expected: The contract is not added, and an error message requesting a contract name is displayed.
- [ ] CS-02: Prevent analyzing a contract that has no text.
  - Action: Enter a name only, leave the contract-text area empty, and submit.
  - Expected: The contract is not added, and an error message requesting contract text is displayed.
- [ ] CS-03: Prevent duplicate contract names from being silently created.
  - Action: Add a contract named "Vendor A", then attempt to add a second contract with the same name "Vendor A".
  - Expected: The system blocks the submission or clearly flags the name conflict; two indistinguishable entries named "Vendor A" are not created.
- [ ] CS-04: Keep clauses in only their detected type group.
  - Action: Inspect all clause groups after auto-detection.
  - Expected: The same clause text does not appear under more than one clause type, and no clause is left unassigned outside every group.

## Interaction
- [ ] IX-01: Highlight wording differences between contracts.
  - Action: In a clause group, compare contracts whose clause wording differs (e.g., "net 30" vs "net 60").
  - Expected: The differing words/phrases are visually highlighted with a distinct mark, while identical wording is not highlighted.
- [ ] IX-02: Show no difference markers for identical wording.
  - Action: View a clause group where two contracts contain the exact same clause text.
  - Expected: No difference highlighting is applied to the identical text.
- [ ] IX-03: Switch between summarized and full-text views for a clause group.
  - Action: Click the view toggle (e.g., "Summary" / "Full Text") for a specific clause group.
  - Expected: The group's content switches immediately to the selected view without reloading the page; full-text shows complete wording, summary shows a condensed version.
- [ ] IX-04: Preserve the active filter when switching views.
  - Action: Filter by "Termination", then toggle the view mode of that group.
  - Expected: The filter stays applied (only the Termination group visible) and the view mode changes for it.
- [ ] IX-05: Indicate which filter and view mode are currently active.
  - Action: Observe the filter control and view toggle after selecting "Payment Terms" and "Full Text".
  - Expected: Both controls visibly show their current selections (e.g., selected/highlighted state).

## Content
- [ ] CT-01: Display clause group headings with recognizable type labels.
  - Action: Review the comparison area after detection.
  - Expected: Each group has a clear heading naming its clause type (e.g., "Payment Terms", "Confidentiality", "Termination") relevant to contract-comparison purposes.
- [ ] CT-02: Show contract names as the column/panel headers.
  - Action: Inspect a side-by-side clause group.
  - Expected: Each contract's name is displayed at the top of its column so the source of each clause is unambiguous.
- [ ] CT-03: Keep full-text view verbatim to the source clause.
  - Action: Compare the full-text view of a clause against the text originally entered for that contract.
  - Expected: The displayed clause wording matches the input exactly, with no truncation, paraphrase, or missing sentences.
- [ ] CT-04: Keep summarized view faithful to key contract terms.
  - Action: Read a summarized clause that contains amounts and deadlines in the source (e.g., "payment due within 30 days of invoice").
  - Expected: The summary retains the key obligations (amounts, deadlines, parties) and contains no information absent from the source.