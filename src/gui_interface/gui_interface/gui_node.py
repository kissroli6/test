#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class GuiNode(Node):
    def __init__(self):
        super().__init__('gui_node')
        self.get_logger().info("GUI Node elindult - itt majd célokat adhatsz meg")

def main(args=None):
    rclpy.init(args=args)
    node = GuiNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

