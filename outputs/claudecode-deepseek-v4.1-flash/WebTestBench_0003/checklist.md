# Test Checklist

## Functionality
- [ ] FT-01: Employer can create a job listing with all required details.
  - Action: Log in as employer, open "Create Job Listing", enter title, description, location, salary range, required skills, industry, and employment type, then click "Post Job".
  - Expected: New listing is saved and appears in the employer's posted jobs list.

- [ ] FT-02: Employer can edit an existing job listing.
  - Action: On the dashboard, open a posted job and click "Edit", change the title, then save.
  - Expected: The updated title is reflected in both the dashboard and the public listing.

- [ ] FT-03: Employer can delete an existing job listing.
  - Action: On the dashboard, click "Delete" on a posted job and confirm.
  - Expected: The listing is removed from the dashboard and from public browse/search results.

- [ ] FT-04: Job seeker can browse all available listings.
  - Action: Open the job board homepage as a job seeker.
  - Expected: All posted job listings are displayed in a list/grid.

- [ ] FT-05: Job seeker can filter listings by industry.
  - Action: Select an industry from the industry filter.
  - Expected: Only listings matching the selected industry are shown.

- [ ] FT-06: Job seeker can filter listings by location.
  - Action: Select a location from the location filter.
  - Expected: Only listings matching the selected location are shown.

- [ ] FT-07: Job seeker can filter listings by employment type.
  - Action: Select an employment type (e.g., Full-time, Part-time, Contract).
  - Expected: Only listings matching the selected employment type are shown.

- [ ] FT-08: Job seeker can search listings by keyword.
  - Action: Type a keyword (e.g., a job title or skill) into the search box and submit.
  - Expected: Only listings containing the keyword in title, description, or skills are shown.

- [ ] FT-09: Job listing page displays full job details.
  - Action: Click any listing to open its detail page.
  - Expected: Page shows title, description, location, salary range, required skills, industry, and employment type.

- [ ] FT-10: Job seeker can submit an application.
  - Action: On a job detail page, fill the application form with contact information and a short message, then submit.
  - Expected: Application is accepted and recorded against that listing.

- [ ] FT-11: Employer dashboard shows posted jobs and their applications.
  - Action: Open the employer dashboard and select a posted job.
  - Expected: Dashboard lists the employer's jobs, and selecting one shows a list of applications submitted for that listing.

## Constraint
- [ ] CS-01: Job listing cannot be created with empty required fields.
  - Action: On "Create Job Listing", leave title (or another required field) empty and click "Post Job".
  - Expected: Submission is blocked and a validation message identifies the missing field.

- [ ] CS-02: Salary range rejects a minimum greater than the maximum.
  - Action: Enter salary min higher than salary max and submit.
  - Expected: Submission is blocked with a validation message about the salary range.

- [ ] CS-03: Application cannot be submitted without required contact information.
  - Action: On the application form, leave a required contact field empty and submit.
  - Expected: Submission is blocked and a validation message identifies the missing field.

- [ ] CS-04: Search/filter with no matches shows an empty state.
  - Action: Apply a filter or keyword that matches no listings.
  - Expected: A clear "no results" message is shown instead of a blank or stale list.

## Interaction
- [ ] IX-01: Success confirmation shown after a listing is created.
  - Action: Successfully post a new job listing.
  - Expected: A success toast/message confirms the listing was created.

- [ ] IX-02: Confirmation shown after an application is submitted.
  - Action: Successfully submit an application.
  - Expected: A confirmation message is shown to the job seeker.

- [ ] IX-03: Clearing filters restores the full listing set.
  - Action: Apply filters, then click "Clear Filters" (or reset).
  - Expected: All listings are displayed again and the filter inputs reset.

## Content
- [ ] CT-01: Listing cards display the required job fields.
  - Action: View the browse/search results.
  - Expected: Each card shows at least title, location, salary range, and required skills.

- [ ] CT-02: Application list shows applicant contact info and message.
  - Action: Open the applications for a posted job in the dashboard.
  - Expected: Each entry displays the applicant's contact information and their submitted short message.