import json
import os

import boto3
from flask import redirect, url_for, request
from flask_login import current_user

# from app import app
#
#
# @app.route("/sign_s3")
# def sign_s3():
#     S3_BUCKET = os.environ.get("S3_BUCKET")
#     file_name = request.args.get("file_name")
#     file_type = request.args.get("file_type")
#     s3 = boto3.client("s3")
#     presigned_post = s3.generate_presigned_post(
#         Bucket=S3_BUCKET,
#         Key=file_name,
#         Fields={"acl": "public-read", "Content-Type": file_type},
#         Conditions=[{"acl": "public-read"}, {"Content-Type": file_type},],
#         ExpiresIn=3600,
#     )
#     return json.dumps(
#         {
#             "data": presigned_post,
#             "url": f"https://{S3_BUCKET}.s3.amazonaws.com/{file_name}",
#         }
#     )
#
#
# @app.route("/submit_form/", methods=["POST"])
# def submit_form():
#     avatar_url = request.form["avatar-url"]
#
#     # Save image url to db
#
#     return redirect(url_for("user", username=current_user.username))
