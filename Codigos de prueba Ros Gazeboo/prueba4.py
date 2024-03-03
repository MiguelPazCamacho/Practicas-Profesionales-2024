import rclpy
from sensor_msgs.msg import LaserScan
import math

file_path = "Nubes/"

class LidarSubscriber:
    def __init__(self):
        self.node = rclpy.create_node('lidar_subscriber')
        self.subscription = self.node.create_subscription(
            LaserScan,
            '/laser_scan',
            self.lidar_callback,
            10)
        self.node.get_logger().info('Lidar subscriber node is running.')

    def lidar_callback(self, msg):
        print("Callback")
        # Obtener los ángulos mínimo y máximo del escaneo
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        # Calcular el ángulo de paso entre cada medida
        angle_increment = msg.angle_increment
        # Obtener las distancias medidas por el Lidar
        ranges = msg.ranges
        # Inicializar una lista para almacenar las coordenadas (x, y) de los puntos de intersección
        intersection_points = []
        # Iterar sobre las distancias medidas y calcular las coordenadas (x, y)
        for i in range(len(ranges)):
            # Calcular el ángulo actual
            angle = angle_min + i * angle_increment
            # Calcular las coordenadas (x, y) del punto de intersección
            x = ranges[i] * math.cos(angle)
            y = ranges[i] * math.sin(angle)
            intersection_points.append((x, y))
        # Guardar las coordenadas en un archivo CSV
        self.save_to_csv(intersection_points)

    def save_to_csv(self, points):
        print("Se saveo")
        # Guardar las coordenadas en un archivo CSV
        with open(file_path+'intersection_pointshhhhhhhhhhhhhhh.csv', 'w') as f:
            f.write('x,y\n')
            for point in points:
                f.write(f'{point[0]},{point[1]}\n')
        self.node.get_logger().info('Intersection points saved to intersection_points.csv.')

def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
