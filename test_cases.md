# Test Cases for Login and Registration

## Login Test Cases

Detailed test cases for Login functionality.

---

## TC001 – Valid Login

**Objective:** Verify successful login with valid email and password.  
**Preconditions:** User is on the login page.

| Step | Action                  | Test Data            | Expected Result                          |
|------|-------------------------|----------------------|------------------------------------------|
| 1    | Enter valid email       | <user@example.com>     | Email field accepts input                |
| 2    | Enter valid password    | correct123           | Password field accepts input             |
| 3    | Click Login             | —                    | User is redirected to dashboard          |

**Priority:** High  
**Severity:** Critical

---

## TC002 – Invalid Email Format

**Objective:** Validate email format check.  
**Preconditions:** User is on the login page.

| Step | Action               | Test Data     | Expected Result                                 |
|------|----------------------|---------------|-------------------------------------------------|
| 1    | Enter email          | user.com      | Validation error: "Enter a valid email"         |
| 2    | Enter password       | correct123    | Password field accepts input                    |
| 3    | Click Login          | —             | Show error and prevent login                    |

**Priority:** High

---

## TC003 – Incorrect Password

**Objective:** Verify error when password is incorrect.  
**Preconditions:** User is on the login page.

| Step | Action               | Test Data          | Expected Result                             |
|------|----------------------|--------------------|----------------------------------------------|
| 1    | Enter valid email    | <user@example.com>   | —                                            |
| 2    | Enter wrong password | wrongpass123       | —                                            |
| 3    | Click Login          | —                  | Show error: "Invalid email or password"      |

**Priority:** High

---

## TC004 – Empty Email and Password

**Objective:** Verify error when both fields are left empty.  
**Preconditions:** User is on the login page.

| Step | Action               | Test Data | Expected Result                            |
|------|----------------------|-----------|--------------------------------------------|
| 1    | Leave email blank    | —         | Email field remains empty                  |
| 2    | Leave password blank | —         | Password field remains empty               |
| 3    | Click Login          | —         | Error: "Email and password are required"   |

**Priority:** Medium

---

## TC005 – Password Field Masking

**Objective:** Ensure password input is masked.  
**Preconditions:** User is on the login page.

| Step | Action            | Test Data  | Expected Result                     |
|------|-------------------|------------|-------------------------------------|
| 1    | Enter password    | correct123 | Input is displayed as bullets/dots  |

**Priority:** Low

---

## TC006 – Case Sensitivity in Email

**Objective:** Check if email entry is case-insensitive (should normalize).  
**Preconditions:** User is on the login page.

| Step | Action            | Test Data         | Expected Result                        |
|------|-------------------|-------------------|----------------------------------------|
| 1    | Enter email       | <User@Example.com>  | System normalizes input (treats as <user@example.com>) |
| 2    | Enter password    | correct123        | —                                      |
| 3    | Click Login       | —                 | User is redirected to dashboard        |

**Priority:** Low

---

## TC007 – “Remember Me” Functionality

**Objective:** Validate that “Remember Me” keeps user logged in.  
**Preconditions:** User is on the login page.

| Step | Action               | Test Data       | Expected Result                                         |
|------|----------------------|-----------------|---------------------------------------------------------|
| 1    | Enter valid email    | <user@example.com>| —                                                       |
| 2    | Enter password       | correct123      | —                                                       |
| 3    | Check "Remember Me"  | —               | Checkbox selected                                       |
| 4    | Click Login          | —               | User logs in                                            |
| 5    | Reopen browser       | —               | User remains logged in without re-entering credentials |

**Priority:** Medium

---

## TC008 – Forgot Password Navigation

**Objective:** Ensure user is redirected to password recovery page.  
**Preconditions:** User is on the login page.

| Step | Action               | Test Data | Expected Result                      |
|------|----------------------|-----------|--------------------------------------|
| 1    | Click "Forgot Password?" | —     | Redirected to password recovery page |

**Priority:** Low

---

