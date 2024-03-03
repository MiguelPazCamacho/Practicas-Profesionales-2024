import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2

class LidarFilterNode(Node):
    def __init__(self):
        super().__init__('lidar_filter_node')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/point_cloud',
            self.lidar_callback,
            10)
        self.subscription  # prevent unused variable warning

    def lidar_callback(self, msg):
        # Convertir PointCloud2 a una lista de puntos
        points_list = list(pc2.read_points(msg, skip_nans=True))

        #self.get_logger().info(f'Ranges: {msg.ranges}')
        print("-",points_list)
        # Procesar los puntos aquí (por ejemplo, quitar intensidades si están presentes)
        # Esto depende del formato específico de tus datos PointCloud2
        
        # Haz algo con los puntos procesados
        # Por ejemplo, imprimirlos, guardarlos o publicarlos en un nuevo tópico

def main(args=None):
    print("inicio")
    rclpy.init(args=args)
    node = LidarFilterNode()
    rclpy.spin(node)
    rclpy.shutdown()
    print("fin")

if __name__ == '__main__':
    main()
