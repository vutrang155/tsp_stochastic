from TSP import TSP
if __name__ == '__main__':
    filename = 'berlin52'
    m = TSP(filename+'.tsp')

    # Generate distance matrix
    n = m.dimension
    D = m.distance_matrix()

    # Write to dat
    f = open(filename+".dat", "w")
    f.write("n = "+str(n)+";\n")
    f.write("C = [")
    for i in range(n):
        f.write("[")
        for j in range(n):
            f.write(str(D[i, j]))
            if j != n-1:
                f.write(",")
        f.write("]")
        if i != n-1:
            f.write(",\n\t")
    f.write("];")
    f.close()
