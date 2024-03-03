import rclpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped  # Cambiado de Pose a PoseStamped
from geometry_msgs.msg import PoseArray
import math
import sys

file_path = 'Nubes/mundo_81/'

class LidarPoseSubscriber:
    def __init__(self, file_suffix):
        self.node = rclpy.create_node('lidar_pose_subscriber')
        self.file_suffix = file_suffix
        self.robot_x = None
        self.robot_y = None
        self.robot_z = None  # Agregado para la posición en Z
        self.intersection_points = None
        self.iter = 0
        self.lidar_subscription = self.node.create_subscription(
            LaserScan,
            '/laser_scan',
            self.lidar_callback,
            10)
        self.pose_subscription = self.node.create_subscription(
            PoseArray,
            '/world/visualize_lidar_world/pose/info',
            self.pose_callback,
            10)
        self.node.get_logger().info('Lidar and Pose subscriber node is running.')


    def lidar_callback(self, msg):
        # Procesar datos del LIDAR
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        angle_increment = msg.angle_increment
        ranges = msg.ranges
        intersection_points = [(ranges[i] * math.cos(angle_min + i * angle_increment),
                                ranges[i] * math.sin(angle_min + i * angle_increment)) for i in range(len(ranges))]
        # Almacenar los puntos de intersección para su uso posterior
        self.intersection_points = intersection_points
        # Intentar guardar los datos si la posición del robot está disponible
        self.try_save_data()

    def pose_callback(self, msg):
        # Actualizar la posición del robot usando PoseStamped
        self.robot_x = msg.poses[1].position.x
        self.robot_y = msg.poses[1].position.y
        self.robot_z = msg.poses[1].position.z  # Ahora también se captura la posición en Z
        self.try_save_data()

    def try_save_data(self):
        # Verificar si tanto la posición como los puntos de intersección están disponibles
        #print("Se intenta",self.intersection_points)
        if self.robot_x is not None and self.robot_y is not None and self.intersection_points is not None:
            self.save_to_csv()
            # Opcional: reiniciar los datos para evitar guardar múltiples veces los mismos datos
            self.robot_x = None
            self.robot_y = None
            
            self.intersection_points = None

    def save_to_csv(self):
        # Guardar la posición del robot y los puntos de intersección en un archivo CSV
        file_name = file_path + f'intersection_points_{self.iter}.csv'
        #print(f'Robot Position,{self.robot_x},{self.robot_y}\n')
        with open(file_name, 'w') as f:
            
            f.write('x,y\n')
            f.write(f'{self.robot_x},{self.robot_y}\n')
            print(f'{self.robot_x},{self.robot_y}\n')
            for point in self.intersection_points:
                f.write(f'{point[0]},{point[1]}\n')
        self.node.get_logger().info(f'Data saved to {file_name}')
        self.iter = self.iter+1

    def shutdown_node(self):
        # Método para cerrar el nodo correctamente
        self.node.get_logger().info('Shutting down node.')
        self.node.destroy_node()
        rclpy.shutdown()
        sys.exit(0)

def main(args=None):
    rclpy.init(args=args)
    file_suffix = sys.argv[1] if len(sys.argv) > 1 else 'default'
    subscriber = LidarPoseSubscriber(file_suffix)
    rclpy.spin(subscriber.node)

if __name__ == '__main__':
    main()
