# One use case, one workflow

!!! note "Use case modeled as a workflow"
    Core business logic is more stable that framework decisions. Either you are exposing your application via a CLI, RestAPI, gRPC, or even as a Slack/WhatsApp application the business use cases supported should be the same across the Presentation Layer you are using.
    
    Of course, this also applied to whether you are using an specif framework for you API (`FastAPI`, `Django`, `Flask`, etc) or your CLI (`parseargs`, `click`, `Typer`, etc) whatever you decide you use where, should be couple to the core logic of your application.