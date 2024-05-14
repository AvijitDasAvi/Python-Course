class JugState:
    #Initializing Object
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    #Equality Operator
    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __repr__(self):
        return f'({self.jug1}, {self.jug2})'

def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited = set()
    queue = [(0, 0)]
    visited.add(JugState(0, 0))

    while queue:
        current_state = queue.pop(0)
        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            return True

        # Jug1
        if JugState(0, jug2) not in visited:
            queue.append((0, jug2))
            visited.add(JugState(0, jug2))

        # Jug2
        if JugState(jug1, 0) not in visited:
            queue.append((jug1, 0))
            visited.add(JugState(jug1, 0))

        # Fill jug1
        if JugState(capacity_jug1, jug2) not in visited:
            queue.append((capacity_jug1, jug2))
            visited.add(JugState(capacity_jug1, jug2))

        # Fill jug2
        if JugState(jug1, capacity_jug2) not in visited:
            queue.append((jug1, capacity_jug2))
            visited.add(JugState(jug1, capacity_jug2))

        # Pour from jug1 to jug2
        pour_amount = min(jug1, capacity_jug2 - jug2)
        if JugState(jug1 - pour_amount, jug2 + pour_amount) not in visited:
            queue.append((jug1 - pour_amount, jug2 + pour_amount))
            visited.add(JugState(jug1 - pour_amount, jug2 + pour_amount))

        # Pour from jug2 to jug1
        pour_amount = min(jug2, capacity_jug1 - jug1)
        if JugState(jug1 + pour_amount, jug2 - pour_amount) not in visited:
            queue.append((jug1 + pour_amount, jug2 - pour_amount))
            visited.add(JugState(jug1 + pour_amount, jug2 - pour_amount))

    return False

capacity_jug1 = int(input("Enter the jug1 capacity: "))
capacity_jug2 = int(input("Enter the jug2 capacity: "))
target = int(input("Enter the target to fill both jug: "))

if water_jug_problem(capacity_jug1, capacity_jug2, target):
    print("Possible to measure the target amount of water.")
else:
    print("Not possible to measure the target amount of water.")
