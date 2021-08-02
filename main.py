from element_classes.Pipe import Pipe
from element_classes.RedConc import RedConc


my_pipe_dict = {
    'type': 'PIPE',
    'Id': 50,
    'node_1': (6, 0, 0, 0),
    'node_2': (7, 0, 0, 10),
}


my_red_conc_dict = {
    'type': 'RED_CONC',
    'node_1': (3, 200, 100, 0, 100),
    'node_2': (4, 200, 200, 0, 20),
}


#from create_main_csv import create_main_csv

if __name__ == '__main__':
    # create_main_csv()
    my_pipe = Pipe(pipe_dict=my_pipe_dict, fluid_dict={'rho': 1000})
    response_1 = my_pipe.get_info(Q=100000, P_1=150000)
    print(response_1)

    my_red_conc = RedConc(pipe_dict=my_red_conc_dict, fluid_dict={'rho': 1000})
    response_2 = my_red_conc.get_info(Q=100000, P_1=150000)
    print(response_2)
