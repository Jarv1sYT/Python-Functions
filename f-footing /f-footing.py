def dibujar_zapata_columna3D(ancho,base,altura,col_base,col_ancho,col_altura,num_x,sep_x,num_y,sep_y,rec,l_gancho):

    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    # # Dimensiones de la zapata
    # ancho = 2.6
    # base = 2.7
    # altura = 0.4

    # # Dimensiones de la columna
    # col_base = 0.5
    # col_ancho = 0.6
    # col_altura = 1

    # # Parámetros del acero
    # num_x = 5              # Número de varillas en la dirección x
    # sep_x = 13/100          # Espaciado de las varillas en la dirección x

    # num_y = 5              # Número de varillas en la dirección y
    # sep_y = 14/100          # Espaciado de las varillas en la dirección y

    # rec = 0.05              # rec en metros
    # l_gancho = 21 / 100     # Longitud del gancho en metros

    # Definir los vértices de la zapata
    vertices_zapata = np.array([[0, 0, 0],
                                [base, 0, 0],
                                [base, ancho, 0],
                                [0, ancho, 0],
                                [0, 0, altura],
                                [base, 0, altura],
                                [base, ancho, altura],
                                [0, ancho, altura]])

    # Definir las caras de la zapata usando los vértices
    caras_zapata = [
        [vertices_zapata[0], vertices_zapata[1], vertices_zapata[2], vertices_zapata[3]],  # Base
        [vertices_zapata[4], vertices_zapata[5], vertices_zapata[6], vertices_zapata[7]],  # Top
        [vertices_zapata[0], vertices_zapata[1], vertices_zapata[5], vertices_zapata[4]],  # Front
        [vertices_zapata[2], vertices_zapata[3], vertices_zapata[7], vertices_zapata[6]],  # Back
        [vertices_zapata[1], vertices_zapata[2], vertices_zapata[6], vertices_zapata[5]],  # Right
        [vertices_zapata[4], vertices_zapata[7], vertices_zapata[3], vertices_zapata[0]]   # Left
    ]

    # Calcular los vértices de la columna centrada en la zapata
    col_x_offset = (ancho - col_base) / 2
    col_y_offset = (base - col_ancho) / 2
    vertices_columna = np.array([[col_x_offset, col_y_offset, altura],
                                [col_x_offset + col_base, col_y_offset, altura],
                                [col_x_offset + col_base, col_y_offset + col_ancho, altura],
                                [col_x_offset, col_y_offset + col_ancho, altura],
                                [col_x_offset, col_y_offset, altura + col_altura],
                                [col_x_offset + col_base, col_y_offset, altura + col_altura],
                                [col_x_offset + col_base, col_y_offset + col_ancho, altura + col_altura],
                                [col_x_offset, col_y_offset + col_ancho, altura + col_altura]])

    # Definir las caras de la columna usando los vértices
    caras_columna = [
        [vertices_columna[0], vertices_columna[1], vertices_columna[2], vertices_columna[3]],  # Base
        [vertices_columna[4], vertices_columna[5], vertices_columna[6], vertices_columna[7]],  # Top
        [vertices_columna[0], vertices_columna[1], vertices_columna[5], vertices_columna[4]],  # Front
        [vertices_columna[2], vertices_columna[3], vertices_columna[7], vertices_columna[6]],  # Back
        [vertices_columna[1], vertices_columna[2], vertices_columna[6], vertices_columna[5]],  # Right
        [vertices_columna[4], vertices_columna[7], vertices_columna[3], vertices_columna[0]]   # Left
    ]

    # Crear la figura en 3D
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Agregar las caras de la zapata a la figura
    ax.add_collection3d(Poly3DCollection(caras_zapata, facecolors='lightgrey', linewidths=0.5, edgecolors='black', alpha=0.25))

    # Agregar las caras de la columna a la figura
    ax.add_collection3d(Poly3DCollection(caras_columna, facecolors='lightgrey', linewidths=0.5, edgecolors='black', alpha=0.5))

    # Definir las posiciones de las varillas de acero en la zapata
    posiciones_acero_zapata_x = [[x, rec, 0] for x in np.arange(rec, base - rec + sep_x, sep_x)][:num_x]
    posiciones_acero_zapata_y = [[rec, y, 0] for y in np.arange(rec, ancho - rec + sep_y, sep_y)][:num_y]

    # Función para agregar barras de acero con ganchos de 90 grados hacia arriba
    def agregar_barras_acero_con_ganchos(ax, posiciones, altura, l_gancho, color='red', orientacion='vertical'):
        for pos in posiciones:
            x, y, z = pos
            if orientacion == 'vertical':
                ax.plot([x, x], [y, y], [z, z + altura], color=color, linewidth=1)
                ax.plot([x, x], [y, y], [z + altura, z + altura + l_gancho], color=color, linewidth=1)
            elif orientacion == 'horizontal_x':
                ax.plot([x, x + altura], [y, y], [z, z], color=color, linewidth=1)
                ax.plot([x, x], [y, y], [z, z + l_gancho], color=color, linewidth=1)
                ax.plot([x + altura, x + altura], [y, y], [z, z + l_gancho], color=color, linewidth=1)
            elif orientacion == 'horizontal_y':
                ax.plot([x, x], [y, y + altura], [z, z], color=color, linewidth=1)
                ax.plot([x, x], [y, y], [z, z + l_gancho], color=color, linewidth=1)
                ax.plot([x, x], [y + altura, y + altura], [z, z + l_gancho], color=color, linewidth=1)

    # Agregar las barras de acero a la zapata en dirección x con ganchos
    agregar_barras_acero_con_ganchos(ax, posiciones_acero_zapata_x, ancho - 2 * rec, l_gancho, color='red', orientacion='horizontal_y')

    # Agregar las barras de acero a la zapata en dirección y con ganchos
    agregar_barras_acero_con_ganchos(ax, posiciones_acero_zapata_y, base - 2 * rec, l_gancho, color='blue', orientacion='horizontal_x')

    # Configurar los límites de los ejes
    ax.set_xlim([0, base])
    ax.set_ylim([0, ancho])
    ax.set_zlim([0, altura])

    # Configurar la numeración de los ejes
    ax.set_xticks(np.arange(0, base + 0.5, 0.5))
    ax.set_yticks(np.arange(0, ancho + 0.5, 0.5))
    ax.set_zticks(np.arange(0, altura + 0.5, 0.5))

    # Etiquetas de los ejes
    ax.set_xlabel('Base $m$')
    ax.set_ylabel('Ancho $m$')
    ax.set_zlabel('Altura $m$')

    # Ajustar la relación de aspecto de los ejes
    ax.set_box_aspect([base, ancho, altura])  # Relación de aspecto ajustada

    # Modificar el tamaño de la numeración de los ejes x y z
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='z', labelsize=8)

    # Mostrar la gráfica interactiva
    plt.show()
