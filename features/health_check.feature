Feature: status health-check endpoint

  Scenario: check for server status
     Given the server is up and running correctly
      When a GET request is sent to "/status"
      Then the response code should be 200