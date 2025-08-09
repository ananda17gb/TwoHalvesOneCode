def sort_array(source_array):
    print(source_array)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            min = i
            for j in range(i+1,len(source_array)):
                if source_array[j] % 2 != 0:
                    if source_array[j] < source_array[min]:
                        min = j
            source_array[i],source_array[min] = source_array[min],source_array[i]
    return source_array
        
