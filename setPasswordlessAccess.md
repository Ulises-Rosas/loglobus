# Passwordless access to clusters

This procedure should be done for each cluster


## Requirements

* ssh
* ssh-keygen (usually this comes with ssh installation)
* ssh-copy-id (usually this comes with ssh installation)

### Create a key file without a password 

```
ssh-keygen
```
```
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/admin/.ssh/id_rsa): mykey
Enter passphrase (empty for no passphrase): [press enter]
Enter same passphrase again: [press enter]
```
### Copy the recently created key into the cluster

```
ssh-copy-id -i mykey [userid]@[host]
```

### Test key file

```
ssh -i mykey [userid]@[host]
```

Source: [**askubuntu.com**](https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login)

