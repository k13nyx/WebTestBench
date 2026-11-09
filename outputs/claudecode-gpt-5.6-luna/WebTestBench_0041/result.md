# Test Result

## Functionality

- [X] FT-01: View all default smart home devices in the admin dashboard.
  - Action: Open the admin dashboard.
  - Expected: Every default device is displayed with enough information to identify it.

- [X] FT-02: Group or filter devices by room.
  - Action: Select a room from the room view or room filter.
  - Expected: Only devices assigned to the selected room are shown.

- [X] FT-03: Group or filter devices by device type.
  - Action: Select a device type such as light or thermostat.
  - Expected: Only devices of the selected type are shown.

- [X] FT-04: Adjust a light’s brightness.
  - Action: Select a default light and change its brightness setting.
  - Expected: The light displays the newly selected brightness value.

- [X] FT-05: Adjust a thermostat’s target temperature.
  - Action: Select a default thermostat and change its target temperature.
  - Expected: The thermostat displays the newly selected target temperature.

- [X] FT-06: Create a schedule for a light to change state.
  - Action: Open the scheduling controls, select a default light, specify a valid time and state change, and save the schedule.
  - Expected: The saved light schedule appears in the schedule list with the selected device, time, and state change.

- [X] FT-07: Create a schedule for a thermostat to change state.
  - Action: Open the scheduling controls, select a default thermostat, specify a valid time and target change, and save the schedule.
  - Expected: The saved thermostat schedule appears in the schedule list with the selected device, time, and target change.

- [X] FT-08: View recent device activity.
  - Action: Open the recent activity panel or section.
  - Expected: Recent device events are listed, including the affected device and when it was used or changed.

- [X] FT-09: Filter devices by Offline status.
  - Action: Select the `Offline` status filter.
  - Expected: Only devices currently marked `Offline` are displayed.

- [X] FT-10: Filter devices by Idle status.
  - Action: Select the `Idle` status filter.
  - Expected: Only devices currently marked `Idle` are displayed.

## Constraint

- [ ] CS-01: Prevent saving an incomplete schedule.
  - Action: Open the schedule form, leave one required field such as device, time, or state change empty, and select `Save`.
  - Expected: The schedule is not saved and the missing field is identified for correction.
  - Bug Report:
    - Issue: Missing required-field validation
    - Actual: Selecting `Create Schedule` with all fields empty left the dialog open and did not save a schedule, but no missing field or validation message was identified for correction.

- [X] CS-02: Keep brightness within the control’s supported range.
  - Action: Attempt to set a light’s brightness below its minimum or above its maximum.
  - Expected: The dashboard does not accept or display a brightness value outside the supported range.

- [X] CS-03: Keep thermostat targets within the control’s supported range.
  - Action: Attempt to set a thermostat target below its minimum or above its maximum.
  - Expected: The dashboard does not accept or display a target temperature outside the supported range.

## Interaction

- [X] IX-01: Update device settings immediately after a valid change.
  - Action: Change a light brightness or thermostat target temperature and wait for the operation to complete.
  - Expected: The device card or control reflects the new setting without requiring a page refresh.

- [ ] IX-02: Confirm successful schedule creation.
  - Action: Save a valid light or thermostat schedule.
  - Expected: A visible confirmation appears, and the new schedule is shown in the schedule list.
  - Bug Report:
    - Issue: Missing schedule creation confirmation
    - Actual: The new schedule appeared in the schedule list, but no visible success confirmation or notification appeared after saving.

- [X] IX-03: Refresh results when room, type, or status filters change.
  - Action: Apply a room, device-type, or status filter, then change to a different filter.
  - Expected: The displayed device list updates to match the newly selected filter without showing devices excluded by it.

## Content

- [ ] CT-01: Display complete and relevant device information.
  - Action: Inspect the default device cards or rows.
  - Expected: Each device identifies its name, room, device type, and current status; all values correspond to that device.
  - Bug Report:
    - Issue: Device type is not explicitly displayed
    - Actual: Device cards displayed the device name, room, and status, but did not provide an explicit textual device-type value; the type was only implied by the icon and available controls.

- [X] CT-02: Display meaningful recent-activity details.
  - Action: Inspect entries in the recent activity section.
  - Expected: Each entry identifies the relevant device, the activity performed, and a usable date or time, including the device’s last-used information where available.