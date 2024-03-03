import rclpy
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion

def main():
    rclpy.init()

    node = rclpy.create_node('vehicle_position_controller')

    # Publicar en el tópico de posición del modelo
    publisher = node.create_publisher(Pose, '/model/vehicle_blue/cmd_pose', 10)

    # Crear un mensaje Pose para establecer la nueva posición
    pose_msg = Pose()
    pose_msg.position.x = 35.0  # Nueva posición en el eje x
    pose_msg.position.y = 12.0  # Nueva posición en el eje y
    pose_msg.position.z = 0.0  # Nueva posición en el eje z

    # Establecer la orientación (si es necesario) - Aquí un ejemplo con orientación neutral
    pose_msg.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

    # Publicar el mensaje para mover el modelo
    publisher.publish(pose_msg)
    node.get_logger().info('Nueva posición enviada: (%.2f, %.2f, %.2f)' % (pose_msg.position.x, pose_msg.position.y, pose_msg.position.z))

    # Esperar un poco para que el mensaje sea procesado
    rclpy.spin_once(node, timeout_sec=0.5)

    # Cerrar el nodo
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
