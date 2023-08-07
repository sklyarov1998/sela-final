## Make sure to create a Secret for the DB Credentials. Create a file ./templates/db-secret.yaml using the following template:

```
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  db-password: <enterYourDBPasswordHere>

```

## To activate the Secret in your Cluster run the following command:

```
kubectl apply -f db-secret.yaml
```

## Alternatively you can supply the Secret directly to the Cluster running:

```
kubectl create secret generic db-secret --from-literal=db-password="enterYourDBPasswordHere"

```
