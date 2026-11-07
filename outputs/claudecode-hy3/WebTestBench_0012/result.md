I have reached the tool-call budget limit. Based on all executed interactions, here is the complete test report.

# Test Result

## Functionality

- [X] FT-01: Student can create a new account
  - Action: Open the sign-up screen and submit a valid email, password, and display name.
  - Expected: A new student account is created and the user is logged in / redirected to the app home.
  - Result: PASS — Account created; redirected to `/profile` with "Welcome to StudyHub! Your account has been created."

- [X] FT-02: Student can set up a profile with subjects, level, and study times
  - Action: On the profile setup screen, select subjects, set current level, and choose preferred study times, then save.
  - Expected: The profile is saved and the selected subjects, level, and study times are displayed on the profile.
  - Result: PASS — Subjects render as selected (`bg-primary` filled chips: Mathematics, Computer Science, Physics after selecting/saving), level "undergraduate" shown in the profile header, and study times (monday/wednesday/saturday) displayed under the Availability tab.

- [X] FT-03: Student can create a focused study group around a topic
  - Action: Click "Create Group", enter a topic (e.g., Calculus), and confirm.
  - Expected: A new study group is created and appears in the list of available groups.
  - Result: PASS — "Group created!"; "Quantum Physics Study" (Physics) appears in "Your Groups".

- [X] FT-04: Student can join an existing study group
  - Action: Open an existing study group and click "Join Group".
  - Expected: The student becomes a member and the group appears in "My Groups".
  - Result: PASS — "Joined group!"; Biology Study Circle moved from Discover to "Your Groups" with Alex Chen in the member avatars.

- [X] FT-05: Members can organize notes, outlines, and summaries into labeled sections
  - Action: In the group's shared space, create a labeled section and add a note, an outline, and a reading summary.
  - Expected: The entries are saved under the correct labeled section and are visible to group members.
  - Result: PASS — Three entries saved under three labeled categories: Lecture Notes ("Wave-Particle Duality"), Study Guides ("Chapter 1 Outline"), and Summaries ("Reading Summary: Feynman Lectures"); all visible.

- [X] FT-06: Members can post questions and answers in the discussion area
  - Action: In the group discussion area, post a question, then reply with an answer.
  - Expected: Both the question and the answer appear in the running discussion thread.
  - Result: PASS — "Discussion started!" for "What is wavefunction collapse?" and the answer reply appears beneath it in the thread.

- [X] FT-07: Members can schedule a study session with the time selector
  - Action: Open the schedule view and use the time selector to pick a date/time, then save the session.
  - Expected: A new upcoming session is created and listed for the group.
  - Result: PASS — "Session scheduled!"; "Midterm Exam Review" (Sun Nov 15, 2026, 14:00–16:00) listed in Sessions.

- [X] FT-08: Members can mark availability and RSVP for a session
  - Action: Open an upcoming session and click "Mark Available" / "RSVP".
  - Expected: The member is marked as planning to attend and is added to the session's attendance list.
  - Result: PASS — Clicking "Attending" produced "RSVP updated!"; the button became active and attendance showed "1 attending".

- [X] FT-09: Advanced students can mark their profile as a mentor
  - Action: On the profile screen, toggle/enable the "Mentor" option and save.
  - Expected: The profile is flagged as a mentor with the mentor role applied.
  - Result: PASS — Alex Chen's profile shows the Mentor Status checkbox checked and a distinct "Mentor" badge in the profile header and avatar menu (mentor role applied).

- [ ] FT-10: A group can invite a mentor to join
  - Action: In the group, use "Invite Mentor" and select an available mentor profile.
  - Expected: The mentor receives the invite and can join the group with mentor status.
  - Bug Report:
    - Issue: Invited mentor joins with regular "member" status instead of "mentor" status.
    - Actual: After inviting Dr. Emily Wong (a mentor) and her joining via "Join Group", the Members list shows her role as "member" (Alex Chen retains "mentor"). The invite is delivered ("Invitation sent!") and she can join, but the expected mentor status on join is not applied.

