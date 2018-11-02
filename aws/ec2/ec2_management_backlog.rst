AWS EC2 Infrastructure Backlog
==============================

Adapted from Ashley's AWS Infrastructure Backlog with just stuff specific
to EC2 management




EC2 Management in Legacy Data Center and elsewhere
--------------------------------------------------

- archetectural review

  - vpc/subnet layout
  - perimeter security
  - DNS/route53
  - loadbalancers

- ensure existing (on-prem) system mgmt tools work reliably

  - puppet
  - ansible
  - sccm
  - AD/Centrify
  - UIM

- ensure AWS system mgmt tools work reliably

  - ssm
  - nakivo
  - system log aggregation to s3

- PCSSC integration

  - control-m
  - goanywhere

- ec2 instance tagging

  - determine required tags
  - enforce tagging compliance
  - integration with CMDB

- security tools

  - idp
  - waf
  - firewall
  - siem/qRadar
  - ssl cert management

- Config Rules

  - ensure ebs volume encryption at rest
  - ensure ec2 instances built from compliant AMI
  - ensure ec2 instances are at current patch levels

- ec2 instance build process

  - intake workflow
  - build proceedure

    - automated instance builder tools
    - IP address assignment
    - DNS configuration

  - template AMIs

    - leveage Eric's Salami Factory AMI builder
    - template image requirements

      - tags
      - central logging config
      - OS hardening
      - AD access
      - system management agents

         - ssm
         - sccm
         - puppet


- maintain repository of UCOP standardized ec2 AMI
- develop SSM service to manage running ec2 instances
