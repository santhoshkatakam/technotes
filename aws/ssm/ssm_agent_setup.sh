#!/bin/bash

[ $# -ge 2 ] || exit 1

ActivationCode=$1
ActivationID=$2
Region=us-west-2

echo $ActivationCode
echo $ActivationID
exit 0

sudo stop amazon-ssm-agent
sudo amazon-ssm-agent -register -code $ActivationCode -id $ActivationID -region $Region
sudo start amazon-ssm-agent

