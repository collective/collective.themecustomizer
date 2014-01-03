*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Test cases ***

Test Aviary photo editor
    Enable Autologin as  Site Administrator
    Go To  ${PLONE_URL}/@@site-controlpanel

    Page Should Contain  Site settings
    Click Button  Save
    Page Should Contain  Site settings
    Page Should Contain  Changes saved
