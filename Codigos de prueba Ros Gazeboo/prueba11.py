import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray

class PoseFilterNode(Node):
    def __init__(self):
        super().__init__('pose_filter_node')
        self.subscription = self.create_subscription(
            PoseArray,
            '/world/visualize_lidar_world/pose/info',
            self.pose_callback,
            10)

    def pose_callback(self, msg):
        print(msg.poses[1].position)
        print(msg.poses[1].position.x)
        i=0
       

def main(args=None):
    rclpy.init(args=args)
    node = PoseFilterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
