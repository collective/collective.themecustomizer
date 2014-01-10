*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Variables ***

${site_title}  My Plone Site!
${site_description}  This is a theme customized Plone site
${site_title_id}  portal-title
${site_description_id}  portal-description

*** Test cases ***

Test themecustomizer settings
    [Documentation]  Before installing, everything looks good
    Everything Looks Good  215  56

    [Documentation]  After a fresh install nothing has changed yet
    Enable Autologin as  Manager
    Go To  ${PLONE_URL}/prefs_install_products_form
    Select Checkbox  id=collective.themecustomizer
    Click Button  Activate
    Everything Looks Good  215  56

    Enable Autologin as  Site Administrator

    [Documentation]  There's a show_header_text checkbox
    ...              Let's test its behavior
    Go To  ${PLONE_URL}/@@site-controlpanel
    Page Should Contain  Site settings
    Input Text  id=form.site_title  ${site_title}
    Input Text  id=form.site_description  ${site_description}
    Select Checkbox  id=form.show_header_text
    Save Settings And Go Home
    Element Text Should Be  id=${site_title_id}  ${site_title}
    Element Text Should Be  id=${site_description_id}  ${site_description}

    [Documentation]  There's a show_header_logo checkbox
    ...              Let's test its behavior
    Go To  ${PLONE_URL}/@@site-controlpanel
    Unselect Checkbox  id=form.show_header_logo
    Save Settings And Go Home
    Page Should Not Contain Element  css=#portal-logo>img

    [Documentation]  Let's upload a new logo and header images
    ...              and make logo visible again
    Go To  ${PLONE_URL}/@@site-controlpanel
    Select Checkbox  id=form.show_header_logo
    Choose File  id=form.image  /tmp/newlogo.png
    Choose File  id=form.background  /tmp/background.png
    Save Settings And Go Home
    Page Should Contain Element  css=#portal-logo>img
    # New uploaded logo
    Wait For Condition  return jQuery('#portal-logo>img').width()==50
    Wait For Condition  return jQuery('#portal-logo>img').height()==50
    # header background-image ends with 'background.png'
    Log Source
    Wait For Condition  return jQuery('#portal-header').css('background-image')!='none'

    [Documentation]  Uninstall and see that everything was left as
    ...              default except for logo.png that wasn't removed
    Enable Autologin as  Manager
    Go To  ${PLONE_URL}/prefs_install_products_form
    Select Checkbox  id=collective.themecustomizer
    Click Button  Deactivate
    Everything Looks Good  50  50

    [Documentation]  Event site-controlpanel is less configurable
    Enable Autologin as  Site Administrator
    Go To  ${PLONE_URL}/@@site-controlpanel
    Page Should Not Contain Element  id=form.show_header_text
    Page Should Not Contain Element  id=form.show_header_logo
    Page Should Not Contain Element  id=form.image
    Page Should Not Contain Element  id=form.background

*** Keywords ***

Save Settings And Go Home
    Click Button  Save
    Page Should Contain  Changes saved
    Go To  ${PLONE_URL}

Everything Looks Good
    [arguments]  ${logo_width}  ${logo_height}

    # No visible site title
    Page Should Not Contain Element  id=${site_title_id}
    # No visible site description
    Page Should Not Contain Element  id=${site_description_id}
    # Visible logo
    Page Should Contain Element  css=#portal-logo>img
    # Logo width is as expected
    Wait For Condition  return jQuery('#portal-logo>img').width()==${logo_width}
    Wait For Condition  return jQuery('#portal-logo>img').height()==${logo_height}
    # No header background
    Wait For Condition  return jQuery('#portal-header').css('background-image')=='none'
