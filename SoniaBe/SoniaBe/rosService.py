from rosClient import RosClient
import roslibpy
import Service

class RosService(Service):

    client = RosClient()

    def __init__(self):
        client.runClient()
    
    def get_thruster_info():
        info
        listener = roslibpy.Topic(client.get_ros(),'/provider_thruster/thruster_effort', 'std_msgs/String')
        return listener.subscribe()
        