- [X] FT-11: Mentors can highlight recommended resources
  - Action: As a mentor, mark a resource/post as "Recommended".
  - Expected: The resource is highlighted as a recommended resource in the group space.
  - Result: PASS — As mentor Alex, the note's star/Recommend icon (`lucide-star`) toggles to active, marking the resource as recommended.

- [X] FT-12: Mentors can pin important posts
  - Action: As a mentor, use the "Pin" action on an important post.
  - Expected: The post is pinned and remains at the top of the group's space/discussion.
  - Result: PASS — As mentor Alex, the pin icon (`lucide-pin`) toggles active and the pinned note reorders toward the top of the notes list.

## Constraint

- [ ] CS-01: Account creation requires valid, unique required fields
  - Action: Attempt to sign up with an invalid email or a blank required field.
  - Expected: Submission is blocked and a validation error names the invalid/required field.
  - Bug Report:
    - Issue: Submission is blocked but no validation error message names the invalid/required field.
    - Actual: Submitting the form with invalid email ("not-a-valid-email"), blank Full Name, and no subject selected was blocked (stayed on /signup, no account created), but no error text was shown; the form only refocused the first empty field.

- [X] CS-02: A study session cannot be scheduled without a selected time
  - Action: Open the schedule view and click save without choosing a time on the selector.
  - Expected: The session is not created and an error states a time must be selected.
  - Result: PASS — Clicking "Schedule Session" with an empty date produced "Please fill in all fields" and no session was created (dialog stayed open).

- [ ] CS-03: Only mentors may pin posts and highlight resources
  - Action: As a regular (non-mentor) member, attempt to pin a post or mark a resource as recommended.
  - Expected: The actions are disabled or blocked; only mentor accounts can perform them.
  - Bug Report:
    - Issue: Non-mentor restriction could not be independently verified within the tool-call budget.
    - Actual: Testing was halted at the 100-call budget limit before a non-mentor account could be created/logged in to confirm the pin/recommend actions are disabled. Mentor-only actions (pin/star) were confirmed available to mentors (Alex, Emily); the non-mentor restriction itself was not exercised.

## Interaction

- [ ] IX-01: Time selector shows who has marked themselves available
  - Action: Open a session's time selector after members mark availability.
  - Expected: The selector/availability view displays the names or avatars of members who marked available.
  - Bug Report:
    - Issue: Availability is shown only as a numeric count, not as member names or avatars.
    - Actual: After a member RSVP'd "Attending", the session's availability/attendance area displayed only "1 attending" / "0 maybe" — no names or avatars of the members who marked available were shown.

- [X] IX-02: RSVP and availability changes update live for the group
  - Action: As one member, RSVP/mark available, then view the session from another member's account.
  - Expected: The updated attendance/availability list is immediately visible to all group members.
  - Result: PASS — Logged in as Dr. Emily Wong (a separate account), the Sessions tab of the shared group showed Alex's "Midterm Exam Review" session with "1 attending" (Alex's RSVP), confirming the RSVP is visible cross-account in the shared store.

## Content

- [X] CT-01: Study group topics are relevant and correctly labeled
  - Action: Browse the list of available groups and open a few group topics.
  - Expected: Each group shows a study-relevant topic (e.g., Calculus, Biology, Literature) with no off-topic or empty groups.
  - Result: PASS — Groups observed: Calculus Champions (Mathematics), Biology Study Circle (Biology), Victorian Literature Society (Literature), Quantum Physics Study (Physics) — all study-relevant, none empty/off-topic.

- [X] CT-02: Mentor role is visually distinguished from regular members
  - Action: View a group's member list containing a mentor and regular members.
  - Expected: The mentor is clearly marked with a distinct mentor label/badge different from regular members.
  - Result: PASS — In Calculus Champions' Members tab, Alex Chen shows a distinct "mentor" badge, Sarah Martinez shows "member", and Marcus Johnson shows "owner" — clearly differentiated.