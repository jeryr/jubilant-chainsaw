def ticket_fields(valids):
    field_control = []
    for field in valids:
        name, possible = field.split(":")
        first, useless, second = possible.split()
        low1, high1 = first.split("-")
        low2, high2 = second.split("-")
        field_control.append([name, int(low1), int(high1), int(low2), int(high2)])
    return field_control


def check_tickets(tickets, field_control):
    error_rate = 0
    valid_tickets = []
    for ticket in tickets:
        valid = True
        for item in ticket:
            for field in field_control:
                if field[1] <= item <= field[2] or field[3] <= item <= field[4]:
                    break
            else:
                error_rate += item
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return error_rate, valid_tickets


def possible_fields(tickets, field):
    possible_fields_places = []
    for i in range(len(tickets[0])):
        for ticket in tickets:
            if field[1] <= ticket[i] <= field[2] or field[3] <= ticket[i] <= field[4]:
                continue
            else:
                break
        else:
            possible_fields_places.append(i)
    return possible_fields_places


def definitive_fields(fields):
    definitive = set()
    while len(definitive) != len(fields):
        for field in fields:
            if len(field[1]) == 1:
                definitive.add(field[1][0])
                continue
            field[1] = [i for i in field[1] if i not in definitive]
    return fields


def answer(fields, ticket, starter="departure"):
    ans = 1
    for field in fields:
        if field[0].startswith(starter):
            ans *= ticket[field[1][0]]
    return(ans)


with open(".\\data\\2020_16.txt") as file:
    content = file.read().splitlines()
    fields = []
    my_ticket = []
    tickets = []
    part_1 = True
    part_2 = False
    for line in content:
        if part_1:
            if line == "":
                continue
            elif "your ticket" in line:
                part_1 = False
                part_2 = True
            else:
                fields.append(line)
        elif part_2:
            my_ticket = list(map(int, line.split(",")))
            part_2 = False
        else:
            if line == "":
                continue
            elif "nearby" in line:
                continue
            else:
                tickets.append(list(map(int, line.split(","))))

valid_fields = ticket_fields(fields)

error_rate, tickets = check_tickets(tickets, valid_fields)
print(error_rate)

fields = [[field[0], possible_fields(tickets, field)]
          for field in valid_fields]
fields = definitive_fields(fields)

print(answer(fields, my_ticket))
