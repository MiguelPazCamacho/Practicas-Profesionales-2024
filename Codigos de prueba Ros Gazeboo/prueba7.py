import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
import time

class ContinuousPositionPublisher(Node):
    def __init__(self):
        super().__init__('continuous_position_publisher')
        self.publisher = self.create_publisher(Pose, '/model/vehicle_blue/cmd_pose', 10)
        self.timer_period = 1.0  # segundos
        self.timer = self.create_timer(self.timer_period, self.update_position)
        self.x_position = 0.0

    def update_position(self):
        pose_msg = Pose()
        pose_msg.position.x = self.x_position
        pose_msg.position.y = 0.0  # Mantener constante en este ejemplo
        pose_msg.position.z = 0.0  # Mantener constante en este ejemplo
        pose_msg.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)  # Orientación neutral

        self.publisher.publish(pose_msg)
        self.get_logger().info('Publicando nueva posición: (%.2f, %.2f, %.2f)' % (pose_msg.position.x, pose_msg.position.y, pose_msg.position.z))

        self.x_position += 0.5  # Incrementar la posición en x para el siguiente mensaje

def main(args=None):
    rclpy.init(args=args)
    continuous_position_publisher = ContinuousPositionPublisher()

    try:
        rclpy.spin(continuous_position_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        continuous_position_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
