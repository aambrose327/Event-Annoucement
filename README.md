# Event-Annoucement

Develop an event announcement website that allows users to:
- Subscribe to event notifications via email.
- View a list of events.
- Create new events through a form.

Upload the HTML, CSS, and events.json files to S3 and enable static hosting to access the website URL.
Set up an API Gateway to handle backend processing for creating new events on /create-event and adding subscribers on/subscribe. 
Subscription Lambda adds new subscriber emails to the SNS topic.
Event Registration Lambda updates events.json in S3 with new event details submitted from the website form and sends notifications via SNS.

Services Used 
1. AWS S3: Host the frontend and store event data in a JSON file.[Frontend Hosting & Storage]
2. AWS SNS: Manage email subscriptions and send event notifications.[Notifications]
3. AWS Lambda: Handle backend logic for creating events and managing subscriptions.[Backend Processing]
4. AWS API Gateway: Provide endpoints for frontend to communicate with backend services.[API Management]
5. IAM Roles & Policies: Secure access to AWS resources like S3 and SNS.[Permissions]

Architecture Diagram ✍️:
<img width="1281" height="540" alt="image" src="https://github.com/user-attachments/assets/200a317a-e7dc-4a5d-9535-65b10818351d" />

Steps to be Performed 👩‍💻
1. Set up frontend hosting with S3
2. Integrate SNS Notifications and Lambda Functions
3. Setup, Test and Deploy the API Gateway
4. Test and Finalize


