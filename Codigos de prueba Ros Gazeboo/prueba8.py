import rclpy
from sensor_msgs.msg import LaserScan
import math
import sys  

file_path = 'Nubes/'

class LidarSubscriber:
    def __init__(self, file_suffix):
        self.node = rclpy.create_node('lidar_subscriber')
        self.file_suffix = file_suffix
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

        self.shutdown_node()  # Llamar a shutdown_node para cerrar el nodo y el programa

    def save_to_csv(self, points):
        print("Se saveo")
        # Guardar las coordenadas en un archivo CSV
        file_name = file_path + f'intersection_points_{self.file_suffix}.csv'
        with open(file_name, 'w') as f:
            f.write('x,y\n')
            for point in points:
                f.write(f'{point[0]},{point[1]}\n')
        self.node.get_logger().info(f'Intersection points saved to {file_name}')

    def shutdown_node(self):
        sys.exit(0)
        # Método para cerrar el nodo correctamente
        self.node.get_logger().info('Shutting down node.')
        self.node.destroy_node()
        rclpy.shutdown()
        

def main(args=None):
    rclpy.init(args=args)
    # Verificar si se pasó un argumento y usar 'default' como sufijo si no se pasó ninguno
    file_suffix = sys.argv[1] if len(sys.argv) > 1 else 'default'
    lidar_subscriber = LidarSubscriber(file_suffix)
    rclpy.spin_once(lidar_subscriber.node)
    #rclpy.shutdown()

if __name__ == '__main__':
    main()
