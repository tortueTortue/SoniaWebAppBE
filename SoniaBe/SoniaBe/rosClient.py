import roslibpy

class RosClient:

	def __init__(self, port, host, name):
		self.__port = port
		self.__host = host
		self.__name = name
		self.client = roslibpy.Ros(host=self.__port, port=self.__port)

	def runClient(self):
		self.client.run()

	def terminateClient(self):
		self.client.terminate()

	def get_port(self):
		return self.__port

	def get_ros(self):
		return self.client

	def get_host(self):
		return self.__host

	def get_name(self):
		return self.__name

	def get_is_ros_connected(self):
		return self.client.is_connected

	def __str__(self):
 		return "port: " + self.__name + " , " + "host: " + self.__name + " , " + "name: " + self.__name
