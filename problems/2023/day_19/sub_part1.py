filename = "input.txt"
workflows, pieces = open(filename).read().split("\n\n")
workflows = [w.replace("}","").split("{") for w in workflows.split("\n")]
pieces = [piece.replace("{","").replace("}","") for piece in pieces.split("\n")]

# mapping of {"workflow_id":"rules"{[rule_1, ...,rule_n]},"dest":workflow id if no rules match}
WORKFLOW_MAP = {
    w[0]:{
    "rules": {rule.split(":")[0]:rule.split(":")[1] for rule in w[1].split(",")[:-1]},
    "dest":w[1].split(",")[-1]
    }
    for w in workflows
}
PIECES = [{v[0]:int(v.split("=")[-1]) for v in piece.split(",")} for piece in pieces]
def propagate_workflow(piece):
    current_workflow = "in"
    x,m,a,s = piece["x"], piece["m"], piece["a"], piece["s"]
    while current_workflow not in "AR":
        no_match = True
        for rule,workflow in WORKFLOW_MAP[current_workflow]["rules"].items():
            if eval(rule):
                current_workflow = workflow
                no_match = False
                break
        if no_match:
            current_workflow = WORKFLOW_MAP[current_workflow]["dest"]
    return sum([x,m,a,s]) if current_workflow == "A" else 0

print(sum(list(map(propagate_workflow,PIECES))))