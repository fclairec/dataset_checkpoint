from datasets.BIMGEOM import BIM
import torch_geometric.transforms as T

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


    BIM("..", "T4", True, transform=T.NormalizeScale())

    a=0
    



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
