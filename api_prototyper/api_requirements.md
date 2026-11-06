API Requirements – TaskFlow API
1. Domain Overview
TaskFlow is a task and project management application that helps individuals and teams organise work, assign responsibilities, track progress, and collaborate on shared projects.

The TaskFlow API provides a secure REST interface for managing user accounts, projects, tasks, and task comments. It will be consumed by a web or mobile frontend and may later support third-party integrations.

Initial scope: User authentication, project membership, task management, and comments. Notifications, file attachments, and external integrations are out of scope for the first prototype.
2. Target Users
- Individual users: Create personal projects, add tasks, and track their own progress.
- Team members: View projects they belong to, update tasks, and collaborate through comments.
- Project owners: Create projects, invite or remove members, and manage task assignments.
- Frontend developers: Integrate TaskFlow features through predictable JSON endpoints.
3. Core Operations
The first version must support the following 12 operations:
#	Operation	Method	Endpoint	Requirement
1	Register account	POST	/api/v1/auth/register	Create a user with a unique email and securely hashed password.
2	Sign in	POST	/api/v1/auth/login	Verify credentials and return an access token.
3	Get current user	GET	/api/v1/users/me	Return the authenticated user's profile without sensitive fields.
4	Create project	POST	/api/v1/projects	Create a project and make its creator the owner.
5	List projects	GET	/api/v1/projects	Return only projects accessible to the authenticated user.
6	Add project member	POST	/api/v1/projects/{projectId}/members	Allow a project owner to add an existing user.
7	Create task	POST	/api/v1/projects/{projectId}/tasks	Create a task within an accessible project.
8	List and filter tasks	GET	/api/v1/projects/{projectId}/tasks	Filter by status, priority, or assignee; support pagination.
9	Get task details	GET	/api/v1/tasks/{taskId}	Retrieve a task only if the user can access its project.
10	Update task	PATCH	/api/v1/tasks/{taskId}	Edit permitted fields such as title, description, status, priority, assignee, or due date.
11	Delete task	DELETE	/api/v1/tasks/{taskId}	Allow the project owner or task creator to delete a task.
12	Add task comment	POST	/api/v1/tasks/{taskId}/comments	Allow project members to post comments on an accessible task.


General API Behaviour
- Request and response bodies use JSON with Content-Type: application/json.
- Use appropriate HTTP status codes: 200 for successful reads/updates, 201 for creation, 204 for deletion, 400 for invalid requests, 401 for unauthenticated requests, 403 for unauthorised actions, 404 for unavailable resources, 409 for conflicts, and 429 for rate limits.
- Return predictable errors, for example: { "error": { "code": "VALIDATION_ERROR", "message": "Title is required" } }.
- Use stable resource identifiers, preferably UUIDs.
- All timestamps use ISO 8601 in UTC.
- Task list responses support page and limit parameters, with a default limit of 20 and maximum of 100.
4. Data Validation Rules
Users
- Email is required, must be a valid email format, and must be unique (case-insensitive).
- Password is required and must contain at least 12 characters; never return or log the plain-text password.
- Display name is required and must contain 2–100 characters after trimming whitespace.
Projects
- Project name is required and must contain 3–100 characters after trimming whitespace.
- Project description is optional, up to 1,000 characters.
- A project member must refer to an existing user; duplicate memberships are not allowed.
- Only a project owner may add members in the initial prototype.
Tasks
- Task title is required and must contain 1–150 characters after trimming whitespace.
- Task description is optional, up to 5,000 characters.
- Status must be one of TODO, IN_PROGRESS, or DONE; default is TODO.
- Priority must be one of LOW, MEDIUM, or HIGH; default is MEDIUM.
- Due date is optional and must be a valid ISO 8601 date or timestamp; past dates are permitted for tracking overdue work.
- Any assignee must be a member of the task's project.
- Project and task IDs must have valid UUID syntax and reference existing, accessible records.
- A task must belong to exactly one project.
Comments
- Comment text is required and must contain 1–2,000 characters after trimming whitespace.
- Comments must reference an existing task in a project accessible to the author.
5. Non-Functional Requirements
Performance and Reliability
- Latency: At least 95% of standard API requests should complete within 300 ms under expected prototype load, excluding network travel time.
- Database queries: Paginate list endpoints and index frequently filtered fields such as project ID, assignee, and status.
- Availability target: Aim for 99.5% uptime in a deployed environment; this is a target, not a guarantee for a local prototype.
- Data integrity: Use database constraints and transactions to prevent orphaned tasks, invalid memberships, and partial writes.
Authentication and Authorisation
- Use HTTPS for all deployed endpoints.
- Require JWT bearer authentication for all endpoints except registration and login.
- Use short-lived access tokens (for example, 15 minutes) and validate token signatures and expiry on every protected request.
- Store password hashes using a suitable adaptive hashing algorithm such as Argon2id or bcrypt.
- Enforce project-based access control on every project, task, and comment operation; clients must not access other users' private projects.
- Keep tokens, passwords, and other secrets out of application logs and source control.
Rate Limits and Security
- Limit authentication attempts to 5 per minute per IP (with additional account-based protection where feasible).
- Limit other authenticated requests to 100 per minute per user for the prototype.
- Respond with 429 Too Many Requests and a Retry-After header when a limit is exceeded.
- Validate inputs server-side; use parameterised database queries and limit request body sizes to mitigate common injection and abuse risks.
- Configure CORS to allow only approved frontend origins in deployed environments.
Maintainability and Observability
- Version routes using /api/v1 to support future changes.
- Document endpoints, schemas, authentication, and sample responses with OpenAPI/Swagger.
- Include automated tests for happy paths, validation failures, authentication, and permission checks.
- Log request method, route, status code, latency, and a request ID without exposing sensitive data.
- Use consistent JSON field naming and error response structures across endpoints.
6. Acceptance Criteria
- All 12 core operations are implemented and documented.
- Invalid data receives an appropriate 4xx response with a clear error message.
- Unauthenticated users cannot access protected endpoints.
- Users cannot read or modify projects and tasks they do not have permission to access.
- Task creation, updates, assignment, filtering, and deletion work end to end.
- Automated tests cover major success and failure cases.
- Performance and rate-limit behaviour can be demonstrated with a basic API test suite.