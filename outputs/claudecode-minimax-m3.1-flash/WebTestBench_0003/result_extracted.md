# Test Result

## Functionality

- [X] FT-01: Employer can create a job listing with all required details
  - Action: As an employer, open the "Post a Job" / "Create Listing" form and enter a title, description, location, salary range (minimum and maximum), required skills, industry, and employment type, then submit.
  - Expected: The listing is created successfully, a success confirmation is displayed, and the new listing appears in the public job listings list.
  - Note: Submitted title "QA Automation Engineer", description, industry "Technology", employment type "Full-time", location "San Francisco, CA", salary 120000/60000, skills "Playwright" + "Selenium". Toast "Job posted successfully! / Your job listing is now live and visible to job seekers." appeared, the dashboard went from 5 → 6 Active Jobs, and the public list went from 8 → 9 jobs with the new card present.

- [ ] FT-02: Employer can edit an existing job listing
  - Action: From the employer dashboard, open one of the employer's posted jobs and change a field (e.g., the title or salary range), then save.
  - Expected: The changes are saved, the dashboard shows the updated values, and the public listing/detail page shows the updated values.
  - Bug Report:
    - Issue: Missing Edit Feature / Non-responsive Edit Control — no edit affordance exists anywhere for a posted listing (Job Detail page shows only "Apply for this position"; employer dashboard row exposes only an applications-count button and a delete button).
    - Actual: Clicking the icon button on a dashboard listing row (e.g. "QA Automation Engineer") opens a confirmation dialog titled "Delete this job?" ("This will permanently delete \"QA Automation Engineer\" and all its applications."), not an edit form; clicking the job title heading in the dashboard does nothing (no navigation, no form). The app defines only the routes `/`, `/jobs/:id`, `/employer/dashboard`, `/employer/post-job`, `*` — there is no edit route, and `/src/pages/employer/PostJob.tsx` contains no `useParams`/`searchParams`/`edit` handling and `/src/context/JobContext.tsx` exposes no update/edit function. A posted listing therefore cannot be modified.

- [X] FT-03: Job seeker can browse all available job listings
  - Action: As a job seeker, open the home/browse jobs page without applying any filters or search terms.
  - Expected: All default job listings are displayed in a list, each showing at least its title, company, location, and employment type.
  - Note: Home page showed "Showing 8 jobs"; each card shows title, company (e.g. TechCorp Solutions), location, employment-type badge, salary and skills.

- [X] FT-04: A job listing detail page shows the full listing details
  - Action: From the listings list, open one listing by clicking its title or card.
  - Expected: A detail page displays the job title, full description, location, salary range, required skills, industry, and employment type.
  - Note: /jobs/job-1 shows "Senior Frontend Developer", company, San Francisco, CA, $140k - $180k, industry "Technology", type "Full-time", full Job Description with Responsibilities/Requirements lists, and a "Required Skills" section (React, TypeScript, CSS, Node.js).

- [X] FT-05: Listings can be filtered by industry
  - Action: On the browse jobs page, select a specific industry in the industry filter and apply it.
  - Expected: Only listings belonging to the selected industry are shown, and listings from other industries are not shown.
  - Note: Selected "Marketing" → count changed 8 → 2, showing only Marketing Manager and Part-Time Content Writer; all other-industry cards (Technology, Design, Healthcare, Finance, Education) disappeared.

- [X] FT-06: Listings can be filtered by location
  - Action: On the browse jobs page, select a specific location in the location filter and apply it.
  - Expected: Only listings with the selected location are shown, and listings in other locations are not shown.
  - Note: With Marketing selected, choosing "Austin, TX" → 1 job (Marketing Manager, Austin, TX); the Remote/other-location Marketing listing was excluded.

- [X] FT-07: Listings can be filtered by employment type
  - Action: On the browse jobs page, select an employment type (e.g., Full-time) in the employment type filter and apply it.
  - Expected: Only listings with that employment type are shown, and listings with other employment types are not shown.
  - Note: With filters cleared, "Part-time" → 1 job (Part-Time Content Writer only); with Marketing+Austin, "Full-time" → 1 job (Marketing Manager only).

- [X] FT-08: Listings can be searched by keyword
  - Action: Enter a keyword that appears in an existing default listing (e.g., a word from its title, description, or required skills) into the search field and submit the search.
  - Expected: Only listings matching that keyword are shown, and non-matching listings are excluded from the results.
  - Note: Typing "React" with no filters → "Showing 1 jobs", only /jobs/job-1 (Senior Frontend Developer, skill "React"). Search filters live as the term changes.

- [X] FT-09: Job seeker can submit an application with contact information and a message
  - Action: Open a listing's detail page, scroll to the application form, enter name, email, and a short message, then submit the application.
  - Expected: A success confirmation is shown, the submitted application is recorded for that listing, and the application appears in the employer's dashboard for that listing.
  - Note: Toast "Application submitted! / Your application for Senior Frontend Developer at TechCorp Solutions has been sent."; dashboard "Total Applications" rose 3 → 4 and the Senior Frontend Developer application counter rose 2 → 3 with a "Jane Tester" entry.

- [X] FT-10: Employer dashboard lists the employer's posted jobs
  - Action: Sign in / navigate as an employer to the dashboard page.
  - Expected: A list of the employer's posted job listings is shown, each showing the job title and enough detail (e.g., location, employment type, posted status) to identify it.
  - Note: /employer/dashboard ("Welcome back, Sarah Chen") lists 5 seed listings + 1 created one (6 Active Jobs), each with title, industry/type badges, location · salary · posted date, and an application counter.

