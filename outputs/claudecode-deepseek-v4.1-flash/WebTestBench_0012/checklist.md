# Test Checklist

## Functionality
- [ ] FT-01: Student can create a new account.
  - Action: Open sign-up, enter valid credentials, submit.
  - Expected: Account is created and the user is signed in.

- [ ] FT-02: Student can set up a profile with subjects, current level, and preferred study times.
  - Action: Edit profile; add at least one subject, a level, and preferred study times; save.
  - Expected: Profile saves and displays the entered subjects, level, and study times.

- [ ] FT-03: Student can create a study group around a topic.
  - Action: Create a group for a topic (e.g., Calculus, Biology, or Literature).
  - Expected: A new group is created and appears in the group list with its topic.

- [ ] FT-04: Student can join an existing study group.
  - Action: Open an existing group and select "Join".
  - Expected: User becomes a member and gains access to the group's shared space and discussion.

- [ ] FT-05: Group shared space organizes notes, outlines, and reading summaries into labeled sections.
  - Action: Open a group's shared space and add a note, an outline, and a reading summary.
  - Expected: Each item is stored under its corresponding labeled section.

- [ ] FT-06: Group discussion area supports posting questions and answers.
  - Action: Post a question in the group discussion, then post a reply.
  - Expected: The question and its reply appear in the running discussion thread.

- [ ] FT-07: Student can schedule an upcoming group study session with a time selector.
  - Action: Create a session using the time selector and confirm.
  - Expected: The session is added to the group's upcoming sessions with the selected time.

- [ ] FT-08: Group member can RSVP to an upcoming session.
  - Action: Open an upcoming session and select an RSVP option.
  - Expected: The member's RSVP is recorded and shown on the session.

- [ ] FT-09: Mentors can mark their profile as a mentor.
  - Action: On the profile, enable the "mentor" option and save.
  - Expected: The profile is marked as a mentor and shows the mentor role.

- [ ] FT-10: A group can invite a mentor to join.
  - Action: From the group, invite a mentor-marked user.
  - Expected: The mentor receives the invite and, on joining, is added with the mentor role.

- [ ] FT-11: Mentors can highlight recommended resources and pin important posts.
  - Action: As a mentor, highlight a resource and pin a discussion post.
  - Expected: The resource is marked as recommended and the post stays pinned at the top of the discussion.

## Constraint
- [ ] CS-01: Account/profile cannot be saved with required fields empty.
  - Action: Submit sign-up or profile with a required field (e.g., subjects or level) left blank.
  - Expected: Submission is blocked with a validation message; no data is saved.

- [ ] CS-02: Session availability shows only members who marked themselves available.
  - Action: Mark yourself available for a session while another member does not.
  - Expected: Only members who marked available appear in the availability list.

- [ ] CS-03: Pinning and highlighting are restricted to the mentor role.
  - Action: As a non-mentor member, attempt to pin a post or highlight a resource.
  - Expected: The action is unavailable/denied for non-mentors.

## Interaction
- [ ] IX-01: Time selector updates the available-members display.
  - Action: Change the selected time in the session time selector.
  - Expected: The list of members marked as available updates to match the selected time.

- [ ] IX-02: System confirms RSVP and account/profile actions.
  - Action: Submit an RSVP (and complete sign-up).
  - Expected: A success confirmation/toast appears after each action.

- [ ] IX-03: Mentor role is visually distinguished from regular members.
  - Action: View a group containing a mentor alongside regular members.
  - Expected: The mentor is shown with a distinct role indicator/label.

## Content
- [ ] CT-01: Group topics align with study themes.
  - Action: Browse existing groups.
  - Expected: Topics displayed are study-related (e.g., calculus, biology, literature).

- [ ] CT-02: Shared-space section labels match notes, outlines, and reading summaries.
  - Action: Open the shared space of a group.
  - Expected: Sections are labeled for notes, outlines, and reading summaries.

- [ ] CT-03: Mentor-highlighted content is relevant recommended material.
  - Action: View a mentor's highlighted resources and pinned posts in a group.
  - Expected: Highlighted items are study resources and pinned posts are important group content.