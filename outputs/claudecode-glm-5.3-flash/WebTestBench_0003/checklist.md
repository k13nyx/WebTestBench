# Test Checklist

## Functionality
- [ ] FT-01: Employer can create a new job listing with all required details
  - Action: Open the employer's "Create Job"/"Post Job" form, enter title, description, location, salary range, and required skills, then submit.
  - Expected: The listing is created successfully and saved with all entered values.
- [ ] FT-02: Newly created listing appears in the job seeker browse view
  - Action: After creating a listing in FT-01, go to the job browse/search page.
  - Expected: The new listing appears in the list with its correct title and details.
- [ ] FT-03: Employer can edit an existing job listing
  - Action: From the employer's view, open one of their posted listings, change its title or salary range, and save.
  - Expected: The updated values are saved and shown on the listing and/or browse page.
- [ ] FT-04: Employer can delete an existing job listing
  - Action: From the employer's view, delete one of their posted listings, then check the browse page.
  - Expected: The deleted listing no longer appears in the browse list.
- [ ] FT-05: Job seeker can browse all available listings
  - Action: Open the job browse page as a job seeker without applying any filter or search.
  - Expected: All available (non-deleted) job listings are displayed.
- [ ] FT-06: Listings can be filtered by industry
  - Action: On the browse page, select one industry from the industry filter.
  - Expected: Only listings belonging to that industry are shown.
- [ ] FT-07: Listings can be filtered by location
  - Action: On the browse page, select one location from the location filter.
  - Expected: Only listings with that location are shown.
- [ ] FT-08: Listings can be filtered by employment type
  - Action: On the browse page, select one employment type (e.g., Full-time).
  - Expected: Only listings with that employment type are shown.
- [ ] FT-09: Job seeker can search listings by keyword
  - Action: Enter a keyword that matches a word in an existing listing's title or description into the search box and run the search.
  - Expected: Only listings matching the keyword are displayed.
- [ ] FT-10: Job detail page displays full listing details
  - Action: Click on a listing from the browse page.
  - Expected: The detail page shows the full title, description, location, salary range, required skills, and employment type.
- [ ] FT-11: Job seeker can submit an application for a listing
  - Action: On a job detail page, fill in the application form with contact information (e.g., name, email) and a short message, then submit.
  - Expected: The application is submitted successfully for that listing.
- [ ] FT-12: Employer dashboard lists all of the employer's posted jobs
  - Action: Open the employer dashboard.
  - Expected: Every job listing posted by the employer is listed in the dashboard.
- [ ] FT-13: Dashboard shows submitted applications for each listing
  - Action: Submit an application to a listing (FT-11), then open that listing's applications view in the dashboard.
  - Expected: The submitted application appears with the applicant's contact information and message.

## Constraint
- [ ] CS-01: Job listing form rejects submission with empty required fields
  - Action: Open the create job form, leave required fields (e.g., title) empty, and submit.
  - Expected: Submission is blocked and a validation message is shown; no listing is created.
- [ ] CS-02: Application form rejects submission with empty required contact fields
  - Action: On a job detail page, leave the contact information fields empty and attempt to submit the application.
  - Expected: Submission is blocked with a validation message; no application is recorded.

## Interaction
- [ ] IX-01: Creating a listing gives visible confirmation feedback
  - Action: Submit a valid create job form.
  - Expected: A success message/confirmation (e.g., toast or inline notice) appears after submission.
- [ ] IX-02: Submitting an application gives visible confirmation feedback
  - Action: Submit a valid application form on a job detail page.
  - Expected: A success message/confirmation (e.g., "Application submitted") appears after submission.

## Content
- [ ] CT-01: Job listing cards display key summary information
  - Action: View the browse page's listing cards.
  - Expected: Each card shows at least the job title, location, salary range, and employment type.
- [ ] CT-02: Job detail page shows the required skills for the job
  - Action: Open a job detail page.
  - Expected: The required skills entered for that listing are displayed.
- [ ] CT-03: Application pre-loaded with default job listings
  - Action: Open the browse page on first load without creating any data.
  - Expected: Pre-existing default job listings are displayed with relevant job content (not empty).