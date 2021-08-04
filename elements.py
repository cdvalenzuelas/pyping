elements = [
            {
                'id': 1,
                'type': 'PIPE',
                'Id': 50,
                'node_1': (6, 300, 300, 0),
                'node_2': (7, 400, 300, 0),
            },
            {   
                'id': 2,
                'type': 'PIPE',
                'Id': 100,
                'node_1': (1, 0, 0, 0),
                'node_2': (2, 100, 0, 0),                
            },
            {
                'id': 3,
                'type': 'RESERVORY',
                'P': 150,
                'Q': (0, 2000), #Min, Max
                'node': 1          
            },
            {   
                'id': 4,
                'type': 'PIPE',
                'Id': 50,
                'node_1': (4, 200, 200, 0),
                'node_2': (5, 200, 300, 0),                
            },
            {
                'id': 5,
                'type': 'SPRINKLER',
                'K': 11.2,
                'Q': (None, None, None), #Requerido, Min, Max
                'P': (None, None), #Entrada, Min, Max
                'node': 7,                
            },
            {
                'id': 6,
                'type': 'ELBOW',
                'Id': 100,
                'node_1': (2, 100, 0, 0),
                'node_2': (3, 200, 100, 0),                     
                'angle': 100,  
            },
            {
                'id': 7,
                'type': 'ELBOW',
                'Id': 50,
                'node_1': (5, 200, 200, 0),
                'node_2': (6, 300, 300, 0),
                'angle': 100,
            },
            {
                'id': 8,
                'type': 'RED_CONC',                
                'node_1': (3, 200, 100, 0, 100),
                'node_2': (4, 200, 200, 0, 50),
            },
]
