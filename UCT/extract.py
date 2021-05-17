#Rob Haynes
#10 May 2021

def location(block):
    if block.find("S ",6) != -1:
        index = block.find("S ",6) + 2
    else:
        index = block.find("N ",6) + 2
    
    location_back = block[index : len(block)-4]
    location = ""

    for x in range(len(location_back)-1,-1,-1):
        if len(location) != 0:
            if location[len(location)-1] == ' ':
                location = location + location_back[x]
            else:
                location = location + location_back[x].lower()
        else:
            location = location + location_back[x]

    return location

def temperature(block):
    temp = eval(block[6 : block.find("_")])
    return float(temp)

def x_coordinate(block):
    if block.find("E,",6) != -1:
        return block[block.find(":")+1 : block.find("E,",6)+1]
    else:
        return block[block.find(":")+1 : block.find("W,",6)+1]

def y_coordinate(block):
    if block.find("S ",6) != -1:
        return block[block.find(",")+1 : block.find("S ",6)+1]
    else:
        return block[block.find(",")+1 : block.find("N ",6)+1]

def pressure(block):
    pres = eval(block[block.find("_")+1 : block.find(":")])
    return float(pres)

def get_block(data):
    x = int(data.find("BEGIN"))
    y = int(data.find("END") + 3)

    return data[x:y]

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