## TC009 – SQL Injection in Email Field

**Objective:** Test against SQL injection vulnerability.  
**Preconditions:** User is on the login page.

| Step | Action        | Test Data       | Expected Result                              |
|------|---------------|-----------------|----------------------------------------------|
| 1    | Enter email   | ' OR 1=1 --     | Input sanitized or validation error displayed |
| 2    | Enter password| any             | —                                            |
| 3    | Click Login   | —               | Login is prevented                            |

**Priority:** High  
**Severity:** Critical (security)

---

## TC010 – Login Button Disabled Until Fields Are Filled

**Objective:** Verify login button is inactive until required fields are filled.  
**Preconditions:** User is on the login page.

| Step | Action                          | Test Data         | Expected Result                    |
|------|---------------------------------|-------------------|------------------------------------|
| 1    | Leave email and password blank  | —                 | Login button is disabled           |
| 2    | Enter email only                | <user@example.com>  | Login button remains disabled      |
| 3    | Enter password only             | correct123        | Login button remains disabled      |
| 4    | Enter both correctly            | valid credentials | Login button becomes active        |

**Priority:** Medium

---

## TC011 – Login Using Copy-Pasted Credentials

**Objective:** Ensure copy-pasted credentials work.  
**Preconditions:** Credentials copied to clipboard.

| Step | Action           | Test Data         | Expected Result                      |
|------|------------------|-------------------|--------------------------------------|
| 1    | Paste email      | <user@example.com>  | Email field accepts pasted input     |
| 2    | Paste password   | correct123        | Password field accepts pasted input  |
| 3    | Click Login      | —                 | User is redirected to dashboard      |

**Priority:** Low

---

## TC012 – Login Rate Limiting After Failed Attempts

**Objective:** Check system behaviour after multiple failed login attempts.  
**Preconditions:** User is on login page.

| Step | Action                            | Test Data         | Expected Result                                        |
|------|-----------------------------------|-------------------|--------------------------------------------------------|
| 1    | Enter valid email                 | <user@example.com>  | —                                                      |
| 2    | Enter wrong password repeatedly   | wrong123 x3       | Error: "Invalid credentials" shown 3 times             |
| 3    | 4th login attempt                 | wrong123          | Account temporarily locked or CAPTCHA presented        |

**Priority:** High

---

## TC013 – Tab Key Navigation

**Objective:** Verify form is accessible via Tab key.  
**Preconditions:** User is on login page.

| Step | Action | Test Data | Expected Result                                  |
|------|--------|-----------|--------------------------------------------------|
| 1    | Press Tab | —      | Cursor moves: email → password → remember checkbox → login button |

**Priority:** Low

---

## Registration Test Cases

Detailed test cases for user Registration.

---

## TC-REG-001 – Successful Registration with Valid Data

**Objective:** Verify successful registration with valid information.  
**Preconditions:** Registration page is accessible, no existing account with the test email.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open Registration page | — | Page loads |
| 2 | Enter First Name | John | Field accepts input |
| 3 | Enter Last Name | Doe | Field accepts input |
| 4 | Enter Email | <john.doe+001@example.com> | Accepts input (unique) |
| 5 | Enter Password | Test@1234 | Meets password policy |
| 6 | Confirm Password | Test@1234 | Matches password |
| 7 | Click Register | — | Success message displayed; user redirected to login/confirmation |

**Priority:** High

---

## TC-REG-002 – Registration with Existing Email

**Objective:** Verify system prevents registration with already registered email.  
**Preconditions:** An account exists for `existing@example.com`.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open Registration page | — | Page loads |
| 2 | Fill fields using existing email | <existing@example.com> | — |
| 3 | Click Register | — | Error: "Email already exists"; registration blocked |

**Priority:** High

---

## TC-REG-003 – Invalid Email Format

**Objective:** Validate email format enforcement.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter invalid email | userexample.com | Error: "Enter a valid email address" |
| 2 | Click Register | — | Registration blocked |

