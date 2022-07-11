# Organisations do not add decimal numbers in data to save space, programmers have to convert data to use.
# Sometimes they keep -ve values such as -9999 to show no data, so we need to ignore that data.

# If there is only if statement, if can come last, but if it is if-else statement, for comes last.


temps = [221, 234, 340, -9999, 230]

new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]

print(new_temps)