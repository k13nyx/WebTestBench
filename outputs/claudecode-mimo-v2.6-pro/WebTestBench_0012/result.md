All testing is complete. Mia's RSVP immediately moved the count to "2 attending", but the card HTML confirms **no attendee names ever appear** (only counts). I now have all evidence needed. Here is the complete checklist with final statuses.

# Test Result

## Functionality

- [ ] FT-01: Student can create an account and log in with the new credentials.
  - Action: On the sign-up page, fill in name, email, and password, submit the form, then log out and log back in with the same email/password.
  - Expected: Account is created, login succeeds, and the student lands on the main dashboard.
  - Bug Report:
    - Issue: Silent Sign-Up Validation Failure / Unresponsive Form Submission
    - Actual: With name, email, and password filled and "Create Account" clicked, the form silently does nothing — no account is created (logging in with those credentials returns "Login failed — No account found with that email."), and no error message is displayed. Creation succeeds only if at least one subject is also selected ("Subjects (select at least one)"), a field not covered by the action and enforced without any message. (With a subject selected, the account is created and logout + log-in succeeds, landing on the main dashboard at /groups.)

- [X] FT-02: Student can set up a profile with subjects, current level, and preferred study times.
  - Action: Open the profile setup page, select subjects (e.g., calculus, biology), choose a current level (e.g., undergraduate), select preferred study times (e.g., weekday evenings), and save.
  - Expected: Profile saves successfully and the selected subjects, level, and study times are recorded on the profile.

- [ ] FT-03: Student can create a focused study group around a topic.
  - Action: Click "Create Group", enter a group name and topic (e.g., "Calculus Study Group – Calculus"), and submit.
  - Expected: The group is created and appears in the group list, with the creator as a member.
  - Bug Report:
    - Issue: Silent Form Validation Failure on Group Creation (No Error Message)
    - Actual: Entering only a group name ("Calculus Study Group") and topic ("Calculus") and clicking "Create Group" produces no response — the dialog stays open with no error message and no group is created (the group list does not contain it). Creation succeeds only after choosing a subject from the "Select a subject" dropdown; with Mathematics selected the group was created and listed under "Your Groups" with the creator as its 1 member.

- [X] FT-04: Student can join an existing study group.
  - Action: From the group list, open a group the student is not a member of and click "Join Group".
  - Expected: The student becomes a member and gains access to that group's shared space, discussion, and sessions.

- [X] FT-05: Group members can add notes, outlines, and reading summaries into labeled sections of the shared space.
  - Action: In a group's shared space, add one note, one outline, and one reading summary, each placed into a labeled section (e.g., "Notes", "Outlines", "Reading Summaries").
  - Expected: All three items are saved and displayed under their respective labeled sections.

- [X] FT-06: Group members can ask questions and answer them in the discussion area.
  - Action: In a group's discussion area, post a question, then post a reply/answer to that question.
  - Expected: The question and the answer both appear in the discussion area, with the answer associated with the question.

- [X] FT-07: Members can schedule an upcoming group study session using a time selector.
  - Action: In a group, open "Schedule Session", pick a date and time using the provided time selector for a future date, and save.
  - Expected: The session is created and listed as an upcoming session showing its date and time.

- [ ] FT-08: Group members can RSVP to a scheduled study session.
  - Action: Open an upcoming group session and click "RSVP" / "I plan to attend".
  - Expected: The RSVP is recorded and the student's name appears in the session's attendee list.
  - Bug Report:
    - Issue: Missing Attendee List — RSVP'd Member Names Not Displayed
    - Actual: The RSVP is recorded (clicking "Attending" activates the button and the count immediately changes from "1 attending" to "2 attending" when a second member RSVPs), but the session card shows only counts ("N attending / N maybe"); no attendee list exists and the student's name never appears (the card DOM contains only "Organized by Alice Tester").

- [X] FT-09: A student can mark their profile as a mentor.
  - Action: Open profile settings and enable the "Mentor" option (available to advanced students/mentors), then save.
  - Expected: The profile is saved with mentor status, and the profile shows a mentor indicator.

- [X] FT-10: A group can invite a mentor, and the mentor can join the group.
  - Action: As a group member, use "Invite" to send an invitation to a profile marked as a mentor; then log in as that mentor and accept the invitation.
  - Expected: The invitation is sent to the mentor, and upon acceptance the mentor becomes a member of the group.

- [X] FT-11: A mentor in a group can highlight recommended resources.
  - Action: As a mentor member of a group, open the shared space and mark a resource/item as "Recommended" (highlight recommended resources).
  - Expected: The resource is saved and visibly highlighted as a recommended resource in the group's space.

- [X] FT-12: A mentor in a group can pin important posts.
  - Action: As a mentor member, select a post in the group's discussion or space and click "Pin".
  - Expected: The post is saved as pinned and remains associated with the group as a pinned item.

## Constraint

- [ ] CS-01: Account creation is rejected for invalid, duplicate, or missing registration data.
  - Action: Attempt to sign up with (a) an email already registered, (b) an invalid email format, and (c) a blank password field.
  - Expected: Each attempt is rejected with an error message; no new account is created for any of the three cases.
  - Bug Report:
    - Issue: Duplicate Registration Accepted — Missing Duplicate-Email Validation / Missing In-App Error Messages
    - Actual: Case (a) signing up with the already-registered email alice.tester@example.com succeeded — a second account ("Dup Tester") was created ("Welcome to StudyHub! Your account has been created."). Cases (b) and (c) were blocked only by the browser's native constraint validation (email/password input marked :invalid) with no in-app error message rendered; no accounts were created in those two cases.

