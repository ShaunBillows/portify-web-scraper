import tabulate

def print_table(dataset):
    if dataset:
        header = dataset[0].keys()
        rows =  [x.values() for x in dataset]
        print(tabulate.tabulate(rows, header))
        