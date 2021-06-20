import boto3

client = boto3.client('batch', "us-east-2")


# Probably doesn't need to be run, just encoding this stuff programatically, as the job queue will likely already exist
def create_compute_environment(subnets, securityGroupIds, instanceRole, serviceRole):
    # subnets, securityGroupIds must be arrays of strings, instanceRole, serviceRole must be strings (of IAM looking things)
    response = client.create_compute_environment(
        computeEnvironmentName='clockworkfinance3', # this looks awful but  there's a stupid bug so I can't use 2 or no number
        type='MANAGED',
        state='ENABLED',
        computeResources={
            'type': 'SPOT',
            'allocationStrategy': 'SPOT_CAPACITY_OPTIMIZED',
            'minvCpus': 0,
            'maxvCpus': 256,
            'instanceTypes': [
                'c5',
            ],
            'subnets': subnets,
            'securityGroupIds': securityGroupIds,
            'instanceRole': instanceRole,
            'tags': {
                'user': 'sasha'
            },
        },
        serviceRole=serviceRole,
        tags={
            'user': 'sasha'
        }
    )
    return response

# Probably doesn't need to be run, just encoding programatically
def create_job_queue():
    response = client.create_job_queue(
        jobQueueName='cffjobqueue',
        state='ENABLED',
        priority=1,
        computeEnvironmentOrder=[
            {
                'order': 1,
                'computeEnvironment': 'clockworkfinance3'
            },
        ]
    )
    return response

# Probably doesn't need to be run, just encoding programatically
def create_job_definition(url): # url must be string
    response = client.register_job_definition(
        jobDefinitionName='cffjob',
        type='container',
        containerProperties={
            'image': 'meatwadsprite/kprove-batch:test',
            'vcpus': 1,
            'memory': 2048,
            'command': [
                "python3",
                "../kprove_batch/batch_worker_python.py",
                url,
            ]
        },
    )
    return response

# N must be greater than 2
def submit_job(N):
    response = client.submit_job(
        jobName='cffArrayJob',
        jobQueue='cffjobqueue',
        arrayProperties={
            'size': N
        },
        jobDefinition='cffjob',
        retryStrategy={
            'attempts': 1
        }
    )
    return response
