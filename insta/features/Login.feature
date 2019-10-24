# Created by farmazonne at 23.10.2019
Feature: Login
  # Enter feature description here

  Scenario: Valid Login
    Given open login page
    When I type "login" in username field
    When I type "pass" in password field
    When I click login button
    Then I see "text" text