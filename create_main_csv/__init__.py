import re

def create_main_csv():
    output_file = open(file = './line_numbers/output_file.csv', mode='w', encoding='utf8')    
    output_file.write('ELEMENT,DESCRIPTION,x_1,y_1,z_1,d_1,j_1,x_2,y_2,z_2,d_2,j_2,c_x,c_y,c_z,b_x,b_y,b_z,b_d,angle\n')

    with open(file = './line_numbers/zvcbzbc.pcf', mode='r', encoding='utf8') as f:

        element = ''
        description = ''
        x_1, y_1, z_1, d_1, j_1 = ("", "", "", "", "")
        x_2, y_2, z_2, d_2, j_2 = ("", "", "", "", "")
        b_x, b_y, b_z, b_d, b_d  = ("", "", "", "", "")
        c_x, c_y, c_z = ("", "", "")    
        angle = ""   

        


        element_expression = re.compile('^(ELBOW|PIPE|TEE|FLANGE|GASKET|OLET)\n')
        no_element_expression = re.compile('^(WELD|BOLT)\n')
        node_expression = re.compile('^\s+(CENTRE|END|BRANCH1)-POINT\s+(\d+).\d+\s+(\d+).\d+\s+(\d+).\d+\s{0,}(\d{0,}.\d{0,})\s{0,}(\w{0,})\n')        
        description_expression =  re.compile('^\s+ITEM-DESCRIPTION\s+([\w\s,.#"\/]+)\n')        
        angle_expression = re.compile('^\s+ANGLE\s+(\d+)\n')

        first_coincidence = False
        founded = False
        end_point_counter = 1


        for line in f:
            #Si se encuentra con la palabra MATERIALS se corta el programa
            if line == 'MATERIALS\n':                               
                output_file.write(f'{element},\"{description}\",{x_1},{y_1},{z_1},{d_1},{j_1},{x_2},{y_2},{z_2},{d_2},{j_2},{c_x},{c_y},{c_z},{b_x},{b_y},{b_z},{b_d},{b_j},{angle}\n')
                output_file.close()                
                f.close()
                break                 

            if first_coincidence and element_expression.match(line):
                output_file.write(f'{element},\"{description}\",{x_1},{y_1},{z_1},{d_1},{j_1},{x_2},{y_2},{z_2},{d_2},{j_2},{c_x},{c_y},{c_z},{b_x},{b_y},{b_z},{b_d},{b_j},{angle}\n')                                  
                founded = False

            if element_expression.match(line) and first_coincidence == False:
                first_coincidence = True             


            #Si first_coincidence es false aún no se hace nada
            if not first_coincidence:
                continue                
                
            if element_expression.match(line):                        
                element = element_expression.search(line).group(1)
                founded = True

                x_1, y_1, z_1, d_1, j_1 = ("", "", "", "", "")
                x_2, y_2, z_2, d_2, j_2 = ("", "", "", "", "")
                b_x, b_y, b_z, b_d, b_j  = ("", "", "", "", "")
                c_x, c_y, c_z = ("", "", "")
                angle = ""
                end_point_counter = 1     
            elif no_element_expression.match(line):                
                founded = False
            elif description_expression.match(line) and founded:                                             
                description = description_expression.search(line).group(1)                
                description = description.replace('"', ' in')
            elif node_expression.match(line) and founded:                
                node_type = node_expression.search(line).group(1)
                x = node_expression.search(line).group(2)
                y = node_expression.search(line).group(3)
                z = node_expression.search(line).group(4)
                d = node_expression.search(line).group(5)
                j = node_expression.search(line).group(6)                

                if node_type == 'END':
                    if end_point_counter == 1:
                        x_1, y_1, z_1, d_1, j_1 = (x, y, z, d, j) 
                        end_point_counter +=1
                    elif end_point_counter ==2:
                        x_2, y_2, z_2, d_2, j_2 = (x, y, z, d, j)
                elif node_type == 'CENTRE':
                    c_x, c_y, c_z = (x, y, z)
                elif node_type == 'BRANCH1':
                    b_x, b_y, b_z, b_d, b_j = (x, y, z, d, j)
            elif angle_expression.match(line) and founded:               
                angle = int(angle_expression.search(line).group(1))/100  