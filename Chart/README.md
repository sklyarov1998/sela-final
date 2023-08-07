## Create a Secret for the DB Credentials using the following template:

```
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  db-password: <enterYourDBPassword>

```
