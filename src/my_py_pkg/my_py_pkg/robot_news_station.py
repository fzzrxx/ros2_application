#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStation(Node):
    def __init__(self):
        super().__init__("py_RobotNewsStation")
        self.robot_name = "RetardRobo333"
        self.publisher_ = self.create_publisher(String,
                                                "robot_news", 10)
        self.timer = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot news station has been started")
        
    def publish_news(self):
        msg = String()
        msg.data = "Hello, " + self.robot_name + ", this is weird, I know."
        self.publisher_.publish(msg)
        

def main(args = None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()