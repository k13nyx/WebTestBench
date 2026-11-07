# Test Checklist

**Preconditions:** Tests run on the default data already loaded in the app (at least two named contracts with overlapping clause types). Feature-level input tests (FT-01, IX-03) use the app's own "Add contract" control; if it offers a sample/demo text option, use that, otherwise paste a short contract excerpt containing a payment clause and a confidentiality clause. Desktop viewport only.

## Functionality
- [ ] FT-01: User can add a new named contract to the comparison
  - Action: Open the "Add Contract" (or "+") control, enter name "Contract C" and a contract text containing a payment clause and a confidentiality clause, then submit.
  - Expected: A new column headed "Contract C" appears alongside the existing contract columns and its clauses participate in the grouped comparison.
- [ ] FT-02: Contracts are displayed side by side within each clause group
  - Action: With the default contracts loaded, open any clause group row.
  - Expected: Each contract occupies its own vertical column; the clauses for that group appear horizontally aligned in the same row across columns.
- [ ] FT-03: Clause types are auto-detected and grouped
  - Action: Load the default contracts and let the page complete its auto-detection (click "Analyze"/"Compare" if such a control exists).
  - Expected: Clause groups are listed with type labels, including at least "Payment Terms", "Confidentiality", and "Termination"; each listed group contains at least one clause from the contracts.
- [ ] FT-04: Clauses are grouped under the correct clause type
  - Action: Open the "Payment Terms" group and read the clause text shown for each contract.
  - Expected: Every clause listed under "Payment Terms" concerns payment, fees, or invoicing; no termination or confidentiality text appears there.
- [ ] FT-05: View can be filtered by clause type
  - Action: In the clause-type filter control, select only "Confidentiality", then clear the filter.
  - Expected: With the filter applied, only the Confidentiality group is displayed (Payment Terms and Termination hidden) and the filter control shows "Confidentiality" as active; after clearing, all clause groups return.
- [ ] FT-06: Full-text view shows the complete clause for a group
  - Action: For the "Termination" group, activate its full-text view control (e.g., "Full text" toggle or expand).
  - Expected: The complete, untruncated termination clause text for each contract is displayed in that group.
- [ ] FT-07: Summarized view can be restored for a group
  - Action: With the "Termination" group in full-text view, activate its summary view control.
  - Expected: The group returns to condensed summary text for each contract, the full text is no longer shown, and the view mode of the other groups is unchanged.

## Constraint
- [ ] CS-01: A contract cannot be added with an empty name or empty text
  - Action: Open "Add Contract", submit once with the name blank (text filled), then submit once with the text blank (name filled).
  - Expected: Both submissions are blocked, an explicit error message is shown (e.g., "Name is required" / "Contract text is required"), and no new empty or unnamed column is added.
- [ ] CS-02: A clause missing from one contract is marked, not silently dropped
  - Action: Find a clause type that at least one default contract does not contain, then open that group.
  - Expected: The contract lacking the clause shows an explicit "Not found" / "No matching clause" marker in its cell; the group remains listed and the other contracts' clauses still display.
- [ ] CS-03: Identical wording is never highlighted as a difference
  - Action: In a group where two contracts' clauses differ, read both texts and inspect the highlighted spans.
  - Expected: Only the words or phrases that actually differ are marked; wording shared by both contracts is left unmarked.
- [ ] CS-04: Filtering to a clause type with no matching clauses shows an empty state
  - Action: In the filter control, select a clause type that none of the loaded contracts contain (or deselect every type).
  - Expected: The comparison area shows an explicit empty-state message (e.g., "No clauses match this filter"); no broken, blank table rows or error output appear.

## Interaction
- [ ] IX-01: Differences in wording are visually highlighted inline
  - Action: Open a clause group where two contracts' wording differs and look at the compared text without hovering.
  - Expected: The differing words/phrases are visually marked inline (distinct background color, underline, or bold) in the compared text.
- [ ] IX-02: View-mode switch is immediate and applies per clause group
  - Action: Click the full-text control on the "Payment Terms" group only.
  - Expected: Payment Terms switches to full text immediately with no page reload; Confidentiality and Termination groups keep their previous view mode.
- [ ] IX-03: Adding a contract updates the existing comparison without losing data
  - Action: With the default contracts compared and a clause-type filter applied, add one more named contract with text.
  - Expected: A new column is appended; all existing columns, contract names, clause groups, and the active filter remain intact; the new contract's clauses appear in the matching groups.
- [ ] IX-04: Difference highlighting is preserved across both view modes
  - Action: Toggle one clause group between summary view and full-text view and inspect the highlighting in each mode.
  - Expected: The differing spans remain highlighted in both the summarized and full-text rendering of that group.

## Content
- [ ] CT-01: Clause type labels are contract-relevant categories
  - Action: Read every clause group label produced for the default contracts.
  - Expected: Labels are contract clause categories (e.g., Payment Terms, Confidentiality, Termination, Liability, Governing Law); the three named types appear when present in the source text; no off-topic or placeholder labels ("Category 1", "Untitled", "lorem").
- [ ] CT-02: Each column shows text belonging to its own contract
  - Action: In the "Confidentiality" group, compare the text shown under each contract column against that contract's own source text.
  - Expected: Each column's clause text appears verbatim in that contract's source text and none of it is duplicated or swapped into another contract's column.
- [ ] CT-03: Summary text is consistent with the full clause text
  - Action: For one clause group, read a contract's summary, switch that group to full text, and read the same contract's full clause.
  - Expected: The summary conveys the same key facts (obligations, time periods, amounts) as the full clause and contradicts none of them.
- [ ] CT-04: No raw placeholder or garbled text in the interface
  - Action: Scan the filter control, group headers, column headers, all clause cells, and empty areas across all groups and both view modes.
  - Expected: No "undefined", "null", "NaN", "[object Object]", "Lorem ipsum", or unformatted placeholder text appears anywhere.