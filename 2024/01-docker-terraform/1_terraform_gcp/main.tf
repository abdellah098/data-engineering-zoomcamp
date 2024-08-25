terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.42.0"
    }
  }
}

# set GOOGLE_CREDENTIAS env variable 
provider "google" {
  project = "terraform-demo-433517"
  region  = "europe-west9-a"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-433517-terra-bucket"
  location      = "EUROPE-WEST9"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}