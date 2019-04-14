
class Averagefit():
    def averagefit(grid):
        for key in grid.batteries:
            count = 1
            backcount = 150
            while grid.batteries[key].filled < grid.batteries[key].capacity:
                if count > 150 or backcount < 1:
                    break
                if grid.houses[count].output + grid.houses[backcount].output + grid.batteries[key].filled < grid.batteries[key].capacity:
                    if grid.houses[count].pluggedin is not False:
                        count += 1
                    elif grid.houses[backcount].pluggedin is not False:
                        backcount -= 1
                    else:
                        grid.batteries[key].connected.append(grid.houses[count])
                        grid.batteries[key].connected.append(grid.houses[backcount])
                        grid.batteries[key].filled += grid.houses[count].output + grid.houses[backcount].output
                        grid.houses[count].pluggedin = grid.batteries[key]
                        grid.houses[backcount].pluggedin = grid.batteries[key]
                        count += 1
                        backcount -= 1
                else:
                    count += 1

            for house in grid.houses:
                print(grid.houses[house].pluggedin)
