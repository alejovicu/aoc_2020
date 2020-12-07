inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

found = 0

for line in lines:
    line = line.strip()

    bags = line.split(" bags contain ")
    bag_color = bags[0]
    shg_color = 'shiny gold'

    if bag_color == "bright white" or bag_color == "muted yellow"  :
        for bag in bags[1].split(","):
            bag_in_bag = bag.strip().replace(".","").replace(" bags","").replace(" bag","")
            bib_count = [int(s) for s in bag_in_bag.split() if s.isdigit()][0]
            bib_color = bag_in_bag[bag_in_bag.find(" ") : len(bag_in_bag)].strip()
            if bib_color == shg_color:
                found = found + bib_count
    if bag_color == "dark orange" :
        for bag in bags[1].split(","):
            bag_in_bag = bag.strip().replace(".","").replace(" bags","").replace(" bag","")
            bib_count = [int(s) for s in bag_in_bag.split() if s.isdigit()][0]
            bib_color = bag_in_bag[bag_in_bag.find(" ") : len(bag_in_bag)]
            if bib_color == "bright white" or bib_color == "muted yellow":
                found += bib_count
    if bag_color == "light red" :
        for bag in bags[1].split(","):
            bag_in_bag = bag.strip().replace(".","").replace(" bags","").replace(" bag","")
            bib_count = [int(s) for s in bag_in_bag.split() if s.isdigit()][0]
            bib_color = bag_in_bag[bag_in_bag.find(" ") : len(bag_in_bag)]
            if bib_color == "bright white" or bib_color == "muted yellow":
                found += bib_count
    if bag_color == shg_color :
        found += 1




print(found)
