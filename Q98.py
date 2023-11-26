# Write a python program to print below pattern.
# ```
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
def print_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

rows = 5

print_pattern(rows)
