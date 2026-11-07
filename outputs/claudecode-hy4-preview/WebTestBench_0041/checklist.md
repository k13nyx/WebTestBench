# Test Checklist

## Functionality
- [ ] FT-01: Dashboard displays the full inventory of smart home devices
  - Action: Open the admin dashboard and read the main device list.
  - Expected: Every default device is listed, each row showing its name, room, device type (e.g. light, thermostat), and current status. No device is missing.

- [ ] FT-02: Devices can be viewed grouped by room
  - Action: Select the "By Room" view/grouping option, then expand or select a room such as "Living Room".
  - Expected: All devices assigned to that room are shown under it; devices from other rooms are not shown under that room. Every room present in the data is listed.

- [ ] FT-03: Devices can be viewed filtered by device type
  - Action: Use the device type filter and select "Lights" (then repeat with "Thermostats").
  - Expected: Only devices of the selected type are displayed; selecting "Thermostats" shows only thermostats.

- [ ] FT-04: Brightness of a light device can be adjusted and applied
  - Action: Open an online light device and set its brightness to a new valid value (e.g. 40%), then save/apply.
  - Expected: The device's displayed brightness value changes to 40% and persists after re-opening the device.

- [ ] FT-05: Target temperature of a thermostat can be adjusted and applied
  - Action: Open an online thermostat and change its target temperature to a new valid value (e.g. 22°C), then save/apply.
  - Expected: The thermostat's displayed target temperature updates to 22°C and persists after re-opening the device.

- [ ] FT-06: A schedule can be created for a light
  - Action: Open a light device, choose "Add Schedule", set a time (e.g. 18:00) and an action (turn on), then save.
  - Expected: The new schedule is saved and appears in that device's schedule list with the correct time and action.

- [ ] FT-07: A schedule can be created for a thermostat
  - Action: Open a thermostat, choose "Add Schedule", set a time (e.g. 22:00), a target temperature/action, then save.
  - Expected: The new schedule is saved and appears in the thermostat's schedule list with the correct time and target state.

- [ ] FT-08: Recent activity shows when each device was last used
  - Action: Open the "Recent Activity" panel on the dashboard.
  - Expected: The panel lists activity entries that include the device name and a last-used time (timestamp or relative time such as "2 hours ago") for default devices.

## Constraint
- [ ] CS-01: Status filter "Offline" shows only offline devices
  - Action: Apply the status filter and select "Offline".
  - Expected: Every displayed device has status "Offline"; no online or idle device appears in the list.

- [ ] CS-02: Status filter "Idle" shows only idle devices
  - Action: Apply the status filter and select "Idle".
  - Expected: Every displayed device has status "Idle"; no online or offline device appears in the list.

- [ ] CS-03: Brightness is restricted to the valid range
  - Action: Open a light device and attempt to set brightness to 150% (and to a negative value), then save.
  - Expected: The out-of-range value is rejected — either blocked from entry or refused on save with a validation message — and the device brightness remains unchanged.

- [ ] CS-04: Incomplete schedules cannot be saved
  - Action: Open "Add Schedule" for a device and attempt to save without specifying a time and without specifying an action/state.
  - Expected: Save is blocked and a validation message is shown; no schedule is added to the device's schedule list.

- [ ] CS-05: Settings cannot be changed on an offline device
  - Action: Apply "Offline" filter, open an offline light or thermostat, and attempt to change brightness/target temperature.
  - Expected: The control is disabled or the change is refused with a message indicating the device is offline; the stored value does not change.

## Interaction
- [ ] IX-01: Selecting a device opens its detail and settings panel
  - Action: Click any device row/card in the list.
  - Expected: A detail panel or view for that device opens showing its name, current status, its adjustable settings, and its schedules.

- [ ] IX-02: Switching room or device type view updates the list in place
  - Action: Click a different room grouping and then a different device type filter.
  - Expected: The device list refreshes to the new selection without a full page reload, and the currently selected room/type is visibly highlighted as active.

- [ ] IX-03: Saving a schedule gives confirmation feedback
  - Action: Complete and save a valid new schedule for a device.
  - Expected: A confirmation message/notification appears (e.g. "Schedule saved"), and the schedule is immediately visible in the device's schedule list.

- [ ] IX-04: Clearing the status filter restores the full device list
  - Action: With "Offline" filter active, clear or deselect the status filter (e.g. select "All").
  - Expected: The full device inventory is shown again, including online and idle devices, and the filter no longer shows "Offline" as active.

## Content
- [ ] CT-01: Page heading identifies it as a smart home device admin dashboard
  - Action: Read the dashboard title/heading and main navigation labels.
  - Expected: Text clearly identifies smart home device management (e.g. "Smart Home Devices" / "Device Management"); no template or placeholder branding such as "Lorem" or "Untitled".

- [ ] CT-02: Device rows show relevant names, types, and icons
  - Action: Inspect 5 device entries in the list including their icons/images.
  - Expected: Each device has a meaningful name and a type-appropriate icon/image (light icon for lights, thermostat icon for thermostats); no broken images and no placeholder text.

- [ ] CT-03: Activity entries reference real devices with readable times
  - Action: Read at least 3 entries in the Recent Activity panel.
  - Expected: Each entry names a device that exists in the device list, describes a real action (e.g. "turned on", "set to 21°C"), and shows a valid readable time; no "undefined", "NaN", or empty values.