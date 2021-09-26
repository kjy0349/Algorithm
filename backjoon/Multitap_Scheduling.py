import sys
N, K = list(map(int, sys.stdin.readline().rstrip().split()))
Electrical_appliances = list(map(int, sys.stdin.readline().split()))
Capacity = []
count = 0
is_removed = False
for i, item in enumerate(Electrical_appliances):
    if len(Capacity) == N:
        if item in Capacity:
            pass
        else:
            far_away_appliance = 0
            max_index = 0
            for appliance in Capacity:
                if appliance in Electrical_appliances[i+1:]:
                    if Electrical_appliances[i+1:].index(appliance) + i + 1 > max_index:
                        max_index = Electrical_appliances[i+1:].index(appliance) + i + 1
                        far_away_appliance = appliance
                else:
                    Capacity.remove(appliance)
                    Capacity.append(item)
                    is_removed = True
                    count += 1
                    break
            if is_removed:
                is_removed = False
                pass
            else:
                Capacity.remove(far_away_appliance)
                Capacity.append(item)
                count += 1
    else:
        if item in Capacity:
            pass
        else:
            Capacity.append(item)
print(count)
