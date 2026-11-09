All 21 checklist items have now been executed. Here is the complete test report:

# Test Result

## Functionality

- [X] FT-01: User can add a contract with a name and full text
  - Action: Enter a contract name (e.g., "Vendor A") into the name field, paste a multi-clause contract text into the text input, and submit via the "Add Contract" button.
  - Expected: The contract is added to the workspace and its name is visible in the contract list / comparison view.
  - (Verified: "Vendor A" appeared in "Added Contracts (1)" list and as a column label in every clause group; stats updated to "1 Contracts / 3 Clauses Detected".)

- [X] FT-02: User can add multiple contracts for comparison
  - Action: Add at least 3 contracts, each with a distinct name and its own contract text.
  - Expected: All 3 contract names appear in the workspace, and all are included in the comparison display.
  - (Verified: "Vendor A", "Vendor B", "Acme MSA 2024" all listed under "Added Contracts (3)", each appearing as a labeled column in all clause groups.)

- [X] FT-03: Clauses are automatically detected and grouped by type
  - Action: Add contract texts containing clauses with distinct topics (e.g., a payment terms clause, a confidentiality clause, a termination clause).
  - Expected: Each clause is assigned to a matching clause-type group (e.g., "Payment Terms", "Confidentiality", "Termination"); no clause is left ungrouped or placed in a clearly wrong group.
  - (Verified: 9/9 clauses detected and correctly assigned — payment clauses → "Payment Terms", confidentiality clauses → "Confidentiality", termination clauses → "Termination"; 3 clauses per group, stats line "Detected types: payment, confidentiality, termination".)

- [X] FT-04: Same-type clauses from different contracts are shown side by side
  - Action: Add 2+ contracts that each contain a payment terms clause; open the "Payment Terms" clause group.
  - Expected: The payment terms clause from each contract is displayed in parallel columns, one column per contract, aligned by clause type.
  - (Verified: "Payment Terms" card renders 3 parallel columns — Vendor A | Vendor B | Acme MSA 2024 — each with its own payment clause beneath its name label.)

- [X] FT-05: Differences in wording between contracts are highlighted
  - Action: Add two contracts whose payment terms clauses differ in specific wording (e.g., "net 30 days" vs "net 60 days"); open that clause group in the comparison view.
  - Expected: The differing words/phrases are visually marked (e.g., background highlight) in each contract's clause text, and identical wording is not marked.
  - (Verified: "30" (Vendor A) and "60" (Vendor B) carry class `diff-highlight-different` with a visible background color; all identical surrounding words have no highlight class/background.)

- [ ] FT-06: Summarized comparison view is available
  - Action: Open a clause group with the view toggle set to the summarized comparison mode.
  - Expected: A condensed summary of each contract's clause is shown per contract column (shorter than the full clause text, conveying the key terms).
  - Bug Report:
    - Issue: Missing/non-functional summarized view — view toggle does not condense clause text
    - Actual: With the "Full text" switch OFF (summary position), each contract's clause column displays the complete, unabridged clause text, byte-identical to full-text mode (e.g., Vendor A's payment column shows the full sentence "Payment Terms: Client shall pay all invoices within net 30 days of receipt."). No text shorter than the full clause text exists anywhere in the DOM in either toggle state; toggling the switch produces zero content change.

