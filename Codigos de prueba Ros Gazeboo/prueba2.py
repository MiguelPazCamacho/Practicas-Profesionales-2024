import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            '/laser_scan',  # Cambiar el nombre del tópico
            self.lidar_callback,
            10)
        self.subscription  # evitar que se elimine la suscripción inmediatamente

    def lidar_callback(self, msg):
        self.get_logger().info('LaserScan data:')
        self.get_logger().info(f'Ranges: {msg.ranges}')
        #self.get_logger().info(f'Intensities: %s {str(msg.intensities)}')


def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)
    lidar_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
