# Specification for Sample Online Survey Tool [PR:55], Release 1.0.0.0 [RL:209]


## Product Overview
<p>This product is for a simple online survey tool that asks uses a bunch of questions and then saves them in a relational database.</p>




## Requirements Document
### Requirement RQ:1099: As a user I want to be able to login to the tool and complete a survey, with the answers stored in a database



### Requirement RQ:1100: As a user, I want to navigate to the survey section after login so that I can start the survey

**Feature:** <p>Once logged in, users should be able to navigate to the survey section seamlessly. The interface should provide a clear and accessible link to the survey from the main dashboard. The navigation should be intuitive and user-friendly.</p>



### Requirement RQ:1105: As a user, I want the survey section to load quickly after clicking the link so that I can start the survey without delay

**Feature:** <p>When the user clicks on the survey link from the main dashboard, the survey section should load swiftly. The page should display a loading indicator if necessary, and the survey section should be fully functional and ready to use within a few seconds. The loading time should be optimized for both mobile and desktop users.</p>



#### Acceptance Criteria


1. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Quick loading of survey section on mobile</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a user is logged into the dashboard on a mobile device</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user clicks on the survey link</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the survey section should load within 3 seconds</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>a loading indicator should be displayed during the loading process</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the survey section should be fully functional upon completion</p>

2. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Survey section functionality post-load</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>the survey section has loaded</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user interacts with the survey section</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>all survey elements should be responsive</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the user should be able to start the survey without any delays</p>

3. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Loading indicator visibility during survey section load</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a user is logged into the dashboard</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user clicks on the survey link</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the survey section takes longer than 2 seconds to load</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>a loading indicator should be visible</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the loading indicator should disappear once the survey section is fully loaded</p>

4. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Quick loading of survey section on desktop</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a user is logged into the dashboard</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user clicks on the survey link</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the survey section should load within 2 seconds</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>a loading indicator should be displayed during the loading process</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the survey section should be fully functional upon completion</p>



#### Test Cases


##### Test Case TC:748: Check responsiveness of survey elements post-load on mobile



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in to the dashboard on a mobile device..</td>
<td>Successful login and access to the dashboard..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the survey link..</td>
<td>The survey link is visible and clickable..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Click on the survey link..</td>
<td>The survey section starts loading..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Interact with the survey elements..</td>
<td>All survey elements are responsive..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Start the survey..</td>
<td>The user can start the survey without any delays..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:747: Verify loading indicator visibility during survey section load on mobile



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in to the dashboard on a mobile device..</td>
<td>Successful login and access to the dashboard..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the survey link..</td>
<td>The survey link is visible and clickable..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Simulate a slow loading time..</td>
<td>The survey section takes longer than 2 seconds to load..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Check for the loading indicator..</td>
<td>The loading indicator is visible..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Verify the loading indicator disappears..</td>
<td>The loading indicator disappears once the survey section is fully loaded..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:749: Verify quick loading of survey section on desktop



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in to the dashboard on a desktop device..</td>
<td>Successful login and access to the dashboard..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the survey link..</td>
<td>The survey link is visible and clickable..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Click on the survey link..</td>
<td>The survey section starts loading..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Measure the loading time..</td>
<td>The survey section loads within 2 seconds..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Check for the loading indicator..</td>
<td>A loading indicator is displayed during the loading process..</td>
<td>.</td>
</tr>
<tr>
<td>6.</td>
<td>Verify the survey section is fully functional..</td>
<td>The survey section is fully functional upon completion..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:746: Verify quick loading of survey section on mobile



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in to the dashboard on a mobile device..</td>
<td>Successful login and access to the dashboard..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the survey link..</td>
<td>The survey link is visible and clickable..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Click on the survey link..</td>
<td>The survey section starts loading..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Measure the loading time..</td>
<td>The survey section loads within 3 seconds..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Check for the loading indicator..</td>
<td>A loading indicator is displayed during the loading process..</td>
<td>.</td>
</tr>
<tr>
<td>6.</td>
<td>Verify the survey section is fully functional..</td>
<td>The survey section is fully functional upon completion..</td>
<td>.</td>
</tr>
</table>


### Requirement RQ:1106: As a user, I want clear instructions on how to start the survey so that I know what to do next

**Feature:** <p>Once the survey section is loaded, users should be greeted with clear and concise instructions on how to begin the survey. This could include a brief overview of the survey's purpose, an example question, and a call to action to start the survey. The instructions should be displayed prominently and should be written in a user-friendly tone.</p>



#### Acceptance Criteria


1. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> User receives clear instructions to start the survey</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>the survey section is loaded</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the survey section</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>clear and concise instructions should be displayed</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the instructions should include an overview of the survey's purpose</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the instructions should include an example question</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the instructions should include a call to action to start the survey</p>

2. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Instructions are displayed prominently</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>the survey section is loaded</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the survey section</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the instructions should be displayed prominently</p>

3. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> User-friendly tone of instructions</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>the survey section is loaded</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the survey section</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>clear instructions are displayed</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the instructions should be written in a user-friendly tone</p>



#### Test Cases


