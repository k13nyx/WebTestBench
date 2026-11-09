# Test Checklist

## Functionality
- [ ] FT-01: View devices grouped by room
  - Action: Select the "View by Room" option on the dashboard.
  - Expected: Devices are grouped/listed under their respective room names (e.g., Living Room, Bedroom, Kitchen).

- [ ] FT-02: View devices by device type
  - Action: Select a device type filter (e.g., "Lights" or "Thermostats").
  - Expected: Only devices matching the selected type are displayed.

- [ ] FT-03: Adjust brightness on a light device
  - Action: Open a light device, change the brightness value, and save.
  - Expected: The new brightness value is saved and reflected on the device card.

- [ ] FT-04: Adjust target temperature on a thermostat
  - Action: Open a thermostat device, change the target temperature, and save.
  - Expected: The new target temperature is saved and reflected on the device card.

- [ ] FT-05: Create a schedule for a light
  - Action: Open the schedules section, create a new schedule for a light with a start time and a state change (on/off), and save.
  - Expected: The new schedule appears in the schedules list.

- [ ] FT-06: Create a schedule for a thermostat
  - Action: Open the schedules section, create a new schedule for a thermostat with a start time and a target temperature, and save.
  - Expected: The new schedule appears in the schedules list.

- [ ] FT-07: View recent activity with last-used timestamps
  - Action: Navigate to the "Recent Activity" panel.
  - Expected: A list of device activities is shown, each entry indicating when the device was last used.

- [ ] FT-08: Filter devices by "Offline" status
  - Action: Apply the "Offline" status filter.
  - Expected: Only devices whose current status is offline are displayed.

- [ ] FT-09: Filter devices by "Idle" status
  - Action: Apply the "Idle" status filter.
  - Expected: Only devices whose current status is idle are displayed.

## Constraint
- [ ] CS-01: Brightness value must be within 0–100%
  - Action: Enter a brightness value below 0 or above 100 and attempt to save.
  - Expected: Save is rejected with a validation message indicating the valid range (0–100%).

- [ ] CS-02: Target temperature must be within a valid range
  - Action: Enter a target temperature below the device's minimum or above its maximum and attempt to save.
  - Expected: Save is rejected with a validation message indicating the valid range.

- [ ] CS-03: Schedule cannot be saved with missing required fields
  - Action: Open the schedule form, leave one or more required fields (device, time, action/state) empty, and attempt to save.
  - Expected: Save is blocked and an error indicates which required fields are missing.

- [ ] CS-04: Schedule end time must not precede start time
  - Action: Create a schedule where the end time is earlier than the start time and attempt to save.
  - Expected: Save is rejected with a time-validation error.

## Interaction
- [ ] IX-01: Active status filter is visually indicated
  - Action: Apply any status filter (e.g., "Offline" or "Idle").
  - Expected: The selected filter is visually highlighted/active in the filter UI so the user can see which filter is applied.

- [ ] IX-02: Successful setting change shows confirmation feedback
  - Action: Save a successful change to a device's brightness or target temperature.
  - Expected: A success message, toast, or on-screen confirmation appears indicating the change was saved.

- [ ] IX-03: Successful schedule creation shows confirmation feedback
  - Action: Save a successfully created schedule.
  - Expected: A success message or visual confirmation appears and the new schedule appears in the list without a page reload.

## Content
- [ ] CT-01: Each device displays its assigned room name
  - Action: View the device list/grid.
  - Expected: Every device card shows the name of the room it is assigned to.

- [ ] CT-02: Recent activity entries include device name and timestamp
  - Action: View entries in the "Recent Activity" panel.
  - Expected: Each entry shows the device name and a date/time of last activity.

- [ ] CT-03: Status filter options include "offline" and "idle"
  - Action: Open the status filter selector.
  - Expected: The available filter options include the labels "Offline" and "Idle".