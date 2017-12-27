
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emps = {employee.id:employee for employee in employees}
        return self.helper(id, emps)

    def helper(self, id, employees):
        res = employees[id].importance
        for sub in employees[id].subordinates:
            res += self.helper(sub, employees)
        
        return res
        
        
o =Solution()
e1 = Employee(1,2,[2])
e2 = Employee(2,3,[])
print(o.getImportance([e1, e2], 2))