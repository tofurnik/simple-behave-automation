@login
Feature: User Authentication

  Background:
    Given I navigate to the login page

  Scenario: Successful login with valid credentials
    When I log in with valid credentials
    Then I should be logged in

  Scenario: Failed login with invalid credentials
    When I log in with incorrect credentials
    Then I should see a login error message

  Scenario: Failed login when no credentials provided
    When I log in with no credentials provided
    Then I should see a login error message
