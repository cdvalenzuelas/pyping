import re

def run():
    dummy = open(file = './line_numbers/dummy.csv', mode='w', encoding='utf8')
    dummy2 = open(file = './line_numbers/dummy.txt', mode='w', encoding='utf8')
    dummy.write('ELEMENT,  DESCRIPTION\n')

    with open(file = './line_numbers/zvcbzbc.pcf', mode='r', encoding='utf8') as f:

        element = ''
        element_expression = re.compile('^(ELBOW|PIPE|TEE|FLANGE|GASKET)\n')
        no_element_expression = re.compile('^(WELD)\n')
        end_point_expression = re.compile('^\s+END-POINT\s+(\d+).\d+\s+(\d+).\d+\s+(\d)+.\d+\s+(\d+.\d+)\s{0,}(\w{0,})\n')
        description = ''
        description_expression =  re.compile('^\s+ITEM-DESCRIPTION\s+([\w\s,.#"\/]+)\n')        

        first_coincidence = False
        founded = False

        for line in f:
            #Si se encuentra con la palabra MATERIALS se corta el programa
            if line == 'MATERIALS\n':                
                dummy.write(f'{element}, {description}\n')                
                dummy.close()
                dummy2.close()
                f.close()
                break

            if no_element_expression.match(line):
                continue      

            if element_expression.match(line) and first_coincidence == False:
                first_coincidence = True             

            if first_coincidence and element_expression.match(line) and founded:
                dummy.write(f'{element}, {description}\n')
                founded = False

            #Si first_coincidence es false aún no se hace nada
            if not first_coincidence:
                continue                
                
            if element_expression.match(line):                        
                element = element_expression.search(line).group(1)
                founded = True
                dummy2.write(line)            
            elif description_expression.match(line) and founded:    
                dummy2.write(line)                           
                description = description_expression.search(line).group(1)                
                description = description.replace(',', '')
            elif end_point_expression.match(line) and founded:
                dummy2.write(line)    
                x_1 = end_point_expression.search(line).group(1)
                y_1 = end_point_expression.search(line).group(2)
                z_1 = end_point_expression.search(line).group(3)
                diameter = end_point_expression.search(line).group(4)
                #print(f'x_1: {x_1}, y_1: {y_1}, z_1: {z_1}, diameter: {diameter}')                           
            else:
                dummy2.write("\n")                

if __name__ == '__main__':
    run()