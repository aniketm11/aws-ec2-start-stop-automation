# AWS EC2 Start/Stop Automation

A beginner cloud/DevOps project to control one EC2 instance from a simple HTML dashboard using two AWS Lambda functions and API Gateway.

## Architecture

Browser (`index.html`) → API Gateway Start endpoint → `EC2StartStopFunction` → EC2  
Browser (`index.html`) → API Gateway Stop endpoint → `stopfunction` → EC2

## Components

- Amazon EC2: target instance
- AWS Lambda (Python/Boto3): separate start and stop functions
- Amazon API Gateway: HTTP endpoints for the functions
- AWS IAM: least-privilege EC2 permissions
- Amazon CloudWatch Logs: function execution logs
- HTML/CSS/JavaScript: simple browser dashboard

## Repository layout

```text
.
├── index.html
├── lambda/
│   ├── start_ec2.py
│   ├── stop_ec2.py
│   └── iam-policy-example.json
├── docs/
│   ├── architecture.png
│   └── screenshots/
└── README.md
```

## Setup

1. Create or select an EC2 test instance in `us-east-1`.
2. Create separate Lambda functions for starting and stopping the instance.
3. Update `REGION` and `INSTANCE_ID` in the Python files for your environment.
4. Attach the policy in `lambda/iam-policy-example.json` to each Lambda execution role. Review and restrict the policy to your own account, region, and instance.
5. Configure each Lambda function's API Gateway trigger.
6. Configure API Gateway CORS for the exact website origin and allow `POST` and `OPTIONS`. The Lambda responses include example CORS headers; adapt these to your API type and CORS configuration.
7. Copy each API Gateway invoke URL into `START_API_URL` and `STOP_API_URL` in `index.html`.
8. Host `index.html` on a web server or static hosting service.
9. Test the two buttons and verify the final state in the EC2 console and execution details in CloudWatch Logs.

## Important notes

- The dashboard HTML must use the **two different API Gateway invoke URLs**.
- The Lambda functions in this repository are examples. The `stop_ec2.py` file calls `stop_instances`; `start_ec2.py` calls `start_instances`.
- The screenshots document the implementation and test flow; they do not prove that every configuration is production-ready.
- If the dashboard is hosted on the same EC2 instance it stops, the dashboard will become unavailable while that instance is stopped. Host the dashboard separately if it must remain available to restart the instance.
- An API endpoint that can start/stop compute resources should not be left open to the public. Add appropriate authorization (for example IAM authorization or a properly authenticated application layer), restrict access, and validate requests. Do not treat CORS as authentication.
- Never commit AWS access keys, secret keys, private keys, session tokens, or other credentials.
- EC2 compute charges generally stop when an instance is stopped, but EBS storage and other resources may continue to incur charges.

## Screenshots

See [`docs/screenshots/`](docs/screenshots/) for screenshots of Lambda code, API triggers, IAM policy, dashboard, and EC2 state changes.

## Suggested improvements

- Add API authorization and request validation.
- Add tests and structured logs.
- Deploy resources using AWS SAM, CloudFormation, or Terraform.
- Add GitHub Actions for linting and deployment.
