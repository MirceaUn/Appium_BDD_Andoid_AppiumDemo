Feature: Scroll View


  Scenario: Navigating through menu with scroll
    Given I am on the basepage and I click on the ScrollView button and I assert that after click I am on the right page
    When I scroll to button 16 and I make sure the button is visible
    And I click on button 16
    Then a pop-up appears and I press Yes