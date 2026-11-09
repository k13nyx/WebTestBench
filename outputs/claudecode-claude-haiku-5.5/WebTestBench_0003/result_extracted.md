# Test Result

## Functionality

- [X] FT-01: Employer can create a new job listing with all required details.
  - Action: Open the employer dashboard, click "Post a Job", enter Title, Description, Location, Industry, Employment Type, Salary Min, Salary Max, and Required Skills, then click "Publish".
  - Expected: The listing is saved and appears in the job seeker browse page with the entered title, location, salary range, and skills.
- [ ] FT-02: Employer can edit an existing job listing.
  - Action: On the employer dashboard, open a default listing, change its Salary Max and Required Skills, click "Save".
  - Expected: The listing detail page shows the updated salary range and skills.
  - Bug Report:
    - Issue: Missing Edit Function
    - Actual: The dashboard has no Edit control. Each row has only an applications-count toggle and an icon-only button that opens "Delete this job?". Clicking the job title does nothing. The edit step could not be performed.
- [X] FT-03: Job seeker can browse all available listings.
  - Action: Click "Browse Jobs" (or the main listings page) without applying any filters.
  - Expected: All default listings are shown, each displaying title, location, salary range, and employment type.
- [X] FT-04: Each filter (Industry, Location, Employment Type) narrows results to matching listings only.
  - Action: Select one value in the Industry dropdown, then clear it. Repeat for Location and Employment Type, checking each result set.
  - Expected: Every listed job matches the selected value. Clearing the filter restores the full list.
- [X] FT-05: Keyword search returns listings containing the keyword.
  - Action: Type a skill keyword that appears in a default listing's Required Skills (e.g., "Python") into the search box and press Enter.
  - Expected: Results include that listing, and every result contains the keyword in its title, description, or skills.
- [ ] FT-06: Listing detail page shows full job details.
  - Action: Click any job title in the browse list.
  - Expected: The page shows title, full description, location, industry, employment type, salary range, required skills, and an "Apply" button.
  - Bug Report:
    - Issue: Missing "Apply" Button
    - Actual: The detail page shows title, description, location, industry, type, salary, and skills. It has no button labeled "Apply". The apply area is an inline form under the heading "Apply for this position", with a "Submit Application" button.
- [ ] FT-07: Submitted application is visible to the employer for the correct listing.
  - Action: As a job seeker, open a listing, enter Name, Email, Phone, and a Message, and click "Submit Application". Then log in to the employer dashboard and open that listing's applications.
  - Expected: The new application appears with the submitted name, email, phone, and message.
- [ ] FT-08: Employer dashboard lists all jobs posted by the employer.
  - Action: Open the employer dashboard.
  - Expected: All default listings posted by this employer are shown with their titles and status.
  - Bug Report:
    - Issue: Missing Listing Status
    - Actual: The dashboard lists the titles (Senior Frontend Developer, Product Designer, Marketing Manager, Part-Time Content Writer, DevOps Engineer (Contract)). No status is shown for any listing. Each row shows only location, salary, and posted date.

## Constraint

- [ ] CS-01: Job listing cannot be published when required fields are empty.
  - Action: Open "Post a Job", leave Title empty, fill the other fields, and click "Publish". Repeat with Description, Location, and Required Skills left empty.
  - Expected: The listing is not saved and does not appear in the browse list or the dashboard. Repeat with Description, Location, and Required Skills left empty.
  - Bug Report:
    - Issue: Required Skills Not Enforced
    - Actual: With Title, Description, Location, Industry, Employment Type, and salaries filled and Required Skills empty, the form showed "Job posted successfully!" and "Skills Test Engineer" appeared on the dashboard. Empty Title was blocked ("Please fill out this field."). Description and Location carry the HTML `required` attribute, but I did not submit those two cases on their own.
