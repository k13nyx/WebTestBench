# Test Result

## Functionality

- [X] FT-01: Student can create an account
  - Action: Open the account registration form, enter valid student details, and select **Create account**.
  - Expected: A student account is created and the student can access the platform.

- [X] FT-02: Student can create and save a study profile
  - Action: Enter at least one subject, a current level, and one preferred study time, then select **Save profile**.
  - Expected: The profile saves and displays the entered subjects, level, and preferred study times.

- [X] FT-03: Student can join an existing focused study group
  - Action: Browse the available groups, select a group focused on a topic such as calculus, biology, or literature, and select **Join group**.
  - Expected: The group appears in the student’s groups and its shared space is accessible.

- [X] FT-04: Student can create a focused study group
  - Action: Select **Create group**, enter a group name and study topic, and submit the form.
  - Expected: The new focused group is created and appears in the available or joined groups list.

- [ ] FT-05: Group members can organize shared study materials
  - Action: In a group’s shared space, create labeled sections and add a note, outline, and reading summary to the appropriate sections.
  - Expected: Each material is saved under its selected label and is visible to group members.
  - Bug Report:
    - Issue: Incomplete shared-material workflow
    - Actual: A note was successfully saved under the preset “Lecture Notes” category, but the test did not provide a workflow to create all requested labeled sections and save separate note, outline, and reading-summary materials.

- [ ] FT-06: Group members can ask and answer questions
  - Action: Post a question in the group discussion area, then use another group member account to submit an answer.
  - Expected: The question and answer appear in the running discussion area for group members.
  - Bug Report:
    - Issue: Multi-account collaboration not verified
    - Actual: The question and answer appeared, but both were submitted using the same student account rather than another group member account.

- [X] FT-07: Group member can schedule an upcoming study session
  - Action: Select **Schedule study session**, choose a future date and time using the time selector, and submit the session.
  - Expected: The upcoming session appears in the group’s scheduled sessions list with its selected date and time.

- [X] FT-08: Group member can RSVP to a scheduled session
  - Action: Open an upcoming study session and select **RSVP** or the equivalent attendance control.
  - Expected: The student’s attendance status is recorded and the session shows the student as planning to attend.

- [X] FT-09: Student can mark their profile as a mentor
  - Action: Open profile settings, enable the **Mentor** profile option, and save the profile.
  - Expected: The profile visibly identifies the student as a mentor.

- [ ] FT-10: Group can invite a mentor and the mentor can join
  - Action: From a group, select **Invite mentor**, choose a student marked as a mentor, and accept the invitation from that mentor account.
  - Expected: The mentor becomes a group member and is displayed with a distinct mentor role.
  - Bug Report:
    - Issue: Missing mentor invitation workflow
    - Actual: No **Invite mentor** control or mentor invitation workflow was available in the group or member views, so a mentor could not be invited or accept an invitation.

- [ ] FT-11: Mentor can recommend resources and pin important posts
  - Action: As a group mentor, mark a study resource as recommended and pin an important discussion post.
  - Expected: The resource is visibly marked as recommended and the post is visibly pinned for group members.
  - Bug Report:
    - Issue: Missing mentor content controls
    - Actual: No controls for marking resources as recommended or pinning discussion posts were available, including while signed in as a mentor.

## Constraint

- [X] CS-01: Required account and profile information is enforced
  - Action: Submit account registration or profile setup with one required field left empty.
  - Expected: Submission is blocked and the missing field is clearly identified.

- [X] CS-02: Shared materials require a labeled section
  - Action: Attempt to save a note, outline, or reading summary without selecting or entering a section label.
  - Expected: The material is not saved and the interface identifies that a labeled section is required.

- [X] CS-03: A student cannot RSVP to the same session more than once
  - Action: RSVP to one scheduled session, then attempt to RSVP to that same session again.
  - Expected: The session records only one RSVP for the student and does not create a duplicate attendance entry.

- [ ] CS-04: Mentor-only group actions are restricted by role
  - Action: As a regular student, attempt to mark a resource as recommended or pin a discussion post.
  - Expected: The mentor-only controls are unavailable or the action is rejected, and no recommendation or pin is created.
  - Bug Report:
    - Issue: Mentor-only restriction could not be verified
    - Actual: No recommendation or pin controls were present anywhere in the tested group interface, so the regular-student rejection behavior could not be exercised or confirmed.

- [ ] CS-05: Scheduled sessions must be upcoming
  - Action: Use the session scheduler to attempt to submit a date and time in the past.
  - Expected: The session cannot be scheduled and the invalid past date or time is identified.
  - Bug Report:
    - Issue: Past session accepted
    - Actual: Submitting a session dated `2020-01-01` displayed “Session scheduled!” instead of rejecting the past date and identifying it as invalid.

## Interaction

- [ ] IX-01: Time selection displays member availability
  - Action: Open the study-session time selector and choose different available date and time options.
  - Expected: The interface updates to show which group members have marked themselves available for the selected time.
  - Bug Report:
    - Issue: Member availability is not displayed
    - Actual: The scheduler provided date, start-time, and end-time fields, but did not show which group members were available for the selected date and time.

- [X] IX-02: RSVP state updates the session attendance display
  - Action: RSVP to an upcoming session, then change the RSVP status if a change option is provided.
  - Expected: The RSVP control and attendee list update immediately to reflect the current attendance status.

- [ ] IX-03: Mentor status changes the visible group role
  - Action: Open a group member list containing a joined mentor.
  - Expected: The mentor has a distinct visible role indicator and mentor-specific actions are presented only to that mentor.
  - Bug Report:
    - Issue: Mentor-specific actions are missing
    - Actual: The member list visibly labeled an existing mentor, but no mentor-specific actions were presented.

- [ ] IX-04: Pinned posts remain visually identifiable
  - Action: Pin a discussion post as a mentor, then navigate away from and back to the discussion area.
  - Expected: The post remains visibly marked as pinned after returning to the discussion area.
  - Bug Report:
    - Issue: Pinning workflow unavailable
    - Actual: No pin control was available on discussion posts, so a pinned post could not be created or verified after navigation.

## Content

- [X] CT-01: Group topics and labels are relevant to study collaboration
  - Action: Review the group list, group names, topics, and shared-space section labels.
  - Expected: Group content is clearly associated with academic subjects such as calculus, biology, literature, or another identifiable study topic.

- [X] CT-02: Profile content accurately represents student study preferences
  - Action: Review a saved student profile.
  - Expected: The displayed subjects, current level, preferred study times, and mentor status match the information entered by that student.

- [ ] CT-03: Recommended resources and pinned posts are clearly distinguished
  - Action: Review a group’s shared space and discussion area after a mentor has marked content.
  - Expected: Recommended resources and pinned posts have clear labels or indicators that distinguish them from ordinary content.
  - Bug Report:
    - Issue: Recommended and pinned content indicators are missing
    - Actual: No workflow or visible labels for recommended resources or pinned discussion posts were available in the group’s shared space or discussion area.