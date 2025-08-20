# Test Plan – BabiHost Project

## 1. Introduction

The purpose of this test plan is to define the strategy, scope, objectives, resources, schedule, and processes for testing the **BabiHost platform**.  
It aims to ensure that the application meets **functional, usability, performance, and security requirements** before release.

---

## 2. Project Overview

BabiHost is a hospitality and accommodation booking platform that connects travelers with verified hosts.  
Key features include:

- Property listing creation and management
- Secure user authentication
- Booking and payment processing
- Host verification
- Search and filter functionalities

---

## 3. Scope of Testing

### In-Scope

- **Functional Testing (UI and API)**: Verifying all features work as specified.
- **Usability Testing**: Ensuring the user interface is intuitive and easy to use.
- **Compatibility Testing**: Checking the platform's behavior across different browsers and devices.
- **Regression Testing**: Rerunning tests to ensure new code hasn't broken existing functionality.
- **Integration Testing**: Verifying that different modules and services interact correctly.
- **Smoke/Sanity Testing**: A quick test to ensure the core functionalities are working after each new build.
- **Security Testing**: Basic vulnerability checks for common issues such as SQL injection and Cross-Site Scripting (XSS).

### Out-of-Scope

- Performance & Load Testing
- Penetration Testing (handled by a security team)
- Localization Testing

---

## 4. Test Objectives

- Validate that all **core features** function as expected.
- Ensure compatibility across **different devices and browsers**.
- Verify that **data is processed securely** during transactions.
- Detect and log defects early in the development lifecycle.
- Maintain a **high-quality user experience** for travelers and hosts.

---

## 5. Test Approach

Testing will be performed in **phases**, starting with smoke testing, followed by functional and regression cycles.

1. **Smoke Testing**: Quick validation after each build to ensure the core application is stable enough for detailed testing.
2. **Functional Testing**: Detailed verification that all features match requirements and user stories.
3. **Integration Testing**: Ensuring that different modules and external services interact and communicate correctly.
4. **Regression Testing**: Re-checking all existing features after new changes or bug fixes are introduced.
5. **User Acceptance Testing (UAT)**: Final validation by end-users or stakeholders to ensure the product meets their needs before release.

---

## 6. Test Deliverables

- Test Cases (`test_cases.md`)
- Test Execution Reports
- Defect Reports
- Automation Scripts
- Test Summary Reports

---

## 7. Test Environment
  
- **Testing Tools**:  
  - Manual: Jira + Zephyr Scale  
  - Automation: Python + Selenium + Pytest  
- **Browsers**: Chrome (latest stable), Firefox (latest stable), Safari (latest stable), Edge (latest stable)
- **Devices**: Windows, macOS, Android (12+), iOS (16+)

---

## 8. Entry & Exit Criteria

### Entry Criteria

- Approved requirements and user stories
- Stable build deployed to QA environment
- Test data prepared

### Exit Criteria

- All **high and critical severity defects resolved**
- 95%+ of planned test cases executed
- Test summary report approved

---

## 9. Risks & Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Changing requirements | Medium | Frequent communication with stakeholders |
| Limited test data | High | Prepare and validate test data early |
| Tight deadlines | High | Prioritize high-risk and high-impact test cases |
| Unstable test environment | High | Work with the DevOps team to ensure the QA environment is consistently available and configured correctly |

---

## 10. Schedule

| Phase | Duration | Dates |
|-------|----------|-------|
| Test Planning | 3 days | TBD |
| Test Case Design | 5 days | TBD |
| Test Execution | 10 days | TBD |
| Reporting & Closure | 2 days | TBD |

---

## 11. Ressources

- **QA Engineer**: _Georges Khabbaz_
- **Product Owner**: _BabiHost Dev Team_
- **Developers**: _TBD_
- **Project Manager**: _TBD_
- **UI/UX**: _TBD_
