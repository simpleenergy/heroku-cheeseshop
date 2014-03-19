Run your own pypi on heroku.

This repo is meant to be a skeleton repository for running
[localshop](https://pypi.python.org/pypi/localshop) on heroku using Amazon Web
Services to host the files.


# Installation

1. Pull or Fork this repository

```bash
$ git clone <url> my_cheeshop
```

2. Setup a new heroku app and add the git remote.


```bash
$ cd my_cheeshop
$ heroku git:remote add --app=<heroku_app_name>
```

3. Add a real database to your herkoku app.

```bash
$ heroku addons:add heroku-postgresql
$ heroku config:set DATABASE_URL='<your_heroku_database_url>'
```

4. Setup AWS credentials

The following IAM policy works nicely.

```json
{
   "Statement":[
      {
         "Effect":"Allow",
       
         "Action":[
            "s3:ListAllMyBuckets"
         ],
         "Resource":"arn:aws:s3:::*"
      },
      {
         "Effect":"Allow",
         "Action":[
            "s3:ListBucket",
            "s3:GetBucketLocation"
         ],
         "Resource":"arn:aws:s3:::bucket-name"
      },
      {
         "Effect":"Allow",
         "Action":[
            "s3:*Object*"
         ],
         "Resource":"arn:aws:s3:::bucket-name/*"
      }
   ]
}
```

5. Add the AWS credentials to heroku

```bash
$ heroku config:set AWS_ACCESS_KEY_ID='<aws_access_key>'
$ heroku config:set AWS_SECRET_ACCESS_KEY='<aws_secret_key>'
$ heroku config:set AWS_STORAGE_BUCKET_NAME='<aws_bucket_name>'
```

6. Add a secret key to heroku

```bash
$ heroku config:set LOCALSHOP_SECRET_KEY='<django_secret_key>'
```

7. Push the repo to your heroku app.

```bash
$ git push heroku master
```

8. Initialize Localshop on heroku

```bash
$ heroku run localshop init
```

9. Profit!

Localshop should be up and running on your heroku app.
