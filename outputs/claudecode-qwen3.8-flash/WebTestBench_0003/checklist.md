# Test Checklist

## Functionality
- [ ] FT-01: Employer can create a new job listing with all required details
  - Action: Open the employer "Create Job" / "Post a Job" form; fill Title, Description, Location, Salary Range, and Required Skills with valid values; click "Submit"/"Post Job".
  - Expected: The job is created and its title now appears in the main job board listing list.

- [ ] FT-02: Employer can edit an existing job listing
  - Action: From the dashboard or listing, open a default job's "Edit" option; change the Title and Salary Range; save.
  - Expected: The updated title and salary range are shown on the job board and on that job's detail page.

- [ ] FT-03: Employer can delete an existing job listing
  - Action: Open a job's "Edit"/"Manage" controls and choose "Delete" (confirm if prompted).
  - Expected: The job no longer appears in the job board or in the employer dashboard list.

- [ ] FT-04: Job seekers can browse all available listings
  - Action: Load the job board main page as a job seeker.
  - Expected: All default listings are shown (e.g., as cards/rows) with title, location, and employment type visible.

- [ ] FT-05: Listings can be filtered by industry
  - Action: In the filter panel, select one industry value (e.g., "Technology") from the "Industry" dropdown.
  - Expected: Only jobs in that industry are shown; jobs from other industries disappear from the list.

- [ ] FT-06: Listings can be filtered by location
  - Action: Select/enter a location (e.g., "New York") in the "Location" filter and apply it.
  - Expected: Only jobs matching that location are displayed.

- [ ] FT-07: Listings can be filtered by employment type
  - Action: Select an employment type (e.g., "Full-time" or "Part-time") in the "Employment Type" filter.
  - Expected: Only jobs of that employment type are displayed.

- [ ] FT-08: Listings can be searched by keyword
  - Action: Type a keyword present in some default jobs (e.g., a skill or title word like "designer") into the search box and submit.
  - Expected: Results are restricted to jobs whose title, description, or skills contain the keyword.

- [ ] FT-09: Each job listing page displays full details
  - Action: Click the title/card of one default job to open its detail page.
  - Expected: The page shows that job's full title, description, location, salary range, required skills, industry, and employment type.

- [ ] FT-10: Job seeker can submit an application from the job detail page
  - Action: On a job's detail page, click "Apply Now", enter name, email, phone (contact info), and a short message, then submit.
  - Expected: The application is accepted and recorded for that specific job.

- [ ] FT-11: Employer dashboard lists the employer's posted jobs
  - Action: Open the employer "Dashboard" page.
  - Expected: A list of posted jobs is shown with each job's title and application count/status.

- [ ] FT-12: Dashboard shows submitted applications per listing
  - Action: In the dashboard, open the applications view for a default job that has at least one application.
  - Expected: The applications for that job are listed, showing applicant name, contact info, and message; applications for other jobs are not mixed in.

## Constraint
- [ ] CS-01: Job creation is blocked when required fields are missing
  - Action: Open "Create Job", leave the Title (and/or Description/Location) empty, and submit.
  - Expected: Submission is rejected with a visible validation error naming the missing field(s); no new listing is created.

- [ ] CS-02: Salary range must be valid
  - Action: In the job form, enter a maximum salary lower than the minimum salary (e.g., min 90000, max 60000) and submit.
  - Expected: The form is rejected with a validation error (max must be ≥ min); the job is not saved.

- [ ] CS-03: Application form is blocked when required contact info is missing or malformed
  - Action: On "Apply Now", submit with the email field empty and, separately, with an invalid email (e.g., "abc@"); leave the message empty in a third attempt.
  - Expected: Each invalid submission is rejected with a validation error on the offending field; no application is recorded.

## Interaction
- [ ] IX-01: Success feedback after creating a job
  - Action: Complete FT-01 (valid job creation).
  - Expected: A confirmation (toast/message such as "Job posted successfully") appears and the user is returned to the board or dashboard showing the new job.

- [ ] IX-02: Success feedback after submitting an application
  - Action: Complete FT-10 (valid application).
  - Expected: A confirmation message/toast (e.g., "Application submitted") appears; the form is cleared or replaced by the confirmation state.

- [ ] IX-03: Results list reacts dynamically to filters/search, including a no-match state
  - Action: Apply an industry filter and a keyword together (e.g., industry "Marketing" + keyword "Python") that no default job satisfies, then clear the filters.
  - Expected: The listing area updates immediately to show only jobs matching all active criteria; with no matches a clear "No jobs found" empty state is shown, and clearing restores the full list.

## Content
- [ ] CT-01: Default data is present and job-board relevant
  - Action: Inspect the default listings on the board and the entries in the employer dashboard.
  - Expected: Multiple pre-seeded, realistic job listings exist (plausible titles, companies, locations, salaries, skills) and the dashboard shows default applications — no placeholder text ("Lorem ipsum", "TODO", "undefined", "null") anywhere.

- [ ] CT-02: Displayed details and application records match their stored data
  - Action: Compare one job's card on the board with its detail page, and compare an application submitted in FT-10 with its row in the dashboard.
  - Expected: Title, location, salary range, skills, and employment type are identical between board and detail page; the dashboard entry shows the exact applicant name, email/phone, message, and the correct job.