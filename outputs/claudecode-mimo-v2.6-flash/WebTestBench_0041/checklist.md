# Test Checklist

## Functionality
- [ ] FT-01: View devices grouped/filtered by room
  - Action: Select a room (e.g., "Living Room") from the room view option
  - Expected: The device list shows only devices assigned to that room

- [ ] FT-02: View devices grouped/filtered by device type
  - Action: Select a device type (e.g., "Lights" or "Thermostats") from the type view option
  - Expected: The device list shows only devices of the selected type

- [ ] FT-03: Adjust light brightness
  - Action: Open a light device's settings and change the brightness to a new value (e.g., 75%)
  - Expected: The brightness setting is saved and the device card reflects the new value

- [ ] FT-04: Adjust thermostat target temperature
  - Action: Open a thermostat's settings and change the target temperature to a new value (e.g., 22°C)
  - Expected: The target temperature is saved and the device card reflects the new value

- [ ] FT-05: Create a schedule for a light
  - Action: Create a schedule selecting a light device, a time, and a target state (e.g., On at 18:00)
  - Expected: The schedule is created and appears in the schedules list with the correct device, time, and state

- [ ] FT-06: Create a schedule for a thermostat
  - Action: Create a schedule selecting a thermostat, a time, and a target temperature/state
  - Expected: The schedule is created and appears in the schedules list with the correct details

- [ ] FT-07: View recent activity
  - Action: Navigate to the recent activity section
  - Expected: A list of recent device events is displayed (e.g., which device was used and when)

- [ ] FT-08: Filter devices by status "Offline"
  - Action: Apply the "Offline" status filter
  - Expected: Only devices with offline status are shown in the device list

- [ ] FT-09: Filter devices by status "Idle"
  - Action: Apply the "Idle" status filter
  - Expected: Only devices with idle status are shown in the device list

## Constraint
- [ ] CS-01: Schedule form cannot be submitted with missing required fields
  - Action: Attempt to save a schedule without selecting a device, time, or target state
  - Expected: The schedule is not created and a validation error identifies the missing field(s)

- [ ] CS-02: Brightness cannot be set outside its valid range
  - Action: Attempt to set brightness below 0% or above 100%
  - Expected: The value is rejected or clamped to the valid range; invalid input is not saved

- [ ] CS-03: Target temperature cannot be set outside its valid range
  - Action: Attempt to set a target temperature outside the allowed range (e.g., below minimum or above maximum)
  - Expected: The value is rejected or clamped to the valid range; invalid input is not saved

- [ ] CS-04: Status filter shows only matching devices
  - Action: With the "Offline" filter active, inspect the returned device list
  - Expected: No device with a non-offline status (e.g., online, idle) appears in the list

## Interaction
- [ ] IX-01: Device list updates immediately when a filter or view option is changed
  - Action: Switch between room view, type view, or a status filter
  - Expected: The device list refreshes right away to reflect the selection without requiring a manual reload

- [ ] IX-02: Confirmation feedback after saving a device setting
  - Action: Change a device setting (brightness or temperature) and save
  - Expected: A visible success confirmation (toast or message) appears indicating the setting was saved

- [ ] IX-03: Confirmation feedback after creating a schedule
  - Action: Submit a valid new schedule
  - Expected: A visible success confirmation appears and the new schedule is shown in the list

## Content
- [ ] CT-01: Recent activity entries include device name and timestamp
  - Action: Open the recent activity section
  - Expected: Each entry clearly shows which device was used and the time of last use

- [ ] CT-02: Device status labels are accurate and consistent
  - Action: Inspect device cards/list against their status filter results
  - Expected: Each device displays a status label (e.g., Online, Idle, Offline) that matches its actual state

- [ ] CT-03: Schedule entries display correct device, time, and action details
  - Action: Open the schedules list and inspect an existing schedule
  - Expected: Each schedule shows the target device name, scheduled time, and the state/temperature it will apply