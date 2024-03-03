import subprocess
import time

#Copiar y pegar en consola lo siguiente  source /opt/ros/humble/setup.bash


file_path = 'Nubes/'

num_mundos = 10

for i in range(num_mundos):

    file_world = 'Mundos/mundo_'+str(i)+'.urdf'

    # Iniciar ign gazebo en un proceso separado sin bloquear el script
    gazebo_process = subprocess.Popen( ['ign', 'gazebo', '-v', '4', '-r', file_world])

    # Ejecutar el comando
    #result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Espera un momento para asegurar que Gazebo inicie correctamente
    time.sleep(10)  # Ajusta este tiempo según necesidad

    # Ejecutar otro comando mientras ign gazebo está corriendo
    #other_command_process = subprocess.Popen(['source', '/opt/ros/humble/setup.bash'], stdout=subprocess.PIPE, text=True)

    # Capturar y mostrar la salida del segundo comando
    #output = other_command_process.communicate()[0]

    #print(output)

    #another_command_process = subprocess.Popen(['ros2','run','ros_gz_bridge','parameter_bridge',
    #                                            '/lidar2@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan',
    #                                            '--ros-args', '-r', '/lidar2:=/laser_scan'], stdout=subprocess.PIPE, text=True)

    #ros2 run ros_gz_bridge parameter_bridge /lidar2@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan --ros-args -r /lidar2:=/laser_scan

    #output1 = another_command_process.communicate()[0]

    print("NEXT")

    #print(output1)

    #time.sleep(5) 
    #Llamada al generador de nubes

    print("Ejecutando nubes")
    nubes_command_process = subprocess.Popen(['python3','prueba8.py',str(i)], stdout=subprocess.PIPE, text=True)
    output2 = nubes_command_process.communicate()[0]

    #print(output2)

    print("Se acabo el programa")
    
    nubes_command_process.terminate()
    nubes_command_process.wait()

    print("nubes terminadas")

    gazebo_process.terminate()
    #another_command_process.terminate()


    gazebo_process.wait()
    #another_command_process.wait()



 
