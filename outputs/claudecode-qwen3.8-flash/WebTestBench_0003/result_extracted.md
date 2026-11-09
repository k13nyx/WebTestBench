# Test Result

> Execution note: the app keeps all jobs/applications in memory only (no localStorage). After I submitted the FT-10 application, a full-page navigation reseeded the store and my first application was lost, so I resubmitted the application and verified it end-to-end within a single client-side session. This non-persistence also explains why the invalid CS-02 job vanished after reload (FT-10 was nonetheless verified against the required flow, per the checklist's expectations).

## Functionality
- [X] FT-01: Employer can create a new job listing with all required details
  - Action: Opened "Post a Job" (/employer/post-job); filled Title "Full-Stack React Engineer", Description, Location "Seattle, WA", Salary 120000–160000, Required Skills "React" and "Node.js" (added via the skill chip control); clicked "Post Job".
  - Expected: The job is created and its title now appears in the main job board listing list. → Verified: board showed "Showing 9 jobs" with a "Full-Stack React Engineer" card (TechCorp Solutions · Seattle, WA · $120k - $160k · React, Node.js), and the row appears in the employer dashboard.
- [ ] FT-02: Employer can edit an existing job listing
  - Action: Looked for an "Edit" option on the employer dashboard rows (only an applications-count toggle and a delete/trash button exist) and on the job detail page (only the public apply form exists).
  - Expected: The updated title and salary range are shown on the job board and on that job's detail page.
  - Bug Report:
    - Issue: Missing feature — no job-edit capability anywhere in the UI
    - Actual: No "Edit" control exists on the dashboard rows, the job detail page, or navigation; a source scan of the app modules (App.tsx and all loaded route components) found no edit route or component ("hasEditWord: false"). Jobs can only be created or deleted, so the title/salary update flow cannot be performed.
- [X] FT-03: Employer can delete an existing job listing
  - Action: Clicked the delete (trash) button on the "Full-Stack React Engineer" dashboard row; alert dialog "Delete this job?" appeared; clicked "Delete".
  - Expected: Verified — job removed from dashboard ("Your Job Listings" no longer contains it; Active Jobs dropped 6→5) and from the board ("Showing 8 jobs", card absent).
- [X] FT-04: Job seekers can browse all available listings
  - Action: Loaded the job board main page (/).
  - Expected: Verified — 8 default listings rendered as cards ("Showing 8 jobs"), each with title, location, and employment type visible (plus company, salary, posted date, skills).
- [X] FT-05: Listings can be filtered by industry
  - Action: Opened the "Industry" combobox and selected "Technology".
  - Expected: Verified — "Showing 2 jobs", only Senior Frontend Developer and DevOps Engineer (Technology); Healthcare/Marketing/Finance/etc. cards disappeared. "Clear filters" appeared.
- [X] FT-06: Listings can be filtered by location
  - Action: Opened the "Location" combobox and selected "New York, NY".
  - Expected: Verified — "Showing 1 jobs", only Registered Nurse (New York, NY) displayed.
- [X] FT-07: Listings can be filtered by employment type
  - Action: Opened the "Job Type" combobox and selected "Part-time".
  - Expected: Verified — "Showing 1 jobs", only Part-Time Content Writer (Part-time) displayed.
- [X] FT-08: Listings can be searched by keyword
  - Action: Typed "designer" into the search box.
  - Expected: Verified — list updated live to "Showing 1 jobs" (Product Designer only; skill/description matches restricted correctly; a separate check of "Python" returned only Data Analyst).
- [X] FT-09: Each job listing page displays full details
  - Action: Clicked the "Senior Frontend Developer" card → /jobs/job-1.
  - Expected: Verified — page shows full title, full description with Responsibilities/Requirements lists, location (San Francisco, CA), salary range ($140k - $180k), required skills (React, TypeScript, CSS, Node.js), industry (Technology) and employment type (Full-time).
- [X] FT-10: Job seeker can submit an application from the job detail page
  - Action: On /jobs/job-1 filled Full Name "Alicia QA", Email "alicia.qa@example.com", Phone "555-9911", Cover Letter, clicked "Submit Application".
  - Expected: Verified — "Application submitted!" toast appeared and the application was recorded for that specific job (it appears in Sr. Frontend Developer's dashboard list as "Applications (3)"; job count 2→3, total 3→4, and Product Designer's list stayed at 1).
- [X] FT-11: Employer dashboard lists the employer's posted jobs
  - Action: Opened /employer/dashboard (client-side nav).
  - Expected: Verified — "Your Job Listings" shows 5 posted jobs each with title, location/salary line, employment type and an application-count button (Sr FE 3, PD 1, others 0), plus "Active Jobs" and "Total Applications" stat tiles.
- [X] FT-12: Dashboard shows submitted applications per listing
  - Action: Expanded the applications views for Product Designer and Senior Frontend Developer.
  - Expected: Verified — PD shows only James Wilson (james.w@email.com, 555-0103, message); Sr FE shows only Alicia QA, Alex Johnson, Maria Garcia, each with email, phone, date and message; no cross-job mixing.

## Constraint
- [X] CS-01: Job creation is blocked when required fields are missing
  - Action: Opened "Post a Job" and clicked "Post Job" with all fields (Title, Industry, Type, Location, Salaries, Description) empty.
  - Expected: Verified (via native HTML5 validation) — submission rejected: no navigation, no job created; the empty "Job Title" input has `required=true` with `checkValidity()=false`, focus moved to that offending field, and the browser's validation bubble targets it. Note: the app itself renders no custom error message; validation relies entirely on the browser's native UI.
- [ ] CS-02: Salary range must be valid
  - Action: In the job form, filled valid Title/Industry/Type/Location/Description with Min Salary 90000 and Max Salary 60000, clicked "Post Job".
  - Expected: The form is rejected with a validation error (max must be ≥ min); the job is not saved.
  - Bug Report:
    - Issue: Missing validation — inverted salary range accepted and saved
    - Actual: The job was created: redirected to dashboard with toast "Job posted successfully!" and the new listing row showed "QA Salary Validation Engineer — Austin, TX · **$90k - $60k**". No error was raised (inputs only enforce min="0"), so an invalid max < min range persists.
- [X] CS-03: Application form is blocked when required contact info is missing or malformed
  - Action: On /jobs/job-1 with a submit-event listener attached to the form, (1) submitted with Email empty, (2) with Email "abc@", (3) with the Message cleared (name/email/phone valid).
  - Expected: Verified — all three attempts were rejected (listener `__submitCount` remained 0 through all three; form kept its values, no success toast). After completing valid data, exactly 1 submit fired and the success toast appeared, proving the three invalid submissions recorded no application. Note: blocking is via native HTML5 `required`/email-format validation with focus moved to the offending field (no app-rendered error text).

## Interaction
- [X] IX-01: Success feedback after creating a job
  - Action: Completed FT-01 (valid job creation).
  - Expected: Verified — toast "Job posted successfully! Your job listing is now live and visible to job seekers." appeared and the user was redirected to the dashboard, which shows the new "Full-Stack React Engineer" row (the new job also appears on the board).
- [X] IX-02: Success feedback after submitting an application
  - Action: Completed FT-10 (valid application).
  - Expected: Verified — toast "Application submitted! Your application for Senior Frontend Developer at TechCorp Solutions has been sent." appeared and the form fields were cleared back to placeholders (all input values empty after submit).
- [X] IX-03: Results list reacts dynamically to filters/search, including a no-match state
  - Action: Typed keyword "Python" (live-filtered to Data Analyst), then selected Industry "Marketing" together with it; then clicked "Clear filters".
  - Expected: Verified — combined criteria updated instantly to "Showing 0 jobs" with an explicit empty state ("No jobs found — Try adjusting your filters or search terms"); clearing filters reset search + dropdowns and restored the full "Showing 8 jobs" list.

## Content
- [X] CT-01: Default data is present and job-board relevant
  - Action: Inspected all 8 default board cards, detail pages, the dashboard listings, and seeded applications; ran a DOM text scan for "lorem/ipsum/TODO/FIXME/placeholder/undefined/NaN/null".
  - Expected: Verified — 8 realistic seeded listings (plausible titles, companies, locations, salary ranges, skills, industries) and seeded applications with realistic applicant profiles (Alex Johnson, Maria Garcia, James Wilson); scan returned zero placeholder/"undefined"/"null" strings.
- [X] CT-02: Displayed details and application records match their stored data
  - Action: Compared the Senior Frontend Developer board card with its detail page, and the FT-10 submission with its dashboard row.
  - Expected: Verified — card and detail identical (Senior Frontend Developer / TechCorp Solutions / San Francisco, CA / $140k - $180k / Full-time / Technology / React, TypeScript, CSS, Node.js); dashboard row shows exactly the submitted "Alicia QA", alicia.qa@example.com, 555-9911, verbatim message, under the correct job (Senior Frontend Developer).
