from copy import deepcopy
filename = "input.txt"

# Cut input document into workflows and pieces (only workflows will be used for part2):
workflows, pieces = open(filename).read().split("\n\n")
workflows = [w.replace("}","").split("{") for w in workflows.split("\n")]

# Compute workflows as mappings of the type :
# {"workflow_id":"rules"{[rule_1, ...,rule_n]},"dest":workflow id if no rules match}
WORKFLOW_MAP = {
    w[0]:{
    "rules": {rule.split(":")[0]:rule.split(":")[1] for rule in w[1].split(",")[:-1]},
    "dest":w[1].split(",")[-1]
    }
    for w in workflows
}

def propagate_workflow(current_workflow, values_intervals):
    """Recursive function that propagates among different branching workflows
    Accepted/Rejected intervals + current workflow state get updated and function is called again
    until current workflow is in "A" or "R" (terminal condition).

    Args:
        current_workflow (str): current workflow key
        values_intervals (dict[range]): current possible intervals for variables x,m,a,s

    Returns:
        count : total count of combination of accepted pieces quadruplet (x,m,a,s)
    """
    
    # If current workflow is A (accepted), we reach a valid terminal branch :
    # we compute the total possibilities by prod_{i in (x,m,a,s)}(len(values_intervals_{i}))
    if current_workflow == "A":
        possibilities = 1
        for variable in ["x","m","a","s"]:  
            possibilities *= len(values_intervals[variable])
        return possibilities
    
    # If current workflow is R (rejected), we reach an unvalid terminal branch :
    # we don't update the count and return 0
    if current_workflow == "R":
        return 0
    
    # Otherwise, we aren't in a terminal state and need to continue branching search :
    count = 0
    # Propagate (i.e loop) among all rules of the current workflow :
    for rule, workflow in WORKFLOW_MAP[current_workflow]["rules"].items():
        # Check type of inequality :
        for ineq in "><":
            if rule.__contains__(ineq):
                variable, value = rule.split(ineq)
                # Case of rule type "variable<value"
                # We split the full package of values into two groups :
                # - branch_acceped : ranges of values that match the condition 
                # - branch_rejected : ranges of values that doesnt match the conditions
                if ineq == "<":
                    # Compute the ranges for accepted and rejected (wrt current variable intervals):
                    branch_accepted = range(values_intervals[variable].start, int(value))
                    branch_rejected = range(int(value),values_intervals[variable].stop)
                    # Deep copy in order to get detached from origin values_interval :
                    accepted_interval = deepcopy(values_intervals)
                    # Update intervals of concerned variable and assign branch_rejected to values_interval
                    accepted_interval[variable] = branch_accepted
                    values_intervals[variable] = branch_rejected
                    # Propagate the process for accepted_intervals into the associated workflow :
                    count += propagate_workflow(workflow,accepted_interval)
                    
                # Case of rule type "variable<value"
                # Process is exactly the same than before, but symmetrical
                elif ineq == ">":
                    branch_accepted = range(int(value)+1,values_intervals[variable].stop)
                    branch_rejected = range(values_intervals[variable].start,int(value)+1)
                    accepted_interval = deepcopy(values_intervals)
                    accepted_interval[variable] = branch_accepted
                    values_intervals[variable] = branch_rejected
                    count += propagate_workflow(workflow,accepted_interval)
    
    # Case of no past condition in the workflow is match (i.e always rejected)
    # The process is propagated to the 'dest' workflow (i.e the last workflow id) 
    workflow = WORKFLOW_MAP[current_workflow]["dest"]
    count += propagate_workflow(workflow,values_intervals)  

    return count 
    
# We start in the workflow id = "in"
starting_workflow = "in"
# No restrictions for the possible intervals at the beginning : [1,4000] for all variables :
VALUES_INTERVALS = {variable:range(1,4001) for variable in ["x","m","a","s"]}
print(propagate_workflow(current_workflow=starting_workflow,values_intervals=VALUES_INTERVALS))
