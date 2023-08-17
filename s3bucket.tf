provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "s3bucket" {
    bucket = "weather"
    acl = "public"
    versioning{
        enabled = true
    }
}