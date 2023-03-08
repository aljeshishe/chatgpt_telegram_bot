#!/bin/bash
set -ex

curl -X POST "https://api.telegram.org/bot5803765903:AAH2ayWpVcook4JpoiHvMzgOvJCjsLItcmw/sendMessage" -d chat_id=99044115 -d text="preparing environment"
echo "preparing environment"
sudo apt update -y
sudo apt install -y docker.io awscli curl
aws --profile default configure set region eu-central-1
# sudo service docker start

echo running command: ${TASK}
sudo ${TASK}
# docker run -t ubuntu bash -c 'for i in {0..10}; do echo ; sleep 1; done'


echo "stopping instance"
aws cloudformation delete-stack --stack-name ec2scheduler --region eu-central-1
curl -X POST "https://api.telegram.org/bot5803765903:AAH2ayWpVcook4JpoiHvMzgOvJCjsLItcmw/sendMessage" -d chat_id=99044115 -d text="job done"