- [X] FT-07: Full-text view is available for each clause group
  - Action: Open a clause group with the view toggle set to full-text mode.
  - Expected: The complete, unabridged clause text is displayed for every contract in that group.
  - (Verified with toggle ON: all clauses render verbatim, e.g., Acme MSA 2024's payment clause shown complete including its second sentence "Late payments incur a two percent monthly fee.")

- [ ] FT-08: View mode can be switched per clause group
  - Action: With multiple clause groups displayed, switch one group to "Full Text" while another remains on "Summary".
  - Expected: Only the targeted group changes its display mode; the other group stays in its previously selected mode.
  - Bug Report:
    - Issue: No per-clause-group view controls exist — view mode is global-only (and non-functional)
    - Actual: The only view-mode control is a single global "Full text" switch in the toolbar. No toggle exists on any clause-group card (a full inventory of buttons/switches found only the 2 global switches and per-contract remove buttons). The single switch affects all groups simultaneously and renders no content change, so one group cannot be "Full Text" while another remains "Summary".

- [X] FT-09: Filter view by clause type
  - Action: Apply a filter selecting only "Termination" (deselecting all other clause types).
  - Expected: Only the "Termination" clause group is displayed; all other clause groups are hidden from view.
  - (Verified: with only Termination selected, DOM contained exactly one group card ("Termination", 3 clauses); Payment Terms and Confidentiality cards and their clause texts were completely removed from the page.)

- [X] FT-10: Clearing the clause type filter restores all groups
  - Action: With a clause-type filter active, clear the filter (or re-select all clause types).
  - Expected: All clause-type groups present in the loaded contracts are visible again.
  - (Verified: clicking "Clear all" removed the filter and restored all groups — Payment Terms, Confidentiality, Termination all re-rendered with their full clause columns.)

## Constraint

- [X] CS-01: Contract cannot be added without a name
  - Action: Leave the contract name field empty, enter valid contract text, and attempt to submit.
  - Expected: The contract is NOT added, and the user is informed the name is required (inline message or disabled submit).
  - (Verified: with name empty + text filled, the "Add Contract" button is disabled (cannot submit); workspace unchanged — "No contracts to compare" state persists.)

- [X] CS-02: Contract cannot be added without text
  - Action: Enter a contract name but leave the text area empty, and attempt to submit.
  - Expected: The contract is NOT added, and the user is informed the contract text is required.
  - (Verified: with name "Vendor A" filled + text empty, the "Add Contract" button is disabled (cannot submit); no contract added.)

- [X] CS-03: Identical clause wording is not flagged as a difference
  - Action: Add two contracts containing a confidentiality clause with identical wording; open that clause group in comparison view.
  - Expected: No difference highlights are shown for that clause group (identical text has no highlighting).
  - (Verified: Vendor A and Vendor B confidentiality clauses are word-for-word identical and their columns contain zero `diff-highlight-different` elements and no highlight backgrounds — identical wording is not flagged.)

- [X] CS-04: Filtered-out clause types are fully excluded from the display
  - Action: Add contracts containing Payment Terms, Confidentiality, and Termination clauses; apply a filter for "Payment Terms" only; switch the visible group between Summary and Full Text modes.
  - Expected: Confidentiality and Termination content never appears anywhere in the filtered view, in either display mode.
  - (Verified in BOTH switch states: with filter = Payment Terms only, the page contained only payment clause text; confidentiality/termination clause texts and group cards were absent from the entire DOM in each mode.)

## Interaction

- [ ] IX-01: Switching between summary and full-text updates the display immediately
  - Action: With a clause group open in Summary mode, click the control to switch to Full Text, then back to Summary.
  - Expected: The clause group's content switches instantly between the summary and the full clause text on each click, without requiring a page reload.
  - Bug Report:
    - Issue: Unresponsive view toggle — clicking the control does not change any clause content
    - Actual: Toggling the "Full text" switch OFF→ON→OFF (3 times) left every clause paragraph byte-identical in both states (same texts, same word-span token counts, same highlight markup). The clause content never switches between a summary and the full text; only the switch's own visual state changes. (The adjacent "Highlight differences" switch does work, confirming switches render correctly — the full-text switch specifically has no effect.)

- [X] IX-02: Applying the clause-type filter updates the view immediately
  - Action: Select/deselect clause types in the filter control one at a time.
  - Expected: The displayed clause groups update immediately after each selection change to match the current filter selection.
  - (Verified: each individual chip click updated the view instantly with no reload — select "Payment Terms" → only payment group; select "Termination" → payment + termination groups; deselect "Payment Terms" → only termination group remained, exactly matching the selection each time.)

- [X] IX-03: Each contract is clearly labeled in the side-by-side view
  - Action: Open any clause group containing multiple contracts.
  - Expected: Each clause column is labeled with its contract's name, and the labels correctly match the clause content shown beneath them.
  - (Verified: every column header shows the contract name ("Vendor A" / "Vendor B" / "Acme MSA 2024") above its clause, and the content matches the named contract's input text — e.g., the "Vendor A" payment column contains the "net 30 days" clause from Vendor A's contract.)

## Content

- [X] CT-01: Clause type labels match the clause content
  - Action: Review each auto-detected clause group (e.g., "Payment Terms", "Confidentiality", "Termination") and read its member clauses.
  - Expected: Every clause placed in a group is genuinely about that group's topic (e.g., the "Payment Terms" group contains only clauses about payment amounts, schedules, or invoicing).
  - (Verified: all 12 detected clauses sit in topically correct groups — payment clauses (fees/invoicing) under "Payment Terms", non-disclosure clauses under "Confidentiality", termination-notice clauses under "Termination"; probe clauses landed correctly under "Liability", "Dispute Resolution", "Intellectual Property".)

- [X] CT-02: Summaries accurately reflect the full clause text
  - Action: For a clause group, compare the summarized view against the full-text view of the same clauses.
  - Expected: Each summary is consistent with its full clause text (no contradictions, no terms introduced that are absent from the full text, e.g., the correct payment period in both).
  - (Verified: comparing the toggle's summary position against full-text position, the rendered clause content is identical for every group — no contradictions, no terms absent from the full text, and the payment periods ("net 30" / "net 60" / "forty-five days") match in both modes. Note: because no distinct condensed summary is rendered — see FT-06 failure — consistency holds trivially.)

- [X] CT-03: Contract names are displayed exactly as entered
  - Action: Add a contract with a specific name (e.g., "Acme MSA 2024") and inspect all views where the contract appears (list, side-by-side columns, labels).
  - Expected: The name is displayed verbatim, identical everywhere it appears.
  - (Verified: "Acme MSA 2024" appears character-for-character identically in the Added Contracts list and in every clause-group column label; same for "Vendor A", "Vendor B", and "TechVentures SaaS Agreement".)

---

**Summary**: 18 of 21 checks passed. The app correctly adds named contracts, auto-detects and groups clauses by type, renders side-by-side per-contract columns with accurate labels, highlights genuine wording differences (without flagging identical text), and filters clause types instantly and completely. The single systemic defect is the **summary/full-text view toggle**: it is a global (not per-group) control and it has no effect on rendered content — no condensed summary view exists, so FT-06, FT-08, and IX-01 fail.