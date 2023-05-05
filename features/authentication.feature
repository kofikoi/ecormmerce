Feature: Authentication

  Scenario: Admin login
    Given I am on the login page
    When I enter valid admin credentials
    And click the login button
    Then I should be redirected to the admin dashboard

  Scenario: Normal user login
    Given I am on the login page
    When I enter valid normal user credentials
    And click the login button
    Then I should be redirected to the vehicle list page

  Scenario: Logout
      Given I am logged in
      When I click the logout button
      Then I should be redirected to the login page
  