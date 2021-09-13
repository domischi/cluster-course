import json

params = []
for gamma in [0.2, 0.5, 1.0, 2.0, 5.0]:
    d = {"gamma": gamma}
    params.append(d)

with open("queue.json", "w") as f:
    json.dump(params, f, indent=4)
