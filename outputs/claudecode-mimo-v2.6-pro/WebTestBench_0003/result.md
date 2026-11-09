**CS-02 CONFIRMED FAIL** — "Test Job" was created with "$100k - $50k" (min > max) without any salary validation. Now I have all test results. Let me compile the complete checklist.

# Test Result

## Functionality
- [X] FT-01: Employer can create a new job listing with all required details.
  - Action: As an employer, open the job creation form and enter title "QA Analyst", description, location "Berlin", salary range "40,000–55,000", and required skills "Testing, SQL"; click the create/submit button.
  - Expected: The listing is created and appears in the employer's dashboard with all entered details saved.
- [ ] FT-02: Employer can edit an existing job listing.
  - Action: On the employer dashboard, open a previously posted job, change its title and salary range, and save.
  - Expected: The listing is updated and the new title and salary range are shown on the listing page and dashboard.
  - Bug Report:
    - Issue: Missing Edit Functionality
    - Actual: The employer dashboard provides no edit button or edit link for any job listing. Each listing row contains only two buttons: an applications-count button and a delete button (which opens a "Delete this job?" confirmation dialog). There is no way to open an edit form to change a listing's title or salary range.
- [X] FT-03: Employer can delete a job listing.
  - Action: On the employer dashboard, delete a posted job listing and confirm the deletion.
  - Expected: The listing is removed from the dashboard and no longer appears in the public browse list.
- [X] FT-04: Job seeker can browse all available listings.
  - Action: Open the job board browse page without applying any filters or search.
  - Expected: All available default job listings are displayed, each showing at least title, location, and employment type.
- [X] FT-05: Job seeker can filter listings by industry.
  - Action: Select one industry value in the industry filter.
  - Expected: Only listings belonging to that industry are shown; listings from other industries are hidden.
- [X] FT-06: Job seeker can filter listings by location.
  - Action: Select one location value in the location filter.
  - Expected: Only listings in that location are shown; listings in other locations are hidden.
- [X] FT-07: Job seeker can filter listings by employment type.
  - Action: Select one employment type (e.g., Full-time) in the employment type filter.
  - Expected: Only listings of that employment type are shown; other types are hidden.
- [X] FT-08: Job seeker can search listings by keyword.
  - Action: Type a keyword that matches an existing default listing's title or skills (e.g., a skill name shown in a listing) into the search field and submit.
  - Expected: Listings containing the keyword in their title, description, or skills are shown.
- [X] FT-09: Job listing page displays full job details.
  - Action: Click an existing default listing from the browse page to open its detail page.
  - Expected: The page shows the job title, description, location, salary range, required skills, and employment type.
- [X] FT-10: Job seeker can submit an application with contact information and a short message.
  - Action: On a job detail page, fill in the application form with name, email, and a short message, then click "Apply"/"Submit".
  - Expected: The application is submitted and a confirmation is shown; the application appears in the employer's applications list for that listing.
- [X] FT-11: Employer dashboard lists the employer's posted jobs.
  - Action: Open the employer dashboard.
  - Expected: All job listings created by the employer are displayed in a list with identifying information (e.g., title).
- [X] FT-12: Employer can view submitted applications for a specific listing.
  - Action: On the employer dashboard, open the applications view for one posted job that has received an application.
  - Expected: The applicant's name, email, and message from FT-10 are displayed for that listing.

## Constraint
- [X] CS-01: Job listing cannot be created with empty required fields.
  - Action: Open the job creation form, leave title and description empty, and click the create/submit button.
  - Expected: The listing is not created; an error or validation message indicates the missing required fields.
- [ ] CS-02: Salary range must be valid (minimum not greater than maximum).
  - Action: In the job creation/edit form, enter a minimum salary greater than the maximum salary and submit.
  - Expected: The submission is rejected with a validation message about the invalid salary range.
  - Bug Report:
    - Issue: Missing Salary Range Validation
    - Actual: The job creation form accepts a minimum salary of 100,000 and a maximum salary of 50,000 (min > max) and submits without any validation error. The listing "Test Job" is created and appears in the dashboard with the salary displayed as "$100k - $50k", confirming the invalid range was saved without rejection.
- [X] CS-03: Application form cannot be submitted with missing or invalid contact information.
  - Action: On a job detail page, submit the application form with an empty name and an invalid email (e.g., "abc").
  - Expected: The application is not submitted; validation errors identify the empty name and invalid email.
- [ ] CS-04: Applying twice to the same listing is prevented (or flagged).
  - Action: Submit a valid application for a listing, then submit a second application for the same listing using the same email.
  - Expected: The second submission is rejected or flagged as a duplicate; only one application for that email appears in the employer's applications list.
  - Bug Report:
    - Issue: Missing Duplicate Application Prevention
    - Actual: Submitting a second application for the same listing (Senior Frontend Developer) with the same email "john@test.com" is accepted without any rejection or duplicate flag. A second "Application submitted!" success toast appears, and the form resets normally, confirming no duplicate detection logic exists.
- [X] CS-05: Job seeker cannot submit an application with an empty message.
  - Action: On a job detail page, fill in name and valid email but leave the short message empty, then submit.
  - Expected: The application is not submitted; a validation message indicates the message field is required.

## Interaction
- [X] IX-01: Success feedback is shown after creating a job listing.
  - Action: Create a valid job listing and submit the form.
  - Expected: A success message (e.g., toast or inline confirmation) appears indicating the listing was created.
- [X] IX-02: Success feedback is shown after submitting an application.
  - Action: Submit a valid application on a job detail page.
  - Expected: A success message (e.g., "Application submitted") appears confirming the submission.
- [ ] IX-03: Validation errors are displayed inline when submitting an invalid application form.
  - Action: Submit the application form with an invalid email and empty message.
  - Expected: Error messages appear next to the corresponding fields without a page reload.
  - Bug Report:
    - Issue: Missing Inline Validation Error Messages
    - Actual: When the application form is submitted with invalid data, the form relies entirely on HTML5 native browser validation (required attributes and type="email"). No custom inline DOM error message elements are rendered next to the form fields. The browser shows a native tooltip on the first invalid field only, with no visible error text elements in the DOM for each corresponding field.

## Content
- [ ] CT-01: Listing detail page content matches the entered job data.
  - Action: Create a listing with known values (title "QA Analyst", location "Berlin", salary "40,000–55,000", skills "Testing, SQL"), then open its detail page.
  - Expected: The detail page shows exactly those values with no missing or altered fields.
  - Bug Report:
    - Issue: Form Dropdown Missing Expected Location Value
    - Actual: The location "Berlin" specified in the test cannot be entered because the Location field is a dropdown limited to US cities (San Francisco, CA / New York, NY / Austin, TX / Chicago, IL / Seattle, WA / Boston, MA) and "Remote". The detail page shows "New York, NY" (the substituted value) instead of "Berlin". Additionally, the salary range is displayed as "$40k - $55k" rather than the entered "40,000–55,000" format. Title "QA Analyst" and skills "Testing, SQL" match correctly.