- [ ] CS-02: Salary must be numeric, and Salary Min cannot exceed Salary Max.
  - Action: Enter Salary Min "90000" and Salary Max "60000", then click "Publish". Repeat with Salary Max "abc".
  - Expected: Publishing is blocked in both cases, and the listing is not saved.
  - Bug Report:
    - Issue: Salary Range Not Validated
    - Actual: With Salary Min 90000 and Salary Max 60000, "Job posted successfully!" appeared and the listing card shows "$90k - $60k". The "abc" case was not run, because the Maximum Salary field is a numeric spinbutton.
- [X] CS-03: Application cannot be submitted without a name or with an invalid email.
  - Action: On a listing's "Apply" form, leave Name empty and click "Submit Application". Then enter Email "john@" and submit.
  - Expected: Submission is blocked in both cases, and no application appears on the employer dashboard.

## Interaction

- [X] IX-01: Success confirmation is shown after an application is submitted, and the form is reset.
  - Action: Fill in all application fields with valid data and click "Submit Application".
  - Expected: A confirmation message such as "Application submitted" is displayed, and the form fields are cleared or the form is replaced by the confirmation.
- [ ] IX-02: Validation errors appear next to the specific invalid fields when a form is submitted.
  - Action: Submit the "Post a Job" form with Title and Salary Min empty. Then submit the "Apply" form with Email "not-an-email".
  - Expected: Each invalid field shows its own error message (e.g., "Title is required", "Enter a valid email address") next to the field.
  - Bug Report:
    - Issue: Missing Inline Validation Messages
    - Actual: Empty Title and Salary Min show only the browser's native tooltip ("Please fill out this field."), and no "Title is required" text appears in the DOM. The Apply form's invalid email shows only the native tooltip ("Please enter a part following '@'") and no custom message. I used "john@" in place of "not-an-email".
- [X] IX-03: An empty-state message is shown when no listings match the filters or search.
  - Action: Type "zzzzqqq" into the search box and press Enter.
  - Expected: The result list is empty and the message "No jobs found" (or equivalent) is displayed.
- [X] IX-04: "Clear Filters" resets all filters and search and restores the full list.
  - Action: Select an Industry, a Location, and an Employment Type, enter a keyword, then click "Clear Filters".
  - Expected: All dropdowns return to their default values, the search box is empty, and the full listing set is displayed.
- [X] IX-05: Deleting a listing requires confirmation, and canceling keeps the listing.
  - Action: On the employer dashboard, click "Delete" for a default listing, then click "Cancel" in the confirmation dialog. Repeat and click "Confirm".
  - Expected: After Cancel, the listing remains. After Confirm, the listing is removed from the dashboard and the browse page.

## Content

- [X] CT-01: Default listings show no placeholder, broken, or missing values.
  - Action: Browse all listings and open several detail pages.
  - Expected: Every field contains real content. No "undefined", "null", "N/A", "lorem ipsum", or blank fields appear.
- [ ] CT-02: Filter dropdown options match the industries and employment types present in the listings.
  - Action: Open the Industry and Employment Type dropdowns and compare the options with the Industry and Employment Type values on the default listings.
  - Expected: Each option corresponds to values that exist in the data, with no unused or misspelled options.
  - Bug Report:
    - Issue: Unused Filter Options
    - Actual: The Industry dropdown lists "Sales" and "Engineering", and no listing uses either value. The listings use Technology, Healthcare, Finance, Marketing, Education, and Design. All Job Type options (Full-time, Part-time, Contract, Remote) match values in the data.
- [X] CT-03: Salary range is displayed consistently across the browse card and the detail page.
  - Action: Note the salary range for a default listing on the browse page, then open its detail page.
  - Expected: Both pages show the same salary range, with the same currency and number format.
- [X] CT-04: Application count on the employer dashboard matches the applications listed for that job.
  - Action: On the employer dashboard, note the application count for a listing, then open that listing's applications.
  - Expected: The number of applications listed equals the count shown, and each entry displays the applicant's contact details and message.
