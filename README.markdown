# tsuru-django-sample

This is the example project used in the guide ["Deploying Python applications in tsuru"](https://docs.tsuru.io/stable/using/python.html).

## Configuration

Before deploying this app to tsuru, you need to add the host/domain name to `ALLOWED_HOSTS` configuration in `blog/settings.py`:

```
ALLOWED_HOSTS = ['my-app.cloud.example.com']
```
