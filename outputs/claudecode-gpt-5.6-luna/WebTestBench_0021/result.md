# Test Result

## Functionality

- [X] **FT-01: View existing customer records and detailed profiles**
  - **Action:** Open the CRM admin page and select an existing customer.
  - **Expected:** A customer list and a detailed profile view are available, including the customer’s niche-specific information.

- [X] **FT-02: Create a customer record**
  - **Action:** Select **“Add Customer”**, enter valid customer details, and select **“Save”**.
  - **Expected:** The new customer record is saved and appears in the customer list.

- [ ] **FT-03: Update an existing customer**
  - **Action:** Open an existing customer, modify a customer detail, and select **“Save”**.
  - **Expected:** The updated value appears in the profile and remains after reopening the customer record.
  - **Bug Report:**
    - **Issue:** Updated customer detail does not persist after reopening.
    - **Actual:** After changing the customer Notes field to “Updated QA note for private viewing.” and saving, reopening the profile showed the original note, “Prefers private viewings. Interested in large-scale installations.”

- [X] **FT-04: Attach a related item to a customer**
  - **Action:** Open a customer, choose **“Add Related Item”**, select an existing artwork or other relevant default item, and save.
  - **Expected:** The selected item appears in that customer’s related-items section.

- [X] **FT-05: Apply and update workflow statuses**
  - **Action:** Open a customer workflow, choose an available custom status, save it, then change the status to another available status.
  - **Expected:** The selected status is displayed for the customer and the updated status replaces the previous one.

- [X] **FT-06: Filter customers by attributes**
  - **Action:** Open **“Filters”**, select an available customer attribute such as interest or purchase history, and apply the filter.
  - **Expected:** The customer list shows only records matching the selected attribute.

- [ ] **FT-07: Segment customers by behavior**
  - **Action:** Create or select a customer segment using a behavior criterion such as invitations or purchases.
  - **Expected:** The segment displays the customers who match the selected behavior criterion.
  - **Bug Report:**
    - **Issue:** Customer segmentation feature is unavailable.
    - **Actual:** The Customers page provides search and status filtering, but no control to create or select a behavior-based customer segment.

- [ ] **FT-08: Configure a summary report**
  - **Action:** Open **“Reports”**, select available engagement and revenue measures, choose a grouping or filter, and apply the configuration.
  - **Expected:** The report updates to use the selected measures and grouping.
  - **Bug Report:**
    - **Issue:** Configurable report controls are missing.
    - **Actual:** The Reports page displays Revenue, Engagement, and Sales Funnel tabs, but provides no controls for selecting measures, groupings, or filters.

- [X] **FT-09: Review engagement and revenue patterns**
  - **Action:** Open a configured summary report for the default customer data.
  - **Expected:** The report presents understandable summaries of customer engagement and revenue patterns.

## Constraint

- [ ] **CS-01: Prevent saving incomplete customer records**
  - **Action:** Select **“Add Customer”**, leave required customer fields empty, and select **“Save”**.
  - **Expected:** The record is not saved and each missing required field displays a validation message.
  - **Bug Report:**
    - **Issue:** Missing-field validation is not displayed for each required field.
    - **Actual:** Saving an empty form prevented record creation and displayed one toast, “Please fill in first name, last name, and email.”, but no individual validation message appeared beside each missing required field.

- [ ] **CS-02: Keep related items associated with the correct customer**
  - **Action:** Attach an existing item to Customer A, then open Customer B.
  - **Expected:** The item appears under Customer A and does not appear under Customer B unless separately attached.
  - **Bug Report:**
    - **Issue:** Related artwork association is not isolated to the selected customer.
    - **Actual:** After attaching “Urban Fragments” to Victoria Ashworth, James Morrison’s profile also displayed “Urban Fragments” in his Interested Artworks section without a separate attachment during this test.

- [X] **CS-03: Enforce active filter and segment criteria**
  - **Action:** Apply a customer filter or segment, then inspect every displayed customer.
  - **Expected:** Every displayed customer satisfies all active filter or segment criteria.

- [ ] **CS-04: Scope report results to the selected customer set**
  - **Action:** Apply a customer filter or segment, open a report, and compare the report scope with the filtered customer list.
  - **Expected:** Report results include only data from customers in the selected filter or segment.
  - **Bug Report:**
    - **Issue:** Report results cannot be scoped to a filtered or segmented customer set.
    - **Actual:** The report page has no customer-set filter or segment selector, and the report displayed all-customer summary metrics rather than results tied to the filtered customer list.

## Interaction

- [X] **IX-01: Confirm successful customer saves**
  - **Action:** Save a valid new or edited customer record.
  - **Expected:** A visible success confirmation appears and the customer list or profile reflects the saved data without requiring a manual page reload.

- [X] **IX-02: Refresh the customer list when filters change**
  - **Action:** Apply a filter, then remove it or select a different filter.
  - **Expected:** The displayed customer results update immediately to match the current filter selection.

- [ ] **IX-03: Update the report when configuration changes**
  - **Action:** Change a report measure, grouping, or filter.
  - **Expected:** The report visibly refreshes and its displayed summaries correspond to the new configuration.
  - **Bug Report:**
    - **Issue:** Report measure, grouping, and filter configuration controls are unavailable.
    - **Actual:** The only report interaction available was switching between Revenue, Engagement, and Sales Funnel tabs; no configurable measure, grouping, or filter could be changed.

## Content

- [ ] **CT-01: Display niche-specific customer fields**
  - **Action:** Open a customer profile for the gallery-style business scenario.
  - **Expected:** The profile includes relevant fields or sections for collector interests, exhibition invitations, and artwork purchases.
  - **Bug Report:**
    - **Issue:** Exhibition invitation information is not represented.
    - **Actual:** The profile included collector interests, artwork interests, purchase history, and an activity entry for “Attended winter gala,” but did not include a field or section for exhibition invitations.

- [X] **CT-02: Use workflow-relevant labels and statuses**
  - **Action:** Review customer list, profile, related-item, and workflow-status areas.
  - **Expected:** Labels, statuses, and related-item names clearly describe the niche business context and do not use unrelated generic content.

- [X] **CT-03: Label report measures clearly**
  - **Action:** Review the configured summary report and its controls.
  - **Expected:** Engagement and revenue measures, groupings, and displayed summaries have clear, accurate labels that match the data shown.