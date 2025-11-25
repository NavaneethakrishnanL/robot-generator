*** Settings ***
Library    SerialLibrary
Library    OperatingSystem
Library    Process
Library    Collections

*** Variables ***
${ECU_PORT}           COM3
${BAUDRATE}           115200
${TIMEOUT}            5
${EXPECTED_SW_VER}    1.2.5
${CAN_INTERFACE}      can0

*** Test Cases ***
ECU Boots And Sends Heartbeat
    [Documentation]    Verifies ECU boot-up and periodic heartbeat on CAN
    Open Serial Port    ${ECU_PORT}    baudrate=${BAUDRATE}
    ${data}=    Read Until    READY    timeout=${TIMEOUT}
    Should Contain    ${data}    READY
    Start Process    candump    ${CAN_INTERFACE} -n 1
    ${heartbeat}=    Wait For Process
    Should Contain    ${heartbeat.stdout}    0x701

ECU Software Version Check
    [Documentation]    Reads software version from ECU and validates it.
    Open Serial Port    ${ECU_PORT}    baudrate=${BAUDRATE}
    Write To Serial    VERSION?
    ${resp}=    Read Serial    timeout=${TIMEOUT}
    Should Contain    ${resp}    ${EXPECTED_SW_VER}

ECU Sensor Self-Test
    [Documentation]    Validates GNSS, IMU, RADAR inputs via HIL injection.
    Inject CAN Frame    ${CAN_INTERFACE}    0x310    11 22 33 44 55 66 77 88
    ${sensor}=    Read Serial Until    SELFTEST_OK
    Should Contain    ${sensor}    SELFTEST_OK
