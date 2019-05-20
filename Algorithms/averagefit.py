def averagefit(grid, b, h):
    for key in b:
        count = 1
        backcount = 150
        while b[key].filled < b[key].capacity:
            if count > 150 or backcount < 1:
                break
            if h[count].output + h[backcount].output + b[key].filled < b[key].capacity:
                if h[count].pluggedin is not False:
                    count += 1
                elif h[backcount].pluggedin is not False:
                    backcount -= 1
                else:
                    b[key].connected.append(h[count])
                    b[key].connected.append(h[backcount])
                    b[key].filled += h[count].output + h[backcount].output
                    h[count].pluggedin = b[key]
                    h[backcount].pluggedin = b[key]
                    count += 1
                    backcount -= 1
            else:
                count += 1
    for house in h:
        print(h[house].pluggedin)
