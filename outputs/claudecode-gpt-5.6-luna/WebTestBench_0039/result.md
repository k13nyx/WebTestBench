# Test Result

## Functionality

- [ ] FT-01: User can create and save a profile containing income sources, expense categories with budget amounts, and savings goals.
  - Action: Open the profile setup page, enter valid values in each section, and select **Save Profile**.
  - Expected: The profile saves successfully and all entered income sources, expense categories, budget amounts, and savings goals are displayed.
  - Bug Report:
    - Issue: Missing Save Profile control
    - Actual: The Profile Settings dialog has separate tabs and individual add controls, but no **Save Profile** button. Income data added through the form is displayed after reopening, but the specified profile-save workflow cannot be completed.

- [X] FT-02: User can add an individual transaction and assign it to an existing expense category.
  - Action: Open **Transactions**, select **Add Transaction**, enter a valid amount, date, description, and existing category, then save.
  - Expected: The transaction appears in transaction history with the entered details and assigned category.

- [X] FT-03: The monthly summary compares actual spending with the budget for every expense category.
  - Action: Open **Monthly Summary** for a month containing default transactions and budgets.
  - Expected: Each expense category displays both its budget amount and its actual spending amount for the selected month.

- [X] FT-04: User can filter transaction history by a date range.
  - Action: In transaction history, enter a start date and end date, then apply the date filter.
  - Expected: Only transactions whose dates fall within the selected range are displayed.

- [X] FT-05: User can filter transaction history by expense category.
  - Action: Select an existing expense category in the transaction history category filter.
  - Expected: Only transactions assigned to the selected category are displayed.

- [X] FT-06: User can combine date-range and category filters.
  - Action: Apply both a date range and an expense category filter.
  - Expected: The transaction list contains only records matching both selected criteria.

## Constraint

- [X] CS-01: Required profile information cannot be saved when required fields are empty.
  - Action: Leave a required income source, expense category, budget amount, or savings goal field empty and select **Save Profile**.
  - Expected: The profile is not saved and the incomplete field is identified with a validation message or required-field indicator.

- [X] CS-02: A transaction cannot be saved without a valid amount, date, and category.
  - Action: In **Add Transaction**, leave one required field empty or enter an invalid amount, then select **Save**.
  - Expected: The transaction is not saved and the invalid or missing field is identified.

- [X] CS-03: A transaction cannot be assigned to a category that does not exist in the profile.
  - Action: Open the transaction category selector and attempt to assign a category not present in the saved expense-category list.
  - Expected: The unavailable category cannot be selected or the transaction is rejected with a clear validation message.

- [ ] CS-04: The monthly summary identifies categories whose actual spending exceeds their budget.
  - Action: Open a month containing a default category where actual spending is greater than its budget.
  - Expected: That category is marked as overspending, and categories at or below budget are not marked as overspending.
  - Bug Report:
    - Issue: No default overspending category is available
    - Actual: The available November summary showed Food & Dining at $42.50 of a $600 budget and all other categories at $0. The default December transactions also do not produce an over-budget category, so the required overspending state could not be verified.

## Interaction

- [ ] IX-01: Saving a valid profile provides a clear completion response.
  - Action: Save a profile containing valid income, expense, and savings information.
  - Expected: A visible success response appears and the saved profile data remains available after leaving and returning to the profile page.
  - Bug Report:
    - Issue: Missing profile-save completion response
    - Actual: No visible success response or confirmation appeared because there is no **Save Profile** control. Added profile data did remain visible after reopening Profile Settings.

- [X] IX-02: Applying transaction filters refreshes the displayed results without showing nonmatching records.
  - Action: Apply a date-range or category filter, then change or clear the filter.
  - Expected: The transaction list updates immediately to match the current filter state, and clearing filters restores the unfiltered transaction list.

- [ ] IX-03: Overspending categories receive a distinct visual highlight in the monthly summary.
  - Action: View a monthly summary containing at least one category over budget.
  - Expected: The over-budget category is visually distinguishable from categories that are within budget.
  - Bug Report:
    - Issue: Overspending visual state unavailable
    - Actual: The tested summary contained no category over budget, so no distinct overspending highlight was displayed or verifiable.

- [ ] IX-04: Changing the selected month updates the monthly summary.
  - Action: Select a different month in the monthly summary month control.
  - Expected: The displayed budgets, actual spending values, and overspending indicators correspond to the newly selected month.
  - Bug Report:
    - Issue: Missing month-selection control
    - Actual: The Budget Overview page displayed “November 2026” but contained no month selector or other month control to change the selected month.

## Content

- [X] CT-01: Profile content clearly distinguishes income sources, expense categories, budget amounts, and savings goals.
  - Action: Review the saved profile page.
  - Expected: Each displayed value appears under the correct section or label, with no income, expense, budget, or savings-goal data shown in the wrong section.

- [X] CT-02: Transaction history displays complete and accurate transaction details.
  - Action: Review a saved default transaction and a transaction created through the transaction form.
  - Expected: Each record shows the correct amount, date, description, and assigned expense category.

- [X] CT-03: Monthly summary labels and values accurately represent spending performance.
  - Action: Compare category totals in the monthly summary with the corresponding transaction records and budget amounts.
  - Expected: Actual spending totals, budget values, and overspending status are consistent with the displayed transaction data.