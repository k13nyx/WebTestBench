# Test Checklist

## Functionality
- [ ] FT-01: Student can create a new account
  - Action: Open the sign-up screen and submit a valid email, password, and display name.
  - Expected: A new student account is created and the user is logged in / redirected to the app home.

- [ ] FT-02: Student can set up a profile with subjects, level, and study times
  - Action: On the profile setup screen, select subjects, set current level, and choose preferred study times, then save.
  - Expected: The profile is saved and the selected subjects, level, and study times are displayed on the profile.

- [ ] FT-03: Student can create a focused study group around a topic
  - Action: Click "Create Group", enter a topic (e.g., Calculus), and confirm.
  - Expected: A new study group is created and appears in the list of available groups.

- [ ] FT-04: Student can join an existing study group
  - Action: Open an existing study group and click "Join Group".
  - Expected: The student becomes a member and the group appears in "My Groups".

- [ ] FT-05: Members can organize notes, outlines, and summaries into labeled sections
  - Action: In the group's shared space, create a labeled section and add a note, an outline, and a reading summary.
  - Expected: The entries are saved under the correct labeled section and are visible to group members.

- [ ] FT-06: Members can post questions and answers in the discussion area
  - Action: In the group discussion area, post a question, then reply with an answer.
  - Expected: Both the question and the answer appear in the running discussion thread.

- [ ] FT-07: Members can schedule a study session with the time selector
  - Action: Open the schedule view and use the time selector to pick a date/time, then save the session.
  - Expected: A new upcoming session is created and listed for the group.

- [ ] FT-08: Members can mark availability and RSVP for a session
  - Action: Open an upcoming session and click "Mark Available" / "RSVP".
  - Expected: The member is marked as planning to attend and is added to the session's attendance list.

- [ ] FT-09: Advanced students can mark their profile as a mentor
  - Action: On the profile screen, toggle/enable the "Mentor" option and save.
  - Expected: The profile is flagged as a mentor with the mentor role applied.

- [ ] FT-10: A group can invite a mentor to join
  - Action: In the group, use "Invite Mentor" and select an available mentor profile.
  - Expected: The mentor receives the invite and can join the group with mentor status.

- [ ] FT-11: Mentors can highlight recommended resources
  - Action: As a mentor, mark a resource/post as "Recommended".
  - Expected: The resource is highlighted as a recommended resource in the group space.

- [ ] FT-12: Mentors can pin important posts
  - Action: As a mentor, use the "Pin" action on an important post.
  - Expected: The post is pinned and remains at the top of the group's space/discussion.

## Constraint
- [ ] CS-01: Account creation requires valid, unique required fields
  - Action: Attempt to sign up with an invalid email or a blank required field.
  - Expected: Submission is blocked and a validation error names the invalid/required field.

- [ ] CS-02: A study session cannot be scheduled without a selected time
  - Action: Open the schedule view and click save without choosing a time on the selector.
  - Expected: The session is not created and an error states a time must be selected.

- [ ] CS-03: Only mentors may pin posts and highlight resources
  - Action: As a regular (non-mentor) member, attempt to pin a post or mark a resource as recommended.
  - Expected: The actions are disabled or blocked; only mentor accounts can perform them.

## Interaction
- [ ] IX-01: Time selector shows who has marked themselves available
  - Action: Open a session's time selector after members mark availability.
  - Expected: The selector/availability view displays the names or avatars of members who marked available.

- [ ] IX-02: RSVP and availability changes update live for the group
  - Action: As one member, RSVP/mark available, then view the session from another member's account.
  - Expected: The updated attendance/availability list is immediately visible to all group members.

## Content
- [ ] CT-01: Study group topics are relevant and correctly labeled
  - Action: Browse the list of available groups and open a few group topics.
  - Expected: Each group shows a study-relevant topic (e.g., Calculus, Biology, Literature) with no off-topic or empty groups.

- [ ] CT-02: Mentor role is visually distinguished from regular members
  - Action: View a group's member list containing a mentor and regular members.
  - Expected: The mentor is clearly marked with a distinct mentor label/badge different from regular members.