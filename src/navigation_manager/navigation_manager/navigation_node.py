#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.get_logger().info("Navigation Manager Node elindult")

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

