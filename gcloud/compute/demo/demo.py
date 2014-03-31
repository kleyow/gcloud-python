# Welcome to the gCloud Compute Demo! (hit enter)

# We're going to walk through some of the basics...,
# Don't worry though. You don't need to do anything, just keep hitting enter...

# Let's start by importing the demo module and getting a connection:
from gcloud.compute import demo
connection = demo.get_connection()

# OK, now let's retrieve an instance
# instance = connection.get_instance('gcloud-computeengine-instance',
#                                   'us-central1-b')

# Let us give that instance a reset - Got the reset!
# instance.reset()
# connection.get_aggregatedDiskList()
# connection.get_diskList('us-central1-b')
# connection.delete_disk('disk-1','us-central1-b')
# connection.create_snapshot('gcloud-computeengine-instance','us-central1-b')
# disk = connection.get_disk('gcloud-computeengine-instance','us-central1-b')
# disk.snapshot()
# Thats it for now more is coming soon
