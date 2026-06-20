@echo off
REM Run all tests and generate an HTML report (report.html).
REM Pass any extra behave flags as arguments, e.g.:
REM   run_tests.bat --tags=smoke
REM   run_tests.bat features/login.feature
behave -f behave_html_formatter:HTMLFormatter -o report.html %*
