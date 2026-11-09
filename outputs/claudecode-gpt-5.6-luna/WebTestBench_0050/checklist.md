# Test Checklist

## Functionality

- [ ] FT-01: User can enter and save multiple contracts with simple names.
  - Action: Enter a name in the “Contract name” field and text in the “Contract text” field for at least two contracts, then use “Add contract” for each.
  - Expected: Each contract is added to the comparison setup with its entered name and text preserved.

- [ ] FT-02: User can start a comparison using the entered contracts.
  - Action: Add at least two named contracts and select “Compare contracts.”
  - Expected: A comparison view opens containing all submitted contracts.

- [ ] FT-03: Page automatically detects and groups clauses by type.
  - Action: Compare contracts containing payment, confidentiality, and termination clauses.
  - Expected: The page displays separate clause groups labeled with the detected types, including “Payment,” “Confidentiality,” and “Termination” when those clauses are present.

- [ ] FT-04: Clauses are displayed side by side across contracts.
  - Action: Open a detected clause group in the comparison view.
  - Expected: The corresponding clause content from each contract appears in parallel columns, with each column identified by the contract’s simple name.

- [ ] FT-05: User can filter the comparison by clause type.
  - Action: Select a single clause type from the clause-type filter.
  - Expected: Only the selected clause group or groups remain visible; unrelated clause groups are hidden.

- [ ] FT-06: User can highlight wording differences between contracts.
  - Action: In a clause group where contract wording differs, enable the differences-highlighting control.
  - Expected: The differing words or passages are visibly highlighted, while matching wording is not highlighted as a difference.

- [ ] FT-07: User can switch each clause group between summarized and full-text views.
  - Action: For a clause group, select the “Summary” view and then select the “Full text” view.
  - Expected: “Summary” shows a concise comparison of the group, and “Full text” shows the complete clause text for every included contract.

## Constraint

- [ ] CS-01: Required contract information must be present before a contract can be added.
  - Action: Leave the contract name or contract text empty and select “Add contract.”
  - Expected: The contract is not added, and the empty required field is clearly identified for correction.

- [ ] CS-02: Comparison requires multiple contracts.
  - Action: Add only one contract and attempt to select “Compare contracts.”
  - Expected: Comparison does not start, and the page indicates that another contract is required.

- [ ] CS-03: Every detected clause is assigned to one visible clause group without duplicated display.
  - Action: Review all clause groups after comparing contracts containing multiple clause types.
  - Expected: Each clause appears in the appropriate type group once and is not repeated in multiple groups unless the page explicitly identifies it as belonging to multiple types.

## Interaction

- [ ] IX-01: Adding a contract updates the comparison setup immediately.
  - Action: Add a named contract with text.
  - Expected: The new contract appears in the contract list or comparison setup without removing or changing previously added contracts.

- [ ] IX-02: Selecting a clause type updates the view without losing comparison data.
  - Action: Apply a clause-type filter, then clear the filter.
  - Expected: The filtered view shows only the selected type, and clearing the filter restores all available clause groups and contract columns.

- [ ] IX-03: Difference highlighting can be turned off without changing clause text.
  - Action: Enable differences highlighting, record the displayed clause wording, then disable highlighting.
  - Expected: Highlight markers disappear while all clause wording and contract alignment remain unchanged.

- [ ] IX-04: Switching between summary and full-text views preserves the selected clause group and contracts.
  - Action: Switch a selected clause group from “Summary” to “Full text” and back.
  - Expected: The same clause group and contract columns remain selected, and only the presentation detail changes.

## Content

- [ ] CT-01: Contract names are displayed consistently wherever contracts appear.
  - Action: Compare contracts using distinct simple names such as “Contract A” and “Contract B.”
  - Expected: Those names appear consistently in the comparison headers, clause groups, summaries, and full-text columns.

- [ ] CT-02: Displayed clause content matches the source contract text.
  - Action: Compare contracts and inspect each detected clause in “Full text” view.
  - Expected: Each clause’s displayed wording matches its source contract, with no omitted, substituted, or cross-assigned text.