- [ ] CS-02: A profile cannot be saved while required study fields are empty.
  - Action: Open profile setup, leave subjects, current level, or preferred study times empty, and click "Save".
  - Expected: Save is blocked with a validation message identifying the missing field; the profile is not updated.
  - Bug Report:
    - Issue: Missing Form Validation — Invalid Profile Saves Accepted
    - Actual: Saving with all subjects deselected succeeded ("Profile updated — Your changes have been saved."), and saving availability with zero study-time entries succeeded with the same success toast. No validation message identifies any missing field, and the profile is updated to the empty values (subject list cleared). (The level dropdown offers no empty option, so that sub-case could not be exercised.)

- [ ] CS-03: A study session cannot be scheduled without a time or in the past.
  - Action: Attempt to create a session (a) with no date/time selected and (b) with a date/time in the past.
  - Expected: Both attempts are rejected with an error; no invalid session appears in the upcoming sessions list.
  - Bug Report:
    - Issue: Missing Date Validation — Past-Dated Session Accepted
    - Actual: Attempt (a) with no date was rejected ("Please fill in all fields"), but attempt (b) with the past date 2026-11-07 was accepted with the success toast "Session scheduled!" and no error; the session was persisted (the group card count rose to "2 sessions"). It is correctly absent from the upcoming sessions list, but the past-dated attempt produced no rejection.

- [ ] CS-04: Non-mentor members cannot use mentor-only features.
  - Action: As a regular (non-mentor) group member, attempt to highlight recommended resources and to pin a post.
  - Expected: Both actions are unavailable or rejected; only mentor-role members can perform them.
  - Bug Report:
    - Issue: Broken Access Control — Mentor-Only Actions Not Restricted to Mentor Role
    - Actual: As a plain member (Alice in Calculus Champions) the pin/highlight controls are hidden (unavailable ✓), but as the group Owner — a non-mentor role — Alice successfully highlighted a resource (star icon became active, "text-accent") and pinned a post (pin icon became active, "text-primary") in Calculus Study Group, and both states persisted. A non-mentor member can therefore perform both mentor-only actions.

- [X] CS-05: A student cannot join the same group twice.
  - Action: As a student who is already a member of a group, view that group's page and attempt to join it again.
  - Expected: The "Join Group" action is not offered or is rejected; the member list shows the student only once.

## Interaction

- [ ] IX-01: The session time selector reflects member availability as it changes.
  - Action: Open the session scheduling time selector; have one member mark themselves available for a given time slot, then have another member mark themselves unavailable.
  - Expected: The list of who is available for each time slot updates immediately to include the available member and exclude the unavailable one.
  - Bug Report:
    - Issue: Missing Feature — No Member-Availability Display in Session Scheduling Time Selector
    - Actual: The "Schedule Session" time selector contains only Title, Description, Date, Start Time, and End Time fields — there is no list of who is available for any time slot and no way to mark availability from the selector (verified with a date selected and with 2 group members; no availability-related element exists in the dialog). The described interaction cannot be performed and no list ever updates.

- [ ] IX-02: RSVP and pin actions produce immediate visible state changes.
  - Action: RSVP to a session, and as a mentor pin a post in the group's space.
  - Expected: The attendee list immediately shows the RSVP-ing student, and the pinned post immediately displays a pin indicator / pinned placement within the group.
  - Bug Report:
    - Issue: Missing Attendee List on RSVP (Partial State Feedback)
    - Actual: The pin action immediately displays a pin indicator (pin icon turns active and persists), but RSVP changes only the attendance count ("1 attending" → "2 attending" immediately); no attendee list shows the RSVP-ing student's name anywhere in the session card.

## Content

- [X] CT-01: Displayed profile information matches exactly what the student saved.
  - Action: Save a profile with known subjects, current level, and preferred study times; then reopen the profile view.
  - Expected: The profile displays the same subjects, level, and preferred study times that were entered, with no missing or altered values.

- [ ] CT-02: Group pages show accurate labels, content, and session details.
  - Action: View a group's shared space, discussion area, and an upcoming session that has one RSVP.
  - Expected: Each item appears under its correct labeled section with its correct type (note / outline / reading summary), and the session shows the correct date, time, and the names of members who RSVP'd.
  - Bug Report:
    - Issue: Session Details Missing RSVP'd Member Names
    - Actual: Shared-space items appear under their labeled sections ("Lecture Notes", "Study Guides", "Summaries") and the session shows the correct date/time ("Sunday, November 15, 2026", "14:00 - 16:00"), but the session displays only RSVP counts ("1 attending / 0 maybe" → "2 attending") and never the names of members who RSVP'd (Alice Tester and Mia Mentor both RSVP'd; neither name appears). Additionally, items carry no explicit type label (note / outline / reading summary) — their kind is conveyed only by the chosen section/category.

---

**Summary:** 11 PASS / 10 FAIL. The most impactful defects: sign-up and group-creation forms fail silently when a required subject is omitted (no error message), registration accepts duplicate emails, profile/session forms accept invalid data (empty profile fields, past-dated sessions), the Owner role bypasses mentor-only restrictions, and — most consistently — the session UI lacks any attendee-name list and the scheduling time selector has no member-availability display at all.