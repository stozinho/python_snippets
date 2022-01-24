from datetime import datetime 

# isoformat 
today = datetime.utcnow().isoformat()

date_for_filename = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")

# argparse 
parser = argparse.ArgumentParser(description="This script will query ssm & EC2 for the latest AL2 AMIs. It will check that they are older than our threshold date (i.e. the bed in date for the AMI). By default it will print the vars to stdout, or if 'write' flag set it will update the relevant Ansible vars file with the relevant AMI names, if they are old enough.")
parser.add_argument('--repo_location', dest='repo_location', default='.')
parser.add_argument('--write', dest='write_to_file', action='store_true')
parser.set_defaults(write=True)
args = parser.parse_args()
