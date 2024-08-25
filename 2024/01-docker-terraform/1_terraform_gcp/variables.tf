variable "credentials" {
  description = "Terraform project service account key"
  default     = "./keys/tf_demo_service_account.json"
}

variable "project" {
  description = "My Terraform project"
  default     = "terraform-demo-433517"
}

variable "region" {
  description = "Project region"
  default     = "europe-west9-a"
}

variable "location" {
  description = "Bucket location"
  default     = "EUROPE-WEST9"
}

variable "bucket" {
  description = "Terraform project bucket name"
  default     = "terraform-demo-433517-terra-bucket"
}

variable "big-query-name" {
  description = "Terraform project Big query name"
  default     = "terraform_demo_433517_terra_big_query"
}

