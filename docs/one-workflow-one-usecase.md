# One workflow, one use case

To me, one of best ways to think about a use case is that each one of these **must satisfy one and only one requirement your software may have.** For example, let's say we are building a lending application, some use cases that must be satisfied by the applications are:

- `open loan` -> As a user I want to open a loans to my clients.
- `pay loan` -> As a user I want to registry a loan payments made by my clients.

Ok, so ***one workflow, one use case*** means that a use case can easily be thought as an orchestrated workflow that **interacts with the application database and/or other services** (for me, a service means a third party application I want to interact with). Let's think about the workflow for the two use cases we need for our application.


```mermaid
flowchart
    id1[(Denotes interaction with database)]
```
```mermaid
flowchart
    id1(Denotes in memory transformation)
```
```mermaid
flowchart
    id1{{Denotes interaction with service}}
```

1. **Open Loan** use case.
```mermaid
flowchart LR
    Start --> id1[(insert_loan)] --> id2{{send_notification_via_email}} --> End
```

1. **Pay Loan** use case.
```mermaid
flowchart LR
    Start --> id1[(get_loan)] --> id2(add_payment_to_loan) --> id3[(update_loan)] --> id4{{send_notification_via_email}} --> End
```

This abstraction is easily extensible, assume we want to send some data to another service... well you just have to add a new step on your workflow use cases.
