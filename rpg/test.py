#
# "If" statements
#
x = int(input("Please enter a number: "))

if x == 0:
	print("test")
elif x > 0:
	print("loser!!!")

#
# Iterate through lists
#
words = ["test1", "test2", "test3"]

for value in words:
	print(value, len(value))

#
# Functions
#
def test(value = "test"):
	print(value)

test("hello world!")

#
# Import system
#
import lib

test(lib.tryGetNumber("hey"))
test(lib.tryGetNumber("123"))