def barbacue(skewers):
    non_only = 0
    only = 0
    for skewer in skewers:
        if "x" in skewer:
            non_only +=1
        else:
            only +=1
    return [only, non_only]

print(barbacue(["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",    
"--xx--x--ox--",
"--xx--x--ox--",
"--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"]))