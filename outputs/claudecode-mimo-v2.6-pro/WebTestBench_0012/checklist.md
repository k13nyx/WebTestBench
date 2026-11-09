# Test Checklist

## Functionality
- [ ] FT-01: Student can create an account and log in with the new credentials.
  - Action: On the sign-up page, fill in name, email, and password, submit the form, then log out and log back in with the same email/password.
  - Expected: Account is created, login succeeds, and the student lands on the main dashboard.

- [ ] FT-02: Student can set up a profile with subjects, current level, and preferred study times.
  - Action: Open the profile setup page, select subjects (e.g., calculus, biology), choose a current level (e.g., undergraduate), select preferred study times (e.g., weekday evenings), and save.
  - Expected: Profile saves successfully and the selected subjects, level, and study times are recorded on the profile.

- [ ] FT-03: Student can create a focused study group around a topic.
  - Action: Click "Create Group", enter a group name and topic (e.g., "Calculus Study Group – Calculus"), and submit.
  - Expected: The group is created and appears in the group list, with the creator as a member.

- [ ] FT-04: Student can join an existing study group.
  - Action: From the group list, open a group the student is not a member of and click "Join Group".
  - Expected: The student becomes a member and gains access to that group's shared space, discussion, and sessions.

- [ ] FT-05: Group members can add notes, outlines, and reading summaries into labeled sections of the shared space.
  - Action: In a group's shared space, add one note, one outline, and one reading summary, each placed into a labeled section (e.g., "Notes", "Outlines", "Reading Summaries").
  - Expected: All three items are saved and displayed under their respective labeled sections.

- [ ] FT-06: Group members can ask questions and answer them in the discussion area.
  - Action: In a group's discussion area, post a question, then post a reply/answer to that question.
  - Expected: The question and the answer both appear in the discussion area, with the answer associated with the question.

- [ ] FT-07: Members can schedule an upcoming group study session using a time selector.
  - Action: In a group, open "Schedule Session", pick a date and time using the provided time selector for a future date, and save.
  - Expected: The session is created and listed as an upcoming session showing its date and time.

- [ ] FT-08: Group members can RSVP to a scheduled study session.
  - Action: Open an upcoming group session and click "RSVP" / "I plan to attend".
  - Expected: The RSVP is recorded and the student's name appears in the session's attendee list.

- [ ] FT-09: A student can mark their profile as a mentor.
  - Action: Open profile settings and enable the "Mentor" option (available to advanced students/mentors), then save.
  - Expected: The profile is saved with mentor status, and the profile shows a mentor indicator.

- [ ] FT-10: A group can invite a mentor, and the mentor can join the group.
  - Action: As a group member, use "Invite" to send an invitation to a profile marked as a mentor; then log in as that mentor and accept the invitation.
  - Expected: The invitation is sent to the mentor, and upon acceptance the mentor becomes a member of the group.

- [ ] FT-11: A mentor in a group can highlight recommended resources.
  - Action: As a mentor member of a group, open the shared space and mark a resource/item as "Recommended" (highlight recommended resources).
  - Expected: The resource is saved and visibly highlighted as a recommended resource in the group's space.

- [ ] FT-12: A mentor in a group can pin important posts.
  - Action: As a mentor member, select a post in the group's discussion or space and click "Pin".
  - Expected: The post is saved as pinned and remains associated with the group as a pinned item.

## Constraint
- [ ] CS-01: Account creation is rejected for invalid, duplicate, or missing registration data.
  - Action: Attempt to sign up with (a) an email already registered, (b) an invalid email format, and (c) a blank password field.
  - Expected: Each attempt is rejected with an error message; no new account is created for any of the three cases.

- [ ] CS-02: A profile cannot be saved while required study fields are empty.
  - Action: Open profile setup, leave subjects, current level, or preferred study times empty, and click "Save".
  - Expected: Save is blocked with a validation message identifying the missing field; the profile is not updated.

- [ ] CS-03: A study session cannot be scheduled without a time or in the past.
  - Action: Attempt to create a session (a) with no date/time selected and (b) with a date/time in the past.
  - Expected: Both attempts are rejected with an error; no invalid session appears in the upcoming sessions list.

- [ ] CS-04: Non-mentor members cannot use mentor-only features.
  - Action: As a regular (non-mentor) group member, attempt to highlight recommended resources and to pin a post.
  - Expected: Both actions are unavailable or rejected; only mentor-role members can perform them.

- [ ] CS-05: A student cannot join the same group twice.
  - Action: As a student who is already a member of a group, view that group's page and attempt to join it again.
  - Expected: The "Join Group" action is not offered or is rejected; the member list shows the student only once.

## Interaction
- [ ] IX-01: The session time selector reflects member availability as it changes.
  - Action: Open the session scheduling time selector; have one member mark themselves available for a given time slot, then have another member mark themselves unavailable.
  - Expected: The list of who is available for each time slot updates immediately to include the available member and exclude the unavailable one.

- [ ] IX-02: RSVP and pin actions produce immediate visible state changes.
  - Action: RSVP to a session, and as a mentor pin a post in the group's space.
  - Expected: The attendee list immediately shows the RSVP-ing student, and the pinned post immediately displays a pin indicator / pinned placement within the group.

## Content
- [ ] CT-01: Displayed profile information matches exactly what the student saved.
  - Action: Save a profile with known subjects, current level, and preferred study times; then reopen the profile view.
  - Expected: The profile displays the same subjects, level, and preferred study times that were entered, with no missing or altered values.

- [ ] CT-02: Group pages show accurate labels, content, and session details.
  - Action: View a group's shared space, discussion area, and an upcoming session that has one RSVP.
  - Expected: Each item appears under its correct labeled section with its correct type (note / outline / reading summary), and the session shows the correct date, time, and the names of members who RSVP'd.