##### Test Case TC:754: Check for instructions after survey completion



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Complete the survey..</td>
<td>The survey is successfully completed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Check if the instructions are still displayed..</td>
<td>The instructions are still displayed after survey completion..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:757: Check for instructions after survey reset



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Start the survey and then reset it..</td>
<td>The survey is reset..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Check if the instructions are still displayed..</td>
<td>The instructions are still displayed after the survey reset..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:756: Check for instructions in offline mode



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section while offline..</td>
<td>The survey section is loaded while offline..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Check if the instructions are displayed..</td>
<td>The instructions are displayed even while offline..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:751: Check for prominent display of instructions



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Check if the instructions are displayed prominently..</td>
<td>The instructions are displayed prominently..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:753: Test instructions visibility on different screen sizes



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section on a desktop screen..</td>
<td>The instructions are visible and readable on a desktop screen..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the survey section on a tablet screen..</td>
<td>The instructions are visible and readable on a tablet screen..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Navigate to the survey section on a mobile screen..</td>
<td>The instructions are visible and readable on a mobile screen..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:755: Test instructions with different languages



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Change the language preference to Spanish..</td>
<td>The language preference is changed to Spanish..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Check if the instructions are available in Spanish..</td>
<td>The instructions are available in Spanish..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Change the language preference to French..</td>
<td>The language preference is changed to French..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Check if the instructions are available in French..</td>
<td>The instructions are available in French..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:759: Test instructions with keyboard navigation



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Use keyboard navigation to access the instructions..</td>
<td>The instructions are accessible using keyboard navigation..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Verify that the instructions are navigable using keyboard shortcuts..</td>
<td>The instructions are navigable using keyboard shortcuts..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:758: Test instructions with screen reader



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Activate the screen reader..</td>
<td>The screen reader starts reading the instructions..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Verify that the screen reader reads the instructions correctly..</td>
<td>The screen reader reads the instructions correctly..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:750: Verify clear instructions on starting the survey



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Check for the presence of instructions..</td>
<td>Instructions are displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Verify the instructions include an overview of the survey's purpose..</td>
<td>The instructions contain a brief overview of the survey's purpose..</td>
<td>.</td>
</tr>
<tr>
<td>4.</td>
<td>Verify the instructions include an example question..</td>
<td>The instructions contain an example question..</td>
<td>.</td>
</tr>
<tr>
<td>5.</td>
<td>Verify the instructions include a call to action to start the survey..</td>
<td>The instructions contain a call to action to start the survey..</td>
<td>.</td>
</tr>
<tr>
<td>6.</td>
<td>Check if the instructions are displayed prominently..</td>
<td>The instructions are displayed prominently..</td>
<td>.</td>
</tr>
<tr>
<td>7.</td>
<td>Verify the instructions are written in a user-friendly tone..</td>
<td>The instructions are written in a user-friendly tone..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:752: Verify user-friendly tone of instructions



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Navigate to the survey section..</td>
<td>The survey section is loaded..</td>
<td>.</td>
</tr>
<tr>
<td>2.</td>
<td>Check if the instructions are written in a user-friendly tone..</td>
<td>The instructions are written in a user-friendly tone..</td>
<td>.</td>
</tr>
</table>


### Requirement RQ:1107: As a user, I want a visible survey link on the main dashboard so that I can easily access the survey section

**Feature:** <p>Upon logging in, users should see a prominent link to the survey section on the main dashboard. This link should be clearly labeled and positioned in a location that is easily noticeable. The link should be accessible via keyboard navigation and should be styled to stand out from other dashboard elements.</p>



#### Acceptance Criteria


1. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> User sees survey link on main dashboard</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a logged-in user</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the main dashboard</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the survey link should be visible</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the survey link should be clearly labeled</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the survey link should be positioned in a noticeable location</p>

2. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> Survey link stands out from other dashboard elements</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a logged-in user</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the main dashboard</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the survey link should be styled to stand out from other dashboard elements</p>

3. <p><strong><span style="color:hsl(210, 75%, 60%);">Scenario:</span></strong><strong><span style="color:hsl(210, 75%, 60%);"> User accesses survey link using keyboard navigation</span></strong></p><p><strong><span style="color:hsl(162, 100%, 32%);">Given </span></strong>a logged-in user</p><p><strong><span style="color:hsl(162, 100%, 32%);">When </span></strong>the user navigates to the main dashboard</p><p><strong><span style="color:hsl(162, 100%, 32%);">And </span></strong>the user uses keyboard navigation to access the survey link</p><p><strong><span style="color:hsl(162, 100%, 32%);">Then </span></strong>the survey link should be accessible</p>



#### Test Cases


##### Test Case TC:766: Check for visual issues on survey link



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Inspect the survey link for any visual issues..</td>
<td>There are no visual issues with the survey link..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:765: Check survey link functionality on different devices



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Test the survey link on different devices (e.g., desktop, tablet, mobile)..</td>
<td>The survey link works correctly on all tested devices..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:767: Check survey link performance



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Measure the load time of the survey link..</td>
<td>The survey link loads within an acceptable time frame..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:762: Check survey link styling to stand out



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Compare the styling of the survey link with other dashboard elements..</td>
<td>The survey link is styled to stand out from other dashboard elements..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:763: Check survey link visibility on different screen sizes



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Resize the browser window to different screen sizes..</td>
<td>The survey link remains visible on all screen sizes..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:761: Test survey link accessibility via keyboard navigation



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username: user123</p><p>Password: password123</p>.</td>
</tr>
<tr>
<td>2.</td>
<td>Navigate to the main dashboard..</td>
<td>The main dashboard is displayed..</td>
<td>.</td>
</tr>
<tr>
<td>3.</td>
<td>Use keyboard navigation to access the survey link..</td>
<td>The survey link is accessible via keyboard navigation..</td>
<td>.</td>
</tr>
</table>
##### Test Case TC:764: Test survey link under different network conditions



##### Steps


<table>
<tr><th>Step #</th><th>Description</th><th>Expected Result</th><th>Sample Data</th></tr>
<tr>
<td>1.</td>
<td>Log in as a user..</td>
<td>Successful login and access to the main dashboard..</td>
<td><p>Username:
