OpenShift Dynatrace Agent cartridge
===================================

An embedded cartridge to enable Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges (AS,EAP,EWS).


Requirements
------------

- OpenShift JBoss AS/EAP/EWS as primary cartridge.


Install
-------

- Install the cartridge from GitHub.

```
  rhc add-cartridge -a <your_app_name> \
    -e DYNATRACE_COLLECTOR=<your_dynatrace_collector> \
    -e DYNATRACE_AGENT_NAME=<your_agent_name> \
    -c <git_server_of_cartridge>/latest/metadata/manifest.yml
```

- Restart your application.

```
  rhc app restart <your_app_name>
```

Remove
------

```
  rhc cartridge-remove dynatrace-agent -a <your_app_name>
```

Known Issues
------------

* A **JAVA\_OPTS\_EXT** user defined environment variable will override the one defined by the cartridge, so you could inadvertently disable the agent.
