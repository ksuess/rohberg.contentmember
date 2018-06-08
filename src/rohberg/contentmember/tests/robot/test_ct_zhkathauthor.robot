# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s rohberg.contentmember -t test_zhkathauthor.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src rohberg.contentmember.testing.ROHBERG_CONTENTMEMBER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/rohberg/contentmember/tests/robot/test_zhkathauthor.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a zhkathauthor
  Given a logged-in site administrator
    and an add zhkathauthor form
   When I type 'My zhkathauthor' into the title field
    and I submit the form
   Then a zhkathauthor with the title 'My zhkathauthor' has been created

Scenario: As a site administrator I can view a zhkathauthor
  Given a logged-in site administrator
    and a zhkathauthor 'My zhkathauthor'
   When I go to the zhkathauthor view
   Then I can see the zhkathauthor title 'My zhkathauthor'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add zhkathauthor form
  Go To  ${PLONE_URL}/++add++zhkathauthor

a zhkathauthor 'My zhkathauthor'
  Create content  type=zhkathauthor  id=my-zhkathauthor  title=My zhkathauthor

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the zhkathauthor view
  Go To  ${PLONE_URL}/my-zhkathauthor
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a zhkathauthor with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the zhkathauthor title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