- [X] FT-11: Employer dashboard shows submitted applications for each listing
  - Action: On the employer dashboard, select one of the posted jobs (e.g., a job that has received an application).
  - Expected: A list of applications for that specific job is shown, each entry identifying the applicant, and the applications of other jobs are not mixed in.
  - Note: Senior Frontend Developer → "Applications (3)": Jane Tester, Alex Johnson, Maria Garcia. Product Designer → "Applications (1)": James Wilson only — no cross-contamination between listings.

## Constraint

- [X] CS-01: Job listing cannot be created with missing required details
  - Action: On the job creation form, leave the title (and the other required fields) blank and submit the form.
  - Expected: The submission is rejected, an inline validation error identifies the missing field(s), and no new listing is created or added to the dashboard.
  - Note: With every field filled except the title, clicking "Post Job" was rejected — the app stayed on /employer/post-job, focus moved to the empty Job Title field (`#title` validity = false, browser "required" constraint error shown on that field), and no listing was created (dashboard stayed at 6 Active Jobs, public list stayed at 9 jobs). Validation is provided by native HTML5 constraint validation (`required` attributes / `aria-required`), so the error is the browser field-level message rather than a separately rendered inline element.

- [ ] CS-02: Salary range cannot have a minimum greater than its maximum
  - Action: On the job creation form, enter a salary minimum that is higher than the salary maximum (e.g., min 120000, max 60000) and submit.
  - Expected: The submission is rejected with a clear error about the invalid salary range, and no listing is created.
  - Bug Report:
    - Issue: Missing Input Validation / Incorrect Form Submission — inverted salary range is accepted and published.
    - Actual: With minimum salary 120000 and maximum salary 60000, the form submitted successfully with the toast "Job posted successfully! / Your job listing is now live and visible to job seekers." No error about the salary range was displayed anywhere. The listing was created and published: the employer dashboard shows "QA Automation Engineer — San Francisco, CA · $120k - $60k · Posted Yesterday" and the public listing card/detail page displays the invalid range "$120k - $60k" (Active Jobs 5 → 6).

- [X] CS-03: Application cannot be submitted with missing or invalid contact information
  - Action: On a listing's application form, submit with the email field blank; then repeat with a malformed email such as "applicant@" and observe the result each time.
  - Expected: Both submissions are rejected with a validation error on the email field, and no application is recorded in the employer's dashboard.
  - Note: Blank email → submit rejected (form not submitted, no toast, values retained); malformed "applicant@" → submit rejected (`#email.checkValidity() === false`, email `type="email"` constraint). The employer dashboard application counts remained unchanged (no new application recorded). As with CS-01, the validation message is the browser's native field-level error rather than a rendered inline element.

## Interaction

- [X] IX-01: Clicking a listing in the results opens its detail page
  - Action: Click the title of a listing card in the browse/search results.
  - Expected: The application navigates to that specific listing's detail page, with the correct listing's details shown (not another listing's).
  - Note: Clicking the "Senior Frontend Developer" card navigated to /jobs/job-1 and showed that listing's title, company, salary, skills and description; clicking the newly created card navigated to /jobs/job-1794060110265 showing "QA Automation Engineer".

- [X] IX-02: Filter and search controls update the result list and can be reset
  - Action: Apply an industry filter, then a location filter, then enter a search term and observe the result list; afterwards click the "Clear"/"Reset filters" control.
  - Expected: The result list updates immediately after each filter/search change to show only matching listings, and clicking "Clear"/"Reset" restores the full unfiltered list of listings.
  - Note: Industry "Marketing" → 8→2 jobs; Location "Austin, TX" → 2→1 job; search "React" → 1→0 jobs ("No jobs found"); clicking "Clear filters" restored "Showing 8 jobs" and reset the search box and all three filter controls to their default labels.

- [X] IX-03: Successful job creation gives visible feedback
  - Action: Successfully submit a valid job creation form and observe the page immediately after submission.
  - Expected: A success confirmation message or notification is displayed, and the new listing is either shown in the result or redirected to the listing/dashboard view.
  - Note: Toast "Job posted successfully! / Your job listing is now live and visible to job seekers." was displayed and the app redirected to the Employer Dashboard where "QA Automation Engineer" was listed as a new Active Job.

## Content

- [X] CT-01: Salary range is displayed in a clear min–max format with currency
  - Action: Open a listing detail page and inspect the salary range shown for the default listings.
  - Expected: The salary range is displayed as a minimum–maximum pair with a currency symbol (e.g., "$80,000 – $110,000"), matching the values entered.
  - Note: Detail pages show a minimum–maximum pair with the currency symbol, e.g. "$140k - $180k" (Senior Frontend Developer, entered 140000–180000), "$75k - $95k" (Registered Nurse), "$85k - $110k" (Marketing Manager); the employer-entered values are shown verbatim as a min–max pair.

- [X] CT-02: Required skills are displayed exactly as entered by the employer
  - Action: Open a listing detail page and compare the "Required Skills" section with the skills specified in the listing data.
  - Expected: All required skills for the job are listed with no skills missing and no extra or unrelated skills shown.
  - Note: Senior Frontend Developer shows exactly React, TypeScript, CSS, Node.js (identical to its listing card/data). The employer-created listing shows exactly "Playwright" and "Selenium" — the two skills entered, with no extras.

- [X] CT-03: Dashboard application entries show the applicant's submitted details
  - Action: Open the applications list for a listing that has at least one submitted application.
  - Expected: Each application entry displays the applicant's name, contact information (email), and short message exactly as it was submitted, with no placeholder or blank values.
  - Note: The Senior Frontend Developer applications panel shows "Jane Tester", jane.tester@example.com, 555-0142 and the message "I am excited about this role and believe I am a strong fit." exactly as submitted, alongside the seeded entries (Alex Johnson / alex.j@email.com, Maria Garcia / maria.g@email.com) with their full messages.