**Priority:** High

---

## TC-REG-004 – Password Too Short

**Objective:** Enforce minimum password length.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter short password | aB1! | Error: "Password must be at least 8 characters" |
| 2 | Click Register | — | Registration blocked |

**Priority:** High

---

## TC-REG-005 – Password Complexity (missing required classes)

**Objective:** Ensure password contains required character classes.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter password without uppercase | test@1234 | Error: "Password must include uppercase" |
| 2 | Click Register | — | Registration blocked |

**Priority:** High

---

## TC-REG-006 – Mismatched Confirm Password

**Objective:** Check that Confirm Password must match Password.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter password | Test@1234 | — |
| 2 | Enter confirm password | Test@4321 | Error: "Passwords do not match" |
| 3 | Click Register | — | Registration blocked |

**Priority:** High

---

## TC-REG-007 – Missing Required Fields

**Objective:** Verify required field validation messages appear.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Leave required fields blank | — | Error messages for each missing field |
| 2 | Click Register | — | Registration blocked |

**Priority:** High

---

## TC-REG-008 – SQL Injection in Input Fields

**Objective:** Ensure inputs are sanitized against SQL injection.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter `'; DROP TABLE users; --` into name/email fields | `'; DROP TABLE users; --` | Input is escaped or rejected; no backend error |
| 2 | Click Register | — | Registration blocked or input sanitized |

**Priority:** Critical (security)

---

## TC-REG-009 – Cross-Site Scripting (XSS) Attempt

**Objective:** Verify inputs do not allow XSS payloads.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter `<script>alert(1)</script>` into name field | `<script>alert(1)</script>` | Input sanitized and displayed escaped if shown |
| 2 | Click Register | — | No script execution in UI; registration blocked or sanitized |

**Priority:** Critical (security)

---

## TC-REG-010 – Registration With Leading/Trailing Spaces

**Objective:** Ensure system trims leading/trailing spaces in inputs.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter email `user@example.com` | with spaces | System trims spaces and treats email as `user@example.com` |
| 2 | Click Register | — | Registration succeeds if email unique and other validations pass |

**Priority:** Medium

---

## TC-REG-011 – Registration With Maximum Field Length

**Objective:** Check behavior for very long input values (boundary test).  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter 256+ characters in name fields | 256+ chars | System either trims input or shows "Field too long" error |
| 2 | Click Register | — | Registration blocked or input truncated per spec |

**Priority:** Medium

---

## TC-REG-012 – Registration With International Characters

**Objective:** Verify support for Unicode characters in name fields.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Enter name with accents `José Álvarez` | `José Álvarez` | Input accepted and stored/displayed correctly |
| 2 | Click Register | — | Registration succeeds (if other validations pass) |

**Priority:** Low

---

## TC-REG-013 – Copy-Pasted Credentials

**Objective:** Ensure pasted values are accepted and processed.  
**Preconditions:** Registration page accessible; credentials copied to clipboard.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Paste email/password into fields | pasted values | Fields accept pasted input |
| 2 | Click Register | — | Registration succeeds if data valid |

**Priority:** Low

---

## TC-REG-014 – Email Confirmation Sent

**Objective:** Verify that a confirmation email is sent after registration and link works.  
**Preconditions:** Access to test email inbox (or mailcatcher).

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Register with valid, reachable test email | <test.mail@example.com> | Registration accepted |
| 2 | Check inbox | — | Confirmation email received within expected time |
| 3 | Click confirmation link | — | Account is activated; user can login |

**Priority:** High

---

## TC-REG-015 – UI Accessibility & Tab Navigation

**Objective:** Ensure registration form is keyboard accessible and tab order is logical.  
**Preconditions:** Registration page accessible.

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Press Tab to navigate fields | — | Focus order: First Name → Last Name → Email → Password → Confirm Password → Register |
| 2 | Use Enter to submit when focus is on Register | — | Form submits (if valid) |

**Priority:** Low

---
